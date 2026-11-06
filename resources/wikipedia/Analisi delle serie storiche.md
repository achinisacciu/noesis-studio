---
title: "Analisi delle serie storiche"
source: "https://it.wikipedia.org/wiki/Analisi_delle_serie_storiche"
author:
  - "[[Wikipedia]]"
published: 2008-07-10
created: 2026-11-06
description:
tags:
  - "clippings"
---
L' **analisi delle serie storiche** raggruppa una serie di metodi [statistici](https://it.wikipedia.org/wiki/Statistica "Statistica") atti a indagare una [serie storica](https://it.wikipedia.org/wiki/Serie_storica "Serie storica"), determinare il processo alla base della stessa e a trarre previsioni. Secondo l'approccio tradizionale, si assume che il processo abbia una parte deterministica, che consente di scomporlo in componenti tendenziali, cicliche e/o stagionali, e che la differenza tra i dati teorici del modello deterministico ed i dati osservati sia attribuibile ad una componente casuale residuale. Secondo l'approccio moderno, invece, si assume che il processo descritto sia stato generato da un [processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico") descrivibile mediante un modello probabilistico di tipo parametrico.

## Obiettivi

L'analisi di una serie storica può avere diversi obiettivi:

- descrivere sinteticamente l'andamento nel tempo di un fenomeno; il grafico di una serie, in particolare, mette facilmente in evidenza sia eventuali regolarità, sia valori anomali;
- spiegare il fenomeno, individuando il suo meccanismo generatore ed eventuali relazioni con altri fenomeni;
- filtrare la serie; con ciò si intende la scomposizione della serie stessa nelle sue componenti non osservabili;
- prevedere l'andamento futuro del fenomeno.

## Operazioni preliminari

Prima di qualsiasi analisi, si esaminano i dati grezzi e si apportano spesso alcuni aggiustamenti per depurare i dati da discontinuità o dagli effetti della diversa durata degli intervalli o periodi di tempo considerati, oppure per tenere conto di valori anomali.

### Discontinuità

