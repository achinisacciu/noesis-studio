# Architettura Tecnica

## Piattaforma IA per l'Auto-Apprendimento Avanzato

**Versione:** 0.2\
**Stato:** Proposta aggiornata sulla base delle preferenze architetturali\
**Data:** 6 novembre 2026

---

## 1. Obiettivo del documento

Questo documento definisce la proposta di architettura tecnica della piattaforma IA per l'auto-apprendimento avanzato.

L'architettura deve supportare un'applicazione Desktop local-first, capace di elaborare documenti, fornire assistenza didattica tramite modelli linguistici, recuperare informazioni contestuali attraverso RAG e consentire l'esecuzione controllata di codice Python.

Le scelte architetturali devono rispettare i principi già definiti nel PRD, nella Roadmap e nelle User Stories:

- Elaborazione prevalentemente locale.
- Utilizzo di componenti IA open source e self-hosted.
- Funzionamento delle funzionalità principali senza connessione Internet.
- Risposte verificabili attraverso riferimenti alle pagine e alle sezioni dei documenti.
- Separazione tra interfaccia, logica applicativa e servizi di elaborazione.
- Esecuzione del codice in un ambiente isolato.
- Possibilità di evolvere progressivamente le funzionalità senza compromettere l'MVP.

Le tecnologie indicate in questo documento rappresentano proposte tecniche da verificare, salvo le preferenze architetturali già espresse.

## 2. Decisioni architetturali validate

Le seguenti preferenze costituiscono la base della versione 0.2.

| **Area** | **Scelta** | **Stato** |
| --- | --- | --- |
| Tipologia applicazione | Desktop Tauri | Validata |
| Architettura backend | Microservizi | Validata |
| Persistenza e ricerca | SQLite + ChromaDB | Validata |
| Runtime AI | Adapter multipli | Validata |
| Sandbox Python | Da valutare con prototipo | Aperta |

La validazione della direzione architetturale non implica che siano già stati definiti tutti i dettagli implementativi.

In particolare, restano da verificare i protocolli di comunicazione, il packaging dei servizi, la gestione dei processi locali, la distribuzione dei modelli e il sistema di isolamento del notebook.

## 3. Architettura generale

### 3.1 Modello architetturale

La piattaforma adotterà un'architettura Desktop basata su Tauri 2, con frontend React e servizi backend locali indipendenti.

Il backend sarà organizzato secondo un modello a microservizi, nel quale ciascun servizio avrà una responsabilità funzionale specifica e un'interfaccia di comunicazione definita.

I servizi saranno eseguiti sulla macchina dell'utente. Non è previsto, per l'MVP, un backend distribuito su infrastrutture cloud.

La separazione dei servizi dovrà essere funzionale e operativa, ma non dovrà introdurre complessità infrastrutturale non necessaria.

### 3.2 Schema logico

```
┌──────────────────────────────────────────────┐
│                DESKTOP APP                    │
│                                              │
│              Tauri 2 + React                 │
│                                              │
│  ┌──────────────────┐  ┌──────────────────┐  │
│  │ Document Reader  │  │   AI Tutor       │  │
│  │                  │  │                  │  │
│  └──────────────────┘  └──────────────────┘  │
│                                              │
│  ┌──────────────────┐  ┌──────────────────┐  │
│  │ Python Notebook │  │ Learning Tools   │  │
│  └──────────────────┘  └──────────────────┘  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│          LOCAL API / ORCHESTRATION           │
│                                              │
│     Routing, sessioni, coordinamento         │
└──────────┬───────────┬───────────┬───────────┘
           │           │           │
           ▼           ▼           ▼
   ┌────────────┐ ┌───────────┐ ┌─────────────┐
   │ Document   │ │ RAG       │ │ AI          │
   │ Service    │ │ Service   │ │ Service     │
   └────────────┘ └───────────┘ └─────────────┘
           │           │           │
           ▼           ▼           ▼
   ┌────────────┐ ┌───────────┐ ┌─────────────┐
   │ Learning   │ │ Job       │ │ AI Runtime  │
   │ Service    │ │ Service   │ │ Adapters    │
   └────────────┘ └───────────┘ └─────────────┘
                       │
                       ▼
                ┌──────────────┐
                │ Notebook     │
                │ Execution    │
                │ Service      │
                └──────────────┘

        ┌──────────────────────────────┐
        │       LOCAL PERSISTENCE      │
        │                              │
        │  SQLite       ChromaDB       │
        │  File Storage Vector Index  │
        └──────────────────────────────┘
```

