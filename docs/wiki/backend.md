# Backend

Cinque servizi FastAPI indipendenti. Ognuno ha il proprio `pyproject.toml`, `.venv` e `uv.lock`. Comandi sempre dalla cartella del servizio con `uv run ...`.

## Struttura comune

```
services/<nome>/
  app/
    main.py            creazione FastAPI, middleware request_id, log JSON
    api/routes.py      router pubblici (health/ready) + router protetti
    core/security.py   require_token
    core/errors.py     envelope degli errori
    store.py           SQLite (solo dove serve)
    client.py          chiamate HTTP verso altri servizi (solo dove serve)
  tests/test_api.py    TestClient + monkeypatch dello store
  pyproject.toml
```

Convenzioni:

- Ogni risposta è `ApiResponse[T]` (`status`, `data`, `error`), anche gli errori.
- Gli ID nei path rispettano `^[A-Za-z0-9_-]{1,64}$`; gli ID generati sono `uuid4().hex`.
- Gli endpoint sotto `api` richiedono `Authorization: Bearer $NOESIS_TOKEN`; `health`/`ready` restano aperti.
- `NOESIS_DATA` sceglie la cartella dati; senza variabile si usa `data/` alla radice del repo.
- Log JSON con `service`, `request_id`, `method`, `path`, `status`, `duration_ms`.
- Timeout espliciti verso gli altri servizi (10-15 s); errori HTTP tradotti in 502/504.

## Gateway (`services/gateway`)

Unico ingresso della UI. Non possiede dati: inoltra, orchestra e limita CORS.

| File | Ruolo |
| --- | --- |
| `app/api/routes.py` | Tutte le rotte `/api/*`, URL dei servizi, ordine di delete |
| `app/proxy.py` | `forward`, `forward_file`, `stream`, `check` |
| `app/main.py` | CORS da `NOESIS_FRONTEND_ORIGIN`, middleware, log |

Rotte:

| Metodo | Percorso | Destinazione |
| --- | --- | --- |
| `GET` | `/health` | gateway |
| `GET` | `/ready` | document + rag |
| `POST` | `/api/documents` | document (multipart) |
| `GET` | `/api/documents` | document |
| `GET` | `/api/documents/{id}` | document |
| `GET` | `/api/documents/{id}/chunks` | document |
| `DELETE` | `/api/documents/{id}` | rag → learning → learning → document |
| `POST` | `/api/index/{id}` | rag |
| `POST` | `/api/index/rebuild` | rag |
| `POST` | `/api/rag/search` | rag |
| `GET/POST` | `/api/flashcards` | learning |
| `PATCH/DELETE` | `/api/flashcards/{id}` | learning |
| `GET` | `/api/reading-positions/{id}` | learning |
| `PUT` | `/api/reading-positions/{id}` | learning |
| `GET` | `/api/ai/models` | ai |
| `POST` | `/api/ai/chat` | ai (SSE) |

Punti da conoscere:

- `stream()` non bufferizza e propaga `Cache-Control: no-cache` e `X-Accel-Buffering: no`.
- Il delete cascade è l'unico punto che conosce l'ordine tra servizi: se aggiungi dati derivati, aggiungi qui la pulizia prima del documento.
- Test: `services/gateway/tests/test_api.py` (proxy, ordine delete, abort su 5xx, SSE).

## Document (`services/document`)

Importa file, estrae testo, crea chunk, conserva gli originali.

| File | Ruolo |
| --- | --- |
| `app/api/routes.py` | Upload, lista, dettaglio, chunk, delete; limite 50 MB |
| `app/parsing.py` | Parser PDF/DOCX/MD/TXT e `chunk_blocks` |
| `app/store.py` | Tabelle `documents` e `chunks`, file su disco |

- Formati: `.pdf`, `.docx`, `.md`, `.markdown`, `.txt`.
- PDF: PyMuPDF, `page` valorizzata; DOCX: `Heading*` → sezione; MD/TXT: titoli `#` → sezione.
- Chunk da circa 800 caratteri; non attraversano pagina o sezione. ID chunk: `<document_id>:<position>`.
- File originali: `data/files/<document_id>/<filename>`.
- `DELETE` cancella riga SQLite (cascade sui chunk) e cartella file.
- Test: 8 in `services/document/tests/test_api.py` (formati, pagina PDF, errori, delete).

## RAG (`services/rag`)

Indice vettoriale derivato. Non è fonte di verità.

| File | Ruolo |
| --- | --- |
| `app/index.py` | Protocol `Index`, implementazione `ChromaIndex`, embedding locale |
| `app/client.py` | Lettura documenti/chunk da Document |
| `app/api/routes.py` | Index, delete index, rebuild, search |

