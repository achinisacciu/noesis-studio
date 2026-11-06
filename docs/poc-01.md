# POC-01 — Microservizi locali

**Stato:** primo prototipo funzionante
**Obiettivo:** verificare che Document Service, RAG Service e Local API Gateway girino come processi Python indipendenti, comunicando solo via HTTP locale, con health check, errori uniformi e arresto controllato.

## Cosa è stato costruito

| Componente | Cartella | Ruolo |
| --- | --- | --- |
| Document Service | `services/document` | Crea e recupera documenti (store in memoria) |
| RAG Service | `services/rag` | Riceve una query, chiede il documento al Document Service, restituisce le frasi pertinenti |
| Local API Gateway | `services/gateway` | Unico punto di accesso: proxy verso i servizi e readiness aggregata |
| Contratti | `packages/contracts` | Modelli Pydantic condivisi, nessuna logica |
| Supervisore | `scripts/stack.py` | Avvia i tre processi su porte libere, attende `/ready`, arresta tutto |

Flusso verificato dal supervisore:

```
POST /api/documents  -> gateway -> document
POST /api/rag/search -> gateway -> rag -> document
```

## Endpoint

| Servizio | Endpoint | Auth |
| --- | --- | --- |
| tutti | `GET /health`, `GET /ready` | no |
| document | `POST /documents`, `GET /documents/{id}` | sì |
| rag | `POST /search` | sì |
| gateway | `POST /api/documents`, `GET /api/documents/{id}`, `POST /api/rag/search` | sì |

Formato di risposta unico:

```json
{ "status": "success", "data": {}, "error": null }
```

Gli errori usano le categorie di `docs/service-communication.md` §4.3. Il 404 è mappato su `VALIDATION_ERROR` perché il contratto non prevede ancora `NOT_FOUND`: da valutare quando si consolida il contratto.

## Esecuzione

```bash
python scripts/stack.py --check   # avvia, verifica il flusso completo, arresta
python scripts/stack.py           # avvia e resta attivo fino a Ctrl+C
```

Log dei servizi in `data/logs/`. I servizi si avviano con `NOESIS_TOKEN` condiviso generato dal supervisore.

> Il supervisore è oggi `scripts/stack.py`, che verifica anche il flusso POC-04 (import file, indice, ricerca con citazioni). I comandi originali `scripts/poc01.py` non esistono più.

Test e controlli, per singolo servizio:

```bash
cd services/document
uv run pytest -q
uv run ruff check . && uv run ruff format --check .
uv run mypy app
```

## Cosa è stato verificato

- Tre processi indipendenti avviati e arrestati senza processi residui.
- Porte assegnate dinamicamente dal supervisore.
- `/ready` di ogni servizio e readiness aggregata del gateway (503 se un servizio manca).
- Comunicazione gateway → servizio e servizio → servizio con timeout e mappatura errori.
- Token obbligatorio sulle API, rifiutato con 401.
- 15 test unitari (5 per servizio) su API, envelope degli errori e logica di ricerca.

## Limiti noti (fuori dal POC)

- Store in memoria: i documenti si perdono al riavvio. SQLite arriva con POC-04.
- La ricerca è per parole chiave, non semantica: embedding e ChromaDB sono POC-04.
- Nessuna integrazione Tauri: l'avvio è uno script Python. Il ciclo di vita da Tauri è POC-02 di `docs/service-communication.md`.
- Token condiviso unico; senza `NOESIS_TOKEN` i servizi restano aperti per lo sviluppo locale.
- Porte scelte dal supervisore e comunicate via variabili d'ambiente: la strategia definitiva resta APERTA (ADR-012 e COM-006).