Lo schema rappresenta i confini logici dei componenti. Le modalità effettive di comunicazione e distribuzione dei processi saranno definite durante i prototipi.

## 4. Desktop application

### 4.1 Tauri 2

Tauri 2 sarà il framework di riferimento per la realizzazione dell'applicazione Desktop.

Responsabilità principali:

- Gestione della finestra applicativa.
- Integrazione tra frontend e funzionalità native.
- Avvio e arresto dei servizi locali.
- Gestione del ciclo di vita dell'applicazione.
- Accesso controllato alle risorse locali.
- Packaging e distribuzione dell'applicazione.

Tauri consentirà di mantenere un'interfaccia Desktop senza richiedere l'esecuzione di un browser esterno.

### 4.2 Frontend

**Tecnologie proposte:**

- React.
- TypeScript.
- Vite.

Il frontend sarà responsabile della presentazione e dell'interazione con l'utente.

Le aree principali saranno:

1. Document Reader.
2. AI Tutor.
3. Notebook Python.
4. Flashcard e quiz.
5. Dashboard degli agenti e delle operazioni in background.
6. Gestione di workspace e documenti.

Il frontend non dovrà implementare direttamente la logica di elaborazione documentale, indicizzazione, retrieval o generazione delle risposte. Queste responsabilità saranno delegate ai servizi backend.

## 5. Architettura backend a microservizi

### 5.1 Principi di progettazione

Il backend sarà composto da servizi locali indipendenti, organizzati per responsabilità funzionale.

Ogni servizio dovrà:

- Esporre un'interfaccia definita.
- Possedere una responsabilità circoscritta.
- Gestire autonomamente la propria logica applicativa.
- Evitare dipendenze dirette dalle implementazioni interne degli altri servizi.
- Comunicare attraverso contratti espliciti.
- Gestire errori e timeout.
- Esporre uno stato operativo verificabile.

Per l'MVP si propone di utilizzare un numero contenuto di servizi, evitando una frammentazione eccessiva.

### 5.2 Servizi previsti

#### A. Document Service

Responsabile della gestione documentale.

Funzionalità:

- Importazione dei documenti.
- Lettura e parsing dei formati supportati.
- Estrazione del testo.
- Estrazione e gestione dei riferimenti a pagine e sezioni.
- Gestione dei metadati.
- Suddivisione del contenuto in chunk.
- Gestione delle annotazioni.
- Gestione dei workspace e delle associazioni documentali.

Formati MVP:

- PDF.
- Markdown.
- DOCX.

**Tecnologie proposte:**

- Python.
- PyMuPDF.
- python-docx.
- Parser Markdown dedicato.

#### B. RAG Service

Responsabile del recupero delle informazioni dai documenti e dal workspace.

Funzionalità:

- Generazione degli embedding.
- Indicizzazione dei chunk.
- Ricerca semantica.
- Recupero dei contenuti pertinenti.
- Ranking dei risultati.
- Filtraggio per documento e workspace.
- Preparazione del contesto per il tutor.
- Associazione dei risultati alle relative citazioni.

**Tecnologie proposte:**

- Python.
- ChromaDB.
- Sentence Transformers, inizialmente come implementazione proposta per gli embedding.

Il servizio dovrà distinguere chiaramente il recupero dei contenuti dalla generazione della risposta.

#### C. AI Service

Responsabile dell'orchestrazione delle funzionalità basate sui modelli linguistici.

Funzionalità:

- Gestione delle richieste al tutor.
- Costruzione dei prompt.
- Selezione del modello.
- Coordinamento con il RAG Service.
- Gestione delle risposte in streaming.
- Applicazione dei livelli di approfondimento didattico.
- Gestione degli adapter dei runtime.
- Verifica delle citazioni restituite dal modello.

Il servizio non dovrà dipendere direttamente da un singolo runtime o modello.

#### D. Learning Service

Responsabile delle funzionalità didattiche.

Funzionalità previste:

