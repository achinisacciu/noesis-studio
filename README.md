# Noesis Studio

Piattaforma desktop **local-first** per studiare Statistica, Matematica, ML e Deep Learning: lettore di documenti, tutor IA con RAG citazionale, notebook Python in sandbox, flashcard e quiz.

**Stato:** POC-01, POC-04 e POC-02/03 completati (microservizi locali, persistenza SQLite + ChromaDB con citazioni, tutor locale in streaming SSE). Nessuna funzionalità MVP ancora implementata.

## Documenti

| Documento | Contenuto |
| --- | --- |
| [docs/PRD.md](docs/PRD.md) | Visione, utenti, metriche, ambito MVP |
| [docs/roadmap.md](docs/roadmap.md) | Fasi e criteri di uscita |
| [docs/user-stories.md](docs/user-stories.md) | Storie e criteri di accettazione |
| [docs/architecture.md](docs/architecture.md) | Architettura, microservizi, persistenza, AI, sandbox |
| [docs/service-communication.md](docs/service-communication.md) | Protocolli, processo, gateway, sicurezza locale |
| [docs/poc-01.md](docs/poc-01.md) | POC-01: microservizi locali, esito e limiti |
| [docs/poc-04.md](docs/poc-04.md) | POC-04: SQLite + ChromaDB, RAG con citazioni |
| [docs/poc-02.md](docs/poc-02.md) | POC-02/03: adapter AI, Ollama, streaming SSE |
| [AGENTS.md](AGENTS.md) | Regole operative per gli agenti di sviluppo |

## Stack

Tauri 2 + React/TypeScript per il desktop, microservizi Python/FastAPI in locale, SQLite + ChromaDB per la persistenza, adapter per runtime AI locali (Ollama come primo runtime).

## Struttura

- `docs/` — documenti di progetto.
- `services/` — `document`, `rag`, `ai`, `gateway`: processi Python indipendenti.
- `packages/contracts` — modelli Pydantic condivisi.
- `packages/ai-adapters` — contratto adapter e implementazione Ollama.
- `scripts/` — supervisore del POC e aggiornamento della skill ponytail.
- `apps/desktop` — non ancora creata (Tauri 2 + React).

La struttura target completa è in [AGENTS.md §4](AGENTS.md#4-struttura-del-repository-target).

## Sviluppo

Prerequisiti: Python 3.11+, `uv`, Ollama con un modello installato (default `qwen3.5:0.8b`). Per il desktop serviranno anche Node 22+, `pnpm` e Rust.

```bash
ollama pull qwen3.5:0.8b          # una volta sola
python scripts/stack.py --check   # avvia i servizi, verifica il flusso completo, arresta
python scripts/stack.py           # avvia e resta attivo fino a Ctrl+C
```

Il tutor si interroga via gateway:

```bash
curl -N -X POST http://127.0.0.1:<porta>/api/ai/chat \
  -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  -d '{"question": "Che cosa misura la varianza?"}'
```

Test di un servizio:

```bash
cd services/document
uv run pytest -q
uv run ruff check . && uv run ruff format --check .
uv run mypy app
```

Dettagli e limiti in [docs/poc-04.md](docs/poc-04.md) e [docs/poc-02.md](docs/poc-02.md); il primo prototipo è in [docs/poc-01.md](docs/poc-01.md).

Aggiornamento della skill ponytail:

```bash
node scripts/update-ponytail.mjs
```
