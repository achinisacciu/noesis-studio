# POC-05 — Shell desktop Tauri 2

**Stato:** in verifica
**Obiettivo:** aprire l'interfaccia in una finestra desktop nativa, avviare i servizi Python all'apertura e arrestarli alla chiusura, senza processi residui.

## Cosa è stato costruito

| Componente | Cartella | Ruolo |
| --- | --- | --- |
| Shell Tauri 2 | `apps/desktop/src-tauri` | Finestra nativa, CSP, icona, ciclo di vita |
| Supervisore servizi | `scripts/stack.py --dev` | Avvia document, rag, ai, learning e gateway su porte fisse con `dev-token` |
| Frontend | `apps/desktop/src` | Stessa UI React, invariata: parla solo con il gateway |

## Ciclo di vita

1. Tauri esegue `corepack pnpm dev` (Vite su `http://localhost:5173`).
2. Nel `setup` la shell prova a connettersi a `127.0.0.1:8010`.
3. Se il gateway è spento, avvia `python scripts/stack.py --dev --no-sync` dalla radice del repo.
4. Alla chiusura della finestra, `RunEvent::Exit` termina l'albero di processi con `taskkill /T /F` (Windows) o `kill` (altri sistemi).

Se il gateway è già attivo, la shell non avvia un secondo stack: si può tenere il backend in un terminale separato.

## Configurazione

- Finestra: 1280×820, minimo 900×600, centrata.
- CSP: `default-src 'self'`, connessioni solo verso `127.0.0.1:8010` e `ws://localhost:5173`; niente script remoti.
- Icone generate da `src-tauri/icons/logo.svg`.
- `bundle.targets = "all"`: installer nativo per la piattaforma corrente.

## Esecuzione

```bash
cd apps/desktop
corepack pnpm install
corepack pnpm tauri:dev
```

Build del bundle:

```bash
corepack pnpm tauri:build
```

## Cosa è stato verificato

- `cargo build` del crate `noesis-desktop` con toolchain `stable-x86_64-pc-windows-gnu`.
- Avvio con `corepack pnpm tauri:dev` a gateway spento: la finestra si apre, la shell avvia `scripts/stack.py --dev --no-sync` e i cinque servizi rispondono su 8010/8011/8012/8013/8014.
- La UI dentro la finestra carica la libreria dal gateway (documento `statistica`, 3 chunk) e mostra il pannello tutor.
- Chiusura con `WM_CLOSE`: l'albero di processi Python viene terminato, porte 8010-8014 libere, nessun processo `python`, `node` o `noesis-desktop` residuo.
- Avvio con gateway già attivo: la shell non avvia un secondo stack e, alla chiusura della finestra, lascia attivo quello esterno.
- `python scripts/stack.py --check --no-sync` completo: import, indice, ricerca con citazione, rebuild, tutor SSE, creazione/lettura/modifica delle flashcard, posizione di lettura e delete cascade.
- Test CORS del gateway per l'origine `http://tauri.localhost` del webview di produzione.

Durante la prima compilazione il linker mingw ha rifiutato la `cdylib` (`export ordinal too large: 91023`). Il crate desktop ora dichiara solo `crate-type = ["rlib"]`, che è quanto serve al binario; `staticlib` e `cdylib` restano utili solo ai target mobili.

## Limiti noti

- Il binario di produzione non include i servizi Python: cerca `scripts/stack.py` risalendo dalla directory corrente e richiede Python nel PATH. Il sidecar impacchettato (PyInstaller o equivalente) è il passo successivo.
- Il bundle (`corepack pnpm tauri:build`) non è stato provato: su questa macchina manca la toolchain MSVC e il packaging NSIS non è stato scaricato.
- Il token resta `dev-token` perché il supervisore parte in modalità `--dev`. Un token casuale richiede un canale IPC tra shell e frontend.
- Nessuna gestione di crash del backend con riavvio automatico o messaggio in UI.
- Nessun test automatico della shell Rust: la verifica è manuale (finestra, gateway, processi residui).
