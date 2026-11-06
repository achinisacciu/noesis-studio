# Noesis Studio

Piattaforma desktop **local-first** per studiare Statistica, Matematica, ML e Deep Learning: lettore di documenti, tutor IA con RAG citazionale, notebook Python in sandbox, flashcard e quiz.

**Stato:** POC-01, POC-04, POC-02/03 e POC-05 completati; app desktop Tauri 2 con import, indice, tutor in streaming, citazioni, lettore con ripresa della lettura, annotazioni e flashcard create dal testo. Funzionalità MVP ancora da fare.

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
| [docs/poc-05.md](docs/poc-05.md) | POC-05: shell desktop Tauri 2 e ciclo di vita |
| [docs/frontend.md](docs/frontend.md) | Client React: import, chat, citazioni, annotazioni |
| [docs/wiki/README.md](docs/wiki/README.md) | Wiki: mappa delle aree di implementazione |
| [AGENTS.md](AGENTS.md) | Regole operative per gli agenti di sviluppo |

## Stack

Tauri 2 + React/TypeScript per il desktop, microservizi Python/FastAPI in locale, SQLite + ChromaDB per la persistenza, adapter per runtime AI locali (Ollama come primo runtime).

## Struttura

- `docs/` — documenti di progetto.
- `services/` — `document`, `rag`, `ai`, `learning`, `gateway`: processi Python indipendenti.
- `packages/contracts` — modelli Pydantic condivisi.
- `packages/ai-adapters` — contratto adapter e implementazione Ollama.
- `apps/desktop` — app desktop Tauri 2 + React/TypeScript.
- `scripts/` — supervisore dei servizi e aggiornamento della skill ponytail.

La struttura target completa è in [AGENTS.md §4](AGENTS.md#4-struttura-del-repository-target).

## Sviluppo

Prerequisiti: Python 3.11+, `uv`, Ollama con un modello installato (default `qwen3.5:0.8b`). Per il desktop servono anche Node 22+, `pnpm` (via `corepack`) e Rust.

App desktop (avvia anche i servizi se il gateway è spento):

```bash
cd apps/desktop
corepack pnpm install
corepack pnpm tauri:dev
```

Solo frontend nel browser:

```bash
ollama pull qwen3.5:0.8b          # una volta sola
python scripts/stack.py --dev     # backend su porte fisse, token dev-token
```

In un secondo terminale:

```bash
cd apps/desktop
corepack pnpm dev                 # http://localhost:5173
```

`python scripts/stack.py --check` verifica invece l'intero flusso e termina senza aprire l'interfaccia.

Con lo stack attivo (`python scripts/stack.py --dev`), `python scripts/eval_rag.py` misura l'accuratezza delle citazioni sul corpus di `evaluation/`: 48 domande, risultato attuale 95,8% (gate 90%).

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

Test del frontend:

```bash
cd apps/desktop
corepack pnpm test
corepack pnpm typecheck
```

Dettagli e limiti in [docs/poc-04.md](docs/poc-04.md), [docs/poc-02.md](docs/poc-02.md), [docs/poc-05.md](docs/poc-05.md) e [docs/frontend.md](docs/frontend.md); il primo prototipo è in [docs/poc-01.md](docs/poc-01.md).

Aggiornamento della skill ponytail:

```bash
node scripts/update-ponytail.mjs
```
