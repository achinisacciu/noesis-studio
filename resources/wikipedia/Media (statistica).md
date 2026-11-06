---
title: "Media (statistica)"
source: "https://it.wikipedia.org/wiki/Media_(statistica)"
author:
  - "[[Wikipedia]]"
published: 2003-06-07
created: 2026-11-06
description:
tags:
  - "clippings"
---
![](https://it.wikipedia.org/wiki/File:Moda.jpg)

Una funzione di distribuzione con evidenziate la moda, la mediana e la media

In [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica"), la **media** è un singolo valore numerico che descrive sinteticamente un insieme di dati. Esistono diversi tipi di media che possono essere scelte per descrivere un fenomeno: quelle più comunemente impiegate sono le tre cosiddette *medie pitagoriche* (aritmetica, geometrica e armonica). Nel linguaggio ordinario, con il termine *media* si intende comunemente la [media aritmetica](#Media_aritmetica). È l' [indice di posizione](https://it.wikipedia.org/wiki/Indice_di_posizione "Indice di posizione") più usato.[^1]

## Definizione generale di Chisini

[Oscar Chisini](https://it.wikipedia.org/wiki/Oscar_Chisini "Oscar Chisini") ha formalizzato una definizione generale di media ampiamente accettata, che riflette la relatività del concetto di media rispetto al particolare fenomeno in analisi.

Dato un campione $\left(x_{1} , x_{2} , \ldots , x_{n}\right)$ di numerosità $n$ e una funzione $f$ in $n$ variabili, la media delle $x_{i}$ rispetto a $f$ è definita come quell'unico numero $M$, se esiste, tale che sostituendolo a tutte le variabili il valore della funzione rimane inalterato:

$f \left(x_{1} , x_{2} , \ldots , x_{n}\right) = f \left(M , M , \ldots , M\right) .$

Le medie comunemente impiegate (aritmetica, geometrica, armonica, di potenza) sono casi particolari ottenibili tramite questa definizione, per una funzione $f$ opportuna [^2].

## Media aritmetica

La media aritmetica è il tipo di media impiegato più comunemente e quello al quale, con il termine "media", si fa in genere riferimento nel parlare comune. Viene usata per riassumere con un solo numero un insieme di dati su un fenomeno misurabile (per esempio, l'altezza media di una popolazione).

Viene calcolata sommando tutti i valori a disposizione e dividendo il risultato per il numero complessivo di dati.

La formula della media aritmetica semplice per $n$ elementi è:[^3] [^4]

$M_{a} = \frac{1}{n} \sum_{i = 1}^{n} x_{i} .$

Nel caso in cui si disponga della [distribuzione di frequenze](https://it.wikipedia.org/wiki/Distribuzione_\(statistica\) "Distribuzione (statistica)") del fenomeno ([carattere](https://it.wikipedia.org/wiki/Variabile_\(statistica\) "Variabile (statistica)")) misurato è possibile calcolare più agilmente la media aritmetica a partire dalla seguente formula:

$M_{a} = \frac{1}{n} \sum_{j = 1}^{K} x_{j} n_{j} ,$

dove $K$ è il numero di [modalità](https://it.wikipedia.org/wiki/Modalit%C3%A0_\(statistica\) "Modalità (statistica)") assunte dal [carattere](https://it.wikipedia.org/wiki/Variabile_\(statistica\) "Variabile (statistica)") $x,$ $x_{j}$ rappresenta la $j$ -esima [modalità](https://it.wikipedia.org/wiki/Modalit%C3%A0_\(statistica\) "Modalità (statistica)") di $x$ e $n_{j}$ la corrispondente [frequenza assoluta](https://it.wikipedia.org/wiki/Frequenza_\(statistica\) "Frequenza (statistica)"). Essendo poi $n_{j} / n = f_{j}$, ne deriva che:

$M_{a} = \sum_{j = 1}^{K} x_{j} f_{j} ,$

dove $f_{j}$ rappresenta la [frequenza relativa](https://it.wikipedia.org/wiki/Frequenza_relativa "Frequenza relativa") della $j$ -esima [modalità](https://it.wikipedia.org/wiki/Modalit%C3%A0_\(statistica\) "Modalità (statistica)") del [carattere](https://it.wikipedia.org/wiki/Variabile_\(statistica\) "Variabile (statistica)") $x.$

La media aritmetica ponderata (o media pesata) viene calcolata sommando i valori in analisi, ognuno moltiplicato per un coefficiente (detto anche peso) che ne definisce l'"importanza", e dividendo tutto per la somma dei pesi (quindi è una [combinazione lineare](https://it.wikipedia.org/wiki/Combinazione_lineare "Combinazione lineare") [convessa](https://it.wikipedia.org/wiki/Combinazione_convessa "Combinazione convessa") dei dati in analisi). Alla luce di questa definizione, la media aritmetica semplice è un caso particolare di media aritmetica pesata nella quale tutti i valori hanno peso unitario.

La formula generale per la media pesata è quindi:

$M_{a , p o n d} = \frac{\sum_{i = 1}^{n} x_{i} f_{i}}{\sum_{i = 1}^{n} f_{i}} ,$

dove $f_{i}$ è il peso del termine $i$ -esimo.

Si dimostra facilmente che la media aritmetica è un [indice di posizione](https://it.wikipedia.org/wiki/Indice_di_posizione "Indice di posizione"), in quanto aggiungendo o moltiplicando tutti i valori per una stessa quantità la media stessa aumenta o è moltiplicata per quella stessa quantità. Come tutti gli [indici di posizione](https://it.wikipedia.org/wiki/Indice_di_posizione "Indice di posizione"), la media aritmetica fornisce l' [ordine di grandezza](https://it.wikipedia.org/wiki/Ordine_di_grandezza "Ordine di grandezza") dei valori esistenti e permette di conoscerne la somma dei valori (moltiplicando la media per il numero $n$ di elementi).

Oltre che in [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica"), la media aritmetica è ampiamente impiegata in svariati campi, quali [economia](https://it.wikipedia.org/wiki/Economia "Economia"), [sociologia](https://it.wikipedia.org/wiki/Sociologia "Sociologia") e nella maggior parte delle discipline accademiche.

Nonostante la media aritmetica sia spesso usata per fare riferimento alle tendenze, non fornisce un dato statistico robusto in quanto risente notevolmente dei valori anomali ([outlier](https://it.wikipedia.org/wiki/Outlier "Outlier")). Per questo si considerano spesso anche altri indici, come la [mediana](https://it.wikipedia.org/wiki/Mediana_\(statistica\) "Mediana (statistica)"), che sono più robusti rispetto ai valori anomali e si fa un'analisi comparata. Un tentativo di ridurre l'effetto dei valori estremi nel calcolo della media aritmetica è costituito dalla [trimmed mean](https://it.wikipedia.org/wiki/Trimmed_mean "Trimmed mean"), ovvero un particolare calcolo della media nel quale si considera solo una certa percentuale dei valori più centrali, tralasciando i valori agli estremi di questi. È comune, per esempio, il calcolo della [trimmed mean](https://it.wikipedia.org/wiki/Trimmed_mean "Trimmed mean") al 50%, che consiste nella media aritmetica del 50% dei valori più centrali, tralasciando dunque il 25% dei valori più piccoli e il 25% di quelli più grandi.

### Proprietà della media aritmetica

La media aritmetica gode delle seguenti proprietà:[^5]

- la somma degli scarti di ciascun valore di $x$ dalla media aritmetica è nulla:

$\sum_{i = 1}^{n} \left(x_{i} - M_{a}\right) = 0 ;$

- la somma del quadrato degli scarti di ciascun valore di $x$ da una costante $c$ è minima quando $c$ è pari alla media aritmetica:

$\sum_{i = 1}^{n} \left(\right. x_{i} - c \left.\right)^{2} , \text{che }\grave{e}\text{ minima per } c = M_{a} ;$

- la media aritmetica relativa ad un collettivo di $n$ unità suddiviso in $K$ sottogruppi disgiunti può essere calcolata come la media ponderata delle medie dei sottogruppi, con pesi uguali alla loro numerosità:

$M_{a} = \frac{1}{n} \sum_{i = 1}^{K} M_{i} N_{i}$

dove $M_{i}$ ed $N_{i}$ rappresentano rispettivamente la media aritmetica e la numerosità dell' $i$ -esimo sottogruppo;

- la media aritmetica $M_{y}$ di un carattere $y$ ottenuto a partire dalla trasformazione lineare $y=ax+b$ di un carattere $x$ è uguale a $M_{y} = a M_{x} + b$, dove $M_{x}$ è la media aritmetica del carattere $x$.

### Esempio

Dati cinque numeri:

$x_{1} = 10 , x_{2} = 13 , x_{3} = 9 , x_{4} = 7 , x_{5} = 12 ,$

la loro media aritmetica è data da:

$M_{a} = \frac{1}{5} \sum_{i = 1}^{5} x_{i} = \frac{51}{5} = 10,2.$

### Media ponderata

Per calcolare la media ponderata di una serie di dati di cui ogni elemento $x_{i}$ proviene da una differente [distribuzione di probabilità](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0 "Distribuzione di probabilità") con una [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") $\left(\sigma_{i}\right)^{2}$ nota, una possibile scelta per i pesi è data da:

$w_{i} = \frac{1}{\sigma_{i}^{2}} .$

La media ponderata in questo caso è:

$\bar{x} = \frac{\sum_{i = 1}^{n} x_{i} / \left(\sigma_{i}\right)^{2}}{\sum_{i = 1}^{n} 1 / \left(\sigma_{i}\right)^{2}}$

e la varianza della media ponderata è:

$\sigma_{\bar{x}}^{2} = \frac{1}{\sum_{i = 1}^{n} 1 / \left(\sigma_{i}\right)^{2}} ,$

che si riduce a $\sigma_{\bar{x}}^{2} = \frac{\left(\sigma_{0}\right)^{2}}{n}$ quando tutti i $\sigma_{i} = \sigma_{0}$.

Intuitivamente questa scelta avviene perché il peso che viene dato ad ogni valore è il reciproco della varianza, ossia il reciproco del quadrato dell'"incertezza". In pratica più è grande l'incertezza (in questo caso misurata dalla varianza) più il valore associato alla stessa pesa meno. Oppure, dal punto di vista opposto, più si è certi del valore più questo pesa.

In modo più formale si può dire che questa media pesata è lo [stimatore di massima verosimiglianza](https://it.wikipedia.org/wiki/Metodo_della_massima_verosimiglianza "Metodo della massima verosimiglianza") della media delle distribuzioni di probabilità nell'ipotesi che esse siano indipendenti e [normalmente distribuite](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale") con la stessa media.

## Media geometrica

La media geometrica di $n$ termini è la radice $n$ -esima del prodotto degli $n$ valori:

$M_{g} = \sqrt[n]{\prod_{i = 1}^{n} x_{i}} .$

Sfruttando le proprietà dei [logaritmi](https://it.wikipedia.org/wiki/Logaritmo "Logaritmo"), l'espressione della media geometrica può essere resa trasformando i prodotti in somme e le potenze in prodotti:

$\sqrt[n]{\prod_{i = 1}^{n} x_{i}} = exp \left[\frac{1}{n} \sum_{i = 1}^{n} ln x_{i}\right] .$

Dalla precedente scrittura si ricava anche una proprietà della media geometrica: il logaritmo della media geometrica è uguale alla media aritmetica dei logaritmi. Infatti, svolgendo il logaritmo su entrambi i lati dell'uguaglianza e ricordando che $ln⁡e=1$, si ottiene:

$ln \sqrt[n]{\prod_{i = 1}^{n} x_{i}} = \frac{1}{n} \sum_{i = 1}^{n} ln x_{i} .$

Nel caso si disponga della [distribuzione di frequenze](https://it.wikipedia.org/wiki/Distribuzione_\(statistica\) "Distribuzione (statistica)") della variabile, è possibile calcolare più facilmente la media geometrica attraverso la seguente formula:

$M_{g} = \sqrt[n]{\prod_{j = 1}^{K} \left(x_{j}\right)^{n_{j}}} ,$

dove $K$ è il numero delle modalità assunte dalla variabile $x$, $x_{j}$ rappresenta la $j$ -esima modalità di $x$ e $n_{j}$ la corrispondente frequenza assoluta. Dalla precedente si ottiene anche:

$M_{g} = \prod_{j = 1}^{K} \left(x_{j}\right)^{f_{j}} .$

Analogamente al caso della media aritmetica, attribuendo un peso ai termini si può calcolare la media geometrica ponderata:

$M_{g , p o n d} = \sqrt[\left(\sum_{i = 1}^{n} f_{i}\right)]{\prod_{i = 1}^{n} x_{i}^{f_{i}}} .$

La media geometrica può essere vista anche come media aritmetico-armonica. Definendo infatti due [successioni](https://it.wikipedia.org/wiki/Successione_\(matematica\) "Successione (matematica)"):

$a_{n + 1} = \frac{a_{n} + h_{n}}{2} , a_{0} = x$

$h_{n + 1} = \frac{2}{\frac{1}{a_{n}} + \frac{1}{h_{n}}} , h_{0} = y$

$a_{n}$ e $h_{n}$ convergono alla media geometrica di $x$ e $y$.

Infatti le successioni convergono ad un [limite](https://it.wikipedia.org/wiki/Limite_\(matematica\) "Limite (matematica)") comune. Si può infatti osservare che:

$\sqrt{a_{i} h_{i}} = \sqrt{\frac{a_{i} + h_{i}}{\frac{a_{i} + h_{i}}{h_{i} a_{i}}}} = \sqrt{\frac{a_{i} + h_{i}}{\frac{1}{a_{i}} + \frac{1}{h_{i}}}} = \sqrt{a_{i + 1} h_{i + 1}} .$

Lo stesso ragionamento può essere applicato sostituendo le medie aritmetica e armonica con una coppia di medie generalizzate di ordine finito e opposto.

La media geometrica si applica a valori positivi. Ha un chiaro significato geometrico: ad esempio la media geometrica di due numeri è la lunghezza del lato di un quadrato [equivalente](https://it.wikipedia.org/wiki/Equiestensione "Equiestensione") ad un rettangolo che abbia i lati di modulo pari ai due numeri. Lo stesso vale in un numero di [dimensioni](https://it.wikipedia.org/wiki/Dimensione_\(matematica\) "Dimensione (matematica)") superiore. La media geometrica trova impiego soprattutto dove i valori considerati vengono per loro natura moltiplicati tra di loro e non sommati. Esempio tipico sono i tassi di crescita, come i [tassi d'interesse](https://it.wikipedia.org/wiki/Tasso_d'interesse "Tasso d'interesse") o i [tassi d'inflazione](https://it.wikipedia.org/wiki/Tasso_d'inflazione "Tasso d'inflazione").

Una caratteristica è che valori piccoli (rispetto alla media aritmetica) sono molto più influenti dei valori grandi. In particolare, è sufficiente la presenza di un unico valore nullo per annullare la media.

### Esempio

Dati cinque numeri:

$x_{1} = 10 , x_{2} = 13 , x_{3} = 9 , x_{4} = 7 , x_{5} = 12 ,$

la loro media geometrica è data da:

$M_{g} = \sqrt[5]{\prod_{i = 1}^{5} x_{i}} = \sqrt[5]{10 \cdot 13 \cdot 9 \cdot 7 \cdot 12} = \sqrt[5]{98 280} \approx 9,97.$

## Media armonica

La media armonica di $n$ termini è definita come il reciproco della media aritmetica dei reciproci:[^6]

$M_{h} = \frac{n}{\sum_{i = 1}^{n} \frac{1}{x_{i}}} .$

Per praticità di calcolo si può applicare la seguente formula, ottenuta tramite le proprietà di somme e prodotti:

$M_{h} = \frac{n \cdot \prod_{i = 1}^{n} x_{i}}{\sum_{j = 1}^{n} \frac{\prod_{i = 1}^{n} x_{i}}{x_{j}}} .$

Se a un insieme di dati è associato un insieme di pesi $w_{1} \ldots w_{n}$, è possibile definire la media armonica ponderata come:

$\frac{\sum_{i = 1}^{n} w_{i}}{\sum_{i = 1}^{n} \frac{w_{i}}{x_{i}}} .$

La media armonica semplice rappresenta un caso particolare, nel quale tutti i pesi hanno valore unitario.

La media armonica è fortemente influenzata dagli elementi di modulo minore: rispetto alla media aritmetica risente meno dell'influenza di [outlier](https://it.wikipedia.org/wiki/Outlier "Outlier") grandi, ma è influenzata notevolmente dagli outlier piccoli.

### Esempio

Dati cinque numeri:

$x_{1} = 10 , x_{2} = 13 , x_{3} = 9 , x_{4} = 7 , x_{5} = 12 ,$

la loro media armonica è data da:

$M_{h} = \frac{5}{\sum_{i = 1}^{5} \frac{1}{x_{i}}} \approx \frac{5}{0,51} \approx 9,72.$

## Media di potenza

La media di potenza (o media generalizzata o media di [Hölder](https://it.wikipedia.org/wiki/Otto_H%C3%B6lder "Otto Hölder") o media $p$ -esima) rappresenta una generalizzazione delle medie pitagoriche. È definita come la radice $p$ -esima della media aritmetica delle [potenze](https://it.wikipedia.org/wiki/Potenza_\(matematica\) "Potenza (matematica)") di esponente $p$ degli $n$ valori considerati:

$M_{p} \left(x_{1} , \ldots , x_{n}\right) = \left(\frac{1}{n} \sum_{i = 1}^{n} x_{i}^{p}\right)^{\frac{1}{p}} .$

Molte altre medie sono casi particolari della media generalizzata, per opportuni valori di $p$:

- media aritmetica, per $p=1$;
- media geometrica, per $p→0$;
- media armonica, per $p=−1$;
- media quadratica, per $p=2$ (usata soprattutto in presenza di numeri negativi per eliminare i segni);
- media cubica, per $p=3$.

Inoltre:

- $M+∞(x1,…,xn)=max⁡{x1,…,xn};$
- $M−∞(x1,…,xn)=min⁡{x1,…,xn}.$

Ad ogni termine può essere associato un coefficiente detto peso, in genere rappresentato dalla [frequenza](https://it.wikipedia.org/wiki/Frequenza_\(statistica\) "Frequenza (statistica)") oppure da un valore il quale descrive l'importanza (oggettiva o soggettiva) che il singolo elemento riveste nella distribuzione. Se ai dati in esame si assegna un insieme di pesi $w_{i}$, tali che $w = \sum w_{i}$, è possibile definire la media pesata:

$M_{p} \left(x_{1} , \ldots , x_{n}\right) = \left(\frac{1}{w} \sum_{i = 1}^{n} w_{i} x_{i}^{p}\right)^{\frac{1}{p}} .$

## Media aritmetico-geometrica

La media aritmetico-geometrica (AGM) di due [numeri reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale") positivi $x$ e $y$ è definita come limite comune di due [successioni](https://it.wikipedia.org/wiki/Successione_\(matematica\) "Successione (matematica)") definite come segue.

Si determinano la media aritmetica $a_{1}$ e la media geometrica $g_{1}$ di $x$ e $y$

$a_{1} = \frac{1}{2} \left(x + y\right)$

$g_{1} = \sqrt{x y} .$

Quindi si itera il procedimento, sostituendo $a_{1}$ ad $x$ e $g_{1}$ a $y$. In questo modo si ottengono due successioni:

$a_{n + 1} = \frac{1}{2} \left(a_{n} + g_{n}\right)$

$g_{n + 1} = \sqrt{a_{n} g_{n}} .$

Le due successioni sono [convergenti](https://it.wikipedia.org/wiki/Convergenza "Convergenza") e hanno limite comune, detto media aritmetico-geometrica di $x$ e $y$, indicata come $M(x,y)$ o talvolta come $agm(x,y)$.

La media geometrica di due numeri è sempre minore della media aritmetica, di conseguenza $g_{n}$ è una successione crescente, $a_{n}$ è decrescente e si ha $g_{n} \leq M \left(x , y\right) \leq a_{n}$ (le [disuguaglianze](https://it.wikipedia.org/wiki/Disuguaglianza "Disuguaglianza") sono strette se $x≠y$).

Quindi $M(x,y)$ è un numero compreso fra la media aritmetica e la media geometrica di $x$ e $y$.

Inoltre, dato un [numero reale](https://it.wikipedia.org/wiki/Numero_reale "Numero reale") $r≥0$, vale la relazione

$M(rx,ry)=rM(x,y).$

Esiste anche un'espressione in forma integrale di $M(x,y)$:

$M \left(x , y\right) = \frac{\pi}{4} \left(x + y\right) / K \left(\frac{x - y}{x + y}\right) ,$

dove $K(m)$ rappresenta l' [integrale ellittico completo di prima specie](https://it.wikipedia.org/wiki/Integrale_ellittico_completo_di_prima_specie "Integrale ellittico completo di prima specie"):

$K \left(m\right) = \int_{0}^{\frac{\pi}{2}} \frac{d \theta}{\sqrt{1 - m^{2} sin^{2} \theta}} .$

Inoltre, poiché la media aritmetico-geometrica converge piuttosto rapidamente, la formula precedente è utile anche nel calcolo degli integrali ellittici.

Il reciproco della media aritmetico-geometrica di $1$ e $\sqrt{2}$ è chiamata [costante di Gauss](https://it.wikipedia.org/wiki/Costante_di_Gauss "Costante di Gauss"), in onore del matematico tedesco [Carl Friedrich Gauss](https://it.wikipedia.org/wiki/Carl_Friedrich_Gauss "Carl Friedrich Gauss").

$\frac{1}{M \left(1 , \sqrt{2}\right)} = G = 0,8346268 \ldots$

## Media integrale

Una generalizzazione del concetto di media a [distribuzioni continue](https://it.wikipedia.org/wiki/Variabile_casuale_continua "Variabile casuale continua") prevede l'uso di [integrali](https://it.wikipedia.org/wiki/Integrale "Integrale"). Supponiamo di avere una [funzione](https://it.wikipedia.org/wiki/Funzione_\(matematica\) "Funzione (matematica)") $f:[a,b]→ℝ$, integrabile. Allora si può definire la media $μ$ come:

$\mu = \frac{1}{b - a} \int_{a}^{b} f \left(x\right) d x .$

Data inoltre una funzione $p:[a,b]→ℝ$ tale che $p(x)>0$, detta *peso*, si può definire la media integrale pesata $\mu_{p}$ come:

$\mu_{p} = \frac{\int_{a}^{b} p \left(x\right) f \left(x\right) d x}{\int_{a}^{b} p \left(x\right) d x} .$

Più in generale data una funzione $f:Ω→ℝ$ dove $Ω$ è un [insieme](https://it.wikipedia.org/wiki/Insieme "Insieme") sul quale è definita una funzione di integrazione, si definisce la media $μ$ come:

$\mu = \frac{\int_{\Omega} f \left(x\right) d x}{\int_{\Omega} d x} .$

### Media temporale

La media temporale, spesso usata nella trattazione di segnali, è chiamata componente continua. Si tratta della media integrale calcolata in un intervallo di tempo tendente all'infinito.

$\langle x \rangle_{\left(t_{2} , t_{1}\right)} = \frac{1}{t_{2} - t_{1}} \int_{t_{1}}^{t_{2}} x \left(t\right) d t .$

per $t_{2} - t_{1} = T_{0} \rightarrow + \infty .$

## Note

## Bibliografia

- Giuseppe Leti, Statistica descrittiva, Bologna, Il Mulino, 1983, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [88-15-00278-2](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/88-15-00278-2 "Speciale:RicercaISBN/88-15-00278-2").
- M. Ross Sheldon, [Introduzione alla statistica](https://books.google.it/books?id=Fnv1AwAAQBAJ), 2ª ed., Santarcangelo di Romagna, Maggioli Editore, 2014, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [8891602671](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/8891602671 "Speciale:RicercaISBN/8891602671").

## Voci correlate

- [Valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso")
- [Variabile](https://it.wikipedia.org/wiki/Variabile_\(statistica\) "Variabile (statistica)")
- [Varianza](https://it.wikipedia.org/wiki/Varianza "Varianza")
- [Covarianza](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\) "Covarianza (probabilità)")
- [Mediana](https://it.wikipedia.org/wiki/Mediana_\(statistica\) "Mediana (statistica)")
- [Moda](https://it.wikipedia.org/wiki/Moda_\(statistica\) "Moda (statistica)")
- [Momento (statistica)](https://it.wikipedia.org/wiki/Momento_\(statistica\) "Momento (statistica)")
- [Trimmed mean](https://it.wikipedia.org/wiki/Trimmed_mean "Trimmed mean")
- [Disuguaglianza tra media aritmetica e media geometrica](https://it.wikipedia.org/wiki/Disuguaglianza_tra_media_aritmetica_e_media_geometrica "Disuguaglianza tra media aritmetica e media geometrica")

## Altri progetti

Altri progetti

- [Wikizionario](https://it.wiktionary.org/wiki/media "wikt:media")
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Means?uselang=it)

- [Wikizionario](https://it.wiktionary.org/wiki/ "wikt:") contiene il lemma di dizionario « **[media](https://it.wiktionary.org/wiki/media "wikt:media")** »
- contiene immagini o altri file sulla **[media](https://commons.wikimedia.org/wiki/Category:Means?uselang=it)**

## Collegamenti esterni

- [Media](https://www.treccani.it/enciclopedia/media), su Treccani.it – Enciclopedie on line, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana").
- [Mèdia](https://www.treccani.it/vocabolario/media), su [Vocabolario Treccani](https://it.wikipedia.org/wiki/Vocabolario_Treccani "Vocabolario Treccani"), [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana").
- [mèdia](https://www.sapere.it/enciclopedia/m%C3%A8dia.html), su sapere.it, [De Agostini](https://it.wikipedia.org/wiki/De_Agostini "De Agostini").
- (EN) [mean](https://www.britannica.com/topic/mean), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Mean](http://mathworld.wolfram.com/Mean.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- [Calcolo della media pesata](http://stat.altervista.org/) [Archiviato](https://web.archive.org/web/20200128090509/http://stat.altervista.org/) il 28 gennaio 2020 in [Internet Archive](https://it.wikipedia.org/wiki/Internet_Archive "Internet Archive"). - Sito italiano che permette di eseguire online il calcolo della media, anche pesata, di una serie di dati.
- [Calcolo della media ponderata](http://www.calcolomedia.it/) - Sito che permette il calcolo della media ponderata e aritmetica con possibilità di grafici e statistiche.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh85010516](http://id.loc.gov/authorities/subjects/sh85010516) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4130070-1](https://d-nb.info/gnd/4130070-1) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007295828005171](https://www.nli.org.il/en/authorities/987007295828005171) |
| --- | --- |

[^1]: [Glossario Istat](https://web.archive.org/web/20111231130402/http://www3.istat.it/servizi/studenti/binariodie/CorsoExcel/Glossario.htm), su www3.istat.it (archiviato dall' url originale il 31 dicembre 2011).

[^2]: Giorgio dall'Aglio, Calcolo delle probabilità, 3ª ed., Bologna, Zanichelli, 2003, p. 127.

[^3]: The International Union of Pure and Applied Chemistry (IUPAC), [IUPAC - arithmetic mean (A00440)](https://goldbook.iupac.org/terms/view/A00440), su goldbook.iupac.org. URL consultato il 16 febbraio 2022.

[^4]: [Sheldon](#CITEREFSheldon), p. 69.

[^5]: Luigi Pace e Alessandra Salvan, INTRODUZIONE alla STATISTICA, I Statistica Descrittiva, Udine e Padova, CEDAM, 1996, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [88-13-19939-2](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/88-13-19939-2 "Speciale:RicercaISBN/88-13-19939-2").

[^6]: The International Union of Pure and Applied Chemistry (IUPAC), [IUPAC - harmonic mean (H02745)](https://goldbook.iupac.org/terms/view/H02745), su goldbook.iupac.org. URL consultato il 16 febbraio 2022.