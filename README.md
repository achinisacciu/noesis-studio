# Noesis Studio

Piattaforma desktop **local-first** per studiare Statistica, Matematica, ML e Deep Learning: lettore di documenti, tutor IA con RAG citazionale, notebook Python in sandbox, flashcard e quiz.

**Stato:** POC-01 completato (microservizi locali). Nessuna funzionalità MVP ancora implementata.

## Documenti

| Documento | Contenuto |
| --- | --- |
| [docs/PRD.md](docs/PRD.md) | Visione, utenti, metriche, ambito MVP |
| [docs/roadmap.md](docs/roadmap.md) | Fasi e criteri di uscita |
| [docs/user-stories.md](docs/user-stories.md) | Storie e criteri di accettazione |
| [docs/architecture.md](docs/architecture.md) | Architettura, microservizi, persistenza, AI, sandbox |
| [docs/service-communication.md](docs/service-communication.md) | Protocolli, processo, gateway, sicurezza locale |
| [docs/poc-01.md](docs/poc-01.md) | POC-01: microservizi locali, esito e limiti |
| [AGENTS.md](AGENTS.md) | Regole operative per gli agenti di sviluppo |

## Stack

Tauri 2 + React/TypeScript per il desktop, microservizi Python/FastAPI in locale, SQLite + ChromaDB per la persistenza, adapter per runtime AI locali.

## Struttura

- `docs/` — documenti di progetto.
- `services/` — `document`, `rag`, `gateway`: processi Python indipendenti.
- `packages/contracts` — modelli Pydantic condivisi.
- `scripts/` — supervisore del POC e aggiornamento della skill ponytail.
- `apps/desktop` — non ancora creata (Tauri 2 + React).

La struttura target completa è in [AGENTS.md §4](AGENTS.md#4-struttura-del-repository-target).

## Sviluppo

Prerequisiti: Python 3.11+, `uv`. Per il desktop serviranno anche Node 22+, `pnpm` e Rust.

Avvio del POC-01:

```bash
python scripts/poc01.py --check   # avvia i servizi, verifica il flusso completo, arresta
python scripts/poc01.py           # avvia e resta attivo fino a Ctrl+C
```

Test di un servizio:

```bash
cd services/document
uv run pytest -q
uv run ruff check . && uv run ruff format --check .
uv run mypy app
```

Dettagli e limiti in [docs/poc-01.md](docs/poc-01.md).

Aggiornamento della skill ponytail:

```bash
node scripts/update-ponytail.mjs
```
