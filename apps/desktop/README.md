# Noesis Studio — desktop

Interfaccia React/TypeScript per importare documenti, indicizzarli e interrogare il tutor locale con citazioni.

## Sviluppo

Dalla radice del repo:

```bash
python scripts/stack.py --dev     # gateway 8010, document 8012, rag 8013, ai 8014, token dev-token
```

In un secondo terminale:

```bash
cd apps/desktop
corepack pnpm install
corepack pnpm dev                 # http://localhost:5173
```

Il client usa `http://127.0.0.1:8010` e `dev-token` come default. Per cambiarli, copia `.env.example` in `.env.local`.

## Comandi

```bash
corepack pnpm test        # Vitest
corepack pnpm typecheck   # tsc --noEmit
corepack pnpm build       # build di produzione in dist/
```

`corepack pnpm` è usato al posto di `pnpm` perché sul sistema attuale il binario globale non è installabile senza permessi di amministratore.

## Cosa c'è

- Lista documenti con import PDF/DOCX/MD/TXT, chunk count ed eliminazione.
- Import che indicizza subito il documento; pulsante per ricostruire l'indice.
- Chat in streaming SSE con stop, citazioni cliccabili e selezione del documento.
- Lettore del documento che si apre sulla citazione ed evidenzia il punto citato.
- Testo del tutor con grassetto, codice ed elenchi resi leggibili.
- Tema scuro e layout responsive.

## Cosa manca

- Wrapper Tauri 2: per ora l'app gira nel browser.
- Rendering del PDF originale: il lettore mostra il testo estratto dai chunk.
- Impostazioni per gateway, token e modello.
- Persistenza della conversazione e cronologia.
- Test E2E Playwright.
