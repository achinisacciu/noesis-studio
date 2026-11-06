# Noesis Studio — desktop

Applicazione desktop Tauri 2 con interfaccia React/TypeScript: importa documenti, li indicizza e interroga il tutor locale con citazioni.

## Avvio rapido (desktop)

Dalla cartella `apps/desktop`:

```bash
corepack pnpm install
corepack pnpm tauri:dev
```

`tauri:dev` avvia Vite e apre la finestra nativa. Se il gateway `127.0.0.1:8010` non risponde, la shell avvia da sola `python scripts/stack.py --dev --no-sync` e arresta i servizi alla chiusura della finestra.

## Avvio solo browser

Utile per lavorare sulla UI senza compilare Rust:

```bash
python scripts/stack.py --dev     # gateway 8010, document 8012, rag 8013, ai 8014, token dev-token
cd apps/desktop
corepack pnpm dev                 # http://localhost:5173
```

Il client usa `http://127.0.0.1:8010` e `dev-token` come default. Per cambiarli, copia `.env.example` in `.env.local`.

## Comandi

```bash
corepack pnpm test        # Vitest
corepack pnpm typecheck   # tsc --noEmit
corepack pnpm build       # build di produzione in dist/
corepack pnpm tauri:dev   # finestra desktop in sviluppo
corepack pnpm tauri:build # bundle desktop (installer nella cartella target)
```

`corepack pnpm` è usato al posto di `pnpm` perché sul sistema attuale il binario globale non è installabile senza permessi di amministratore.

## Cosa c'è

- Shell Tauri 2: finestra 1280×820, icona del prodotto, CSP ristretta a gateway e dev server.
- Ciclo di vita dei servizi: avvio automatico del supervisore Python se il gateway è spento, arresto dell'intero albero di processi alla chiusura.
- Lista documenti con import PDF/DOCX/MD/TXT, chunk count ed eliminazione.
- Import che indicizza subito il documento; pulsante per ricostruire l'indice.
- Chat in streaming SSE con stop, citazioni cliccabili e selezione del documento.
- Lettore del documento che si apre sulla citazione ed evidenzia il punto citato.
- Testo del tutor con grassetto, codice ed elenchi resi leggibili.
- Tema scuro e layout responsive.

## Cosa manca

- Sidecar Python impacchettato: in build di produzione l'app cerca `scripts/stack.py` nel repo e richiede Python installato.
- Token di sessione generato a runtime e passato alla UI: oggi la shell desktop usa `dev-token`.
- Rendering del PDF originale: il lettore mostra il testo estratto dai chunk.
- Impostazioni per gateway, token e modello.
- Persistenza della conversazione e cronologia.
- Test E2E Playwright.
