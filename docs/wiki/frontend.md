# Frontend

React 19 + TypeScript + Vite, dentro la shell Tauri 2. Nessuna logica di parsing, retrieval o generazione: solo UI e chiamate al gateway.

## Mappa dei file

| File | Ruolo |
| --- | --- |
| `src/main.tsx` | Bootstrap React, `QueryClientProvider` |
| `src/App.tsx` | Layout, stato del drawer (`reader` o `cards`), click citazione |
| `src/config.ts` | Istanza `ApiClient` da `VITE_GATEWAY_URL` e `VITE_NOESIS_TOKEN` |
| `src/api.ts` | Tutte le chiamate HTTP, envelope, errori tipizzati, generatore SSE |
| `src/types.ts` | Tipi speculari ai contratti Pydantic |
| `src/sse.ts` | Parser SSE tollerante a chunk spezzati e CRLF |
| `src/markdown.ts` | Grassetto, codice inline ed elenchi senza dipendenze |
| `src/reader.ts` | `ReaderTarget`, scelta del chunk citato/salvato, etichette |
| `src/components/DocumentPanel.tsx` | Import, lista, selezione, apertura, delete, rebuild |
| `src/components/TutorChat.tsx` | Domanda, streaming, stop, citazioni cliccabili |
| `src/components/DocumentReader.tsx` | Lettura chunk, citazione attiva, "Crea scheda", ripresa posizione |
| `src/components/FlashcardsPanel.tsx` | Elenco schede, filtro, mostra risposta, modifica, delete |
| `src/components/MessageText.tsx` | Rendering dei segmenti di `markdown.ts` |
| `src/styles.css` | Tutto lo stile: variabili, layout, componenti, responsive |
| `src/*.test.ts` | Test Vitest di client, SSE, reader e markdown |

## Stato e flussi

- **Server state** con TanStack Query; **local state** con `useState`.
- Query key usate: `["documents"]`, `["chunks", documentId]`, `["reading-position", documentId]`, `["flashcards", filterId]`.
- `App` tiene `selectedId` (documento attivo per il tutor) e `drawer`:
  - `{ kind: "reader", target }`
  - `{ kind: "cards" }`
  - `null`
- Un click su una citazione apre il reader con `{ documentId, page, section }`; un click su un documento lo apre con pagina e sezione `null`, così il reader riprende dalla posizione salvata.
- Dopo mutazioni su schede o posizione si invalidano le query `["flashcards"]`; dopo import/delete `["documents"]`.

### Tutor

1. `TutorChat` invia la domanda con `client.chat(...)`, che fa `fetch` e restituisce un async generator di eventi.
2. Gli eventi `citation` popolano le citazioni, i `token` il testo, `done`/`error` chiudono il messaggio.
3. "Ferma" abortisce il `fetch`; il cleanup avviene a unmount.
4. Ogni citazione è un bottone: il click risale ad `App`, che apre il reader.

### Reader e ripresa

- `selectStartIndex(chunks, target, savedChunkId)` in `reader.ts` decide il punto: citazione → pagina/sezione, altrimenti chunk salvato, altrimenti nessuno.
- Il reader chiede la posizione solo quando non c'è citazione (`enabled` sulla query).
- Lo scorrimento calcola il primo chunk che ha superato il bordo del contenitore e salva `chunk_id` + `position` via `PUT` (throttle `requestAnimationFrame`, nessun salvataggio se il chunk non cambia).
- "Crea scheda" apre una modale con fronte/retro precompilati dal chunk e salva via `POST /api/flashcards`.
- Le schede hanno sezione/pagina del chunk, quindi la fonte resta visibile.

### Flashcard

- Elenco filtrabile per documento selezionato, con "Mostra risposta" e modifica inline.
- Delete immediato, senza conferma; lo stato vuoto spiega come creare la prima scheda.
- Errori di mutazione mostrati in `.notice.error` senza stack trace.

## Client API

`ApiClient` incapsula URL e token:

- `listDocuments`, `importDocument`, `getChunks`, `deleteDocument`, `indexDocument`, `rebuildIndex`
- `listFlashcards`, `createFlashcard`, `updateFlashcard`, `deleteFlashcard`
- `getReadingPosition`, `saveReadingPosition`
- `chat(question, documentId, signal)` → async generator di `TutorEvent`

Regole:

- Tutte le URL passano dal gateway: mai `8011`-`8014` dal browser.
- `envelope()` estrae `data` e traduce `error` in `ApiRequestError` con `code`.
- Le API restituiscono `Promise` tipizzate; niente `any` (strict mode).
- Il token viene da `VITE_NOESIS_TOKEN` (default `dev-token`); in produzione dovrà arrivare dalla shell.

## Stili

- Un solo `styles.css`, con variabili CSS in `:root` (tema scuro).
- Classi per area: `.layout`, `.panel`, `.chat`, `.reader`, `.flashcard`, `.modal`, `.button`.
- Il reader e il pannello schede condividono `.reader` / `.reader-head` / `.reader-body` (drawer a destra).
- Responsive sotto 820 px: layout a colonna singola.
- Feedback immediato: pulsanti disabilitati durante le mutazioni, testi "Salvo…", "Importo…".

## Test

Comandi da `apps/desktop`: `corepack pnpm test`, `pnpm typecheck`, `pnpm build`.

| File | Copre |
| --- | --- |
| `src/api.test.ts` | Envelope, token, import, flashcard, posizione, stream SSE |
| `src/sse.test.ts` | Chunk spezzati, CRLF, eventi multipli, commenti |
| `src/reader.test.ts` | Sezione vs pagina, priorità citazione, ripresa, etichette |
| `src/markdown.test.ts` | Grassetto, codice, elenchi |

Stato attuale: 18 test, `tsc` e `vite build` puliti. Nessun test di componente o E2E: le verifiche UI sono manuali (vedi `docs/frontend.md`).

## Ricette

### Aggiungere una chiamata API

1. Metodo tipizzato in `src/api.ts` con envelope.
2. Tipo in `src/types.ts` (specchio del contratto).
3. Proxy nel gateway e rotta nel servizio proprietario.
4. Test in `src/api.test.ts` con `fetch` mockato.

### Aggiungere un pannello o una schermata

1. Componente in `src/components/`.
2. Nuovo caso nel tipo `Drawer` di `App.tsx` e relativo render.
3. Classi in `styles.css`, riusando `.reader` se è un drawer.
4. Query con chiave propria e invalidazione dopo le mutazioni.

### Aggiungere un evento SSE

1. Contratto evento in `packages/contracts`.
2. Emissione in `services/ai/app/api/routes.py` con `format_event`.
3. Variante in `TutorEvent` (`src/types.ts`) e gestione in `TutorChat`.
4. Test del parser e del client.

## Trappole note

- Il dev server Vite va aperto su `http://localhost:5173`, non `127.0.0.1`, per rispettare il CORS del gateway.
- `corepack pnpm` è obbligatorio: il `pnpm` globale non è installabile senza permessi.
- Non duplicare server state in store globali: usa query e invalidazioni.
- Il reader mostra il testo dei chunk, non il PDF originale.
- Una sola conversazione, non persistita; il testo del modello è reso in modo minimale.
