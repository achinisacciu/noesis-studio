# PRD — Piattaforma IA per l'Auto-Apprendimento Avanzato

Nov 2, 2026 · @Andrea

## Sintesi e visione

La piattaforma trasforma libri, paper e slide in un percorso di studio personalizzato di Statistica, Matematica, Machine Learning e Deep Learning, in un unico ambiente. Un lettore di documenti a sinistra e un tutor IA con notebook a destra sostituiscono l'uso di strumenti separati.

Il prodotto agisce da copilota e tutor privato: spiega ciò che l'utente sta leggendo, individua le lacune del materiale, genera lezioni integrative a cinque livelli di rigore, produce animazioni e widget interattivi e verifica l'apprendimento con esercizi, quiz e ripetizione spaziata. Tutta l'intelligenza artificiale è open source e gira in locale o su infrastruttura self-hosted.

## Utenti target e persona

Il target è un adulto che vuole imparare materie quantitative complesse partendo da qualsiasi livello, senza un docente a disposizione.

| Profilo | Situazione | Bisogno principale |
| --- | --- | --- |
| Autodidatta tecnico | Studia ML da libri e paper, si blocca su formule e prerequisiti | Capire il "perché" e colmare le lacune senza cercare altrove |
| Studente universitario | Segue corsi di statistica o analisi con slide e dispense | Spiegazioni a più livelli, esercizi, ripasso per gli esami |
| Professionista che cambia ambito | Ha poco tempo e basi parziali | Percorso su misura, partenza dal livello giusto |

Ipotesi da validare con interviste: l'utente accetta di usare un'app desktop locale e dispone di un computer con GPU o di un server personale.

## Problema, obiettivi e metriche di successo

Chi studia da solo deve passare da lettore PDF, chatbot, notebook e app di flashcard, perdendo contesto a ogni cambio. Il prodotto unisce questi passaggi e rende verificabile ciò che si impara.

**Obiettivi**

- Portare l'utente da un documento statico a una lezione comprensibile in pochi secondi.
- Rendere ogni risposta dell'IA verificabile, con citazione di pagina o sezione.
- Misurare l'apprendimento reale, non solo l'uso dell'app.

**Metriche** (soglie iniziali, da tarare sui test utente)

| Metrica | Definizione | Obiettivo iniziale |
| --- | --- | --- |
| Padronanza del capitolo | Utenti che superano il quiz finale di un capitolo studiato | ≥ 70% |
| Tempo al primo valore | Dal caricamento del file alla prima risposta contestuale | < 60 s |
| Affidabilità delle risposte | Risposte con citazione corretta sul set di valutazione | ≥ 90% |
| Ritenzione | Flashcard ricordate a 30 giorni | ≥ 80% |
| Uso settimanale | Utenti che aprono almeno 3 sessioni di studio a settimana | ≥ 40% |

## Funzionalità e priorità

Le funzionalità sono raggruppate per area; la colonna Fase indica dove entrano nella roadmap (MVP, v1, v2).

| Area | Funzionalità | Fase |
| --- | --- | --- |
| Documenti | Importazione PDF, Markdown, Word, EPUB, PowerPoint, CSV, Excel; annotazioni, evidenziazioni, segnalibri, stato di lettura | MVP (PDF, MD, DOCX); v1 (resto) |
| Documenti | Visualizzatore integrato in sola lettura con annotazione non distruttiva | MVP |
| RAG | Toolbar sul testo selezionato (Spiega, Semplifica, Formalizza, Cerca collegamenti) | MVP |
| RAG | Tre livelli di contesto: documento, libreria, web; risposte con citazione di pagina o sezione | MVP (livelli 1-2); v1 (web) |
| Didattica | Lezioni a 5 livelli di rigore | MVP (livelli 1-3); v1 (livelli 4-5) |
| Didattica | Analisi delle lacune e lezioni integrative in background | v1 |
| Didattica | Test diagnostico iniziale e assegnazione del livello | v1 |
| Didattica | Grafo dei concetti con prerequisiti | v1 |
| Didattica | Modalità socratica e modalità Feynman | v1 |
| Pratica | Notebook Python integrato con celle eseguibili | MVP |
| Pratica | Esercizi con soluzione passo-passo e correzione simbolica | v1 |
| Pratica | Progetti guidati e da paper a codice | v2 |
| Visuale | Widget interattivi nelle lezioni (slider su media e deviazione standard) | MVP (2-3 widget) |
| Visuale | Animazioni Manim generate in background, con cache | v1 |
| Visuale | Visualizzazioni interattive per ML e DL (gradient descent, backpropagation) | v2 |
| Memoria | Flashcard automatiche, ripetizione spaziata, quiz personalizzati | MVP (flashcard base); v1 (SRS completo, quiz) |
| Memoria | Tracciamento della padronanza per concetto e piano di studio | v1 |
| Audio | Trascrizione locale di audio e video (Whisper) in note strutturate | v2 |
| Sistema | Dashboard degli agenti in background | MVP (versione minima) |
| Sistema | Glossario e notazione unificata tra documenti | v2 |
| Sistema | Export verso Anki, Obsidian, Markdown; backup e sincronizzazione cifrata opzionale | v2 |