- Collection Chroma: `chunks`; client persistente in `data/chromadb`.
- Embedding: modello ONNX locale di Chroma (`all-MiniLM-L6-v2`), telemetria disabilitata.
- Metadati: `document_id`, `page` (`-1` se assente), `section` (`""` se assente).
- `POST /index` sostituisce i chunk del documento; `POST /index/rebuild` azzera e ricostruisce da tutti i documenti.
- `POST /search` filtra per `document_id` se presente e restituisce `SearchHit` con `score`.
- Test: 7 in `services/rag/tests/test_api.py` (indice, delete, rebuild, filtro, hit).

## AI (`services/ai`)

Recupera fonti, costruisce il prompt, streamma token e citazioni.

| File | Ruolo |
| --- | --- |
| `app/api/routes.py` | `/models`, `/chat`, scelta modello e adapter |
| `app/prompt.py` | System prompt, conversione hit → citazioni, messaggi |
| `app/sse.py` | Formato `event:`/`data:` |
| `app/client.py` | Ricerca su RAG |

- Runtime: `OllamaAdapter` in `packages/ai-adapters`; URL `OLLAMA_URL` (default `127.0.0.1:11434`), modello `NOESIS_MODEL` (default `qwen3.5:0.8b`).
- Generazione: `temperature=0.2`, `think=False`, streaming.
- Se la ricerca non produce hit: un solo `token` con "Nessuna fonte nei documenti" e `done` a zero citazioni.
- `AdapterError` diventa evento `error` con `code` del contratto; `abort(request_id)` chiude la risposta HTTP al termine o allo stop.
- Test: 8 in `services/ai/tests/test_api.py` (SSE, citazioni, no-source, errore adapter, modelli).

## Learning (`services/learning`)

Dati didattici dell'utente: flashcard e posizione di lettura.

| File | Ruolo |
| --- | --- |
| `app/api/routes.py` | CRUD flashcard, delete per documento, GET/PUT/DELETE posizione |
| `app/store.py` | Tabelle `flashcards` e `reading_positions` |

- Flashcard: `front`, `back`, `page`, `section`, `document_id`, `created_at`; filtro `?document_id=`.
- Posizione: una riga per documento, `chunk_id` + `position`, upsert su `PUT`.
- Nessuna dipendenza dagli altri servizi: il documento è solo un riferimento.
- Test: 8 in `services/learning/tests/test_api.py` (CRUD, filtro, delete per documento, posizione, validazione, auth).

## Ricette

### Aggiungere un endpoint

1. Modello in `packages/contracts/noesis_contracts/models.py` + export in `__init__.py` (se serve un tipo nuovo).
2. Rotta nel servizio proprietario (`app/api/routes.py`), con `PathParam`/`Query` validati.
3. Se la UI lo usa: proxy nel gateway con lo stesso nome, poi client in `apps/desktop/src/api.ts`.
4. Test: unit/contract nel servizio, proxy nel gateway, `--check` in `scripts/stack.py` se è un flusso.
5. Documenta in `docs/wiki/backend.md` e, se è una funzionalità, in `docs/wiki/funzionalita.md`.

### Aggiungere un servizio

1. `services/<nome>/` con `pyproject.toml`, `app/main.py`, `app/api/`, `app/core/`.
2. Contratti condivisi in `packages/contracts`.
3. Aggiungi il nome a `SERVICES` in `scripts/stack.py` (avvio, porte, URL, environment).
4. Aggiungi un proxy nel gateway se la UI deve raggiungerlo.
5. Aggiungi test e la voce nella [mappa dell'architettura](architettura.md).

### Aggiungere una tabella o una colonna

Oggi non c'è Alembic: lo schema viene creato all'avvio con `CREATE TABLE IF NOT EXISTS`. Una nuova tabella si aggiunge in `SCHEMA` nello `store.py` del servizio. Una nuova colonna su una tabella esistente richiede una migrazione esplicita (non ancora infrastrutturata): apri un ADR o una issue prima di procedere.

### Pulire dati derivati al delete

Aggiungi la chiamata nel `delete_document` del gateway **prima** di `DELETE /documents/{id}`, con abort su 5xx, e aggiorna i test dell'ordine. Non duplicare l'ordine altrove.

### Cambiare runtime AI

Implementa `RuntimeAdapter` in `packages/ai-adapters`, poi sostituisci l'istanza in `services/ai/app/api/routes.py`. L'AI Service non deve conoscere l'API del runtime: solo il contratto.
