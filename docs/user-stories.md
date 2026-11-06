# User Stories e Criteri di Accettazione

Nov 2, 2026 · @Andrea

## Convenzioni

Ogni storia ha la forma "Come utente voglio X per ottenere Y" e criteri di accettazione verificabili con un test. I numeri nei criteri sono soglie iniziali da confermare con il team tecnico.

- **ID:** lettera dell'epica + numero (A1, B3).
- **Fase:** MVP, v1 o v2, coerente con la roadmap.
- **Definizione di completato:** criteri superati, test automatici scritti, nessuna regressione, funzionamento offline per le parti local-first, documentazione aggiornata.

## Epica A: Documenti e spazio di lavoro

| ID | Storia | Criteri di accettazione | Fase |
| --- | --- | --- | --- |
| A1 | Come utente voglio trascinare un file nel workspace per iniziare subito a leggerlo | 1) Il file compare nel lettore entro 2 s per file sotto i 50 MB. 2) Formati MVP: PDF, Markdown, DOCX. 3) Un file non supportato mostra un errore chiaro | MVP |
| A2 | Come utente voglio che il file venga indicizzato in background per fare domande senza attese | 1) La lettura non è bloccata durante l'indicizzazione. 2) Lo stato è visibile nella barra in basso. 3) A indicizzazione finita, la ricerca per similarità risponde in meno di 200 ms | MVP |
| A3 | Come utente voglio evidenziare, annotare e aggiungere segnalibri per ritrovare i passaggi importanti | 1) Annotazioni e evidenziazioni persistono dopo la chiusura dell'app. 2) Il file originale non viene modificato. 3) Le annotazioni sono ricercabili | MVP |
| A4 | Come utente voglio riaprire un documento dal punto in cui ero rimasto | 1) Pagina e posizione si ripristinano all'apertura. 2) Funziona anche dopo un riavvio | MVP |
| A5 | Come utente voglio importare EPUB, PPTX, CSV ed Excel per studiare da ogni tipo di materiale | 1) Ogni formato è indicizzato e citabile. 2) Nei fogli di calcolo le tabelle restano interrogabili dal notebook | v1 |
| A6 | Come utente voglio organizzare i file in spazi di lavoro separati per materia | 1) Ogni spazio ha un indice vettoriale proprio. 2) Una ricerca non pesca da spazi non selezionati, salvo richiesta esplicita | MVP |

## Epica B: Assistente RAG contestuale

| ID | Storia | Criteri di accettazione | Fase |
| --- | --- | --- | --- |
| B1 | Come utente voglio selezionare un testo e vedere una barra rapida per chiedere aiuto senza uscire dal documento | 1) La barra compare entro 50 ms dalla selezione. 2) Opzioni: Spiega, Semplifica, Formalizza, Cerca collegamenti, Mostra codice. 3) La risposta appare nel pannello destro senza spostare il punto di lettura | MVP |
| B2 | Come utente voglio risposte con citazione per verificare che non siano inventate | 1) Ogni affermazione tratta da un documento riporta file e pagina o sezione. 2) Cliccando la citazione il lettore si apre sul passaggio. 3) Se la fonte non c'è, il sistema lo dichiara | MVP |
| B3 | Come utente voglio che la risposta parta dal documento aperto e si estenda alla libreria solo se serve | 1) Il livello 1 usa il solo documento aperto. 2) Il livello 2 integra gli altri documenti dello spazio e lo segnala. 3) L'utente può forzare il livello | MVP |
| B4 | Come utente voglio la ricerca web per chiarimenti e aggiornamenti | 1) Il livello 3 è attivabile e disattivabile. 2) Le fonti web sono distinte da quelle locali. 3) Senza rete il sistema continua a funzionare sui livelli 1-2 | v1 |
| B5 | Come utente voglio vedere la risposta mentre viene scritta | 1) Il primo testo compare entro 1,5 s su hardware di riferimento. 2) Le formule sono mostrate in LaTeX formattato | MVP |
| B6 | Come utente voglio che i calcoli nelle risposte siano controllati | 1) I calcoli numerici e simbolici passano da una verifica (SymPy/NumPy). 2) Un esito discordante è segnalato all'utente | v1 |

