# Wiki di implementazione

Questa wiki dice **dove guardare** nel codice. Non sostituisce i documenti di progetto: in caso di conflitto valgono `AGENTS.md`, `docs/architecture.md` e i POC. Se la wiki e il codice divergono, vince il codice e la wiki va corretta nello stesso cambio.

## Pagine

| Pagina | Quando aprirla |
| --- | --- |
| [Architettura](architettura.md) | Capire chi fa cosa, i confini tra servizi e i flussi completi |
| [Backend](backend.md) | Endpoint, store SQLite, client HTTP, test e ricette per aggiungere API |
| [Frontend](frontend.md) | Componenti React, stato, SSE, stili e test della UI |
| [Dati](dati.md) | Schema SQLite, ChromaDB, file originali, coerenza e reset |
| [Funzionalità](funzionalita.md) | Dalla storia utente ai file da toccare, incluse le funzioni non ancora fatte |
| [Sviluppo](sviluppo.md) | Comandi, porte, token, check completo, valutazione RAG, problemi noti |

## Da dove partire

| Compito | Prima tappa | Poi |
| --- | --- | --- |
| Aggiungere o cambiare un endpoint | `services/<nome>/app/api/routes.py` | [backend](backend.md), [funzionalità](funzionalita.md) |
| Aggiungere un dato persistente | `services/<nome>/app/store.py` | [dati](dati.md), contratti in `packages/contracts` |
| Cambiare la UI o un flusso | `apps/desktop/src/App.tsx` e `src/components/` | [frontend](frontend.md) |
| Cambiare il RAG o le citazioni | `services/rag/app/index.py`, `services/ai/app/prompt.py` | [funzionalità](funzionalita.md), `docs/poc-04.md` |
| Cambiare modello o streaming | `packages/ai-adapters`, `services/ai/app/sse.py` | `docs/poc-02.md` |
| Aggiungere un servizio | `scripts/stack.py`, `packages/contracts` | [backend](backend.md#aggiungere-un-servizio) |
| Capire perché i servizi non partono | `scripts/stack.py`, `data/logs/` | [sviluppo](sviluppo.md#problemi-noti) |
| Tauri, avvio e chiusura | `apps/desktop/src-tauri/src/lib.rs` | `docs/poc-05.md` |
| Dare priorità al prossimo lavoro | `docs/roadmap.md`, `docs/user-stories.md` | [funzionalità](funzionalita.md#non-ancora-implementato) |
| Aggiungere materiale di studio | `resources/README.md` | Import dalla UI, poi ricostruzione dell'indice |

## Mappa del repository

```
apps/desktop/            Tauri 2 + React/TypeScript
  src/                   UI, client API, parser SSE
  src-tauri/             shell Rust, ciclo di vita dei servizi
services/
  gateway/               unico ingresso HTTP per la UI
  document/              import, parsing, SQLite documenti
  rag/                   indice ChromaDB, ricerca semantica
  ai/                    prompt, citazioni, streaming SSE
  learning/              flashcard e posizione di lettura
packages/
  contracts/             modelli Pydantic condivisi
  ai-adapters/           contratto runtime AI + Ollama
scripts/
  stack.py               supervisore dei cinque servizi
  eval_rag.py            valutazione delle citazioni
evaluation/              corpus e domande etichettate
resources/               materiale di studio versionato (es. wikipedia/)
docs/                    PRD, architettura, POC, wiki
data/                    stato locale (gitignored)
```

## Regole di manutenzione

- Una pagina per area, non per file: i dettagli stanno nel codice, la wiki dice dove andare.
- Niente numeri di riga (invecchiano subito): cita file, funzioni e rotte.
- Quando aggiungi un servizio, una rotta, una tabella o un componente, aggiorna la pagina dell'area e la tabella in [funzionalità](funzionalita.md).
- I documenti di prodotto e le decisioni restano in `docs/`; la wiki non introduce decisioni nuove.
- Le decisioni aperte sono elencate in `AGENTS.md` §15 e riassunte in [architettura](architettura.md#decisioni-aperte).
