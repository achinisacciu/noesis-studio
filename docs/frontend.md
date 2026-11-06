# Interfaccia desktop

**Stato:** primo client funzionante (Vite + React + TypeScript), wrapper Tauri non ancora aggiunto.

## Cosa è stato costruito

| Area | File | Ruolo |
| --- | --- | --- |
| Client API | `apps/desktop/src/api.ts` | Envelope, errori tipizzati, import multipart, indice, chat SSE |
| Parser SSE | `apps/desktop/src/sse.ts` | Eventi `event:`/`data:` con chunk spezzati e CRLF |
| Documenti | `apps/desktop/src/components/DocumentPanel.tsx` | Import, lista, selezione, delete, rebuild |
| Tutor | `apps/desktop/src/components/TutorChat.tsx` | Domanda, streaming, stop, citazioni cliccabili |
| Config | `apps/desktop/src/config.ts` | Gateway e token da variabili Vite |

Tutte le chiamate passano dal gateway: il frontend non contatta mai direttamente Document, RAG o AI Service.

## Flusso

1. L'utente importa un file: il client chiama `POST /api/documents` e poi `POST /api/index/{id}`.
2. La lista documenti è server state gestito con TanStack Query.
3. La domanda apre `POST /api/ai/chat` con `fetch` e legge il body come stream.
4. Gli eventi SSE aggiornano il messaggio: prima le citazioni, poi i token.
5. "Ferma" abortisce la fetch; il gateway e l'AI Service chiudono la generazione.

## Esecuzione

```bash
python scripts/stack.py --dev     # backend su porte fisse e token dev-token
cd apps/desktop && corepack pnpm dev
```

Default del client: `http://127.0.0.1:8010`, token `dev-token`. Sovrascrivibili con `.env.local` (vedi `.env.example`).

## Verifica

- 5 test Vitest (parser SSE e client API, incluso lo stream del tutor).
- `tsc --noEmit` e `vite build` puliti.
- Flusso verificato nel browser: import di `statistica.md` → 3 chunk → indice → domanda → risposta in streaming con citazioni `[1]`-`[3]`.
- CORS del gateway limitato a `http://localhost:5173` e `http://127.0.0.1:5173` (configurabile con `NOESIS_FRONTEND_ORIGIN`).

## Limiti noti

- Nessun wrapper Tauri: niente packaging desktop, sidecar o lifecycle gestito dall'app.
- Nessun lettore PDF: le citazioni selezionano il documento ma non aprono la pagina.
- Token e URL non sono configurabili da UI.
- Una sola conversazione, non persistita.
- Nessun test E2E Playwright né test di accessibilità.
- Il modello locale può citare fonti parziali o dichiarare "nessuna fonte" in modo impreciso: serve il set di valutazione RAG.