## Epica C: Diagnostica, lezioni integrative e livelli di rigore

| ID | Storia | Criteri di accettazione | Fase |
| --- | --- | --- | --- |
| C1 | Come utente voglio scegliere il livello di rigore (da 1 a 5) per ogni spiegazione | 1) Il livello è selezionabile da toolbar e da pannello. 2) I livelli 1-3 sono disponibili nell'MVP, 4-5 in v1. 3) La stessa domanda a livelli diversi produce spiegazioni diverse per notazione e profondità | MVP |
| C2 | Come utente voglio che il sistema trovi le lacune del materiale caricato | 1) Al termine dell'importazione parte un'analisi in background. 2) Il risultato elenca gli argomenti omessi o poco trattati (esempio: curtosi, asimmetria). 3) L'utente può ignorare una lacuna | v1 |
| C3 | Come utente voglio lezioni integrative generate per colmare le lacune | 1) Ogni lezione indica la lacuna a cui risponde. 2) Contiene esempi e almeno un esercizio. 3) Rispetta il livello scelto | v1 |
| C4 | Come utente voglio un test diagnostico iniziale per partire dal livello giusto | 1) Il test dura al massimo 15 minuti. 2) Esito: livello consigliato per argomento. 3) L'utente può cambiarlo a mano | v1 |
| C5 | Come utente voglio vedere i prerequisiti di un concetto per non studiare nel vuoto | 1) Ogni concetto mostra i prerequisiti nel grafo. 2) Se un prerequisito risulta debole, il sistema propone di ripassarlo prima | v1 |
| C6 | Come utente voglio una modalità socratica che mi guidi con domande | 1) Il tutor pone domande prima di dare la soluzione. 2) Dopo 3 tentativi sbagliati offre un suggerimento. 3) L'utente può chiedere la risposta in ogni momento | v1 |
| C7 | Come utente voglio spiegare un concetto con parole mie e ricevere un controllo | 1) Il sistema segnala errori e passaggi mancanti. 2) Il feedback cita il documento di riferimento | v1 |

## Epica D: Animazioni Manim e widget interattivi

| ID | Storia | Criteri di accettazione | Fase |
| --- | --- | --- | --- |
| D1 | Come utente voglio manipolare un widget (slider su media e deviazione standard) per vedere cambiare la curva | 1) L'aggiornamento grafico avviene in meno di 100 ms. 2) Il widget è incorporato nella lezione. 3) Almeno 3 widget nell'MVP | MVP |
| D2 | Come utente voglio guardare un'animazione di un concetto astratto (esempio: teorema del limite centrale) | 1) Il blocco "Guarda l'animazione" compare nella lezione. 2) Il video parte in-line o si espande a pannello. 3) Durante il rendering si vede lo stato e la lezione resta utilizzabile | v1 |
| D3 | Come utente non voglio attendere di nuovo per un'animazione già generata | 1) Scene identiche producono lo stesso hash e riusano il file in cache. 2) Il secondo accesso è immediato | v1 |
| D4 | Come utente voglio che un'animazione fallita non blocchi la lezione | 1) Il sistema tenta fino a 3 correzioni automatiche dello script. 2) Dopo il fallimento mostra un'alternativa statica e registra l'errore nella dashboard | v1 |
| D5 | Come utente voglio visualizzazioni interattive di gradient descent e backpropagation | 1) Almeno 3 visualizzazioni 2D o 3D con parametri modificabili. 2) Lo stato è collegato alla lezione corrispondente | v2 |

## Epica E: Notebook e pratica

