# POC-02/03 — Runtime AI, adapter e streaming

**Stato:** completato
**Obiettivo:** collegare un runtime AI locale tramite adapter, costruire il prompt con le fonti RAG e trasmettere la risposta al client in streaming SSE, con citazioni e gestione degli errori.

## Cosa è stato costruito

| Componente | Cartella | Ruolo |
| --- | --- | --- |
| Contratto adapter | `packages/ai-adapters` | `RuntimeAdapter`, `ChatRequest`, `ChatChunk`, `ModelInfo`, `AdapterError` |
| Adapter Ollama | `packages/ai-adapters/noesis_ai_adapters/ollama.py` | Lista modelli, chat in streaming NDJSON, abort, health |
| AI Service | `services/ai` | Recupero fonti dal RAG, prompt, streaming SSE, citazioni |
| Gateway | `services/gateway` | `POST /api/ai/chat` inoltrato senza bufferizzare, `GET /api/ai/models` |
| Supervisore | `scripts/stack.py` | Avvia anche l'AI Service e verifica la risposta del tutor |

Flusso verificato:

```
POST /api/ai/chat -> gateway -> ai -> rag (search)
                              -> adapter -> Ollama (stream)
                              -> SSE: citation, token, done
```

## Contratto adapter

`RuntimeAdapter` espone `list_models`, `chat`, `abort`, `health`. L'AI Service dipende solo dal protocollo: cambiare runtime significa aggiungere un adapter, non modificare le route.

L'adapter Ollama usa `POST /api/chat` con `stream=true` e `think=false` (i modelli con reasoning non emettono testo utile nei primi chunk). Le capacità dichiarate sono `{"chat"}`.

## Prompt e citazioni

- L'AI Service chiede al RAG Service i chunk pertinenti (filtro opzionale per documento).
- Il prompt contiene le fonti numerate con `document_id`, pagina e sezione.
- Il modello deve citare con `[n]` e dichiarare "Nessuna fonte nei documenti" se il contesto non basta.
- Se la ricerca non restituisce hit, il modello **non viene chiamato**: il servizio risponde con il messaggio esplicito e zero citazioni.
- Le citazioni vengono inviate come eventi SSE prima dei token: il client può mostrare le fonti mentre il testo arriva.

## Eventi SSE

Formato: `event: <nome>` + `data: <json>`.

| Evento | Payload | Quando |
| --- | --- | --- |
| `citation` | `Citation` (`document_id`, `page`, `section`, `snippet`) | una per fonte, prima dei token |
| `token` | `{"delta": "..."}` | per ogni frammento di testo |
| `done` | `{"model": "...", "citations": n}` | fine risposta |
| `error` | `{"code": "TIMEOUT" \| ..., "message": "..."}` | errore runtime o dipendenza |

Il gateway inoltra i byte SSE con `StreamingResponse` e non bufferizza. Se l'AI Service non è raggiungibile, il gateway emette un evento `error` invece di rompere lo stream.

## Esecuzione

Prerequisiti: Ollama attivo su `127.0.0.1:11434` e un modello installato.

```bash
ollama pull qwen3.5:0.8b          # una volta sola
python scripts/stack.py --check   # import -> indice -> ricerca -> tutor SSE -> rebuild -> delete
python scripts/stack.py           # avvio interattivo
```

Modello configurabile con `NOESIS_MODEL` (default `qwen3.5:0.8b`), runtime con `OLLAMA_URL`.

## Cosa è stato verificato

- Adapter Ollama: lista modelli, streaming reale, health, abort su disconnessione.
- AI Service: prompt con fonti, eventi `citation`/`token`/`done`, nessuna chiamata al modello senza fonti, errore runtime propagato come evento.
- Gateway: passthrough SSE e inoltro di `/api/ai/models`.
- Flusso end-to-end dal supervisore: risposta di 545 caratteri con 1 citazione su un documento Markdown importato.
- 31 test unitari totali (8 document, 7 rag, 8 gateway, 8 ai), `ruff` e `mypy --strict` puliti.
- Avvio e arresto dei quattro processi senza processi residui.

## Limiti noti

- Primo token intorno a 2,8 s con `qwen3.5:0.8b` su CPU: il gate di 1,5 s dell'MVP non è ancora rispettato con questo modello.
- Un solo modello selezionato via ambiente: manca la UI di scelta e il fallback tra modelli.
- Nessuna cronologia conversazionale: ogni richiesta è indipendente.
- Nessun budget esplicito per la finestra di contesto: con molti hit il prompt può diventare lungo.
- L'abort è best-effort: chiude la risposta HTTP verso Ollama, non annulla il lavoro già accodato nel runtime.
- Nessun set di valutazione delle citazioni: il gate RAG al 90% resta da costruire.
- Il tutor non applica ancora i livelli didattici 1-3 previsti dall'architettura.