- Gestione delle lezioni.
- Generazione e gestione degli esercizi.
- Quiz.
- Flashcard.
- Progressi dell'utente.
- Informazioni sul percorso di apprendimento.
- Gestione delle sessioni di studio.

Le funzionalità non incluse nell'MVP potranno essere implementate progressivamente senza modificare i confini degli altri servizi.

#### E. Job Service

Responsabile delle operazioni asincrone.

Funzionalità:

- Gestione delle attività in background.
- Accodamento dei job.
- Monitoraggio dello stato.
- Gestione degli errori.
- Retry controllati.
- Registrazione dei risultati.

Stati previsti:

- `queued`
- `running`
- `completed`
- `failed`

Esempi di operazioni:

- Indicizzazione documentale.
- Generazione di embedding.
- Elaborazioni documentali.
- Generazione di contenuti didattici.
- Operazioni di manutenzione degli indici.

Per l'MVP si propone una coda persistente basata su SQLite, senza introdurre inizialmente Redis o un message broker esterno.

#### F. Notebook Execution Service

Responsabile dell'esecuzione del codice Python.

Funzionalità:

- Creazione delle sessioni di esecuzione.
- Esecuzione del codice.
- Restituzione degli output.
- Gestione degli errori.
- Gestione del ciclo di vita del kernel.
- Applicazione dei limiti di risorse.
- Isolamento dell'ambiente di esecuzione.

Questo servizio avrà un confine di sicurezza distinto dagli altri servizi.

La tecnologia di isolamento non è ancora definita e dovrà essere selezionata attraverso un prototipo dedicato.

### 5.3 Local API e orchestrazione

Si propone un componente di coordinamento locale con il compito di esporre al frontend un'interfaccia coerente.

Responsabilità:

- Routing delle richieste verso i servizi.
- Gestione delle sessioni applicative.
- Coordinamento delle operazioni che coinvolgono più servizi.
- Gestione degli errori di comunicazione.
- Controllo dello stato dei servizi.
- Gestione dello streaming delle risposte.

La comunicazione tra frontend e backend e quella tra i servizi dovranno rimanere locali.

**Tecnologia proposta:** FastAPI per le API Python.

Resta da decidere se utilizzare un gateway unico oppure un livello di orchestrazione integrato nel processo di supervisione dei servizi.

## 6. Comunicazione tra componenti

### 6.1 Comunicazione frontend-backend

Il frontend comunicherà con i servizi locali attraverso API controllate.

Si propone:

- HTTP per le richieste e le risposte.
- Server-Sent Events (SSE) per lo streaming delle risposte del tutor e degli aggiornamenti di stato.
- API REST per le operazioni applicative.

### 6.2 Comunicazione tra microservizi

La comunicazione dovrà avvenire attraverso contratti espliciti, senza accesso diretto alle strutture interne degli altri servizi.

Per il prototipo iniziale si propone di valutare HTTP locale con API REST.

Non è ancora stata presa una decisione definitiva sull'utilizzo di HTTP, gRPC o altri protocolli.

### 6.3 Gestione dei processi

L'applicazione Tauri dovrà coordinare il ciclo di vita dei servizi locali.

Il sistema dovrà:

1. Avviare i servizi necessari all'apertura dell'applicazione.
2. Verificare che siano disponibili.
3. Gestire l'indisponibilità di un servizio.
4. Evitare processi duplicati.
5. Arrestare correttamente i servizi alla chiusura.
6. Registrare gli errori di avvio e arresto.

La possibilità di avviare alcuni servizi solo quando necessari dovrà essere valutata per ridurre il consumo di risorse.

## 7. Persistenza e gestione dei dati

### 7.1 SQLite

SQLite sarà il database relazionale locale della piattaforma.

Sarà utilizzato per conservare:

- Workspace.
- Documenti e metadati.
- Annotazioni.
- Sessioni di studio.
- Progressi.
- Quiz.
- Flashcard.
- Configurazioni.
- Stato dei job.
- Metadati delle operazioni.

Si propone di mantenere una separazione logica dei dati in base al servizio proprietario.

Un servizio dovrà essere responsabile delle operazioni sui propri dati. Gli altri servizi dovranno utilizzare le API esposte dal servizio proprietario, evitando accessi diretti alle sue tabelle.