## Ambito: MVP e fuori ambito

L'MVP deve dimostrare un solo percorso completo: caricare un PDF di statistica, farsi spiegare un passaggio, eseguire il codice e superare un quiz.

**Nell'MVP**

- Importazione di PDF, Markdown e Word con indicizzazione locale.
- Lettore con annotazioni e toolbar contestuale.
- RAG su documento e libreria, con citazioni.
- Lezioni ai livelli 1-3, con 2-3 widget interattivi.
- Notebook Python in sandbox.
- Flashcard base e quiz semplice.
- Stato dei processi in una barra riducibile.

**Fuori ambito (per ora)**

- Editor di testo completo: il lettore resta in sola consultazione.
- Funzioni collaborative o social.
- App mobile nativa.
- Addestramento o fine-tuning di modelli.
- Contenuti didattici originali venduti come corsi.

## Principi e vincoli

- **Open source al 100%:** nessuna dipendenza da API o modelli proprietari a pagamento; costo di licenza zero.
- **Local-first:** i dati dell'utente risiedono sulla sua macchina o sulla sua istanza; la rete è opzionale (serve solo per la ricerca web).
- **Latenza percepita bassa:** feedback visivo sotto i 50 ms; le risposte lunghe arrivano in streaming e le operazioni pesanti (Manim, indicizzazione) girano in background con anteprima.
- **Risposte verificabili:** ogni risposta cita la fonte e i calcoli sono controllati con strumenti simbolici.
- **Flessibilità tecnologica:** il documento definisce capacità e requisiti; lo stack lo sceglie il team, nel rispetto di velocità e licenze open source.
- **Interfaccia a doppio pannello:** documenti a sinistra, tutor e notebook a destra, tema scuro predefinito.

## Rischi e questioni aperte

| Rischio | Impatto | Mitigazione |
| --- | --- | --- |
| Modelli locali piccoli sbagliano la matematica | Spiegazioni errate | Verifica simbolica (SymPy) e citazione obbligatoria delle fonti |
| Estrazione delle formule da PDF di bassa qualità | RAG e lezioni peggiori | Pipeline OCR matematico con revisione manuale dei casi dubbi |
| Script Manim generati dall'IA che non compilano | Animazioni mancanti | Ciclo di auto-correzione e libreria di scene verificate |
| Esecuzione di codice generato dall'IA | Rischio sicurezza | Sandbox isolata, senza rete né accesso ai file dell'utente |
| Requisiti hardware elevati | Barriera d'ingresso | Profili di configurazione per hardware modesto |
| Portata troppo ampia | Ritardi | MVP ristretto e roadmap a tre fasi |

**Questioni aperte**

- [ ] Il prodotto parte come app desktop o come web app self-hosted?
- [ ] Quali lingue per i contenuti: solo italiano, o italiano e inglese dal primo rilascio?
- [ ] Quale hardware minimo si garantisce per l'MVP?
- [ ] Serve un modello di sostenibilità (donazioni, versione a pagamento) nonostante lo zero licensing?
