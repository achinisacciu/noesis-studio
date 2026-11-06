# Comunicazione tra microservizi e gestione dei processi locali

## Specifica tecnica per l'architettura Desktop

**Progetto:** Piattaforma IA per l'Auto-Apprendimento Avanzato\
**Versione:** 0.1\
**Stato:** Proposta tecnica da validare tramite prototipo\
**Documento collegato:** Architettura Tecnica v0.2

---

# 1. Obiettivo

Questo documento approfondisce due aspetti fondamentali dell'architettura tecnica:

1. La comunicazione tra i microservizi backend eseguiti localmente.
2. La gestione del ciclo di vita dei microservizi da parte dell'applicazione Desktop basata su Tauri.

L'obiettivo è definire un modello operativo che consenta ai diversi componenti di collaborare in modo affidabile, mantenendo la separazione delle responsabilità e senza introdurre infrastrutture tipiche degli ambienti distribuiti.

La piattaforma deve funzionare sulla macchina dell'utente, senza dipendere da un server remoto per le funzionalità principali.

La soluzione deve quindi tenere conto di:

- Risorse hardware limitate rispetto a un'infrastruttura server.
- Necessità di avviare e arrestare correttamente i processi.
- Comunicazione esclusivamente locale.
- Gestione degli errori e dell'indisponibilità dei servizi.
- Sicurezza delle API esposte localmente.
- Distribuzione dei componenti insieme all'applicazione Desktop.

# 2. Architettura di comunicazione

## 2.1 Principio generale

Ogni microservizio sarà un componente backend autonomo, responsabile di una specifica area funzionale.

La comunicazione avverrà attraverso interfacce esplicite, evitando che un servizio acceda direttamente alle funzioni interne di un altro.

Si propone di adottare un modello di comunicazione basato su API HTTP locali.

Questo approccio permette di:

- Separare i processi.
- Definire contratti di comunicazione indipendenti.
- Testare i servizi singolarmente.
- Sostituire un'implementazione senza modificare gli altri componenti.
- Utilizzare strumenti di debugging e testing già consolidati.

## 2.2 Schema di comunicazione

```
┌──────────────────────────────────────────┐
│              TAURI DESKTOP               │
│                                          │
│             React + TypeScript           │
└────────────────────┬─────────────────────┘
                     │
                     │ HTTP / SSE
                     ▼
┌──────────────────────────────────────────┐
│             LOCAL API GATEWAY            │
│                                          │
│       Routing e coordinamento            │
└──────────┬──────────┬──────────┬──────────┘
           │          │          │
           │ HTTP     │ HTTP     │ HTTP
           ▼          ▼          ▼
     ┌──────────┐ ┌─────────┐ ┌──────────┐
     │ Document │ │   RAG   │ │    AI    │
     │ Service  │ │ Service │ │ Service  │
     └──────────┘ └─────────┘ └────┬─────┘
                                   │
                                   ▼
                             ┌──────────┐
                             │ Runtime  │
                             │ Adapter  │
                             └──────────┘

     ┌──────────┐       ┌──────────────┐
     │ Learning │       │   Notebook   │
     │ Service  │       │   Service    │
     └──────────┘       └──────────────┘

     ┌──────────────────────────────────┐
     │          JOB SERVICE             │
     │      Operazioni asincrone        │
     └──────────────────────────────────┘
```

Il Local API Gateway costituisce il punto di accesso principale per il frontend.

I microservizi non devono essere direttamente esposti all'interfaccia utente, salvo eventuali eccezioni giustificate da esigenze tecniche.

# 3. Protocollo di comunicazione

## 3.1 HTTP REST

Per la comunicazione tra i servizi si propone HTTP REST con payload JSON.

Ogni servizio esporrà endpoint dedicati alle proprie responsabilità.

Esempio:

