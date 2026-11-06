# AGENTS.md — Guida per agenti AI di sviluppo

> **Nota:** questo file è un documento operativo per gli agenti AI (Claude Code, Cursor, Cline, Aider, ecc.) che lavorano sul progetto. Non sostituisce i documenti di riferimento, che restano la fonte di verità. Va aggiornato quando vengono prese decisioni architetturali (ADR) o vengono chiusi i POC.

---

## 1. Scopo e documenti di riferimento

Prima di qualunque modifica, l'agente deve leggere:

| Documento | Ruolo |
| --- | --- |
| `docs/PRD.md` | Visione, utenti, metriche, ambito MVP |
| `docs/roadmap.md` | Ordine delle fasi e gate |
| `docs/user-stories.md` | Criteri verificabili per ogni funzionalità |
| `docs/architecture.md` (v0.2) | Architettura, microservizi, persistenza, AI, sandbox |
| `docs/service-communication.md` (v0.1) | Protocolli, processi, gateway, sicurezza locale |
| `docs/wiki/README.md` | Wiki di implementazione: dove guardare per area (servizi, frontend, dati, comandi) |

Questo `AGENTS.md` è la **traduzione operativa** di quei documenti: comandi, regole architetturali, DO/DON'T, workflow. In caso di conflitto, prevale il documento di riferimento.

## 1.1 Skill operativa: ponytail

Ogni task di codice usa la skill `ponytail` in `.opencode/skills/ponytail/SKILL.md`: la modifica più piccola che risolve il task per intero, con un test per la logica non banale.

- È una copia vendorizzata di [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), licenza MIT. Non modificarla a mano.
- Aggiornala a inizio sessione con `node scripts/update-ponytail.mjs`: riscarica le sei skill dall'upstream e registra il commit installato in `.opencode/skills/.ponytail-rev`.

---

## 2. Panoramica del prodotto

- **Cosa:** piattaforma desktop **local-first**, open source, per lo studio di Statistica, Matematica, ML e DL.

- **Come:** lettore documenti + tutor IA con RAG citazionale + notebook Python sandbox + flashcard/quiz.

- **Dove:** sulla macchina dell'utente. Nessuna dipendenza da API a pagamento. Rete opzionale (solo ricerca web livello 3).

- **Lingua:** italiano per UI e documentazione di prodotto (da confermare per i contenuti).

- **Utente target:** autodidatta tecnico, studente universitario, professionista che cambia ambito.

---

## 3. Stack tecnologico e toolchain

| Ambito | Scelta | Note |
| --- | --- | --- |
| Desktop shell | **Tauri 2** | Rust, sidecar per i servizi Python |
| Frontend | **React + TypeScript + Vite** | Strict mode, TanStack Query per server state |
| Backend | **Python 3.11+ con FastAPI** | Un processo per servizio |
| Persistenza relazionale | **SQLite** (WAL, `foreign_keys=ON`) | Separazione logica per servizio |
| Persistenza vettoriale | **ChromaDB** | Indice derivato, ricostruibile |
| Runtime AI | **Adapter multipli** (Ollama iniziale, llama.cpp da valutare) | Contratto comune |
| Embedding | **Sentence Transformers** | Interfaccia separata dai modelli generativi |
| Sandbox notebook | **Da decidere via POC** (Docker/Podman/altro) | Isolamento verificabile |
| Test backend | **Pytest** | Unit + contract + integrazione |
| Test frontend | **Vitest + React Testing Library** | |
| Test E2E | **Playwright** | |
| Lint/format Python | **ruff** + **mypy (strict)** | |
| Lint/format TS | **eslint** + **prettier** (o biome) | |
| Package manager Python | **uv** (proposta; poetry/pip accettabili se motivati) | |
| Package manager JS | **pnpm** (proposta) | |

**Regola:** nessuna dipendenza proprietaria a pagamento. Ogni nuova dipendenza deve essere open source e compatibile con licenza del progetto.

---

## 4. Struttura del repository (target)

La struttura è **proposta** e va confermata con il primo commit. L'agente deve rispettarla o proporre modifiche esplicite.

