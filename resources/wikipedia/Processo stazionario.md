---
title: "Processo stazionario"
source: "https://it.wikipedia.org/wiki/Processo_stazionario"
author:
  - "[[Wikipedia]]"
published: 2016-09-10
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica") e [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica"), un **processo stazionario** (o **processo fortemente stazionario**) è un [processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico") la cui [distribuzione di probabilità congiunta](https://it.wikipedia.org/wiki/Distribuzione_congiunta "Distribuzione congiunta") non cambia se viene traslata nel tempo. Di conseguenza, parametri quali la [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") e la [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza"), se sono presenti, pure non cambiano nel tempo.

Poiché la stazionarietà è un presupposto di fondo in molte procedure statistiche utilizzate nell' [analisi delle serie storiche](https://it.wikipedia.org/wiki/Analisi_delle_serie_storiche "Analisi delle serie storiche"), i dati non stazionari sono spesso trasformati per diventare stazionari. La causa più comune di violazione della stazionarietà sono le tendenze in media, che possono essere dovute sia alla presenza di una [radice unitaria](https://it.wikipedia.org/wiki/Radice_unitaria?action=edit&redlink=1 "Radice unitaria (la pagina non esiste)"), sia ad una tendenza deterministica. Nel secondo caso, il processo è chiamato *processo con tendenza stazionaria*, gli shock stocastici hanno solo effetti transitori e il processo è *mean-reverting* (su una media che cambia deterministicamente nel tempo). Al contrario, nel primo caso gli shock stocastici hanno effetti permanenti e il processo non è *mean-reverting*. Un processo con tendenza stazionaria non è strettamente stazionario, ma può facilmente essere reso tale rimuovendo la tendenza di fondo (funzione unicamente del tempo). Analogamente, i processi con una o più radici unitarie possono essere resi stazionari attraverso la differenziazione. Un tipo importante di processo non stazionario che non include un comportamento di tendenza simile è il [processo ciclostazionario](https://it.wikipedia.org/wiki/Processo_ciclostazionario "Processo ciclostazionario").

Un "processo stazionario" non è la stessa cosa di un "processo con una [distribuzione stazionaria](https://it.wikipedia.org/wiki/Distribuzione_stazionaria?action=edit&redlink=1 "Distribuzione stazionaria (la pagina non esiste)") ". Infatti, ci sono ulteriori possibilità di confusione con l'uso della parola "stazionario" nel contesto dei processi stocastici; per esempio, talvolta si dice che una [catena di Markov](https://it.wikipedia.org/wiki/Catena_di_Markov "Catena di Markov") omogenea nel tempo ha " [probabilità di transizione](https://it.wikipedia.org/wiki/Probabilit%C3%A0_di_transizione "Probabilità di transizione") stazionarie". Inoltre, tutti i processi casuali di Markov stazionari sono omogenei nel tempo.

## Definizione

Formalmente, sia ${Xt}$ un [processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico") e $F_{X} \left(x_{t_{1} + \tau} , \ldots , x_{t_{k} + \tau}\right)$ rappresenti la [funzione cumulativa](https://it.wikipedia.org/wiki/Funzione_di_ripartizione "Funzione di ripartizione") della [distribuzione congiunta](https://it.wikipedia.org/wiki/Distribuzione_congiunta "Distribuzione congiunta") di ${Xt}$ negli istanti $t_{1} + \tau , \ldots , t_{k} + \tau$. Allora, si dice che ${Xt}$ è strettamente (o fortemente) stazionario se, per ogni $k$, per ogni $τ$, e per ogni $t_{1} , \ldots , t_{k}$,

$F_{X} \left(x_{t_{1} + \tau} , \ldots , x_{t_{k} + \tau}\right) = F_{X} \left(x_{t_{1}} , \ldots , x_{t_{k}}\right) .$

Poiché $τ$ non incide su $F_{X} \left(\cdot\right)$, $F_{X}$ non è una funzione del tempo.

## Esempi

Per esempio, il [rumore bianco](https://it.wikipedia.org/wiki/Rumore_bianco "Rumore bianco") è stazionario. Il suono di un [cembalo](https://it.wikipedia.org/wiki/Piatto_\(strumento_musicale\) "Piatto (strumento musicale)") che tintinna, se colpito solo una volta, è non stazionario perché la potenza acustica del colpo (e quindi la sua varianza) diminuisce con il tempo. Tuttavia, sarebbe possibile inventare un processo stocastico che descrive un caso in cui il cembalo è colpito, tale che la risposta globale formi un processo stazionario. Per esempio, se il cembalo viene colpito in momenti nel tempo corrispondenti ad un [processo di Poisson](https://it.wikipedia.org/wiki/Processo_di_Poisson "Processo di Poisson") omogeneo, la risposta generale sarebbe stazionaria.

Un esempio di processo stazionario a [tempo discreto](https://it.wikipedia.org/wiki/Processo_stocastico_a_tempo_discreto?action=edit&redlink=1 "Processo stocastico a tempo discreto (la pagina non esiste)") dove lo spazio campione è anche discreto (in modo che la variabile casuale possa assumere uno di *N* valori possibili) è uno [schema di Bernoulli](https://it.wikipedia.org/wiki/Processo_di_Bernoulli "Processo di Bernoulli"). Altri esempi di processi stazionari a tempo discreto con spazio campione continuo includono alcuni processi [autoregressivi](https://it.wikipedia.org/wiki/Modello_autoregressivo "Modello autoregressivo") e [a media mobile](https://it.wikipedia.org/wiki/Modello_a_media_mobile "Modello a media mobile") che sono entrambi sottoinsiemi del [modello autoregressivo a media mobile](https://it.wikipedia.org/wiki/Modello_autoregressivo_a_media_mobile "Modello autoregressivo a media mobile"). I modelli con una componente autoregressiva non banale possono essere o stazionari o non stazionari, a seconda dei valori del parametro, e casi speciali non stazionari importanti sono quelli in cui nel modello esistono [radici unitarie](https://it.wikipedia.org/wiki/Radice_unitaria?action=edit&redlink=1 "Radice unitaria (la pagina non esiste)").

Sia *Y* una [variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") scalare, e definiamo una [serie storica](https://it.wikipedia.org/wiki/Serie_storica "Serie storica") { *X <sub>t</sub>* }, da

$X_{t} = Y \text{per ogni } t .$

Allora { *X <sub>t</sub>* } è una serie stazionaria, per la quale le realizzazioni sono costituite da una serie di valori costanti, con un diverso valore costante per ogni realizzazione. Una [legge dei grandi numeri](https://it.wikipedia.org/wiki/Legge_dei_grandi_numeri "Legge dei grandi numeri") non si applica in questo caso, poiché il valore limite di una media da una realizzazione singola dà il valore casuale determinato da *Y*, invece del [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") di *Y.*

Come ulteriore esempio di un processo stazionario per il quale ogni singola realizzazione ha una struttura apparentemente priva di rumore, supponiamo che *Y* abbia una [distribuzione uniforme](https://it.wikipedia.org/wiki/Distribuzione_continua_uniforme "Distribuzione continua uniforme") su (0,2π\] e definiamo la serie storica { *X <sub>t</sub>* } come

$X_{t} = cos \left(t + Y\right) \text{per } t \in \mathbb{R} .$

Allora { *X <sub>t</sub>* } è fortemente stazionario.

## Forme più deboli di stazionarietà

### Stazionarietà debole o in senso lato

Una forma più debole di stazionarietà comunemente impiegata in [teoria dei segnali](https://it.wikipedia.org/wiki/Teoria_dei_segnali "Teoria dei segnali") è nota come *stazionarietà in senso debole*, *stazionarietà in senso lato*, *stazionarietà della covarianza*, o *stazionarietà di secondo ordine*. I processi casuali stazionari in senso lato richiedono solo che il primo [momento](https://it.wikipedia.org/wiki/Momento_\(probabilit%C3%A0\) "Momento (probabilità)") e l' [autocovarianza](https://it.wikipedia.org/wiki/Autocovarianza "Autocovarianza") non varino rispetto al tempo. Ogni processo fortemente stazionario che ha una [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") e una [covarianza](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\) "Covarianza (probabilità)") è anche un processo stazionario in senso lato.

Quindi, un [processo casuale](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico") a tempo continuo *x* (*t*) che sia stazionario in senso lato ha le seguenti restrizioni sulla sua funzione di media

$\mathbb{E} \left[x \left(t\right)\right] = m_{x} \left(t\right) = m_{x} \left(t + \tau\right) , \forall \tau \in \mathbb{R}$

e sulla sua funzione di [autocovarianza](https://it.wikipedia.org/wiki/Autocovarianza "Autocovarianza")

$\mathbb{E} \left[\left(x \left(t_{1}\right) - m_{x} \left(t_{1}\right)\right) \left(x \left(t_{2}\right) - m_{x} \left(t_{2}\right)\right)\right] = C_{x} \left(t_{1} , t_{2}\right) = C_{x} \left(t_{1} + \left(- t_{2}\right) , t_{2} + \left(- t_{2}\right)\right) = C_{x} \left(t_{1} - t_{2} , 0\right) .$

La prima proprietà implica che la funzione di media *m* <sub><i>x</i></sub> (*t*) deve essere costante. La seconda proprietà implica che la funzione di covarianza dipende solo dalla *differenza* tra $t_{1}$ e $t_{2}$ e necessita di essere indicizzata da una sola variabile piuttosto che due variabili. Quindi, invece di scrivere,

$C_{x} \left(t_{1} - t_{2} , 0\right)$

la notazione è spesso abbreviata e scritta come:

$C_{x} \left(\tau\right) \text{dove } \tau = t_{1} - t_{2} .$

Ciò implica anche che l' [autocorrelazione](https://it.wikipedia.org/wiki/Autocorrelazione "Autocorrelazione") dipende solo da $\tau = t_{1} - t_{2}$, cioè

$R_{x} \left(t_{1} , t_{2}\right) = R_{x} \left(t_{1} - t_{2}\right) .$

Il principale vantaggio della stazionarietà in senso lato è che essa pone le serie storiche nel contesto degli [spazi di Hilbert](https://it.wikipedia.org/wiki/Spazio_di_Hilbert "Spazio di Hilbert"). Sia *H* lo spazio di Hilbert generato da { *x* (*t*)} (cioè, la chiusura dell'insieme di tutte le [combinazioni lineari](https://it.wikipedia.org/wiki/Combinazione_lineare "Combinazione lineare") di queste variabili casuali nello spazio di Hilbert di tutte le variabili casuali quadrato-integrabili su un dato spazio di probabilità). Essendo la funzione di autocovarianza definita positiva, dal [teorema di Bochner](https://it.wikipedia.org/wiki/Teorema_di_Bochner?action=edit&redlink=1 "Teorema di Bochner (la pagina non esiste)") segue che esiste una misura positiva *μ* sulla retta reale tale che *H* sia isomorfo al sottospazio di Hilbert di *L* <sup>2</sup> (*μ*) generato da { *e <sup>−2πiξ⋅t</sup>* }. Questo dà poi la seguente decomposizione di Fourier per un processo stocastico a tempo continuo: esiste un processo stocastico *ω <sub>ξ</sub>* con [incrementi ortogonali](https://it.wikipedia.org/wiki/Incrementi_ortogonali?action=edit&redlink=1 "Incrementi ortogonali (la pagina non esiste)") tale che, per ogni *t*

$x \left(t\right) = \int e^{- 2 \pi i \lambda \cdot t} d \omega_{\lambda} ,$

dove l'integrale sul lato destro è interpretato in senso opportuno (Riemann). Lo stesso risultato vale per un processo stazionario a tempo discreto, con la misura spettrale in tal caso definita sul cerchio unitario.

Quando si elaborano segnali casuali stazionari in senso lato con [filtri](https://it.wikipedia.org/wiki/Filtro_\(elettronica\) "Filtro (elettronica)") [tempo-invarianti](https://it.wikipedia.org/wiki/Sistema_tempo-invariante "Sistema tempo-invariante") [lineari](https://it.wikipedia.org/wiki/Linearit%C3%A0_\(matematica\) "Linearità (matematica)") (filtri [LTI](https://it.wikipedia.org/wiki/Sistema_dinamico_lineare_stazionario "Sistema dinamico lineare stazionario")), è utile pensare alla funzione di correlazione come a un [operatore lineare](https://it.wikipedia.org/wiki/Trasformazione_lineare "Trasformazione lineare"). Poiché si tratta di un operatore [circolante](https://it.wikipedia.org/wiki/Matrice_circolante?action=edit&redlink=1 "Matrice circolante (la pagina non esiste)") (dipende solo dalla differenza tra i due argomenti), le sue [autofunzioni](https://it.wikipedia.org/wiki/Autofunzione "Autofunzione") sono gli esponenziali complessi di [Fourier](https://it.wikipedia.org/wiki/Serie_di_Fourier "Serie di Fourier"). Inoltre, poiché le autofunzioni di operatori LTI sono anche esponenziali complessi, un'elaborazione LTI di segnali casuale stazionari in senso lato è facilmente trattabile - tutti i calcoli possono essere effettuati nel [dominio della frequenza](https://it.wikipedia.org/wiki/Dominio_della_frequenza "Dominio della frequenza"). In tal modo, l'assunzione di stazionarietà in senso lato è ampiamente impiegata negli [algoritmi](https://it.wikipedia.org/wiki/Algoritmo "Algoritmo") della teoria dei segnali.

### Altra terminologia

La terminologia usata per i tipi di stazionarietà diversi dalla stazionarietà forte possono essere piuttosto contrastanti. Segue qualche esempio.

- [Priestley](https://it.wikipedia.org/wiki/Maurice_Priestley?action=edit&redlink=1 "Maurice Priestley (la pagina non esiste)") parla di **stazionarietà fino all'ordine** *m* se condizioni simili a quelle date qui per la stazionarietà in senso lato si applicano ai momenti fino all'ordine *m*.[^1] [^2] In tal modo la stazionarietà in senso lato sarebbe equivalente alla "stazionarietà fino all'ordine 2", che è diversa dalla definizione di stazionarietà di secondo ordine data qui.

- [Honarkhah](https://it.wikipedia.org/wiki/Mehrdad_Honarkhah?action=edit&redlink=1 "Mehrdad Honarkhah (la pagina non esiste)") e [Caers](https://it.wikipedia.org/wiki/Jef_Caers?action=edit&redlink=1 "Jef Caers (la pagina non esiste)") anche usano l'assunzione di stazionarietà nel contesto della [geostatistica](https://it.wikipedia.org/wiki/Geostatistica "Geostatistica") multi-punto, dove si assume che le statistiche superiori a quella n-punto siano stazionarie nel dominio spaziale.[^3]

- [Tahmasebi](https://it.wikipedia.org/wiki/Pejman_Tahmasebi?action=edit&redlink=1 "Pejman Tahmasebi (la pagina non esiste)") e [Sahimi](https://it.wikipedia.org/wiki/Muhammad_Sahimi?action=edit&redlink=1 "Muhammad Sahimi (la pagina non esiste)") hanno presentato una metodologia, basata sui risultati di Shannon, adattiva che può essere usata per la modellazione di ogni sistema non stazionario.[^4]

## Differenziazione

Un modo per avere una serie storica stazionaria consiste nel calcolare le differenze tra osservazioni consecutive. Ciò è noto come differenziazione.

Trasformazioni quali i logaritmi possono aiutare a stabilizzare la varianza di una serie storica. La differenziazione può aiutare a stabilizzare la media di una serie storica rimuovendo i cambiamenti nel livello di una serie storica, ed eliminando così trend e stagionalità.

Uno dei modi per identificare serie storiche non stazionarie consiste nel graficare la funzione di [autocorrelazione](https://it.wikipedia.org/wiki/Autocorrelazione "Autocorrelazione") (ACF). Per una serie storica stazionaria, la funzione di autocorrelazione tenderà a zero piuttosto rapidamente, mentre la funzione di autocorrelazione di dati non stazionari decresce lentamente.[^5]

## Note

## Bibliografia

- Walter Enders, [Applied Econometric Time Series](https://archive.org/details/appliedeconometr0000ende), Third, New York, Wiley, 2010, pp. [53](https://archive.org/details/appliedeconometr0000ende/page/53) –57, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-0-470-50539-7](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-0-470-50539-7 "Speciale:RicercaISBN/978-0-470-50539-7").
- I. Jestrovic, J. L. Coyle e E Sejdic, [The effects of increased fluid viscosity on stationary characteristics of EEG signal in healthy adults](https://oadoi.org/10.1016%2Fj.brainres.2014.09.035), in Brain Research, vol. 1589, 2015, pp. 45-53, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1016/j.brainres.2014.09.035](https://dx.doi.org/10.1016%2Fj.brainres.2014.09.035).
- Hyndman, Athanasopoulos (2013). Forecasting: Principles and Practice. Otexts. [https://www.otexts.org/fpp/8/1](https://www.otexts.org/fpp/8/1)

## Voci correlate

- [Processo di Lévy](https://it.wikipedia.org/wiki/Processo_di_L%C3%A9vy "Processo di Lévy")
- [Processo ergodico stazionario](https://it.wikipedia.org/wiki/Processo_ergodico_stazionario?action=edit&redlink=1 "Processo ergodico stazionario (la pagina non esiste)")
- [Teorema di Wiener-Chinčin](https://it.wikipedia.org/wiki/Teorema_di_Wiener-Chin%C4%8Din "Teorema di Wiener-Chinčin")
- [Ergodicità](https://it.wikipedia.org/wiki/Ergodicit%C3%A0 "Ergodicità")
- [Autocorrelazione](https://it.wikipedia.org/wiki/Autocorrelazione "Autocorrelazione")

## Collegamenti esterni

- (EN) [stationary process](https://www.britannica.com/topic/stationary-process), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Processo stazionario](https://encyclopediaofmath.org/wiki/Stationary_stochastic_process), su [Encyclopaedia of Mathematics](https://it.wikipedia.org/wiki/Encyclopaedia_of_Mathematics "Encyclopaedia of Mathematics"), Springer e European Mathematical Society.
- [Spectral decomposition of a random function (Springer)](http://eom.springer.de/s/s086360.htm), su eom.springer.de.

[^1]: M. B. Priestley, [Spectral Analysis and Time Series](https://archive.org/details/spectralanalysis0000prie), Academic Press, 1981, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-12-564922-3](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-12-564922-3 "Speciale:RicercaISBN/0-12-564922-3").

[^2]: M. B. Priestley, [Non-linear and Non-stationary Time Series Analysis](https://archive.org/details/nonlinearnonstat0000prie), Academic Press, 1988, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-12-564911-8](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-12-564911-8 "Speciale:RicercaISBN/0-12-564911-8").

[^3]: M. Honarkhah e J. Caers, [Stochastic Simulation of Patterns Using Distance-Based Pattern Modeling](https://oadoi.org/10.1007%2Fs11004-010-9276-7), in Mathematical Geosciences, vol. 42, n. 5, 2010, pp. 487-517, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1007/s11004-010-9276-7](https://dx.doi.org/10.1007%2Fs11004-010-9276-7).

[^4]: P. Tahmasebi e M. Sahimi, [Reconstruction of nonstationary disordered materials and media: Watershed transform and cross-correlation function](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.91.032401) (PDF), in Physical Review E, vol. 91, n. 3, 2015, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1103/PhysRevE.91.032401](https://dx.doi.org/10.1103%2FPhysRevE.91.032401).

[^5]: [8.1 Stationarity and differencing | OTexts](https://www.otexts.org/fpp/8/1), su www.otexts.org. URL consultato il 18 maggio 2016.