Alcuni esempi di discontinuità sono i cambiamenti di base nelle serie storiche di numeri indice, oppure la presenza di metriche diverse per le variabili economiche (prezzi correnti o costanti, diversi criteri di [deflazione](https://it.wikipedia.org/wiki/Deflatore_del_PIL "Deflatore del PIL") ecc.).

In tali casi, se non si riesce ad eliminare la discontinuità può essere preferibile limitare l'analisi a dati omogenei.

### Effetti di calendario

La diversa durata dei periodi incide sui valori osservati nei medesimi periodi di anni diversi, producendo variazioni non ascrivibili all'andamento del fenomeno; ad esempio, in serie mensili di dati di produzione, le variazioni nei dati grezzi dipendono in parte solo dal numero dei giorni lavorativi nei diversi mesi. Si possono eliminare tali perturbazioni in vari modi:

- aggregando i dati in periodi più lunghi, ad esempio passando da serie mensili a serie trimestrali o semestrali;
- passando a dati medi giornalieri, ossia sostituendo il dato mensile grezzo con il rapporto tra il valore osservato ed il numero di giorni rilevanti nel mese cui il valore si riferisce; indicando con *y* <sub>m</sub> il valore osservato nel mese *m* e con *N* <sub>m</sub> il numero dei giorni rilevanti (ad esempio, il numero di giorni lavorativi) nel mese considerato:

${\displaystyle y_{m}^{MG}={\frac {y_{m}}{N_{m}}}}$

- applicando coefficienti correttivi, ad esempio sostituendo il valore mensile *y* <sub>m</sub> con un valore "aggiustato" *y* <sup>AG</sup> <sub>m</sub>, pari al prodotto del valore grezzo per il rapporto tra la media mensile dei giorni rilevanti in tutto l'anno ed il numero di giorni del mese cui il valore si riferisce:

${\displaystyle y_{m}^{AG}=y_{m}c_{m}=y_{m}{\frac {N_{a}}{N_{m}}}\qquad N_{a}={\frac {1}{12}}\sum _{m=1}^{12}N_{m}}$

### Valori anomali

Si possono distinguere due categorie di valori anomali (detti anche *[outlier](https://it.wikipedia.org/wiki/Outlier "Outlier")*):

- si ha una brusca variazione nella serie in un dato istante, dopo il quale però la serie stessa ritorna immediatamente (cosiddetto *outlier* additivo) o gradualmente (cosiddetto *cambiamento temporaneo*) all'andamento precedente;
- si ha una brusca variazione che permane nel tempo, provocando un cambiamento del livello o dello stesso andamento della serie (ad esempio, il [PIL](https://it.wikipedia.org/wiki/PIL "PIL") della [Germania](https://it.wikipedia.org/wiki/Germania "Germania") è salito di livello dopo la riunificazione del [1990](https://it.wikipedia.org/wiki/1990 "1990")).

Nel primo caso si preferisce ignorare il valore anomalo, eventualmente sostituendolo con una media di valori immediatamente precedenti e successivi, nel secondo è preferibile spezzare la serie ed analizzare separatamente i dati anteriori e posteriori alla variazione.

![](https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2c/Outlier.svg/960px-Outlier.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Esempi di valori anomali

### Correlogramma

Si usa spesso visualizzare il [correlogramma](https://it.wikipedia.org/wiki/Correlogramma "Correlogramma") della serie, al fine di individuare l'eventuale prevalenza di una componente tendenziale, stagionale o stocastica.

## Approccio tradizionale

In generale, si assume che i dati in serie storica relativi ad un fenomeno *Y* siano generati da un processo del tipo:

${\displaystyle Y_{t}=f(t)+u_{t}}$

dove *f* (*t*) genera una sequenza completamente deterministica (*parte sistematica* della serie) e { *u* <sub>t</sub> } è una sequenza di [variabili aleatorie](https://it.wikipedia.org/wiki/Variabile_aleatoria "Variabile aleatoria") che obbediscono ad una qualche legge di [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") (*parte stocastica* della serie).

Nell'approccio tradizionale si assume che esista una "legge" di evoluzione temporale del fenomeno, rappresentata da *f* (*t*), e che i *residui* (differenze tra valori teorici e valori osservati) siano dovuti al caso e, pertanto, siano assimilabili a errori accidentali. I residui vengono normalmente indicati con *ε* <sub>t</sub> ed intesi come variabili aleatorie [indipendenti](https://it.wikipedia.org/wiki/Indipendenza_stocastica "Indipendenza stocastica"), identicamente [distribuite](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0 "Distribuzione di probabilità"), con [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") nulla e [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") costante (nell'approccio moderno, invece, si ipotizza che la parte sistematica manchi o sia già stata eliminata, mediante stime o altri modelli, e si studia la componente stocastica *u* <sub>t</sub>).

Si ritiene, inoltre, che la parte sistematica sia la risultante di tre componenti non direttamente osservabili:

- il **trend** (o *componente tendenziale*) è la tendenza di fondo del fenomeno considerato, spesso espressa mediante una funzione polinomiale di grado non troppo elevato;
- il **ciclo** (o *componente congiunturale*) è l'alternanza di fluttuazioni di segno diverso intorno al trend (v. anche [ciclo economico](https://it.wikipedia.org/wiki/Ciclo_economico "Ciclo economico"));
- la **stagionalità** (o *componente stagionale*) è costituita da variazioni che si riscontrano con analoga intensità negli stessi periodi di anno in anno, ma con intensità diversa nel corso di uno stesso anno (ad esempio, la produzione cala tutti gli anni in estate a seguito della chiusura per ferie di molte aziende, ma aumenta tutti gli anni in prossimità del Natale per effetto dei maggiori consumi).

La componente accidentale è data dai residui *ε* <sub>t</sub>. Ad esempio, se si dispone di dati trimestrali, se si stima che i dati sono prodotti da un trend di crescita lineare del tipo:[^1]

${\displaystyle {\hat {y}}_{t}=200+1.5t}$

se si individua una componente stagionale che provoca un aumento nel secondo e nel quarto trimestre ed una diminuzione nel primo e nel terzo:

${\displaystyle {\hat {y}}_{t}=200+1.5t-4Q_{1}+4Q_{2}-8Q_{3}+8Q_{4}}$

(dove le *Q* <sub>i</sub> sono variabili che assumono il valore 1 nell' *i* -esimo trimestre e 0 negli altri), le differenze tra i valori osservati *y* <sub>t</sub> ed i valori stimati sono:

${\displaystyle \varepsilon _{t}=y_{t}-{\hat {y}}_{t}}$

![](https://thumb.wikimedia.org/wikipedia/commons/thumb/1/14/Piltrim.svg/960px-Piltrim.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Esempio di serie storica e di sua scomposizione nelle componenti tendenziale, stagionale e accidentale

### Modelli di combinazione delle componenti

Alcuni tipici modelli tradizionali sono:

- *modello additivo*: ${\displaystyle Y_{t}=T_{t}+C_{t}+S_{t}+\varepsilon _{t}}$;
- *modello moltiplicativo*: ${\displaystyle Y_{t}=T_{t}\cdot C_{t}\cdot S_{t}\cdot \varepsilon _{t}}$;
- *modello misto*: ${\displaystyle Y_{t}=T_{t}\cdot C_{t}\cdot S_{t}+\varepsilon _{t}}$;

dove *T* <sub>t</sub> è il valore del trend al tempo *t*, *C* <sub>t</sub> è il valore del ciclo, *S* <sub>t</sub> quello della stagionalità e *ε* <sub>t</sub> la componente accidentale.

Il modello moltiplicativo può essere trasformato in additivo usando i logaritmi:

${\displaystyle \log(Y_{t})=\log(T_{t})+\log(C_{t})+\log(S_{t})+\log(\varepsilon _{t})}$;

Il ciclo ha una periodicità pluriennale. Per questo motivo, nelle analisi di breve/medio periodo (dette congiunturali) la componente tendenziale e quella ciclica vengono spesso considerate come un tutt'uno e si hanno modelli del tipo:

${\displaystyle Y_{t}=TC_{t}+S_{t}+\varepsilon _{t}}$

dove *TC* <sub>t</sub> è una componente detta "trend-ciclo".

### Trend lineare o linearizzabile nei parametri

Si dice *lineare nei parametri* un trend polinomiale del tipo:

${\displaystyle T_{t}=\alpha _{0}+\alpha _{1}t+\alpha _{2}t^{2}+\dots +\alpha _{p}t^{p}}$

in quanto i parametri da stimare, *α* <sub>0</sub>...*α* <sub>p</sub>, sono tutti di primo grado.

Si dice invece *linearizzabile nei parametri* un trend del tipo:

${\displaystyle T_{t}=\alpha _{0}e^{\alpha _{1}t},\qquad \alpha _{0}>0}$

idoneo a rappresentare fenomeni che aumentano (*α* <sub>1</sub> > 0) o diminuiscono (*α* <sub>1</sub> < 0) secondo una [progressione geometrica](https://it.wikipedia.org/wiki/Progressione_geometrica "Progressione geometrica"), e che può essere linearizzato come segue:

${\displaystyle \ln(T_{t})=\ln(\alpha _{0})+\alpha _{1}t}$

Nel caso di dati mensili o trimestrali, si può tenere conto della componente stagionale, come già sopra accennato, mediante le cosiddette *variabili dummy* (variabili fittizie). Nel caso di dati mensili si usano 12 variabili *M* <sub>i</sub> che valgono 1 nell' *i* -esimo mese e 0 negli altri; nel caso di dati trimestrali si usano 4 variabili *Q* <sub>i</sub> che valgono 1 nell' *i* -esimo trimestre e 0 negli altri. Ad esempio, un modello lineare additivo con componente stagionale per dati trimestrale è del tipo:

${\displaystyle Y_{t}=\alpha +\beta t+\gamma _{1}Q_{1}+\gamma _{2}Q_{2}+\gamma _{3}Q_{3}+\gamma _{4}Q_{4}+\varepsilon _{t}}$

dove:

- *α* rappresenta l'intercetta con l'asse delle ordinate;
- *β* rappresenta l'incremento assoluto di *Y* <sub>t</sub> per ogni unità di tempo;
- *γ* <sub>1</sub>...*γ* <sub>4</sub> sono i parametri delle variabili dummy.

Se si ritiene di poter assumere un trend lineare o linearizzabile, i parametri possono essere facilmente stimati mediante [regressione lineare](https://it.wikipedia.org/wiki/Regressione_lineare "Regressione lineare"). Si deve solo usare qualche accorgimento se si usano variabili dummy. Queste infatti introducono [multicollinearità](https://it.wikipedia.org/wiki/Regressione_lineare#Multicollinearit%C3%A0 "Regressione lineare") nei dati e, pertanto, non si possono stimare insieme l'intercetta *α* ed i parametri delle variabili dummy (*γ* <sub>i</sub>).[^2] Si usa quindi stimare solo i parametri delle variabili dummy, oppure solo l'intercetta e tre dei parametri delle variabili dummy; ad esempio, si assume il modello:

${\displaystyle Y_{t}=\alpha ^{*}+\beta t+\gamma _{1}^{*}Q_{1}+\gamma _{2}^{*}Q_{2}+\gamma _{3}^{*}Q_{3}+\varepsilon _{t}}$

Una volta ottenuta la stima per i parametri asteriscati, si risale all'intera serie dei parametri con una semplice trasformazione che si basa sulle uguaglianze:

- ${\displaystyle \alpha ^{*}=\alpha +\gamma _{4}}$ (l'intercetta ottenuta "incorpora" la variabile non stimata);
- ${\displaystyle \gamma _{i}=\gamma _{i}^{*}+\gamma _{4},\;i=1,2,3}$ (se si calcola una nuova intercetta, minore di quella ottenuta, il grafico "si abbassa"; si deve quindi sommare la differenza ai parametri delle variabili dummy per "rialzare" il grafico);
- ${\displaystyle \gamma _{1}+\gamma _{2}+\gamma _{3}+\gamma _{4}=0}$ (gli effetti stagionali si compensano tra loro).

Da esse si ottiene:

${\displaystyle \gamma _{4}=-{\frac {1}{4}}(\gamma _{1}^{*}+\gamma _{2}^{*}+\gamma _{3}^{*})}$

che consente di calcolare i parametri *α*, *γ* <sub>1</sub>, *γ* <sub>2</sub>, *γ* <sub>3</sub> e *γ* <sub>4</sub> sulla base di *α* <sup>*</sup>, *γ* <sup>*</sup> <sub>1</sub>, *γ* <sup>*</sup> <sub>2</sub>, *γ* <sup>*</sup> <sub>3</sub>.

#### Valutazione del modello e previsioni

In generale, si usa valutare l'adattamento del modello ai dati osservati si usa il [coefficiente di determinazione](https://it.wikipedia.org/wiki/Coefficiente_di_determinazione "Coefficiente di determinazione") *R* <sup>2</sup>. Tuttavia, aumentando il grado del [polinomio](https://it.wikipedia.org/wiki/Polinomio "Polinomio") interpolante l'adattamento migliora, ma diventa più arduo interpretare i parametri, il cui numero aumenta col grado.

Si usa quindi un coefficiente " [corretto](https://it.wikipedia.org/wiki/Coefficiente_di_determinazione#Adjusted_R2 "Coefficiente di determinazione") ":

${\displaystyle {\overline {R}}^{2}=1-\left[{\frac {n-1}{n-p}}(1-R^{2})\right]}$

dove *n* è il numero delle osservazioni e *p* il numero dei parametri (compresa l'intercetta) e il cui valore aumenta se aumenta *R* <sup>2</sup>, ma diminuisce se aumenta *p*.

Si verifica anche il [correlogramma](https://it.wikipedia.org/wiki/Correlogramma "Correlogramma") dei residui, che devono risultare oscillanti entro un banda ristretta.

Se l'adattamento è buono, il modello può essere utilizzato per previsioni. Ad esempio, se si dispone di 80 rilevazioni trimestrali dal primo trimestre 1989 al quarto trimestre 2008, se si è ottenuto un buon adattamento per la stima:

${\displaystyle {\hat {y}}_{t}=200+1.5t-4Q_{1}+4Q_{2}-8Q_{3}+8Q_{4}}$

- la previsione per il primo trimestre 2009 è: 200+1.5×81-4× *Q* <sub>1</sub> =200+121.5-4=317.5 (*Q* <sub>2</sub> = *Q* <sub>3</sub> = *Q* <sub>4</sub> = 0 per il primo trimestre);
- la previsione per il secondo trimestre 2009 è: 200+1.5×82+4× *Q* <sub>2</sub> =200+123+4=327 (*Q* <sub>1</sub> = *Q* <sub>3</sub> = *Q* <sub>4</sub> = 0 per il secondo trimestre).

### Trend non linearizzabile nei parametri

Se il fenomeno osservato presenta una fase di crescita seguita poi da una progressiva decelerazione, si possono ipotizzare trend come i seguenti:

- *curva esponenziale modificata*: ${\displaystyle T_{t}=\alpha (1-\beta e^{-kt})}$;
- *[curva logistica](https://it.wikipedia.org/wiki/Equazione_logistica#L'equazione_di_Verhulst "Equazione logistica")*: ${\displaystyle =T_{t}={\frac {\alpha }{1+\beta e^{-kt}}}}$;
- *[curva di Gompertz](https://it.wikipedia.org/wiki/Legge_di_Gompertz "Legge di Gompertz")*: ${\displaystyle T_{t}=\alpha e^{-\beta e^{-kt}}}$;

che presentano un [asintoto](https://it.wikipedia.org/wiki/Asintoto "Asintoto") orizzontale in quanto tendono ad *α* quando *t* tende all'infinito.

In casi come questi ([dinamica delle popolazioni](https://it.wikipedia.org/wiki/Dinamica_delle_popolazioni "Dinamica delle popolazioni"), evoluzione della domanda di beni durevoli ecc.) la linearizzazione non è possibile e si ricorre, pertanto, alla [regressione non lineare](https://it.wikipedia.org/wiki/Regressione_non_lineare "Regressione non lineare").

### Medie mobili

![](https://thumb.wikimedia.org/wikipedia/commons/thumb/6/62/Mmobile.svg/500px-Mmobile.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Esempio di analisi di una serie storica con una media mobile

Se l'andamento del fenomeno appare irregolare, si preferisce individuare la componente tendenziale in modo empirico, eliminando le componenti stagionale e/o accidentale mediante [medie mobili](https://it.wikipedia.org/wiki/Media_mobile "Media mobile").

In particolare, per eliminare la componente stagionale presente in dati trimestrali si potrebbe usare una media mobile a 4 termini:

${\displaystyle M_{1}={\frac {1}{4}}(y_{t-2}+y_{t-1}+y_{t}+y_{t+1})}$

oppure:

${\displaystyle M_{2}={\frac {1}{4}}(y_{t-1}+y_{t}+y_{t+1}+y_{t+2})}$

In entrambi i casi si userebbero valori che, essendo la media dei valori osservati in quattro trimestri successivi, non risentono della componente stagionale.

Le medie di un numero pari di termini, tuttavia, tendono ad esprimere il valore del fenomeno ad un tempo intermedio rispetto a quelli osservati (intermedio tra *t* –1 e *t* nel caso di *M* <sub>1</sub>, tra *t* e *t* +1 nel caso di *M* <sub>2</sub>).

Si preferisce quindi comporre le medie *M* <sub>1</sub> e *M* <sub>2</sub> in una media mobile a cinque termini centrata sul tempo *t*:

${\displaystyle M={\frac {1}{8}}y_{t-2}+{\frac {1}{4}}y_{t-1}+{\frac {1}{4}}y_{t}+{\frac {1}{4}}y_{t+1}+{\frac {1}{8}}y_{t+2}}$

La serie delle medie mobili costituisce il trend (o trend-ciclo), che può poi essere studiato con altri metodi. La sua individuazione, comunque, consente il calcolo di una *stagionalità lorda*, che incorpora una parte accidentale; indicando con ${\displaystyle y_{t}}$ il dato osservato al tempo *t* e con ${\displaystyle {\widehat {T}}_{t}}$ il trend stimato con le medie mobili, si ha:

${\displaystyle {\widehat {S_{t}+\varepsilon _{t}}}=y_{t}-{\widehat {T}}_{t}}$ oppure ${\displaystyle {\widehat {S_{t}\varepsilon _{t}}}={\frac {y_{t}}{{\widehat {T}}_{t}}}}$

secondo che si preferisca un modello additivo o moltiplicativo.

Nelle analisi basate sulla regressione si ottengono coefficienti di stagionalità costanti. Nelle analisi basate sulle medie mobili, invece, si può scegliere tra:

- modelli a stagionalità costante: si calcola la media, per ciascun trimestre dei fattori di stagionalità lorda e si ottengono così i fattori di stagionalità netta *S* <sub>i</sub>, che vengono poi corretti in modo da assicurare che si compensino tra loro, quindi in modo che la loro somma sia 0 (modelli additivi) o il loro prodotto sia 1 (modelli moltiplicativi);
- modelli a stagionalità variabile: si sostituiscono, per ciascun trimestre, i fattori di stagionalità lorda con una loro media mobile (normalmente a 3 termini), oppure si usa un "trend della stagionalità".

Una volta individuati fattori di stagionalità netta, si calcolano i residui:

${\displaystyle \varepsilon _{t}=y_{t}-{\widehat {T}}_{t}-{\widehat {S}}_{t}}$ oppure ${\displaystyle \varepsilon _{t}={\frac {y_{t}}{{\widehat {T}}_{t}{\widehat {S}}_{t}}}}$

secondo che si stia seguendo l'approccio additivo o quello moltiplicativo, quindi si verifica (in prima istanza con un [correlogramma](https://it.wikipedia.org/wiki/Correlogramma "Correlogramma")) che i residui abbiano media 0 e varianza costante.

### Livellamento esponenziale

Quando si usano le medie mobili, si perdono alcuni dei valori iniziali e finali della serie storica (ad esempio, se si hanno dati dal tempo 1 al tempo 80, con una media mobile a 5 termini si ottengono medie dal tempo 3 al tempo 78). Ciò rappresenta uno svantaggio se si mira soprattutto a formulare previsioni, in quanto vengono a mancare i termini più vicini a quelli da stimare. Si potrebbe pensare di ovviare al problema con medie mobili non centrate ed asimmetriche, ad esempio del tipo:

${\displaystyle M={\frac {1}{4}}(y_{t-3}+y_{t-2}+y_{t-1}+y_{t})}$ oppure: ${\displaystyle M={\frac {1}{16}}(y_{t-3}+3y_{t-2}+4y_{t-1}+8y_{t})}$

Nella pratica, tuttavia, si preferiscono approcci che generalizzano quanto appena ipotizzato.

#### Livellamento esponenziale semplice

Nel *livellamento esponenziale semplice* si muove dalla media degli *n* valori osservati:

${\displaystyle {\bar {y}}={\frac {1}{n}}\sum _{t=1}^{n}y_{t}={\frac {1}{n}}\sum _{j=1}^{n}y_{n-j+1}={\frac {1}{n}}\sum _{i=0}^{n-1}y_{n-i}}$

e la si trasforma in una media ponderata con pesi esponenzialmente crescenti (minori per i valori iniziali, maggiori per quelli finali) la cui somma sia 1. Si attribuisce quindi un peso *α* compreso tra 0 e 1 all'ultimo termine, il peso (1 – *α*) al penultimo, (1 – *α*) <sup>2</sup> al terzultimo e così via, e si ha (v. [serie geometrica](https://it.wikipedia.org/wiki/Serie_geometrica "Serie geometrica")):

${\displaystyle \lim _{n\rightarrow \infty }\sum _{i=0}^{n}\alpha (1-\alpha )^{i}=\alpha \lim _{n\rightarrow \infty }\sum _{i=0}^{n}(1-\alpha )^{i}=\alpha {\frac {1}{1-(1-\alpha )}}=1}$

Si sostituisce quindi la serie osservata *y* <sub>t</sub> con la serie *livellata*:

${\displaystyle \ell _{t}=\alpha \sum _{i=0}^{n-1}(1-\alpha )^{i}y_{n-i}}$

in cui *α*, il peso assegnato all'ultimo valore osservato, viene detto *costante di livellamento*.[^3]

Per il calcolo risultano più comode le seguenti formulazioni ricorsive:

${\displaystyle \ell _{t}=\alpha y_{t}+(1-\alpha )\ell _{t-1},\quad t=1,2,\dots ,n}$ (Roberts, 1959) [^4]

oppure:

${\displaystyle \ell _{t}=\alpha y_{t-1}+(1-\alpha )\ell _{t-1},\quad t\geq 3}$ (Hunter, 1986) [^5]

Il valore iniziale della serie livellata viene calcolato in vari modi: si pone uguale al primo valore osservato, oppure alla media di tutti i valori osservati o di una loro parte (i primi 4 o 5, oppure la loro prima metà). Si tratta di convenzioni che non alterano il risultato finale (la previsione per il tempo *n* + 1), proprio perché ai primi termini della serie sono attribuiti pesi molto bassi.

Le formule di Roberts e di Hunter differiscono per l'interpretazione di *l* <sub>n</sub>, l'ultimo valore calcolato:

- nel primo caso viene inteso come valore previsto, quindi come ${\displaystyle {\hat {y}}_{n+1}}$;[^6]
- nel secondo caso viene inteso come livellamento del valore osservato, quindi come ${\displaystyle {\hat {y}}_{t}}$, sulla cui base si effettua la previsione mediante ripetizione della formula: ${\displaystyle {\hat {y}}_{n+1}=\alpha {\hat {y}}_{n}+(1-\alpha )\ell _{n}}$.

In ogni caso, è sufficiente che la serie osservata non sia troppo breve perché si ottengano gli stessi valori per ${\displaystyle {\hat {y}}_{n+1}}$.

Quanto alla costante di livellamento *α*, essa può essere scelta in modo che minimizzi i quadrati degli scarti tra i valori osservati e quelli livellati, oppure secondo gli obiettivi dell'indagine; un valore elevato (prossimo a 1) conferisce maggiore importanza agli ultimi valori osservati, un valore basso privilegia invece l'andamento medio del fenomeno.

![](https://thumb.wikimedia.org/wikipedia/commons/thumb/7/77/Livell.svg/960px-Livell.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Esempio di livellamento esponenziale di una serie storica (in nero) con costante di livellamento pari a 0.7 (in rosso) ed a 0.1 (in blu)

È piuttosto importante sottolineare che il livellamento esponenziale semplice conduce ad una previsione costante. Infatti, considerando la formula di Roberts, si ha:

${\displaystyle {\begin{aligned}{\hat {y}}_{n+1}&=\ell _{n}\\{\hat {y}}_{n+2}&=\ell _{n+1}=\alpha {\hat {y}}_{n+1}+(1-\alpha )\ell _{n}=\alpha \ell _{n}+(1-\alpha )\ell _{n}=\ell _{n}\end{aligned}}}$

e così via. Si tratta quindi di un metodo utilizzabile solo per serie senza trend.

#### I metodi di Holt-Winters

Un primo modo per tenere conto di un trend consiste nell'introduzione di una *deriva* *d* (*drift* in inglese) che modifichi i valori livellati secondo grandezze variabili col tempo; ad esempio:

${\displaystyle \ell _{t}=\alpha y_{t}+(1-\alpha )(\ell _{t-1}+d_{t-1})}$

Sono usati soprattutto i *metodi di Holt-Winters*, così detti dai nomi di coloro che li hanno introdotti.

Un primo modello tiene conto solo del trend, ipotizzando che al tempo *t* il fenomeno possa essere approssimato mediante una retta del tipo:

${\displaystyle \ell _{t}+d_{t}(t)}$

con intercetta *l* <sub>t</sub> e pendenza *d* <sub>t</sub>. Si definiscono le seguenti relazioni:[^7]

${\displaystyle {\begin{cases}\ell _{t}=\alpha y_{t}+(1-\alpha )(\ell _{t-1}+d_{t-1})\\d_{t}=\beta (\ell _{t}-\ell _{t-1})+(1-\beta )d_{t-1}\end{cases}}}$

La prima (analogamente a quanto avviene nel livellamento esponenziale semplice) può essere vista come una media ponderata tra il valore osservato e la previsione calcolata al tempo precedente; la seconda come una media ponderata tra la differenza tra le previsioni ai tempi *t* e precedente e la pendenza calcolata al tempo precedente (attribuire peso 1 a quest'ultima equivarrebbe ad assumere un trend lineare, ovvero una costanza della pendenza).

Il modello viene esteso per tenere conto della stagionalità, inserendo un ulteriore peso *γ*. Si hanno un modello stagionale additivo:

${\displaystyle {\begin{cases}\ell _{t}=\alpha (y_{t}-s_{n-p})+(1-\alpha )(\ell _{t-1}+d_{t-1})\\d_{t}=\beta (\ell _{t}-\ell _{t-1})+(1-\beta )d_{t-1}\\s_{t}=\gamma (y_{t}-\ell _{t})+(1-\gamma )s_{t-p}\end{cases}}}$

dove *s* <sub>t</sub> è un fattore di stagionalità è *p* la sua periodicità (4 per dati trimestrali, 12 per dati mensili), e un modello stagionale moltiplicativo:

${\displaystyle {\begin{cases}\ell _{t}=\alpha {\dfrac {y_{t}}{s_{n-p}}}+(1-\alpha )(\ell _{t-1}+d_{t-1})\\d_{t}=\beta (\ell _{t}-\ell _{t-1})+(1-\beta )d_{t-1}\\s_{t}=\gamma {\dfrac {y_{t}}{\ell _{t}}}+(1-\gamma )s_{t-p}\end{cases}}}$

Si tratta di modelli molto flessibili, in quanto consentono di tenere conto di trend non polinomiali e di stagionalità non costanti. Quanto alla scelta di *α*, *β* e *γ*, anche in questo caso (ma con ovvia maggiore complessità) si possono cercare i valori che minimizzano i quadrati degli scarti o ci si può regolare secondo gli obiettivi dell'analisi.

#### Valutazione della qualità delle previsioni

Indicando con *T* il tempo del più recente valore considerato nel livellamento di una serie, le previsioni, i valori poi osservati in tempi successivi a *T* e le loro differenze (errori di previsione) si indicano, rispettivamente, con:

${\displaystyle F_{T,k}\qquad y_{T+k}\qquad e_{T,k}=y_{T+k}-F_{T,k}}$

Si usano le seguenti misure di qualità:

- la media degli errori assoluti (MAE, *Mean Absolute Error*, errore medio assoluto); scelto un orizzonte di previsione *k*, la verifica viene condotta per il valore previsto al tempo *T* per il tempo *T* + *k*, poi per il valore previsto al tempo *T* + 1 (grazie alla disponibilità di un nuovo valore osservato) per il tempo *T* + 1 + *k*; si ha quindi:[^8]

${\displaystyle MAE_{k}={\frac {1}{n}}\sum _{s=0}^{n-1}|e_{T+s,k}|={\frac {1}{n}}\sum _{s=0}^{n-1}|y_{T+s+k}-F_{T+s,k}|}$

- la media dei quadrati degli errori (MSE, *Mean Squared Error* in inglese, [errore quadratico medio](https://it.wikipedia.org/wiki/Errore_quadratico_medio "Errore quadratico medio")):

${\displaystyle MSE_{k}={\frac {1}{n}}\sum _{s=0}^{n-1}e_{T+s,k}^{2}}$

- la radice quadrata del precedente (RMSE, *Root Mean Square Error* in inglese):

${\displaystyle RMSE_{k}={\sqrt {MSE_{k}}}}$

Si usa anche il confronto tra i "punti di svolta" (test di Kendall). Per "punto di svolta" si intende un punto in cui una serie da ascendente diventa discendente o viceversa. Si contano i punti di svolta presenti nella serie rilevata ed in quella stimata o livellata e si calcolano:

- indice di errore di prima specie: il rapporto tra il numero dei punti di svolta non coincidenti perché presenti solo nella serie stimata ed il numero totale dei punti di svolta della serie stimata;
- indice di errore di seconda specie: il rapporto tra il numero dei punti di svolta non coincidenti perché presenti solo nella serie rilevata ed il numero totale dei punti di svolta della serie rilevata.

Da notare che, dal momento che il modello viene ricalcolato all'aumentare di *s*, tutte le misure citate servono a stimare la bontà dell'approccio seguito, non quella dell'adattamento ai dati.

## Approccio moderno

### Definizione formale di serie storica

Si ricordi anzitutto che una [variabile aleatoria](https://it.wikipedia.org/wiki/Variabile_aleatoria "Variabile aleatoria") può essere definita come una funzione misurabile a valori reali su uno spazio probabilistico: X:${\displaystyle (\Omega ,F,P)\rightarrow (R,B(R),P_{x}),X^{-1}(B)\in F\forall B\in B(R)}$

Dove:

- ${\displaystyle \Omega }$: spazio degli eventi
- F sigma-algebra di ${\displaystyle \Omega }$
- P probabilità definita di ${\displaystyle (\Omega ,F)}$
- B(R) sigma-algebra di Borel definita sull'insieme dei numeri reali R
- ${\displaystyle P_{x}}$ probabilità indotta da X su (R,B(R))

Stante questa premessa, si può definire un **processo stocastico** ${\displaystyle {X_{t}}_{t\in T}}$ come una successione di [variabili aleatorie](https://it.wikipedia.org/wiki/Variabile_aleatoria "Variabile aleatoria") indicizzate da un parametro. Nell'analisi delle serie storiche, questo parametro è il tempo, che indichiamo con t ${\displaystyle \in }$ T, con T spazio parametrico, che si può considerare [discreto](https://it.wikipedia.org/wiki/Discreto "Discreto") (ipotesi usuale, se si considerano i singoli giorni, o mesi, o anni) oppure [continuo](https://it.wikipedia.org/wiki/Continuo "Continuo").

Da qui si può derivare la nozione di **serie storica**, che sarà la *realizzazione finita* di un processo stocastico, indicata con la notazione ${\displaystyle {X_{t}}_{1...N}}$, dove N« ${\displaystyle \infty }$

### Casi particolari di processi stocastici

- t e ${\displaystyle \omega }$ sono variabili: ${\displaystyle {X_{t}(\omega ),\omega \in \Omega }_{t\in T}}$ è un processo stocastico propriamente detto
- t variabile e ${\displaystyle \omega }$ fissato tale che ${\displaystyle \omega }$ = ${\displaystyle \omega _{0}}$, ${\displaystyle {X_{t}(\omega _{0}}_{t\in T}}$ è la cosiddetta *traiettoria* del processo stocastico
- t fissato, ${\displaystyle \omega }$ variabile e t= ${\displaystyle t_{0}}$, ${\displaystyle {X_{t}(\omega )}}$ è una variabile aleatoria
- tutti i parametri fissati: ${\displaystyle X_{t}}$ è un [numero reale](https://it.wikipedia.org/wiki/Numero_reale "Numero reale")
- dati ${\displaystyle t_{1},t_{2},...,t_{N}}$ e fissati ${\displaystyle \omega _{1},\omega _{2},...,\omega _{N};{x_{1},x_{2},...,x_{N}}}$ si ha una serie storica propriamente detta.

## Note

## Bibliografia

- Estela Bee Dagum, *Analisi delle serie storiche - modellistica, previsione e scomposizione*, Milano, Springer Verlag, 2002. [ISBN 88-470-0146-3](https://it.wikipedia.org/wiki/Special:BookSources/8847001463).
- Tommaso Di Fonzo e Francesco Lisi, *Serie storiche economiche*, Roma, Carocci, 2005. [ISBN 978-88-430-3423-9](https://it.wikipedia.org/wiki/Special:BookSources/9788843034239).
- Gary Koop, *Logica statistica dei dati economici*, Torino, UTET, 2001. [ISBN 88-7750-735-7](https://it.wikipedia.org/wiki/Special:BookSources/8877507357).

## Voci correlate

- [Correlogramma](https://it.wikipedia.org/wiki/Correlogramma "Correlogramma")

[^1]: Si usa normalmente il "cappuccio" ^ per indicare che gli ${\displaystyle {\hat {y}}_{t}}$ sono dati stimati e per distinguerli dai dati osservati ${\displaystyle y_{t}}$.

[^2]: Si usa ovviamente la [regressione lineare multipla](https://it.wikipedia.org/wiki/Regressione_lineare#Regressione_lineare_multipla "Regressione lineare"). Il modello è del tipo:

${\displaystyle y_{t}=\beta _{1}x_{t1}+\beta _{2}x_{t2}+\dots +\beta _{p}x_{tp}+\varepsilon _{t}}$

Vi sono tante righe come questa quanti sono i valori di *t* (ad esempio, 60 se si considerano i dati trimestrali per 15 anni). Si può quindi riscrivere il modello in forma matriciale:

${\displaystyle \mathbf {y} =\mathbf {X} {\boldsymbol {\beta }}+{\boldsymbol {\varepsilon }}}$

dove:

${\displaystyle \mathbf {y} ={\begin{pmatrix}y_{1}\\y_{2}\\\vdots \\y_{n}\end{pmatrix}},\quad \mathbf {X} ={\begin{pmatrix}x_{11}&x_{12}&\dots &x_{1p}\\x_{21}&x_{22}&\dots &x_{2p}\\\vdots &\vdots &\vdots &\vdots \\x_{n1}&x_{n2}&\dots &x_{np}\end{pmatrix}},\quad {\boldsymbol {\beta }}={\begin{pmatrix}\beta _{1}\\\beta _{2}\\\vdots \\\beta _{p}\end{pmatrix}},\quad {\boldsymbol {\varepsilon }}={\begin{pmatrix}\varepsilon _{1}\\\varepsilon _{2}\\\vdots \\\varepsilon _{n}\end{pmatrix}}}$

Il vettore **β** risulta pari a:

${\displaystyle {\boldsymbol {\beta }}=(\mathbf {X} ^{T}\mathbf {X} )^{-1}\mathbf {X} ^{T}\mathbf {y} }$

ma questo comporta che può essere calcolato solo se la matrice **X** <sup>T</sup> **X** è [invertibile](https://it.wikipedia.org/wiki/Matrice_invertibile "Matrice invertibile"), quindi solo se la matrice **X** ha [rango](https://it.wikipedia.org/wiki/Rango_\(algebra_lineare\) "Rango (algebra lineare)") *p*. Tuttavia, se *β* <sub>1</sub> è l'intercetta, allora la prima colonna della matrice **X** è costituita da tutti 1; se quattro variabili indicano la stagionalità, le relative colonne della matrice sono:

${\displaystyle {\begin{aligned}x_{t,i}&=1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,\dots \\x_{t,i+1}&=0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0\dots \\x_{t,i+2}&=0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,\dots \\x_{t,i+3}&=0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,\dots \end{aligned}}}$

Ne segue che la prima colonna è la somma delle quattro colonne corrispondenti alle variabili dummy e, pertanto, il rango di **X** è inferiore a *p*.

[^3]: Alcuni autori chiamano costante di livellamento la quantità *δ* = (1 – *α*).

[^4]: S. W. Roberts, «Control chart test based on geometric moving averages», *Technometrics*, 1959, vol. 1, pp. 239-250 (cfr. [NIST Engineering Statistics Handbook, sezione 6.3.2.4](http://www.itl.nist.gov/div898/handbook/pmc/section3/pmc324.htm)).

[^5]: J. S. Hunter, «The Exponentially Weighted Moving Average», *Journal of Quality Technology*, 1986, vol. 18, pp. 203-210 (cfr. [NIST Engineering Statistics Handbook, sezione 6.4.3.1](http://www.itl.nist.gov/div898/handbook/pmc/section4/pmc431.htm)).

[^6]: A rigore, il valore previsto è ${\displaystyle {\hat {y}}_{n+1}=\ell _{n}+{\hat {\varepsilon }}_{n+1}}$. Tuttavia, poiché nell'approccio tradizionale si assume che le variazioni accidentali abbiano media nulla, quindi [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") nullo, si ha ${\displaystyle {\hat {y}}_{n+1}=\ell _{n}}$.

[^7]: Anche qui, come nel caso del livellamento esponenziale semplice ed in quello del metodo Holt-Winters con stagionalità, alcuni autori invertono i ruoli dei fattori *α* e (1 – *α*), *β* e (1 – *β*), *γ* e (1 – *γ*).

[^8]: In altri termini, se si dispone di dati trimestrali che giungono al 4º trimestre dell'anno *X*, non si verifica la qualità delle previsioni per i successivi *n* trimestri, in quanto il modello viene tarato per effettuare previsioni a brevissimo o a meno breve termine (nel caso del livellamento esponenziale semplice, ad esempio, un *α* prossimo a 1 si presta a previsioni a brevissimo termine, un *α* piccolo si presta meglio a previsioni a meno breve termine). Si effettua quindi, ad esempio, la previsione per il 1º trimestre dell'anno *X* +1, poi, quando diventa disponibile il valore "vero" a tale data, si effettua la previsione per il 2º trimestre e così via. *k* è quindi costante.