```
/
├── AGENTS.md
├── README.md
├── docs/                              # documenti di progetto (PRD, Roadmap, ecc.)
├── apps/
│   └── desktop/                       # Tauri 2 + React
│       ├── src/                       # frontend React/TS
│       ├── src-tauri/                 # shell Rust, sidecar, comandi
│       └── package.json
├── services/                          # microservizi Python (uno per cartella)
│   ├── gateway/                       # Local API Gateway
│   ├── document/                      # Document Service
│   ├── rag/                           # RAG Service
│   ├── ai/                            # AI Service
│   ├── learning/                      # Learning Service
│   ├── jobs/                          # Job Service
│   └── notebook/                      # Notebook Execution Service
├── packages/                          # librerie Python condivise
│   ├── contracts/                     # SOLO modelli Pydantic/enum dei contratti
│   ├── ai-adapters/                   # interfaccia adapter + implementazioni
│   └── embeddings/                    # interfaccia embedding
├── data/                              # dati runtime (gitignored)
│   ├── sqlite/
│   ├── chromadb/
│   └── files/
├── tests/                             # integrazione e E2E
├── scripts/                           # build, dev, packaging
└── .github/workflows/                 # CI
```

Regole sulla struttura:

- Ogni servizio ha un proprio `pyproject.toml` e un proprio ambiente.

- `packages/contracts` contiene **solo** modelli e tipi, nessuna logica.

- Mai import diretto tra `services/*` a livello di codice applicativo. Solo HTTP.

- Il frontend non contiene logica di parsing, retrieval o generazione.

---

## 5. Comandi canonici

> I comandi sono il **target** che l'agente deve contribuire a rendere reali man mano che il repo cresce. Se un comando non esiste ancora, l'agente lo crea nel `package.json` o nello script corrispondente, oppure segnala l'assenza.

### Backend (per singolo servizio)

```bash
# setup
cd services/<nome> && uv sync
# dev
uv run uvicorn app.main:app --reload --host 127.0.0.1 --port <porta>
# test
uv run pytest -q
# lint + format + tipi
uv run ruff check . && uv run ruff format --check .
uv run mypy app
```

### Frontend

```bash
cd apps/desktop
pnpm install
pnpm dev              # Tauri dev (avvia anche i servizi)
pnpm test             # Vitest
pnpm test:e2e         # Playwright
pnpm lint && pnpm typecheck
pnpm tauri build
```

### Orchestrazione full-stack

```bash
pnpm dev:all          # avvia gateway + servizi + Tauri in dev
pnpm build:all        # build sidecar Python + Tauri
```

### Database

```bash
# migrazione (da definire con Alembic o simile)
uv run <script-migrazione>
```

> Se un comando non esiste, l'agente lo aggiunge oppure apre un TODO esplicito. Non inventare comandi ineseguibili.

---

## 6. Regole architetturali non negoziabili

Queste regole non vanno violate senza una decisione architetturale esplicita (ADR) e un aggiornamento di `docs/architecture.md`.

1. **Confini dei servizi.** Nessun servizio importa moduli interni di un altro. La comunicazione è HTTP REST con contratti Pydantic condivisi in `packages/contracts`. Mai accesso diretto al DB di un altro servizio.

2. **Ownership dei dati.** Ogni servizio scrive solo le proprie tabelle SQLite. Gli altri leggono tramite API del servizio proprietario.

3. **ChromaDB è indice derivato.** Non è fonte di verità. Deve essere sempre ricostruibile da SQLite + file originali. Ogni operazione di scrittura deve prevedere la coerenza con SQLite.

4. **AI Service non dipende da un runtime.** Solo tramite `packages/ai-adapters`. Aggiungere un runtime non deve richiedere modifiche all'AI Service.

5. **Sandbox isolata.** Il notebook non condivide privilegi, file o rete con gli altri servizi. Rete off di default. Limiti di CPU, memoria e tempo per cella.

6. **Citazioni obbligatorie.** Ogni affermazione RAG deve citare `document_id` + pagina/sezione. Se la fonte non c'è, va dichiarato esplicitamente.

7. **Local-first.** Le funzionalità principali devono funzionare offline. Il livello 3 (web) è opzionale, separato e disattivabile.

8. **Binding solo localhost.** Tutti i servizi su `127.0.0.1` (o socket locale). Mai `0.0.0.0`.