Per l'MVP si potrà utilizzare un singolo file SQLite con separazione rigorosa delle responsabilità e delle tabelle. La suddivisione in database fisici distinti potrà essere valutata se necessaria.

Questa scelta riduce la complessità operativa, ma richiede attenzione alla concorrenza delle scritture e alle transazioni che coinvolgono più servizi.

### 7.2 ChromaDB

ChromaDB sarà utilizzato come archivio vettoriale per la ricerca semantica.

Responsabilità:

- Memorizzazione degli embedding.
- Gestione delle collezioni.
- Ricerca per similarità.
- Filtraggio tramite metadati.
- Recupero dei chunk associati ai risultati.

La struttura dovrà consentire la separazione logica degli indici per workspace e documento.

ChromaDB sarà considerato un indice derivato: i dati originali e i metadati principali resteranno conservati nei sistemi di persistenza applicativa.

Dovrà essere possibile ricostruire l'indice vettoriale partendo dai contenuti originali e dai metadati.

### 7.3 File Storage

I file originali saranno conservati in un archivio locale gestito dall'applicazione.

La struttura dovrà consentire:

- Organizzazione per workspace.
- Identificazione univoca dei documenti.
- Gestione dei file importati.
- Separazione tra originali e contenuti elaborati.
- Gestione dei file temporanei.

I percorsi fisici non dovranno essere esposti direttamente ai componenti che non ne hanno necessità.

## 8. Architettura AI e adapter multipli

### 8.1 Obiettivo

La piattaforma dovrà supportare runtime AI differenti senza vincolare la logica applicativa a un singolo provider.

L'AI Service dovrà comunicare con un'interfaccia astratta che consenta di selezionare e utilizzare diversi runtime.

### 8.2 Struttura proposta

```
                AI SERVICE
                     |
                     ▼
             RUNTIME ADAPTER
                     |
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
       Ollama     llama.cpp   Altri runtime
```

### 8.3 Adapter

Ogni adapter dovrà implementare un contratto comune.

Operazioni da considerare:

- Elenco dei modelli disponibili.
- Selezione del modello.
- Invio dei prompt.
- Generazione delle risposte.
- Streaming.
- Gestione degli errori.
- Interruzione delle richieste.
- Recupero delle informazioni sulle capacità del runtime.

Il contratto dovrà distinguere le capacità dei modelli, evitando di assumere che tutti supportino le stesse funzionalità.

### 8.4 Runtime iniziali

**Ollama** è il candidato iniziale per il primo prototipo.

**llama.cpp** è un ulteriore runtime da valutare.

L'architettura dovrà permettere l'aggiunta di altri runtime compatibili senza modificare il comportamento generale dell'AI Service.

La compatibilità dovrà essere verificata anche rispetto ai modelli utilizzabili, alla memoria disponibile e alle prestazioni su CPU e GPU.

### 8.5 Embedding

La generazione degli embedding dovrà essere gestita attraverso un'interfaccia separata da quella dei modelli generativi.

Si propone di valutare Sentence Transformers come implementazione iniziale.

La separazione è importante perché il modello di embedding e il modello generativo possono avere requisiti e cicli di aggiornamento differenti.

## 9. Notebook Python e sandbox

### 9.1 Obiettivo

Il notebook dovrà consentire l'esecuzione di codice Python a supporto dello studio.

L'ambiente dovrà essere isolato dal sistema operativo e dai dati privati dell'utente, secondo i requisiti di sicurezza definiti dal progetto.

### 9.2 Requisiti già stabiliti

La sandbox dovrà prevedere:

- Accesso limitato ai file.
- Rete disabilitata per impostazione predefinita.
- Limiti di tempo di esecuzione.
- Limiti di memoria.
- Separazione tra ambiente di esecuzione e applicazione.
- Gestione controllata degli output.

### 9.3 Alternative da prototipare

Le tecnologie da confrontare includono:

- Docker.
- Podman.
- Altre soluzioni di isolamento basate sulle funzionalità native dei sistemi operativi.

Non viene ancora selezionata una tecnologia definitiva.

Il prototipo dovrà verificare:

1. Isolamento dei file.
2. Blocco effettivo della rete.
3. Limiti di CPU e memoria.
4. Terminazione dei processi.
5. Gestione delle dipendenze Python.
6. Compatibilità con Windows, macOS e Linux.
7. Esperienza di installazione per l'utente finale.
8. Avvio e arresto delle sessioni.
9. Possibilità di mantenere lo stato di una sessione.

### 9.4 Criterio di selezione

La scelta non dovrà basarsi esclusivamente sulla semplicità di sviluppo.

La priorità sarà garantire un isolamento verificabile, un comportamento prevedibile e un'esperienza di installazione sostenibile.

La sandbox dovrà essere considerata un componente separato e non dovrà condividere privilegi o accessi non necessari con gli altri servizi.

## 10. Pipeline RAG

Il processo di recupero delle informazioni sarà articolato nelle seguenti fasi.

### 10.1 Indicizzazione

1. Importazione del documento.
2. Parsing del contenuto.
3. Estrazione del testo e dei riferimenti strutturali.
4. Suddivisione in chunk.
5. Associazione dei metadati.
6. Generazione degli embedding.
7. Memorizzazione in ChromaDB.

### 10.2 Retrieval

1. Ricezione della domanda.
2. Identificazione del contesto di ricerca.
3. Generazione dell'embedding della query.
4. Ricerca semantica.
5. Filtraggio per workspace e documento.
6. Ranking dei risultati.
7. Recupero dei contenuti originali e dei riferimenti.

### 10.3 Generazione della risposta

1. Costruzione del contesto.
2. Invio della richiesta all'AI Service.
3. Selezione del runtime attraverso l'adapter.
4. Generazione della risposta.
5. Verifica dei riferimenti.
6. Restituzione della risposta con citazioni.

La piattaforma dovrà preservare il collegamento tra contenuto recuperato, documento originale e posizione nel documento.

## 11. Gestione delle operazioni asincrone

Le operazioni potenzialmente lunghe non dovranno bloccare l'interfaccia.

Il Job Service gestirà le attività in background e renderà disponibile il relativo stato.

Per l'MVP si propone una coda persistente su SQLite con worker locali.

Non si prevede inizialmente l'introduzione di un message broker dedicato.

Dovranno essere definiti:

- Identificativo del job.
- Tipologia dell'operazione.
- Parametri.
- Data di creazione.
- Stato.
- Percentuale di avanzamento, quando disponibile.
- Messaggio di errore.
- Risultato.
- Politiche di retry.

## 12. Sicurezza e funzionamento locale

L'architettura dovrà rispettare il principio local-first.

Le funzionalità principali dovranno poter essere utilizzate senza connessione Internet, nei limiti delle risorse e dei modelli installati localmente.

Le API locali dovranno prevedere:

- Binding esclusivamente su interfacce locali.
- Controllo delle richieste provenienti dal frontend autorizzato.
- Protezione delle sessioni.
- Validazione degli input.
- Gestione dei permessi sui file.
- Protezione contro richieste non autorizzate ai servizi locali.

La sandbox dovrà essere isolata dal resto dell'applicazione.

L'eventuale funzionalità di ricerca Web sarà un'estensione opzionale e dovrà essere separata dal normale funzionamento locale.

## 13. Testing e qualità

### 13.1 Backend

Tecnologia proposta: Pytest.

Saranno necessari:

- Test unitari per ciascun servizio.
- Test dei contratti API.
- Test di integrazione tra servizi.
- Test di persistenza.
- Test di gestione degli errori.
- Test di ricostruzione degli indici.

### 13.2 Frontend

Tecnologie proposte:

- Vitest.
- React Testing Library.
- Playwright.

Saranno verificati:

- Comportamento dell'interfaccia.
- Interazione con i servizi locali.
- Gestione degli stati di caricamento.
- Gestione degli errori.
- Streaming delle risposte.

### 13.3 Test architetturali

Particolare attenzione dovrà essere dedicata a:

- Avvio e arresto dei servizi.
- Indisponibilità di un singolo servizio.
- Comunicazione tra microservizi.
- Consistenza dei dati.
- Recupero dopo un'interruzione.
- Consumo di memoria.
- Prestazioni su hardware di riferimento.
- Isolamento del notebook.

## 14. Evoluzione per fasi

### 14.1 MVP

L'MVP dovrà includere:

