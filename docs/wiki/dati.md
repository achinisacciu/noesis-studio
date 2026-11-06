# Dati e persistenza

Tutto lo stato locale vive in `data/` (gitignored). La cartella è scelta da `NOESIS_DATA`; in sviluppo il supervisore la passa a ogni servizio.

## Layout

```
data/
  sqlite/
    documents.db     Document Service
    learning.db      Learning Service
  files/
    <document_id>/<nome-file>    originali importati
  chromadb/          indice vettoriale (derivato)
  logs/              stdout/stderr dei servizi avviati da stack.py
  check/             dati isolati usati da --check
```

- SQLite in WAL: accanto ai `.db` compaiono `-wal` e `-shm`.
- `data/check/` viene cancellata e ricreata a ogni `python scripts/stack.py --check`.
- Non committare mai `data/`: contiene dati utente.

## Schema Document (`data/sqlite/documents.db`)

```sql
CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    filename TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS chunks (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    position INTEGER NOT NULL,
    text TEXT NOT NULL,
    page INTEGER,        -- NULL se il formato non ha pagine
    section TEXT         -- NULL se non c'è un titolo
);
CREATE INDEX IF NOT EXISTS idx_chunks_document ON chunks(document_id);

CREATE TABLE IF NOT EXISTS annotations (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    chunk_id TEXT NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
    kind TEXT NOT NULL,          -- highlight | note | bookmark
    start INTEGER NOT NULL DEFAULT 0,
    end INTEGER NOT NULL DEFAULT 0,
    note TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_annotations_document ON annotations(document_id);
```

- `PRAGMA journal_mode=WAL`, `PRAGMA foreign_keys=ON`.
- `id` documento: `uuid4().hex`; `id` chunk: `"<document_id>:<position>"`.
- `documents.title` è lo stem del filename; `created_at` è ISO 8601 UTC.
- Il delete del documento cancella i chunk per cascade e poi la cartella `data/files/<id>/`.
- `annotations` è posseduta dal Document Service: `highlight`/`note` coprono `[start, end)` del testo del chunk, `bookmark` ha intervallo vuoto. Gli offset sono in unità UTF-16 per coincidere con la selezione del browser.
- Document elimina chunk e annotazioni per cascade: il gateway non deve ripulirle.

## Schema Learning (`data/sqlite/learning.db`)

```sql
CREATE TABLE IF NOT EXISTS flashcards (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    front TEXT NOT NULL,
    back TEXT NOT NULL,
    page INTEGER,
    section TEXT,
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_flashcards_document ON flashcards(document_id);

CREATE TABLE IF NOT EXISTS reading_positions (
    document_id TEXT PRIMARY KEY,
    chunk_id TEXT NOT NULL,
    position INTEGER NOT NULL,
    updated_at TEXT NOT NULL
);
```

- Nessuna foreign key verso Document: i servizi sono separati. La coerenza la garantisce il delete orchestrato dal gateway.
- Una sola posizione per documento (upsert su `document_id`).
- `reading_positions.chunk_id` è il chunk del Document Service; se il documento viene reimportato con ID nuovo, la posizione vecchia sparisce col delete.

## ChromaDB (`data/chromadb`)

- Client persistente Chroma, collection `chunks`.
- Un record per chunk con `id`, testo e metadati:
  - `document_id`
  - `page`: numero pagina oppure `-1` quando assente
  - `section`: titolo oppure `""` quando assente
- I sentinella `-1`/`""` esistono perché Chroma non accetta `None` nei metadati (commento `shortcut:` in `services/rag/app/index.py`).
- Embedding: modello ONNX locale di Chroma (`all-MiniLM-L6-v2`), scaricato la prima volta; telemetria disabilitata.

**Chroma è derivato.** Non contiene nulla che non sia ricostruibile da SQLite + file originali:

```
POST /api/index/rebuild   -> legge tutti i documenti e reindicizza
```

## Coerenza e delete

Ordine nel gateway (`services/gateway/app/api/routes.py`):

1. `DELETE rag /index/{id}` — via i vettori.
2. `DELETE learning /flashcards?document_id=` — via le schede.
3. `DELETE learning /reading-positions/{id}` — via la posizione.
4. `DELETE document /documents/{id}` — via righe, chunk, annotazioni e file.

Le annotazioni non compaiono nell'ordine del gateway: appartengono al Document Service e spariscono per cascade con il documento.

Se uno dei primi tre passi risponde 5xx, il gateway restituisce 502 e **non** elimina il documento: meglio un orfano ricostruibile che una citazione senza fonte. I test del gateway bloccano questo contratto.

## Migrazioni

Oggi non c'è uno strumento di migrazione versionata: ogni `Store.__init__` esegue `CREATE TABLE IF NOT EXISTS` con lo schema corrente.

- Nuova tabella: aggiungila a `SCHEMA` nello store del servizio.
- Nuova colonna su tabella esistente: **non** basta aggiungerla allo schema, i DB esistenti non la vedranno. Serve una migrazione esplicita (Alembic o script idempotente) e un test up/down. È debito tecnico noto: apri un ADR prima di scegliere lo strumento.
- Cambio del modello di embedding: richiede reindicizzazione esplicita e versionata (vedi `AGENTS.md` §10).

## Ispezione e reset

Ispezione rapida (SQLite è un file):

```bash
python -c "import sqlite3;c=sqlite3.connect('data/sqlite/documents.db');print(c.execute('select id,title from documents').fetchall())"
```

Reset completo in sviluppo (distrugge i dati locali):

```powershell
Remove-Item -Recurse -Force data/sqlite,data/chromadb,data/files,data/logs
python scripts/stack.py --check --no-sync   # ricrea tutto in data/check
```

Backup: copia `data/` a stack fermo. A stack attivo copia anche `-wal`/`-shm` oppure usa la SQLite Backup API.