9. **Streaming.** Il tutor risponde via SSE. L'UI non deve mai bloccare su richieste lunghe.

10. **Job asincroni.** Operazioni > 2 s vanno nel Job Service. Nessuna richiesta HTTP lunga e bloccante.

---

## 7. Convenzioni di codice

### Python

- Type hint obbligatori su funzioni pubbliche.

- Pydantic v2 per tutti i contratti API.

- `async def` per endpoint FastAPI e I/O; sync solo dove motivato.

- Nomi file e moduli: `snake_case`.

- Struttura per servizio: `app/{main.py, api/, core/, models/, services/}`.

- Errori: usare le categorie standard (`VALIDATION_ERROR`, `SERVICE_UNAVAILABLE`, `TIMEOUT`, `RESOURCE_LIMIT`, `INTERNAL_ERROR`, `DEPENDENCY_ERROR`).

- Log strutturati (JSON) con `request_id` e `service`.

- Niente path locali nei log o nelle risposte al frontend.

### TypeScript / React

- Strict mode attivo; `noUncheckedIndexedAccess` consigliato.

- Componenti funzionali + hooks. Nomi PascalCase. File `ComponentName.tsx`.

- Server state con TanStack Query; local state con `useState`/`useReducer`, non duplicare server state in store globali.

- Chiamate API solo attraverso il gateway locale, mai dirette ai servizi.

- SSE gestiti con `EventSource` (o fetch streaming) e cleanup a unmount.

- Errori utente: messaggi chiari, mai stack trace o path.

- Ogni azione deve dare feedback visivo < 50 ms.

### Convenzioni trasversali

- Nomi di variabili, funzioni e file in inglese; commenti e UI in italiano.

- Commit message: `<area>: <azione>` (es. `document: add DOCX parser`).

- Nessun segreto, chiave o path personale nei commit.

- `.env` locale gitignored; `.env.example` documentato.

---

## 8. Sicurezza e local-first

Checklist obbligatoria per ogni servizio:

- [ ] Binding su `127.0.0.1` o socket locale.

- [ ] Token di sessione casuale richiesto su ogni richiesta (header `Authorization`).

- [ ] Validazione payload con Pydantic.

- [ ] CORS ristretto all'origine del frontend Tauri.

- [ ] Nessuna esposizione di path locali, segreti o stack trace.

- [ ] Log senza dati sensibili.

- [ ] Rate limit / timeout su richieste verso altri servizi.

- [ ] Notebook Service: nessun accesso alla rete, file limitati a `data/files/workspace-<id>/`, privilegi separati.

Regole aggiuntive:

- Il codice generato dall'IA **non** va eseguito fuori dalla sandbox.

- La sandbox è un confine di sicurezza, non un dettaglio implementativo.

- Le API dei servizi non sono raggiungibili da processi esterni non autorizzati (token per launch).

- Nessuna chiamata di rete in uscita senza opt-in esplicito dell'utente (livello 3).

---

## 9. Test e qualità

### Backend

- Pytest per unit test di ogni servizio.

- Contract test: schema delle risposte conforme a `packages/contracts`.

- Test di integrazione tra servizi (avvio reale su porte dinamiche).

- Test di persistenza: scrittura/lettura SQLite, ricostruzione ChromaDB.

- Test di gestione errori: timeout, servizio non disponibile, retry.

### Frontend

- Vitest + RTL per componenti e hook.

- Test di streaming SSE: primo chunk entro 1.5 s, gestione interruzioni.

- Test di stati di caricamento/errore.

### E2E (Playwright)

- Percorso MVP completo: importa PDF → spiega passaggio → esegui codice → supera quiz.

- Avvio/arresto app senza processi residui.

- Citazioni cliccabili che aprono il documento.

### Test RAG

- Set di valutazione 50-100 domande su documenti reali.

- Soglia citazioni corrette: ≥ 90% (gate MVP).

- Primo token ≤ 1.5 s su hardware di riferimento.

- Ricerca per similarità < 200 ms dopo indicizzazione.

### Test architetturali

- Avvio/arresto servizi da parte di Tauri.

- Indisponibilità di un servizio → l'app resta usabile per le funzioni non dipendenti.

- Consistenza SQLite ↔ ChromaDB dopo eliminazione/ricostruzione.

---

