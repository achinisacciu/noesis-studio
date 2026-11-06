# Interfaccia desktop

**Stato:** client React/TypeScript dentro una shell Tauri 2; avvio e arresto dei servizi gestiti dalla shell in sviluppo.

## Cosa è stato costruito

| Area | File | Ruolo |
| --- | --- | --- |
| Client API | `apps/desktop/src/api.ts` | Envelope, errori tipizzati, import multipart, indice, chat SSE, flashcard, annotazioni |
| Parser SSE | `apps/desktop/src/sse.ts` | Eventi `event:`/`data:` con chunk spezzati e CRLF |
| Documenti | `apps/desktop/src/components/DocumentPanel.tsx` | Import, lista, selezione, delete, rebuild |
| Tutor | `apps/desktop/src/components/TutorChat.tsx` | Domanda, streaming, stop, citazioni cliccabili |
| Lettore | `apps/desktop/src/components/DocumentReader.tsx` | Testo del documento, evidenzia il punto citato, annota, crea schede, riprende la lettura |
| Annotazioni | `apps/desktop/src/annotations.ts` | Segmenti evidenziati e offset della selezione |
| Schede | `apps/desktop/src/components/FlashcardsPanel.tsx` | Elenco, filtro per documento, mostra risposta, modifica, delete |
| Corrispondenza citazione | `apps/desktop/src/reader.ts` | Sezione citata, altrimenti pagina |
| Config | `apps/desktop/src/config.ts` | Gateway e token da variabili Vite |

Tutte le chiamate passano dal gateway: il frontend non contatta mai direttamente Document, RAG, AI o Learning Service.

## Flusso

1. L'utente importa un file: il client chiama `POST /api/documents` e poi `POST /api/index/{id}`.
2. La lista documenti è server state gestito con TanStack Query.
3. La domanda apre `POST /api/ai/chat` con `fetch` e legge il body come stream.
4. Gli eventi SSE aggiornano il messaggio: prima le citazioni, poi i token.
5. "Ferma" abortisce la fetch; il gateway e l'AI Service chiudono la generazione.
6. Cliccare una citazione apre il lettore sul documento e mette in evidenza il chunk con la sezione citata (o la pagina, se la sezione non esiste).
7. "Crea scheda" su un passaggio apre una modale con fronte e retro precompilati dal chunk; il salvataggio passa da `POST /api/flashcards`.
8. "Schede" nella barra superiore apre l'elenco: filtro per documento selezionato, "Mostra risposta", modifica e delete via `PATCH`/`DELETE /api/flashcards/{id}`.
9. Cliccare un documento apre il lettore. Senza citazione, il punto di partenza è l'ultima posizione salvata (`GET /api/reading-positions/{id}`); lo scorrimento salva il chunk corrente con `PUT`, quindi la posizione sopravvive alla chiusura dell'app.
10. Nel lettore, selezionare del testo mostra "Evidenzia" e "Nota": salvano un'annotazione con offset relativi al chunk (`POST /api/documents/{id}/annotations`). La stella su un chunk aggiunge o toglie un segnalibro; "Annotazioni" elenca, cerca e riporta al passaggio.

## Esecuzione

Desktop (shell Tauri, avvia anche i servizi se il gateway è spento):

```bash
cd apps/desktop
corepack pnpm tauri:dev
```

Solo browser:

```bash
python scripts/stack.py --dev     # backend su porte fisse e token dev-token
cd apps/desktop && corepack pnpm dev
```

Default del client: `http://127.0.0.1:8010`, token `dev-token`. Sovrascrivibili con `.env.local` (vedi `.env.example`).

## Verifica

- 25 test Vitest (parser SSE, client API, corrispondenza citazione → chunk, ripresa della lettura, annotazioni, formattazione del testo).
- `tsc --noEmit` e `vite build` puliti.
- Flusso verificato nel browser: import di `statistica.md` → 3 chunk → indice → domanda → risposta in streaming con citazioni `[1]`-`[3]` → clic su `[2]` → lettore aperto con la sezione "Varianza" evidenziata.
- Flashcard verificate nel browser: "Crea scheda" su un chunk → fronte e retro precompilati → salvataggio → pannello "Schede" con la scheda → "Mostra risposta" → modifica del fronte → delete → stato vuoto.
- Ripresa della lettura verificata: apertura del documento, scorrimento fino a "Mediana", chiusura e riapertura sul chunk salvato; posizione riletta dal Learning Service dopo il riavvio dello stack.
- Annotazioni verificate nel browser: selezione di una frase → "Evidenzia" → tratto evidenziato; "Nota" con testo → comparsa nell'elenco; stella → segnalibro; ricerca nell'elenco; delete.
- CORS del gateway limitato a `http://localhost:5173` e `http://127.0.0.1:5173` (configurabile con `NOESIS_FRONTEND_ORIGIN`).
- Finestra desktop: avvio con `tauri:dev`, servizi avviati dalla shell, chiusura senza processi residui (dettagli in [poc-05.md](poc-05.md)).

## Limiti noti

- Il bundle di produzione non include i servizi Python: serve Python nel PATH e il repo. Sidecar impacchettato ancora da fare.
- La shell desktop usa `dev-token`: il token casuale richiede IPC tra Rust e frontend.
- Il lettore mostra il testo estratto dai chunk, non il PDF originale: manca il rendering della pagina con PyMuPDF/PDF.js.
- Le citazioni con sola pagina (PDF) evidenziano il primo chunk di quella pagina.
- Token e URL non sono configurabili da UI.
- Una sola conversazione, non persistita.
- Le flashcard sono solo manuali: niente generazione automatica dal documento, ripetizione spaziata o quiz.
- La posizione è per documento, non per workspace: nessuna cronologia dei punti visitati.
- Le annotazioni sono ancorate al testo dei chunk, non alle coordinate del PDF: cambiano se il documento viene reimportato.
- Il testo del modello è reso in modo minimale: grassetto, codice inline ed elenchi; niente tabelle, link o titoli.
- Nessun test E2E Playwright né test di accessibilità.
- Il modello locale può citare fonti parziali o dichiarare "nessuna fonte" in modo impreciso: serve il set di valutazione RAG.
