# POC-04 — Persistenza e RAG

**Stato:** completato
**Obiettivo:** verificare SQLite + ChromaDB su un flusso reale: import di un file, indicizzazione con embedding, ricerca semantica con citazioni, eliminazione e ricostruzione dell'indice.

## Cosa è stato costruito

| Componente | Cartella | Ruolo |
| --- | --- | --- |
| Document Service | `services/document` | Import PDF/DOCX/MD/TXT, parsing, chunking, persistenza SQLite, file originali |
| RAG Service | `services/rag` | Indice ChromaDB, embedding locali, ricerca semantica, rebuild |
| Local API Gateway | `services/gateway` | Import multipart, orchestrazione indice/delete, proxy delle ricerche |
| Contratti | `packages/contracts` | `DocumentSummary`, `Chunk`, `SearchHit`, richieste e risposte |
| Supervisore | `scripts/stack.py` | Avvia i processi su porte libere e verifica il flusso completo |

Flusso verificato:

```
POST   /api/documents          -> gateway -> document (parse + chunk + SQLite)
POST   /api/index/{id}         -> gateway -> rag -> document (chunk) -> Chroma
POST   /api/rag/search         -> gateway -> rag (hit con documento, pagina, sezione)
POST   /api/index/rebuild      -> gateway -> rag -> document (tutti i documenti)
DELETE /api/documents/{id}     -> gateway -> rag (indice) -> learning (schede) -> document (SQLite + file)
```

## Persistenza

- **SQLite** (`data/sqlite/documents.db`): tabelle `documents` e `chunks`, WAL, foreign key con `ON DELETE CASCADE`. È la fonte di verità.
- **File originali** (`data/files/<document_id>/`): conservati per la ricostruzione dell'indice.
- **ChromaDB** (`data/chromadb/`): indice derivato, sempre ricostruibile da SQLite + file. Collection `chunks`.
- Embedding: modello ONNX locale di Chroma (`all-MiniLM-L6-v2`), nessuna chiamata di rete a runtime dopo il primo download del modello; telemetria disabilitata.
- La cartella dati è scelta da `NOESIS_DATA` (default `data/`), così i tre processi condividono lo stesso stato.

## Formati e citazioni

- PDF con PyMuPDF: una citazione per pagina (`page`).
- DOCX con python-docx: sezione dallo stile `Heading*`.
- MD/TXT: sezione dai titoli `#`.
- Chunk da circa 800 caratteri, senza attraversare pagina o sezione.
- Limite file: 50 MB.

`SearchHit` contiene `document_id`, `text`, `page`, `section`, `score`: il frontend può aprire il documento alla posizione citata.

## Endpoint

| Servizio | Endpoint | Auth |
| --- | --- | --- |
| tutti | `GET /health`, `GET /ready` | no |
| document | `POST /documents` (multipart), `GET /documents`, `GET /documents/{id}`, `GET /documents/{id}/chunks`, `DELETE /documents/{id}` | sì |
| rag | `POST /index`, `DELETE /index/{id}`, `POST /index/rebuild`, `POST /search` | sì |
| gateway | `POST /api/documents`, `GET /api/documents`, `GET /api/documents/{id}`, `GET /api/documents/{id}/chunks`, `DELETE /api/documents/{id}`, `POST /api/index/{id}`, `POST /api/index/rebuild`, `POST /api/rag/search` | sì |

Il delete passa prima dal RAG e dal Learning Service: se l'indice o le schede non vengono ripuliti, il documento non viene eliminato e non restano citazioni orfane.

## Esecuzione

```bash
python scripts/stack.py --check   # avvia, verifica import -> indice -> ricerca -> rebuild -> delete, arresta
python scripts/stack.py           # avvia e resta attivo fino a Ctrl+C
```

Con `--check` i dati finiscono in `data/check/` e vengono azzerati a ogni esecuzione. Log in `data/check/logs/`.

## Cosa è stato verificato

- Import Markdown via gateway, con metadati e chunk persistiti in SQLite.
- Indice ChromaDB con embedding locali, ricerca semantica filtrata per documento.
- Citazione coerente: stesso `document_id`, sezione `Varianza`, score normalizzato.
- Rebuild completo dell'indice da SQLite.
- Delete orchestrato: documento e indice spariti, ricerca successiva senza hit.
- 36 test unitari (8 document, 7 rag, 13 gateway, 8 ai), `ruff` e `mypy --strict` puliti.
- Avvio e arresto dei tre processi senza processi residui.

## Valutazione delle citazioni

`evaluation/questions.jsonl` contiene 48 domande etichettate su tre documenti sintetici (`evaluation/corpus/`), 16 sezioni in tutto.

```bash
python scripts/stack.py --dev      # in un terminale
python scripts/eval_rag.py         # importa, indicizza, interroga, ripulisce
```

Lo script verifica che la sezione attesa compaia tra i primi 3 hit della ricerca, perché le citazioni mostrate all'utente derivano dagli hit e non dal testo del modello. Se l'accuratezza scende sotto il gate del 90% esce con codice 1.

Risultato misurato: **46/48 = 95,8%**, gate superato. I due casi mancati sono domande sul raggruppamento non supervisionato (il testo sta nella sezione "Apprendimento supervisionato") e sulla pendenza della retta ("Regressione lineare" non emerge su "Validazione incrociata"). Il corpus è sintetico: il numero non sostituisce una valutazione su materiale di studio reale.

## Limiti noti

- Nessun workspace: i documenti sono globali. I workspace sono previsti nella fase successiva.
- `page` è `None` per DOCX/MD/TXT; solo il PDF ha la pagina.
- Il chunking è a blocchi, non a finestre sovrapposte: sufficiente per il POC, da valutare per documenti lunghi.
- Il 404 è ancora mappato su `VALIDATION_ERROR` perché il contratto espone solo sei codici di errore.
- La ricerca è solo semantica: non c'è ancora espansione della query né reranking.
- Primo avvio con download del modello di embedding (~79 MB, già in cache su questa macchina).