## 10. AI/ML: adapter, RAG, citazioni, streaming

### Contratto adapter (in `packages/ai-adapters`)

```python
class ChatMessage(BaseModel):
   role: Literal["system", "user", "assistant"]
   content: str

class ChatRequest(BaseModel):
   model: str
   messages: list[ChatMessage]
   stream: bool = True
   temperature: float = 0.7

class ChatChunk(BaseModel):
   delta: str
   finish_reason: str | None = None

class ModelInfo(BaseModel):
   id: str
   capabilities: set[str]  # es. {"chat", "tools", "vision"}

class RuntimeAdapter(Protocol):
   async def list_models(self) -> list[ModelInfo]: ...
   async def chat(self, req: ChatRequest) -> AsyncIterator[ChatChunk]: ...
   async def abort(self, request_id: str) -> None: ...
   async def health(self) -> HealthStatus: ...
```

Regole:

- Non assumere che tutti i runtime supportino le stesse capacità. Capacità dichiarate in `ModelInfo.capabilities`.

- L'AI Service non chiama mai direttamente un runtime: solo tramite adapter.

- Errori runtime mappati sulle categorie standard.

### Citazioni

```python
class Citation(BaseModel):
   document_id: str
   page: int | None = None
   section: str | None = None
   snippet: str
```

- Ogni risposta RAG che usa contenuto documentale deve restituire `citations: list[Citation]`.

- Il frontend deve rendere cliccabile ogni citazione e aprire il documento alla posizione.

- Se il modello non ha fonte, la risposta deve dichiarare "nessuna fonte nei documenti".

### Streaming

- SSE con eventi tipizzati: `token`, `citation`, `done`, `error`.

- Il gateway inoltra SSE senza bufferizzare.

- Timeout e interruzione devono essere gestiti esplicitamente.

### Embedding

- Interfaccia separata in `packages/embeddings`.

- Il modello di embedding è indipendente dal modello generativo.

- Change di modello di embedding ⇒ reindicizzazione esplicita e versionata.

---

## 11. Job asincroni e sandbox

### Job Service

- Coda persistente su SQLite.

- Stati: `queued`, `running`, `completed`, `failed`.

- Campi: `id`, `type`, `params`, `created_at`, `status`, `progress`, `error`, `result`, `retry_policy`.

- Recupero dopo riavvio: i job `running` vengono marcati `failed` o riaccodati secondo policy.

- Il frontend monitora via polling o SSE.

### Sandbox notebook

- Isolamento a livello di sistema operativo, non solo applicativo.

- Rete disabilitata di default; abilitabile solo con opt-in esplicito (fuori MVP).

- Limiti: CPU, memoria, tempo per cella; terminazione forzata allo scadere.

- Nessun accesso a file fuori da `data/files/workspace-<id>/`.

- Output gestiti e sanitizzati prima di arrivare al frontend.

> La tecnologia di isolamento è **aperta** (POC-03). L'agente non deve sceglierla autonomamente: proporre e aprire un ADR.

---

## 12. Workflow operativi per l'agente

### Aggiungere un endpoint

1. Definisci/aggiorna il modello in `packages/contracts`.

2. Implementa endpoint FastAPI nel servizio proprietario.

3. Aggiungi test di contratto e unit test.

4. Aggiorna OpenAPI (auto-generato) e documentazione del servizio.

5. Se l'endpoint è consumato dal frontend, aggiungi client tipizzato in `apps/desktop/src/api/`.

### Aggiungere un servizio

1. Crea `services/<nome>/` con `pyproject.toml`, `app/main.py`, `app/api/`.

2. Definisci contratti in `packages/contracts`.

3. Aggiungi health/ready.

4. Aggiungi entry nel manifest dei servizi (porte, comandi, env).

5. Aggiorna `scripts/dev:all` e packaging sidecar.

6. Apri un ADR se il servizio introduce un nuovo confine architetturale.

### Aggiungere un adapter AI

1. Implementa `RuntimeAdapter` in `packages/ai-adapters/<runtime>.py`.

2. Aggiungi test con runtime mockato.

3. Documenta capacità supportate e limitazioni.

4. Verifica con POC-02 prima di considerarlo stabile.

### Aggiungere una migrazione SQLite