```
POST /api/documents/import
GET  /api/documents/{document_id}
DELETE /api/documents/{document_id}

POST /api/rag/search
POST /api/ai/chat
POST /api/learning/quiz
POST /api/notebook/execute
GET  /api/jobs/{job_id}
```

Gli endpoint sono esempi illustrativi e non rappresentano ancora contratti API definitivi.

### Vantaggi

- Semplicità di implementazione.
- Compatibilità con FastAPI.
- Facilità di testing.
- Facilità di documentazione attraverso OpenAPI.
- Bassa complessità infrastrutturale.
- Possibilità di utilizzare lo stesso protocollo tra frontend e backend.

### Limiti

- Overhead della serializzazione JSON.
- Gestione esplicita delle richieste asincrone.
- Necessità di definire timeout e politiche di retry.
- Necessità di gestire correttamente le richieste di lunga durata.

Per l'MVP questi limiti sono considerati accettabili.

## 3.2 SSE per lo streaming

Le risposte del tutor IA possono richiedere diversi secondi per essere generate.

Non è opportuno attendere il completamento dell'intera risposta prima di mostrarla all'utente.

Si propone quindi Server-Sent Events (SSE).

Il flusso sarà:

1. Il frontend invia una richiesta al gateway.
2. Il gateway inoltra la richiesta all'AI Service.
3. L'AI Service comunica con il runtime selezionato.
4. Il runtime genera progressivamente la risposta.
5. L'AI Service trasmette gli eventi al gateway.
6. Il frontend riceve e visualizza progressivamente il testo.

Esempio concettuale:

```
Frontend
   |
   | POST /api/ai/chat
   |
   ▼
API Gateway
   |
   ▼
AI Service
   |
   ▼
Runtime Adapter
   |
   ▼
LLM Runtime
   |
   | Token generati
   ▼
AI Service
   |
   | SSE
   ▼
Frontend
```

SSE sarà utilizzato principalmente per:

- Risposte del tutor.
- Aggiornamenti di avanzamento.
- Stato delle operazioni lunghe.
- Notifiche di completamento dei job.

Per operazioni bidirezionali persistenti, come un eventuale notebook interattivo, si valuterà separatamente se utilizzare WebSocket.

## 3.3 HTTP REST oppure gRPC?

È utile confrontare le due alternative prima di congelare la scelta.

| **Criterio** | **HTTP REST** | **gRPC** |
| --- | --- | --- |
| Implementazione | Semplice | Più articolata |
| Payload | JSON | Protocol Buffers |
| Documentazione | OpenAPI | Protobuf |
| Debugging | Immediato | Richiede strumenti specifici |
| Streaming | SSE o altre soluzioni | Supportato nativamente |
| Overhead | Generalmente maggiore | Generalmente minore |
| Integrazione FastAPI | Diretta | Richiede componenti aggiuntivi |
| Complessità MVP | Bassa | Più alta |

**Proposta:** utilizzare HTTP REST per la comunicazione tra servizi nell'MVP.

gRPC potrà essere rivalutato in presenza di problemi misurabili di prestazioni o di necessità specifiche di streaming tra servizi.

Non è opportuno introdurre gRPC solo per ottenere un'architettura apparentemente più sofisticata.

# 4. Contratti API tra microservizi

## 4.1 Principio

Ogni servizio deve esporre un contratto stabile e documentato.

Il contratto definisce:

- Endpoint.
- Metodo HTTP.
- Parametri.
- Struttura delle richieste.
- Struttura delle risposte.
- Codici di errore.
- Autenticazione o autorizzazione richiesta.
- Timeout previsti.

I servizi non dovranno condividere direttamente oggetti Python interni o importare reciprocamente i propri moduli applicativi.

## 4.2 Formato dei messaggi

Si propone JSON per le richieste e le risposte.

Esempio di richiesta:

```
{
  "workspace_id": "workspace_001",
  "document_id": "document_001",
  "query": "Spiega il concetto di varianza"
}
```

Esempio di risposta:

```
{
  "status": "success",
  "data": {
    "answer": "La varianza misura la dispersione...",
    "citations": []
  },
  "error": null
}
```

La struttura è esemplificativa. Gli schemi effettivi dovranno essere definiti per ciascuna API.

## 4.3 Gestione degli errori

Gli errori dovranno essere uniformi e facilmente interpretabili.

Categorie previste:

- `VALIDATION_ERROR`: dati di input non validi.
- `SERVICE_UNAVAILABLE`: servizio non disponibile.
- `TIMEOUT`: operazione non completata entro il tempo previsto.
- `RESOURCE_LIMIT`: limite di risorse raggiunto.
- `INTERNAL_ERROR`: errore interno.
- `DEPENDENCY_ERROR`: errore causato da un servizio dipendente.

Ogni errore dovrà includere un codice, un messaggio e un identificativo utile per la diagnosi.

I dettagli interni e i percorsi locali non dovranno essere esposti inutilmente all'interfaccia utente.

# 5. Comunicazione sincrona e asincrona

## 5.1 Operazioni sincrone

Le operazioni brevi potranno essere eseguite attraverso richieste HTTP sincrone dal punto di vista del protocollo.

Esempi:

- Recupero dei metadati di un documento.
- Lettura delle informazioni di un workspace.
- Recupero dello stato di un job.
- Lettura delle impostazioni.

## 5.2 Operazioni asincrone

Le attività lunghe dovranno essere gestite attraverso un sistema di job.

Esempi:

- Importazione di documenti complessi.
- Generazione di embedding.
- Indicizzazione.
- Elaborazioni didattiche.
- Operazioni di manutenzione.

Il frontend avvierà l'operazione e riceverà un identificativo.

Esempio:

```
{
  "job_id": "job_001",
  "status": "queued"
}
```

Successivamente potrà monitorare lo stato attraverso un endpoint dedicato o un flusso di eventi.

## 5.3 Job Service

Per l'MVP si propone di mantenere il Job Service come componente backend dedicato logicamente, senza obbligare fin da subito a eseguirlo come processo indipendente.

La coda potrà essere persistita su SQLite.

Questo permette di:

- Recuperare i job dopo un riavvio.
- Evitare di perdere lo stato delle operazioni.
- Monitorare le attività.
- Gestire i retry.
- Evitare che le richieste lunghe blocchino l'interfaccia.

# 6. Gestione dei processi attraverso Tauri

## 6.1 Responsabilità di Tauri

Tauri sarà il supervisore del ciclo di vita dell'applicazione e dei servizi backend locali.

Dovrà occuparsi di:

- Avvio dei servizi.
- Verifica della disponibilità.
- Gestione dei processi.
- Monitoraggio dello stato.
- Gestione degli errori di avvio.
- Arresto controllato.
- Pulizia delle risorse temporanee.

È importante distinguere il ruolo di Tauri da quello dei servizi Python.

Tauri non dovrà contenere la logica applicativa del backend. Dovrà principalmente gestire l'esecuzione e l'integrazione dei componenti.

## 6.2 Modello di esecuzione

Si propone di distribuire i servizi Python come processi locali avviati dall'applicazione Desktop.

Tauri potrà utilizzare le funzionalità native di gestione dei processi, in particolare il plugin Shell di Tauri, opportunamente configurato.

La configurazione dovrà limitare i programmi eseguibili e gli argomenti consentiti.

Non dovrà essere possibile utilizzare l'interfaccia applicativa per eseguire comandi arbitrari sul sistema operativo.

## 6.3 Schema di avvio

```
             APERTURA APPLICAZIONE
                       |
                       ▼
                AVVIO TAURI
                       |
                       ▼
             INIZIALIZZAZIONE UI
                       |
                       ▼
             AVVIO LOCAL GATEWAY
                       |
                       ▼
              VERIFICA DISPONIBILITÀ
                       |
                       ▼
            AVVIO SERVIZI NECESSARI
                       |
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Document       RAG           AI
      Service      Service       Service
          |            |            |
          └────────────┼────────────┘
                       |
                       ▼
              HEALTH CHECK COMPLETI
                       |
                       ▼
              APPLICAZIONE PRONTA
```