| ID | Storia | Criteri di accettazione | Fase |
| --- | --- | --- | --- |
| E1 | Come utente voglio passare dalla chat al notebook con un solo clic | 1) Il toggle commuta il pannello in meno di 100 ms. 2) Lo stato della chat resta intatto | MVP |
| E2 | Come utente voglio eseguire il codice suggerito dall'IA e vedere grafici e tabelle subito | 1) Il codice gira in un kernel Python isolato. 2) Gli output compaiono nel client senza ricaricare la pagina. 3) Una cella con errore mostra l'errore senza arrestare il kernel | MVP |
| E3 | Come utente voglio che il codice non possa danneggiare il mio computer | 1) Il kernel non accede a file fuori dallo spazio di lavoro. 2) Rete disattivata per impostazione predefinita. 3) Limiti di tempo e memoria per ogni cella | MVP |
| E4 | Come utente voglio esercizi con soluzione passo-passo e correzione automatica | 1) La risposta simbolica viene confrontata con quella attesa (equivalenza algebrica). 2) L'errore ricorrente è registrato per il ripasso | v1 |
| E5 | Come utente voglio implementare un paper di ML a partire dal suo testo | 1) Dal paper si genera uno scheletro di codice commentato. 2) Ogni passaggio rimanda alla sezione del paper | v2 |
| E6 | Come utente voglio progetti guidati (esempio: regressione logistica da zero) | 1) Il progetto è diviso in passi con verifica automatica. 2) Si può riprendere dal passo lasciato | v2 |

## Epica F: Flashcard, ripetizione spaziata e quiz

| ID | Storia | Criteri di accettazione | Fase |
| --- | --- | --- | --- |
| F1 | Come utente voglio flashcard create dal materiale studiato | 1) Le schede nascono da formule, definizioni e concetti del documento. 2) Ogni scheda rimanda alla fonte. 3) L'utente può modificarle o eliminarle | MVP |
| F2 | Come utente voglio ripassare nei momenti ottimali | 1) Un algoritmo di ripetizione spaziata pianifica le revisioni. 2) La coda del giorno mostra solo le schede in scadenza. 3) La valutazione della risposta aggiorna l'intervallo | v1 |
| F3 | Come utente voglio quiz a risposta multipla o aperta sul livello scelto | 1) Il quiz è calibrato sul livello di rigore selezionato. 2) Le risposte aperte sono valutate con motivazione. 3) Il risultato aggiorna la padronanza | MVP (multipla); v1 (aperta) |
| F4 | Come utente voglio vedere la mia padronanza per concetto | 1) Ogni concetto ha un punteggio basato su quiz e ripassi. 2) Gli errori ricorrenti sono elencati | v1 |
| F5 | Come utente voglio un piano di studio con obiettivi e scadenze | 1) Il piano suggerisce le sessioni in base a scadenza e padronanza. 2) Mostra serie di giorni consecutivi di studio | v1 |
| F6 | Come utente voglio esportare le schede in Anki | 1) L'export produce un file importabile in Anki senza perdita di formule | v2 |

## Epica G: Audio e dashboard agenti

| ID | Storia | Criteri di accettazione | Fase |
| --- | --- | --- | --- |
| G1 | Come utente voglio vedere cosa stanno facendo gli agenti in background | 1) La barra in basso elenca indicizzazione, analisi lacune e rendering. 2) Ogni attività mostra stato (in coda, in corso, completata, fallita) e avanzamento. 3) La barra è riducibile e non invasiva | MVP |
| G2 | Come utente voglio poter annullare o rilanciare un'attività | 1) L'annullamento interrompe il processo entro 2 s. 2) Il rilancio riparte dall'ultimo passo utile | v1 |
| G3 | Come utente voglio caricare una lezione audio o video e ottenere note | 1) La trascrizione avviene in locale con Whisper. 2) Il testo è strutturato in titoli e punti chiave. 3) La nota è indicizzata come ogni altro documento | v2 |
| G4 | Come utente voglio un'interfaccia scura e fluida durante sessioni lunghe | 1) Tema scuro predefinito. 2) Feedback visivo a ogni azione in meno di 50 ms | MVP |