1. Aggiungi migrazione versionata (Alembic o equivalente).

2. Aggiorna il modello del servizio proprietario.

3. Test: up, down, idempotenza.

4. Se cambia lo schema, valuta impatto su ricostruzione ChromaDB.

### Proporre un cambio architetturale

1. Apri un ADR in `docs/adr/`.

2. Descrivi contesto, opzioni, decisione, conseguenze.

3. Aggiorna `docs/architecture.md` se la decisione è approvata.

4. Aggiorna questo `AGENTS.md` se cambiano regole operative.

---

## 13. Definizione di "completato"

Una modifica è completa quando:

- [ ] Criteri di accettazione della user story superati.

- [ ] Test automatici scritti (unit + contract + integrazione dove serve).

- [ ] Nessuna regressione su test esistenti.

- [ ] Funzionamento offline per le parti local-first.

- [ ] Documentazione aggiornata (README del servizio, ADR se serve).

- [ ] Nessuna violazione delle regole architetturali (sezione 6).

- [ ] Nessun segreto o path personale nel diff.

- [ ] Se la modifica tocca il confine di sicurezza (sandbox, token, rete), revisione esplicita.

---

## 14. Cosa NON fare

- ❌ Importare moduli interni di un altro servizio.

- ❌ Accedere direttamente alle tabelle SQLite di un altro servizio.

- ❌ Usare ChromaDB come fonte di verità.

- ❌ Chiamare un runtime AI senza passare dall'adapter.

- ❌ Eseguire codice generato dall'IA fuori dalla sandbox.

- ❌ Bloccare l'UI con richieste sincrone lunghe.

- ❌ Binding su `0.0.0.0` o interfacce di rete esterne.

- ❌ Inserire dipendenze da API o modelli a pagamento.

- ❌ Committare modelli AI pesanti, segreti, `.env`, dati utente.

- ❌ Restituire path locali o stack trace al frontend.

- ❌ Implementare funzionalità v1/v2 dentro l'MVP senza approvazione.

- ❌ Decidere autonomamente le questioni aperte (sezione 15).

---

## 15. Decisioni aperte (non decidere da solo)

Queste scelte sono **aperte** nei documenti di riferimento. L'agente deve proporre, motivare e aprire un ADR, non implementare unilateralmente.

| ID | Decisione | Riferimento |
| --- | --- | --- |
| ADR-006 | Organizzazione fisica dei DB SQLite (unico file vs per servizio) | Architettura §16 |
| ADR-010 | Tecnologia sandbox Python (Docker/Podman/altro) | Architettura §9.3 |
| ADR-011 | Comunicazione tra servizi (HTTP REST vs gRPC) | Comunicazione §3.3 |
| ADR-012 | Gestione processi locali (plugin Shell Tauri vs altro) | Comunicazione §6 |
| — | Porte: dinamiche vs socket locale | Comunicazione §6.6 |
| — | Hardware minimo garantito per l'MVP | PRD "Questioni aperte" |
| — | Lingue dei contenuti (solo IT, IT+EN) | PRD "Questioni aperte" |
| — | Modello di sostenibilità economica | PRD "Questioni aperte" |
| — | WebSocket per notebook bidirezionale | Comunicazione §3.2 |

---

## 16. Comunicazione e lingua

- **Documentazione di prodotto e UI:** italiano.

- **Codice, nomi, commit, ADR tecnici:** inglese (per i termini tecnici), italiano per la prosa.

- **Commenti nel codice:** italiano solo se aggiungono contesto di dominio; altrimenti il codice deve essere autoesplicativo.

- **Risposte dell'agente all'utente:** italiano, conciso, con riferimenti ai documenti.

---

## 17. Manutenzione di questo file

- Aggiorna `AGENTS.md` quando:

  - viene approvato un ADR che cambia regole operative;

  - viene chiuso un POC con una decisione tecnica;

  - cambia la struttura del repository o i comandi canonici;

  - cambia la mappa dei file (nuovo servizio, rotta, tabella o componente): aggiorna `docs/wiki/`;

  - emerge una regola ricorrente che vale la pena codificare.

- Non aggiornare `AGENTS.md` per decisioni tattiche o di breve periodo: quelle stanno nel README del servizio o nell'ADR.

---

**Fine AGENTS.md**