L'ordine effettivo di avvio dovrà rispettare le dipendenze.

Ad esempio, il RAG Service potrebbe non essere considerato operativo finché non sono disponibili il database e il sistema di embedding necessari.

Il Notebook Service potrà essere avviato solo quando l'utente richiede il notebook, se il prototipo confermerà che l'avvio differito è vantaggioso.

## 6.4 Avvio differito dei servizi

Non tutti i servizi devono necessariamente essere avviati all'apertura dell'applicazione.

Si propone una strategia di avvio differenziata.

| **Servizio** | **Strategia proposta** |
| --- | --- |
| Local API Gateway | All'avvio |
| Document Service | All'avvio o al primo utilizzo |
| RAG Service | All'avvio o al primo utilizzo |
| AI Service | All'avvio o al primo utilizzo |
| Learning Service | All'avvio o al primo utilizzo |
| Job Service | All'avvio |
| Notebook Service | Al primo utilizzo |

La strategia definitiva dovrà essere valutata attraverso misurazioni dei tempi di avvio e del consumo di memoria.

## 6.5 Health check

Ogni servizio dovrà esporre un endpoint di verifica dello stato.

Esempio:

```
GET /health
```

Risposta:

```
{
  "status": "healthy",
  "service": "document-service"
}
```

Si propone inoltre un endpoint di readiness:

```
GET /ready
```

La differenza è importante:

- Health indica che il processo è attivo e risponde.
- Readiness indica che il servizio è pronto a gestire richieste operative.

Un servizio potrebbe essere attivo ma non ancora pronto perché sta inizializzando il modello, verificando il database o caricando le proprie dipendenze.

## 6.6 Gestione delle porte locali

Ogni servizio HTTP dovrà utilizzare una porta locale.

Non è consigliabile affidarsi a porte fisse senza una strategia di verifica.

Si propone di valutare:

- Assegnazione di porte dinamiche.
- Comunicazione al supervisore della porta effettivamente utilizzata.
- Verifica di eventuali conflitti.
- Registrazione delle porte assegnate.
- Binding esclusivamente su localhost.

Il gateway dovrà conoscere gli endpoint effettivi dei servizi.

La gestione delle porte dovrà evitare che un'altra applicazione possa intercettare richieste destinate ai servizi della piattaforma.

# 7. Arresto e riavvio

## 7.1 Chiusura dell'applicazione

Quando l'utente chiude la finestra Desktop, l'applicazione dovrà avviare una procedura di arresto controllato.

Sequenza proposta:

1. Impedire l'avvio di nuove operazioni.
2. Segnalare ai servizi che l'applicazione sta terminando.
3. Consentire il completamento delle operazioni brevi.
4. Interrompere le operazioni annullabili.
5. Terminare le sessioni notebook.
6. Arrestare i servizi backend.
7. Chiudere i processi figli residui.
8. Rilasciare le risorse.

Non tutte le operazioni dovranno necessariamente essere completate prima della chiusura.

I job persistenti dovranno poter essere recuperati o marcati correttamente come interrotti al successivo avvio.

## 7.2 Riavvio di un servizio

Se un servizio termina in modo anomalo, il supervisore dovrà rilevarne l'indisponibilità.

Si propone una strategia di recupero controllata:

- Registrazione dell'errore.
- Verifica della possibilità di riavvio.
- Tentativo limitato di riavvio.
- Nuovo health check.
- Aggiornamento dello stato dell'interfaccia.

Non tutti i servizi dovranno essere riavviati automaticamente.

Ad esempio, un riavvio del Notebook Service potrebbe comportare la perdita dello stato della sessione Python.