- Desktop application Tauri.
- Frontend React e TypeScript.
- Servizi backend locali.
- Importazione PDF, Markdown e DOCX.
- Gestione workspace.
- RAG locale su documento e workspace.
- Tutor IA con livelli di approfondimento 1-3.
- Runtime AI attraverso adapter.
- Notebook Python con sandbox da selezionare.
- Widget didattici iniziali.
- Flashcard di base.
- Quiz semplice.
- Dashboard degli agenti e delle operazioni.

L'architettura a microservizi dovrà essere implementata con il numero minimo di componenti necessario a garantire una separazione effettiva delle responsabilità.

### 14.2 Versione 1

Estensioni previste:

- Analisi delle lacune formative.
- Lezioni integrative.
- Test diagnostici.
- Livelli didattici 4-5.
- Grafo dei prerequisiti.
- Modalità socratica e Feynman.
- Visualizzazioni Manim.
- Sistema SRS.
- Esercizi simbolici.
- Supporto a ulteriori formati.

### 14.3 Versione 2

Estensioni previste:

- Trascrizione audio e video.
- Paper-to-code.
- Progetti guidati.
- Visualizzazioni avanzate ML/DL.
- Glossario.
- Export, backup e sincronizzazione.

## 15. Rischi e conseguenze delle scelte

| **Scelta** | **Vantaggio** | **Rischio o costo** |
| --- | --- | --- |
| Desktop Tauri | Applicazione locale, integrazione nativa, distribuzione Desktop | Packaging multipiattaforma e gestione dei processi |
| Microservizi | Separazione delle responsabilità e maggiore indipendenza evolutiva | Comunicazione, orchestrazione e debugging più complessi |
| SQLite | Semplicità, portabilità e persistenza locale | Concorrenza delle scritture e limiti nelle transazioni distribuite |
| ChromaDB | Ricerca vettoriale dedicata | Gestione della coerenza tra database relazionale e indice |
| Adapter multipli | Libertà di scelta e sostituzione dei runtime | Maggiore complessità dei contratti e delle compatibilità |
| Sandbox da valutare | Possibilità di scegliere in base a prove concrete | Necessità di prototipi e verifiche di sicurezza |

### 15.1 Rischio specifico: microservizi su Desktop

La scelta dei microservizi è il principale elemento di complessità architetturale.

In un'applicazione Desktop locale non si ottengono automaticamente i vantaggi tipici dei microservizi distribuiti su più server.

I servizi condivideranno la stessa macchina e le stesse risorse hardware. Un processo separato comporta costi di memoria, avvio e comunicazione.

Per questo motivo è importante evitare di trasformare ogni singola funzionalità in un servizio autonomo.

La proposta è mantenere servizi con confini funzionali chiari e separare fisicamente i processi soprattutto quando esistono ragioni concrete, come:

- Necessità di isolamento.
- Dipendenze incompatibili.
- Cicli di vita indipendenti.
- Carichi di lavoro differenti.
- Necessità di riavviare un componente senza arrestare l'intera applicazione.

### 15.2 Consistenza tra SQLite e ChromaDB

La persistenza relazionale e quella vettoriale non potranno essere gestite attraverso un'unica transazione atomica.

Ad esempio, se un documento viene eliminato da SQLite ma non da ChromaDB, potrebbero rimanere embedding non più associati a un documento valido.

Sarà quindi necessario implementare operazioni di sincronizzazione e procedure di ricostruzione dell'indice.

### 15.3 Gestione delle dipendenze

La separazione dei servizi può comportare duplicazione di dipendenze Python e maggiore complessità di packaging.

Sarà necessario definire una strategia che consenta di distribuire e aggiornare i servizi in modo affidabile, senza richiedere all'utente di configurare manualmente l'ambiente Python.

## 16. Decisioni ancora aperte

| **ID** | **Decisione** | **Stato** |
| --- | --- | --- |
| ADR-001 | Desktop Tauri | Validata |
| ADR-002 | Architettura backend a microservizi | Validata |
| ADR-003 | React + TypeScript | Proposta |
| ADR-004 | FastAPI | Proposta |
| ADR-005 | SQLite + ChromaDB | Validata |
| ADR-006 | Organizzazione fisica dei database SQLite | Aperta |
| ADR-007 | Adapter AI multipli | Validata |
| ADR-008 | Runtime iniziale Ollama | Proposta |
| ADR-009 | Embedding con Sentence Transformers | Proposta |
| ADR-010 | Sandbox Python | Da prototipare |
| ADR-011 | Comunicazione tra servizi | Aperta |
| ADR-012 | Gestione dei processi locali | Aperta |
| ADR-013 | SSE per lo streaming | Proposta |
| ADR-014 | Gestione dei job con SQLite | Proposta |
| ADR-015 | Plotly per i widget | Proposta |

