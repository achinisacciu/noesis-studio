# Funzionalità: dalla storia utente ai file

Tabella di raccordo tra ciò che l'utente vede e il codice che lo realizza. Le storie complete sono in `docs/user-stories.md`.

## Implementato

| Funzionalità | Storia | Backend | Frontend | Test / verifica |
| --- | --- | --- | --- | --- |
| Import PDF/DOCX/MD/TXT con chunk e citazioni | A1 | `services/document/app/api/routes.py`, `parsing.py`, `store.py` | `DocumentPanel.tsx` | 11 test Document; `docs/poc-04.md` |
| Indicizzazione e rebuild | A2 (parziale) | `services/rag/app/index.py`, `api/routes.py`; `gateway` `/api/index/*` | `DocumentPanel.tsx` (Importa, Ricostruisci) | 7 test RAG; `--check` |
| Tutor in streaming con citazioni | B2, B5 | `services/ai/app/api/routes.py`, `prompt.py`, `sse.py`; gateway `/api/ai/chat` | `TutorChat.tsx`, `sse.ts`, `markdown.ts`, `MessageText.tsx` | 8 test AI; `api.test.ts`, `sse.test.ts`, `markdown.test.ts`; `--check` |
| Citazione cliccabile → lettore sul passaggio | B2 | hit con `page`/`section` da RAG | `reader.ts`, `DocumentReader.tsx`, `App.tsx` | `reader.test.ts`; verifica manuale |
| Ripresa della lettura | A4 | `services/learning/app/api/routes.py`, `store.py`; gateway `/api/reading-positions/*` | `DocumentReader.tsx`, `DocumentPanel.tsx`, `App.tsx` | 2 test Learning, 2 test gateway, `reader.test.ts`, `api.test.ts`; verifica manuale con riavvio |
| Evidenziazioni, note e segnalibri | A3 | `services/document/app/api/routes.py`, `store.py`; gateway `/api/documents/{id}/annotations`, `/api/annotations/{id}` | `DocumentReader.tsx`, `annotations.ts` | 3 test Document, 1 test gateway, `annotations.test.ts`; `--check` |
| Flashcard manuali con fonte | F1 (manuale) | `services/learning/app/api/routes.py`, `store.py`; gateway `/api/flashcards*` | `DocumentReader.tsx` (crea), `FlashcardsPanel.tsx` | 6 test Learning, 3 test gateway, `api.test.ts`; verifica manuale |
| Eliminazione documento con pulizia derivati | A1, A2 | gateway `delete_document` + test ordine/abort | `DocumentPanel.tsx` | 3 test gateway; `--check` |
| Valutazione delle citazioni RAG | gate MVP | `scripts/eval_rag.py`, `evaluation/` | — | 48 domande, 46 corrette (95,8%), soglia 90% |

### Traccia: import → indice → domanda

1. `DocumentPanel` chiama `client.importDocument(file)`.
2. Gateway inoltra il multipart a Document; Document parsa, chunkka e salva.
3. Il client chiama subito `client.indexDocument(id)`.
4. Gateway → RAG; RAG legge i chunk da Document e scrive Chroma.
5. `TutorChat` chiama `client.chat`; AI cerca in RAG, emette citazioni, prompt, token.

Punti di modifica tipici: un nuovo formato richiede `PARSERS` in `parsing.py`; un nuovo evento SSE richiede contratto + AI + `TutorChat`.

### Traccia: apertura documento e ripresa

1. Click su un documento in `DocumentPanel` → `onSelect` + `onOpen`.
2. `App` apre `DocumentReader` con target `{ page: null, section: null }`.
3. Reader legge `GET /api/reading-positions/{id}` e calcola `selectStartIndex`.
4. Lo scroll salva `PUT /api/reading-positions/{id}` con throttle.
5. Una citazione passa pagina/sezione: la posizione salvata viene ignorata.

### Traccia: annotazioni

1. La selezione dentro un chunk diventa `{ chunk_id, start, end }` con `rangeOffsets`.
2. `POST /api/documents/{id}/annotations` salva evidenziazione o nota; la stella salva un `bookmark`.
3. Il reader ricarica `GET .../annotations` e rende i tratti con `segmentsFor`.
4. L'elenco "Annotazioni" filtra nota e testo del chunk, scorre al passaggio e consente il delete.
5. Il documento eliminato porta con sé le annotazioni per cascade; nessuna pulizia nel gateway.

### Traccia: creazione e ripasso scheda

1. Nel reader, "Crea scheda" su un chunk precompila fronte (`Spiega: <sezione>` o "Spiega questo passaggio") e retro (testo del chunk).
2. `POST /api/flashcards` salva con `page`/`section` del chunk.
3. Il pannello "Schede" legge `GET /api/flashcards` (eventualmente filtrato).
4. "Mostra risposta", modifica (`PATCH`) e delete (`DELETE`) aggiornano la lista.

## Non ancora implementato

| Funzionalità / storia | Cosa manca | Dove andrebbe |
| --- | --- | --- |
| Spazi di lavoro per materia (A6) | `workspace_id` diffuso, indici separati | Contratti, tutti gli store, routing RAG, UI |
| Toolbar contestuale sulla selezione (B1) | Testo selezionato nella richiesta, pannello risposta | `DocumentReader`, `TutorRequest`, `TutorChat` |
| Livelli di rigore 1-3 (C1) | Livello nel contratto e nel prompt | `TutorRequest`, `prompt.py`, toolbar UI |
| Widget interattivi (D1) | Modello di lezione e blocchi | Frontend + contenuti; nessun motore lezioni oggi |
| Notebook Python in sandbox (E1-E3) | Notebook Service, isolamento, streaming bidirezionale | Nuovo servizio; **dipende da ADR-010** (tecnologia sandbox) |
| Auto-generazione flashcard (F1 completo) | Generazione dal documento, revisione | AI + Learning + **Job Service** (operazione > 2 s) |
| Quiz a risposta multipla (F3) | Banco domande, valutazione, padronanza | Learning + AI + **Job Service**; schema progressi |
| Job Service | Coda persistente, stati, retry | Nuovo servizio; regola `AGENTS.md` §11 |
| Persistenza conversazione | Tabella + ripristino UI | Learning o servizio dedicato; decidere ownership |
| Import di una cartella di risorse | Oggi solo un file alla volta; niente scansione né coda | Document (endpoint batch) + UI, sopra `resources/` |
| Sidecar Python nel bundle | Packaging e avvio senza repo | `apps/desktop/src-tauri`, `scripts/` (vedi `docs/poc-05.md`) |
| Test E2E Playwright | Percorso completo automatico | `tests/` o `apps/desktop/e2e` |

Per le priorità: `docs/roadmap.md` (MVP, v1, v2). Per i criteri di accettazione: `docs/user-stories.md`.

## Dove finisce una funzionalità

Una funzionalità è completa quando ha:

1. contratto (se espone dati nuovi) in `packages/contracts`;
2. rotta nel servizio proprietario + proxy nel gateway;
3. UI o client che la usa;
4. test di servizio, proxy e (se c'è logica) frontend;
5. flusso in `scripts/stack.py --check` se attraversa più servizi;
6. riga in questa tabella e aggiornamento della pagina wiki dell'area.