L'utente dovrà essere informato quando un'operazione o una sessione viene interrotta.

## 7.3 Stati dei servizi

Si propone di standardizzare gli stati visualizzati nella dashboard.

| **Stato** | **Significato** |
| --- | --- |
| `stopped` | Servizio arrestato |
| `starting` | Avvio in corso |
| `healthy` | Servizio operativo |
| `degraded` | Servizio attivo ma con funzionalità limitate |
| `unavailable` | Servizio non raggiungibile |
| `stopping` | Arresto in corso |
| `failed` | Avvio o esecuzione terminati con errore |

La dashboard degli agenti potrà utilizzare queste informazioni per rendere trasparente lo stato dei componenti.

# 8. Sicurezza della comunicazione locale

Il fatto che i servizi siano eseguiti sulla macchina dell'utente non significa che siano automaticamente sicuri.

Un servizio in ascolto su localhost può comunque ricevere richieste da altri processi e, in determinate condizioni, da contenuti Web non attendibili.

Si propongono le seguenti misure:

- Binding esclusivo su `127.0.0.1` o su un socket locale appropriato.
- Token di sessione casuali e non prevedibili.
- Validazione dell'origine delle richieste.
- Controllo degli header Origin e delle policy CORS.
- Validazione dei payload.
- Limitazione degli endpoint esposti.
- Nessuna esposizione diretta dei servizi su interfacce di rete esterne.
- Gestione sicura dei log.
- Separazione dei privilegi del Notebook Service.

Il token di accesso ai servizi locali dovrà essere gestito in modo da non essere esposto a script o contenuti documentali non attendibili.

Per il notebook, l'isolamento dovrà essere garantito a livello di sistema operativo o runtime di esecuzione, non semplicemente attraverso controlli applicativi.

# 9. Packaging e distribuzione

## 9.1 Obiettivo

L'utente finale non dovrà essere costretto a installare e configurare manualmente Python, FastAPI o i singoli servizi.

L'applicazione dovrà distribuire i componenti backend necessari oppure predisporre un sistema guidato per la loro installazione.

## 9.2 Modello proposto

```
Desktop Application
│
├── Tauri Runtime
│
├── Frontend
│
├── Local Gateway
│
├── Backend Services
│   ├── Document Service
│   ├── RAG Service
│   ├── AI Service
│   ├── Learning Service
│   └── Job Service
│
├── Notebook Runtime
│
├── Application Data
│   ├── SQLite
│   ├── ChromaDB
│   └── Documents
│
└── AI Models
```

Il modello rappresenta una struttura logica. Non implica che tutti i componenti debbano essere distribuiti nello stesso eseguibile o nella stessa directory.

## 9.3 Aspetti da verificare

- Packaging degli eseguibili Python.
- Gestione delle dipendenze native.
- Compatibilità Windows, macOS e Linux.
- Aggiornamento dei servizi.
- Distribuzione dei modelli AI.
- Gestione delle directory dati.
- Firma e distribuzione dell'applicazione.
- Dimensione complessiva dell'installazione.

La distribuzione dei modelli AI dovrà essere gestita separatamente dal packaging dei servizi, perché i modelli possono occupare molto spazio e avere requisiti hardware differenti.

# 10. Decisioni architetturali proposte

| **ID** | **Decisione** | **Proposta** | **Stato** |
| --- | --- | --- | --- |
| COM-001 | Comunicazione tra servizi | HTTP REST | Da validare |
| COM-002 | Formato dei messaggi | JSON | Da validare |
| COM-003 | Streaming tutor | SSE | Proposta |
| COM-004 | Comunicazione bidirezionale notebook | Da valutare, possibile WebSocket | Aperta |
| COM-005 | Gestione operazioni lunghe | Job Service + SQLite | Proposta |
| COM-006 | API frontend | Local API Gateway | Proposta |
| PROC-001 | Supervisione processi | Tauri | Direzione validata |
| PROC-002 | Avvio servizi | Processi locali gestiti da Tauri | Da validare |
| PROC-003 | Health check | `/health` e `/ready` | Proposta |
| PROC-004 | Avvio differito | Per i servizi non essenziali | Da validare |
| PROC-005 | Porte | Strategia dinamica o socket locale | Aperta |
| PROC-006 | Arresto | Shutdown controllato | Proposta |
| PROC-007 | Riavvio | Retry limitati e controllati | Proposta |
| PROC-008 | Packaging | Backend distribuito con Desktop | Da prototipare |