### 16.1 Questioni da approfondire

1. **Granularità dei microservizi:** definire quali servizi saranno processi indipendenti nell'MVP e quali potranno essere accorpati inizialmente.
2. **Comunicazione:** confrontare HTTP REST e gRPC per i servizi locali.
3. **Orchestrazione:** definire il componente responsabile dell'avvio, del monitoraggio e dell'arresto dei servizi.
4. **Database:** stabilire se utilizzare un unico file SQLite con ownership logica oppure database distinti per servizio.
5. **Packaging:** verificare la distribuzione dei servizi Python insieme all'applicazione Tauri.
6. **Runtime AI:** valutare il comportamento dei diversi adapter e la distribuzione dei modelli.
7. **Sandbox:** completare il confronto tra le alternative di isolamento.
8. **Hardware:** definire i requisiti minimi di memoria, CPU e GPU.
9. **Cross-platform:** verificare la compatibilità dell'architettura con Windows, macOS e Linux.

## 17. Prototipi tecnici prioritari

Prima di consolidare definitivamente l'architettura, si propongono quattro prototipi.

### POC-01 — Microservizi locali

Obiettivo: verificare la fattibilità dell'architettura backend su Desktop.

Attività:

- Avvio di almeno due servizi Python indipendenti.
- Comunicazione tramite API locali.
- Gestione delle dipendenze.
- Monitoraggio dello stato.
- Arresto controllato.
- Verifica del consumo di risorse.

Criterio di successo: i servizi devono poter essere avviati, monitorati e arrestati dall'applicazione senza richiedere interventi manuali.

### POC-02 — Runtime AI e adapter

Obiettivo: verificare la possibilità di utilizzare runtime differenti attraverso un'interfaccia comune.

Attività:

- Definizione del contratto adapter.
- Collegamento a un primo runtime.
- Prova di un secondo runtime.
- Streaming delle risposte.
- Gestione degli errori e delle capacità non supportate.

Criterio di successo: la logica applicativa deve poter cambiare runtime senza essere riscritta.

### POC-03 — Sandbox Python

Obiettivo: individuare una soluzione di isolamento adeguata.

Attività:

- Confronto tra Docker, Podman e alternative.
- Test di accesso ai file.
- Test di accesso alla rete.
- Test dei limiti di risorse.
- Test di terminazione dei processi.
- Verifica multipiattaforma.

Criterio di successo: dimostrare che il codice eseguito non possa accedere liberamente alle risorse del sistema host.

### POC-04 — Persistenza e RAG

Obiettivo: verificare il funzionamento integrato di SQLite e ChromaDB.

Attività:

- Importazione di un documento.
- Persistenza dei metadati.
- Generazione degli embedding.
- Indicizzazione vettoriale.
- Ricerca semantica.
- Recupero delle citazioni.
- Eliminazione e ricostruzione dell'indice.

Criterio di successo: i risultati devono mantenere il collegamento con il documento originale e le relative posizioni.

## 18. Conclusione

L'architettura proposta adotta un modello Desktop local-first basato su Tauri e un backend composto da microservizi locali.

La separazione dei servizi permette di organizzare in modo indipendente le responsabilità documentali, didattiche, di retrieval, di orchestrazione AI e di esecuzione del codice.

SQLite e ChromaDB costituiscono la base della persistenza locale, mentre il sistema di adapter consente di mantenere flessibile la scelta dei runtime AI.

La sandbox Python rappresenta il principale elemento tecnico ancora da validare attraverso un prototipo specifico.

La versione 0.2 definisce quindi una direzione architetturale coerente con gli obiettivi del progetto, ma non costituisce ancora una specifica implementativa definitiva. Le scelte aperte dovranno essere risolte attraverso prototipi, test e successivi aggiornamenti del documento.
