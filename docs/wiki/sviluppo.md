# Sviluppo e verifica

## Prerequisiti

- Python 3.11+ e `uv`.
- Ollama con il modello di default: `ollama pull qwen3.5:0.8b`.
- Node 22+ e `corepack` (per `pnpm`).
- Rust + toolchain Tauri per la shell desktop (su questa macchina: `stable-x86_64-pc-windows-gnu`).

## Avvio

App desktop (avvia i servizi se il gateway è spento):

```bash
cd apps/desktop
corepack pnpm install
corepack pnpm tauri:dev
```

Solo browser:

```bash
python scripts/stack.py --dev          # cinque servizi, porte fisse, dev-token
cd apps/desktop && corepack pnpm dev   # http://localhost:5173
```

Aprire sempre `http://localhost:5173`: il gateway consente CORS per `localhost` e `127.0.0.1`, ma il dev server pubblica `localhost`.

## Supervisore `scripts/stack.py`

| Flag | Effetto |
| --- | --- |
| _(nessuno)_ | Porte dinamiche, token casuale, resta attivo fino a Ctrl+C |
| `--dev` | Porte fisse 8010-8014 e token `dev-token` per la UI |
| `--check` | Esegue il flusso completo in `data/check/`, stampa l'esito ed esce |
| `--no-sync` | Salta `uv sync` (utile quando le dipendenze sono già installate) |
| `--data <dir>` | Usa una cartella dati alternativa |

Porte in `--dev`:

| Servizio | Porta |
| --- | --- |
| gateway | 8010 |
| learning | 8011 |
| document | 8012 |
| rag | 8013 |
| ai | 8014 |

Variabili passate ai servizi: `NOESIS_TOKEN`, `NOESIS_DATA`, `NOESIS_MODEL`, `DOCUMENT_URL`, `RAG_URL`, `AI_URL`, `LEARNING_URL`. I log finiscono in `data/logs/<servizio>.log`.

## Check completo

```bash
python scripts/stack.py --check --no-sync
```

Atteso: cinque righe `ready`, poi

```
gateway   ok     tutor SSE (...)
gateway   ok     flashcard create + list + update
gateway   ok     posizione di lettura salvata e riletta
gateway   ok     annotazioni create + list + delete
gateway   ok     schede e posizione rimosse con il documento
gateway   ok     import + indice + ricerca + rebuild + delete (...)
servizi arrestati
```

Exit code 0 solo se tutto passa. `--check` usa `data/check/`, non tocca la libreria di sviluppo.

## Test e lint per servizio

```bash
cd services/<nome>
uv run pytest -q
uv run ruff check . && uv run ruff format --check .
uv run mypy app
```

In alternativa, senza cambiare cartella (usato negli script di verifica):

```bash
python -m uv run --project <abs services/nome> --directory <abs services/nome> pytest -q
```

Stato attuale: 52 test backend — document 11, rag 7, ai 8, learning 8, gateway 18.

Frontend:

```bash
cd apps/desktop
corepack pnpm test        # 25 test Vitest
corepack pnpm typecheck   # tsc --noEmit
corepack pnpm build       # build in dist/
```

## Valutazione RAG

Con lo stack `--dev` attivo:

```bash
python scripts/eval_rag.py
```

- Importa `evaluation/corpus/*.md`, indicizza, interroga le 48 domande di `evaluation/questions.jsonl`, controlla la sezione attesa nei primi 3 hit e ripulisce.
- Default: gateway `127.0.0.1:8010`, token `dev-token`, soglia 90%.
- `--keep` lascia i documenti importati; `--min-accuracy` cambia la soglia.
- Risultato attuale: 46/48 = 95,8% (gate superato). I due casi mancati sono documentati in `docs/poc-04.md`.

## Desktop Tauri

```bash
cd apps/desktop
corepack pnpm tauri:dev
corepack pnpm tauri:build
```

- `beforeDevCommand` è `corepack pnpm dev`; URL di sviluppo `http://localhost:5173`.
- La shell (`apps/desktop/src-tauri/src/lib.rs`) avvia `python scripts/stack.py --dev --no-sync` solo se `127.0.0.1:8010` non risponde.
- Alla chiusura termina l'albero di processi (`taskkill /T /F` su Windows).
- CSP ristretta in `tauri.conf.json`: connessioni solo verso `127.0.0.1:8010` e `ws://localhost:5173`.
- Il crate è `crate-type = ["rlib"]`: la `cdylib` rompe il linker mingw su questa macchina.

## Problemi noti

| Sintomo | Causa probabile | Rimedio |
| --- | --- | --- |
| UI con "Gateway non raggiungibile" o 502 | Servizio non avviato o crashato | Controlla `data/logs/<servizio>.log`; riavvia lo stack |
| `Address already in use` | Porte 8010-8014 occupate | Chiudi lo stack precedente o usa porte dinamiche |
| Prima risposta molto lenta | Modello Ollama non caricato | `ollama pull qwen3.5:0.8b`; il primo token può richiedere secondi |
| `pnpm` fallisce con EPERM | Installazione globale non permessa | Usa sempre `corepack pnpm` |
| Linker mingw: `export ordinal too large` | `cdylib` nel crate Tauri | Tieni solo `rlib` in `Cargo.toml` |
| CORS bloccato nel browser | URL `127.0.0.1` invece di `localhost` (o viceversa) | Apri `http://localhost:5173` |
| Test AI non trovano il package | `mypy_path`/path del monorepo | `mypy_path = "../../packages/ai-adapters"` in `services/ai/pyproject.toml`; `tests/__init__.py` presente |
| Dati sporchi da prove precedenti | Libreria di sviluppo condivisa | `--check` usa `data/check/`; per ripartire pulisci `data/` (vedi [dati](dati.md#ispezione-e-reset)) |
| Output illeggibile su Windows | Console cp1252 | Gli script usano testo ASCII negli esiti (niente `✗`, `≥`) |

## Comandi utili di ricognizione

```bash
rg "NOESIS_TOKEN" services packages      # auth e propagazione del token
rg "reading-positions|flashcards" -g "*.py" -g "*.ts" -g "*.tsx"
rg "forward\(" services/gateway           # tutte le chiamate proxate
rg "shortcut:" -g "*.py" -g "*.ts"        # debito tecnico marcato
```

La skill `ponytail` (`.opencode/skills/ponytail/SKILL.md`) vale per ogni task di codice: modifica minima completa e test per la logica non banale.
