# Roadmap e Definizione di MVP

Nov 2, 2026 · @Andrea

## Principi di prioritizzazione

La roadmap procede in tre fasi: l'MVP dimostra il percorso completo "leggi, chiedi, pratica, verifica", la v1 aggiunge la profondità didattica, la v2 allarga i formati e le funzioni avanzate. Le durate vanno stimate dal team tecnico dopo la prima validazione dell'architettura; questo documento fissa ordine e criteri, non date.

- **Prima il valore didattico, poi la ricchezza:** ogni fase si chiude solo se un utente studia un capitolo e viene misurato su un quiz.
- **Prima il rischio tecnico:** parsing delle formule, qualità degli LLM locali e sandbox si provano all'inizio con prototipi.
- **Ogni fase rilasciabile:** al termine c'è un prodotto usabile, non un cantiere.

&#91;embedded content: roadmap · 3 fasi, 3 gate\]

Ogni fase passa al gate successivo solo se i criteri elencati nella sezione della fase sono soddisfatti.

## Fase 1: MVP

Obiettivo: un utente carica un PDF di statistica, si fa spiegare un passaggio con citazione, esegue il codice e supera un quiz sul capitolo.

**Contenuto**

- Importazione di PDF, Markdown e Word, con indicizzazione locale e lettore con annotazioni (storie A1-A4, A6).
- Toolbar contestuale e RAG su documento e libreria, con citazioni e streaming (B1, B2, B3, B5).
- Lezioni ai livelli 1-3 (C1) e 3 widget interattivi (D1).
- Notebook Python in sandbox (E1-E3).
- Flashcard base e quiz a risposta multipla (F1, F3).
- Barra di stato dei processi e tema scuro (G1, G4).

**Criteri di uscita (gate)**

- Le citazioni risultano corrette sul set di valutazione RAG, con soglia da fissare (obiettivo iniziale: 90%).
- Il feedback visivo resta sotto i 50 ms e il primo testo di risposta compare entro 1,5 s su hardware di riferimento.
- Il kernel non accede a file fuori dallo spazio di lavoro né alla rete.
- Almeno un test con utenti reali su un capitolo completo.

## Fase 2: v1

Obiettivo: trasformare lo strumento di consultazione in un tutor che diagnostica, adatta il percorso e misura la padronanza.

**Contenuto**

- Analisi delle lacune, lezioni integrative e test diagnostico (C2-C4).
- Livelli 4-5, grafo dei prerequisiti, modalità socratica e Feynman (C1, C5-C7).
- Animazioni Manim con cache e auto-correzione (D2-D4).
- Ripetizione spaziata completa, quiz a risposta aperta, padronanza per concetto, piano di studio (F2-F5).
- Esercizi con correzione simbolica e verifica dei calcoli (E4, B6).
- Importazione di EPUB, PPTX, CSV, Excel e ricerca web (A5, B4).
- Annullamento e rilancio delle attività (G2).

**Criteri di uscita (gate)**

- Gli script Manim compilano al primo o dopo al massimo 3 correzioni nella maggior parte dei casi; soglia da fissare sul set di scene di prova.
- Il test diagnostico assegna un livello coerente con l'esito dei quiz su un gruppo pilota.
- La ritenzione a 30 giorni delle flashcard raggiunge l'obiettivo iniziale dell'80%.

## Fase 3: v2

Obiettivo: coprire l'intero ciclo di studio e di ricerca, con più input e più strumenti di pratica.

**Contenuto**

- Trascrizione locale di audio e video con Whisper e note strutturate (G3).
- Da paper a codice e progetti guidati (E5, E6).
- Visualizzazioni interattive per ML e DL (D5).
- Glossario e notazione unificata tra documenti.
- Export verso Anki, Obsidian e Markdown; backup e sincronizzazione cifrata opzionale (F6).
- Mappe concettuali automatiche, sintesi vocale, accessibilità avanzata e supporto multilingua.

**Criteri di uscita (gate)**

- Le trascrizioni raggiungono una qualità accettabile sul set di lezioni di prova.
- Esportazioni verificate nei formati supportati, senza perdita di formule.

## Dipendenze e rischi di pianificazione

| Dipendenza | Blocca | Azione |
| --- | --- | --- |
| Parsing delle formule in LaTeX pulito | RAG, lezioni, flashcard | Prototipo all'inizio dell'MVP e scelta dello strumento OCR matematico |
| Scelta del runtime LLM e del modello di riferimento | Tutto il tutor | Benchmark su hardware di riferimento prima di sviluppare la UI del tutor |
| Sandbox per notebook e Manim | Esecuzione di codice | Decidere l'isolamento (container, WebAssembly o processo ristretto) nella prima fase |
| Set di valutazione RAG | Gate dell'MVP | Costruirlo in parallelo con 50-100 domande su documenti reali; numeri indicativi, da confermare |
| Concetti e prerequisiti (grafo) | Diagnostica, piano di studio | Definire il modello dati nell'MVP, anche se la funzione arriva in v1 |

Per evitare ritardi a cascata, il modello dati (concetti, padronanza, schede) va fissato nell'MVP anche se parte delle funzioni arriva dopo.

## Fuori ambito

- Editor di testo completo: il lettore resta in sola consultazione e annotazione.
- Collaborazione in tempo reale e funzioni social.
- App mobile nativa.
- Addestramento o fine-tuning di modelli.
- Qualsiasi dipendenza da API o modelli proprietari a pagamento.