# 11. Proof of Concept

Prima di adottare definitivamente queste soluzioni, si propone un prototipo circoscritto.

## POC-01 — Comunicazione tra servizi

**Obiettivo:** verificare la comunicazione HTTP tra due servizi Python indipendenti.

Attività:

1. Creare un Document Service minimale.
2. Creare un RAG Service minimale.
3. Esporre endpoint HTTP.
4. Effettuare richieste tra i servizi.
5. Definire un contratto JSON.
6. Gestire timeout e indisponibilità.
7. Verificare il comportamento del gateway.

Criteri di successo:

- Comunicazione funzionante.
- Contratti documentati.
- Errori gestiti.
- Nessuna dipendenza diretta dai moduli interni degli altri servizi.

## POC-02 — Gestione processi Tauri

**Obiettivo:** verificare che Tauri possa gestire i processi backend locali.

Attività:

1. Creare una piccola applicazione Tauri.
2. Distribuire un servizio Python.
3. Avviarlo attraverso il sistema di gestione processi.
4. Verificare la disponibilità.
5. Visualizzare lo stato nella UI.
6. Arrestare l'applicazione.
7. Verificare la terminazione del servizio.

Criteri di successo:

- Avvio automatico.
- Health check funzionante.
- Arresto controllato.
- Nessun processo residuo.
- Gestione degli errori di avvio.

## POC-03 — Streaming AI

**Obiettivo:** verificare il flusso completo di generazione progressiva.

Attività:

1. Collegare un runtime locale.
2. Implementare l'adapter.
3. Inviare una richiesta attraverso il gateway.
4. Trasmettere la risposta tramite SSE.
5. Visualizzare progressivamente il testo.
6. Gestire interruzione e timeout.

Criteri di successo:

- Streaming fluido.
- Nessun blocco dell'interfaccia.
- Gestione corretta delle interruzioni.
- Errori comunicati al frontend.

## POC-04 — Avvio e arresto completo

**Obiettivo:** verificare il comportamento dell'applicazione in uno scenario realistico.

Attività:

1. Avviare più servizi.
2. Verificare le dipendenze.
3. Simulare l'indisponibilità di un servizio.
4. Simulare un crash.
5. Provare un riavvio controllato.
6. Chiudere l'applicazione.
7. Verificare la terminazione di tutti i processi.

Criteri di successo:

- Gestione affidabile del ciclo di vita.
- Nessun processo residuo.
- Stato dei servizi coerente.
- Errori tracciabili.

# 12. Raccomandazione conclusiva

Per la piattaforma si raccomanda un modello di comunicazione semplice e un sistema di supervisione centralizzato.

La proposta di riferimento è:

- Tauri come supervisore dei processi locali.
- React come interfaccia utente.
- Local API Gateway come punto di accesso del frontend.
- HTTP REST per la comunicazione tra servizi.
- JSON come formato dei messaggi.
- SSE per lo streaming delle risposte.
- Job Service per le operazioni asincrone.
- Health check per monitorare la disponibilità.
- Shutdown controllato per la chiusura dell'applicazione.

La priorità non è ottenere la massima sofisticazione infrastrutturale, ma costruire un sistema locale affidabile, manutenibile e compatibile con le risorse disponibili.

Le decisioni definitive dovranno essere prese dopo i POC, documentando i risultati e aggiornando l'Architettura Tecnica.

---

**Fine documento**
