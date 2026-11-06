# Noesis Studio

Piattaforma desktop **local-first** per studiare Statistica, Matematica, ML e Deep Learning: lettore di documenti, tutor IA con RAG citazionale, notebook Python in sandbox, flashcard e quiz.

**Stato:** fondamenta del repository. Nessuna funzionalità MVP ancora implementata.

## Documenti

| Documento | Contenuto |
| --- | --- |
| [docs/PRD.md](docs/PRD.md) | Visione, utenti, metriche, ambito MVP |
| [docs/roadmap.md](docs/roadmap.md) | Fasi e criteri di uscita |
| [docs/user-stories.md](docs/user-stories.md) | Storie e criteri di accettazione |
| [docs/architecture.md](docs/architecture.md) | Architettura, microservizi, persistenza, AI, sandbox |
| [docs/service-communication.md](docs/service-communication.md) | Protocolli, processo, gateway, sicurezza locale |
| [AGENTS.md](AGENTS.md) | Regole operative per gli agenti di sviluppo |

## Stack

Tauri 2 + React/TypeScript per il desktop, microservizi Python/FastAPI in locale, SQLite + ChromaDB per la persistenza, adapter per runtime AI locali.

## Struttura

`apps/`, `services/` e `packages/` sono definite in [AGENTS.md §4](AGENTS.md#4-struttura-del-repository-target) e verranno create con i primi prototipi. Oggi esistono solo `docs/` e gli script di manutenzione.

## Sviluppo

Prerequisiti previsti: Node 22+, Python 3.11+, Rust, `uv`, `pnpm`.

I comandi applicativi (`dev`, `test`, `build`) sono il target descritto in [AGENTS.md §5](AGENTS.md#5-comandi-canonici) e non esistono ancora. L'unico script disponibile è l'aggiornamento della skill ponytail:

```bash
node scripts/update-ponytail.mjs
```
