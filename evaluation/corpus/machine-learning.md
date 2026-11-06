# Machine learning

## Apprendimento supervisionato

Nell'apprendimento supervisionato il modello impara da esempi già etichettati: a ogni input è associata la risposta corretta. Se la risposta è una categoria si parla di classificazione, se è un numero continuo si parla di regressione. Nell'apprendimento non supervisionato, come il clustering, le etichette non esistono e l'algoritmo cerca raggruppamenti o strutture nei dati. La differenza centrale è quindi la presenza di una risposta di riferimento durante l'addestramento.

## Regressione lineare

La regressione lineare stima una relazione lineare tra una o più variabili di input e una variabile di output, trovando la retta o l'iperpiano che meglio approssima i dati. Il metodo dei minimi quadrati sceglie i coefficienti che minimizzano la somma dei quadrati delle differenze tra valori osservati e valori previsti. Il coefficiente angolare, o pendenza, indica di quanto cambia l'output quando l'input aumenta di una unità. L'intercetta è il valore previsto quando tutti gli input valgono zero.

## Discesa del gradiente

La discesa del gradiente è un algoritmo iterativo di ottimizzazione: calcola il gradiente della funzione di perdita rispetto ai parametri e sposta i pesi nella direzione opposta, cioè verso il basso, per ridurre l'errore. Il learning rate, o passo di apprendimento, decide quanto grande è ogni spostamento. Un passo troppo grande fa oscillare o divergere la perdita; un passo troppo piccolo rende l'addestramento lentissimo. Esistono varianti come il gradiente stocastico, che aggiorna i pesi su piccoli lotti di esempi.

## Overfitting e regolarizzazione

L'overfitting si riconosce quando il modello ottiene ottime prestazioni sui dati di addestramento ma scarse su dati nuovi: ha memorizzato il rumore invece della regolarità. La regolarizzazione combatte il fenomeno aggiungendo alla perdita una penalità sulla complessità dei pesi. La penalità L2, o ridge, somma i quadrati dei pesi e li mantiene piccoli; la penalità L1, o lasso, somma i valori assoluti e tende a portare alcuni pesi esattamente a zero, producendo selezione delle variabili. Ridurre il numero di parametri o raccogliere più dati sono altre difese.

## Validazione incrociata

La validazione incrociata stima le prestazioni del modello dividendo i dati in più parti, dette pieghe: si addestra su alcune e si valida sulla piega esclusa, ripetendo la rotazione e mediando i risultati. È preferibile a una singola divisione perché riduce la variabilità della stima e usa tutti gli esempi sia per l'addestramento sia per la valutazione. Il test set resta separato fino alla fine, per misurare le prestazioni su dati mai visti ed evitare di scegliere il modello guardando la stessa informazione usata per stimarlo.

## Metriche di classificazione

La matrice di confusione confronta previsioni e verità e da essa derivano le metriche principali. La precisione, o precision, è la quota di positivi previsti che sono davvero positivi. Il richiamo, o recall, è la quota di positivi reali che il modello ha trovato. L'accuratezza è la quota totale di previsioni corrette, ma inganna con classi sbilanciate. La F1 combina precisione e richiamo con una media armonica e si usa quando entrambi gli errori contano.
