# Architettura implementata

Riferimenti: `docs/architecture.md` (progetto), `docs/service-communication.md` (protocolli), `AGENTS.md` §6 (regole non negoziabili).

## I cinque servizi

| Servizio | Porta in `--dev` | Responsabilità | Dati posseduti | Entry point |
| --- | --- | --- | --- | --- |
| Gateway | 8010 | Unico ingresso della UI, proxy, orchestrazione delete, CORS | Nessun dato | `services/gateway/app/main.py` |
| Learning | 8011 | Flashcard manuali, posizione di lettura | `data/sqlite/learning.db` | `services/learning/app/main.py` |
| Document | 8012 | Import, parsing, chunk, file originali | `data/sqlite/documents.db`, `data/files/` | `services/document/app/main.py` |
| RAG | 8013 | Indice vettoriale e ricerca semantica | `data/chromadb/` (derivato) | `services/rag/app/main.py` |
| AI | 8014 | Recupero fonti, prompt, citazioni, streaming | Nessun dato | `services/ai/app/main.py` |

Le porte effettive le assegna `scripts/stack.py`: fisse in `--dev`, dinamiche altrimenti. I default negli `os.getenv` dei servizi valgono solo fuori dal supervisore.

## Chi chiama chi

```
React (Vite/Tauri)
        |
        v
     Gateway 8010
     |   |   |   |
     |   |   |   +--> Learning 8011  (flashcard, posizione)
     |   |   +------> AI 8014 ------> RAG 8013 (ricerca) ------> Document 8012 (chunk)
     |   +----------> RAG 8013
     +--------------> Document 8012
```

- La UI parla **solo** con il gateway (`apps/desktop/src/config.ts`); mai con gli altri servizi.
- RAG e AI si parlano via HTTP usando i contratti, non con import Python.
- Ogni chiamata interna porta `Authorization: Bearer <NOESIS_TOKEN>` (`app/client.py` del servizio chiamante).

## Flussi principali

### Import e indicizzazione

1. `POST /api/documents` (multipart) → gateway → Document.
2. Document salva il file in `data/files/<document_id>/`, estrae testo, crea i chunk e scrive SQLite.
3. La UI chiama `POST /api/index/{id}` → gateway → RAG.
4. RAG legge i chunk da Document (`GET /documents/{id}/chunks`) e li scrive in Chroma.

L'import nel client attuale indicizza subito, in serie: non c'è ancora un Job Service.

### Domanda al tutor (SSE)

1. `POST /api/ai/chat` → gateway inoltra lo stream senza bufferizzare.
2. AI cerca gli hit in RAG, emette gli eventi `citation`.
3. AI costruisce il prompt con le fonti e chiama l'adapter (`packages/ai-adapters`).
4. I token arrivano come eventi `token`, poi `done`; un errore runtime diventa `error`.
5. Se non ci sono hit, AI risponde "Nessuna fonte nei documenti" e chiude con `done` a zero citazioni.

Ordine eventi atteso: `citation*` → `token*` → `done` oppure `error`.

### Eliminazione documento

Il gateway orchestra l'ordine (`services/gateway/app/api/routes.py`, `delete_document`):

```
RAG /index/{id}  ->  Learning /flashcards?document_id=  ->  Learning /reading-positions/{id}  ->  Document /documents/{id}
```

Se una pulizia risponde 5xx, il gateway si ferma e il documento resta: niente riferimenti orfani. I test del gateway in `services/gateway/tests/test_api.py` fissano l'ordine e gli abort.

### Lettura e ripresa

1. Click su un documento → `App` apre `DocumentReader` con target senza pagina/sezione.
2. Reader chiede `GET /api/reading-positions/{id}` al gateway.
3. La citazione vince sempre: se c'è sezione o pagina si usa quella, altrimenti il chunk salvato (`selectStartIndex` in `apps/desktop/src/reader.ts`).
4. Lo scorrimento salva il chunk corrente con `PUT /api/reading-positions/{id}` (throttle con `requestAnimationFrame`).

## Contratti condivisi

`packages/contracts/noesis_contracts/models.py` contiene **solo** modelli Pydantic e tipi (nessuna logica). Ogni servizio importa da `noesis_contracts`.

- Envelope: `ApiResponse[T]` con `status`, `data`, `error`; errori con `ApiError` e `ErrorCode`.
- Entità: `DocumentSummary`, `Chunk`, `SearchHit`, `Citation`, `Flashcard`, `ReadingPosition`.
- Richieste: `SearchRequest`, `TutorRequest`, `IndexRequest`, `FlashcardCreate/Update`, `ReadingPositionUpdate`.
- Eventi SSE: `TokenEvent`, `CitationEvent`, `DoneEvent`, `ErrorEvent`.

Quando aggiungi un modello, aggiorna anche `noesis_contracts/__init__.py`: i servizi importano dal package, non dal modulo.

## Confini e invarianti

- Nessun import tra `services/*`; la comunicazione è HTTP.
- Ogni servizio scrive solo le proprie tabelle. Nessun accesso al DB di un altro.
- ChromaDB è un indice derivato: ricostruibile con `POST /api/index/rebuild`.
- Binding solo su `127.0.0.1`; il gateway è l'unico esposto alla UI e ha CORS ristretto.
- La UI non blocca su richieste lunghe: SSE per il tutor, stato di caricamento per le altre.
- Nessuna funzionalità a pagamento o cloud: runtime AI locale via adapter, embedding locale.

## Decisioni aperte

Elenco completo in `AGENTS.md` §15. Stato attuale del codice:

| Decisione | Oggi nel codice |
| --- | --- |
| ADR-006 file SQLite unico vs per servizio | File separati per servizio (documents, learning) |
| ADR-010 sandbox notebook | Non implementata; nessun Notebook Service |
| ADR-011 REST vs gRPC | REST + JSON, SSE per lo streaming |
| ADR-012 gestione processi locali | `scripts/stack.py` lanciato dalla shell Rust |
| Porte dinamiche vs socket | Dinamiche nel supervisore, fisse 8010-8014 in `--dev` |
| Job asincroni | Non c'è un Job Service; l'indicizzazione è sincrona dal client |

Queste scelte non vanno cambiate in un task ordinario: serve un ADR in `docs/adr/`.
