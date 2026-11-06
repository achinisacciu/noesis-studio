---
title: "Processo markoviano"
source: "https://it.wikipedia.org/wiki/Processo_markoviano"
author:
  - "[[Wikipedia]]"
published: 2003-04-17
created: 2026-11-06
description:
tags:
  - "clippings"
---
![](https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2b/Markovkate_01.svg/250px-Markovkate_01.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Un diagramma rappresentante un processo markoviano a due stati, etichettati con A ed E. Ogni numero rappresenta la probabilità del processo di cambiare da uno stato all'altro e la freccia rappresenta la direzione di tale cambiamento. Per esempio, se il processo si trova nello stato A, allora la probabilità di rimanervi è 0.6, mentre la probabilità di passare allo stato E è di 0.4.

Si definisce **processo stocastico markoviano** (o **di Markov**), un [processo aleatorio](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico") in cui la [probabilità di transizione](https://it.wikipedia.org/wiki/Probabilit%C3%A0_di_transizione "Probabilità di transizione") che determina il passaggio a uno [stato di sistema](https://it.wikipedia.org/wiki/Stato_di_sistema "Stato di sistema") dipende solo dallo stato del sistema immediatamente precedente ([proprietà di Markov](https://it.wikipedia.org/wiki/Propriet%C3%A0_di_Markov "Proprietà di Markov")) e non da come si è giunti a questo stato.[^1] Viceversa si dice processo non markoviano un processo aleatorio per cui non vale la proprietà di Markov. Prende il nome dal [matematico](https://it.wikipedia.org/wiki/Matematico "Matematico") [russo](https://it.wikipedia.org/wiki/Russia "Russia") [Andrej Andreevič Markov](https://it.wikipedia.org/wiki/Andrej_Andreevi%C4%8D_Markov_\(1856\) "Andrej Andreevič Markov (1856)") che per primo ne sviluppò la teoria. Modelli di tipo markoviano vengono utilizzati nella progettazione di [reti di telecomunicazioni](https://it.wikipedia.org/wiki/Reti_di_telecomunicazioni "Reti di telecomunicazioni"): la [teoria delle code](https://it.wikipedia.org/wiki/Teoria_delle_code "Teoria delle code") che ne consegue trova applicazione in molti ambiti, dalla fila agli sportelli ai [pacchetti](https://it.wikipedia.org/wiki/Pacchetto_\(reti\) "Pacchetto (reti)") dati in coda in un [router](https://it.wikipedia.org/wiki/Router "Router").

Un processo di Markov può essere descritto per mezzo dell'enunciazione della [proprietà di Markov](https://it.wikipedia.org/wiki/Propriet%C3%A0_di_Markov "Proprietà di Markov"), o condizione di "assenza di memoria", che può essere scritta come

$P \left(\right. X \left(t_{n + 1}\right) = x_{n + 1} \left|\right. X \left(t_{n}\right) = x_{n} , X \left(t_{n - 1}\right) = x_{n - 1} , \ldots , X \left(t_{0}\right) = x_{0} \left.\right) = P \left(\right. X \left(t_{n + 1}\right) = x_{n + 1} \left|\right. X \left(t_{n}\right) = x_{n} \left.\right) .$

## Catene di Markov

![](https://it.wikipedia.org/wiki/File:AAMarkov.jpg)

Il matematico russo Andrey Markov

Una **catena di Markov** è un processo di Markov con [spazio degli stati](https://it.wikipedia.org/wiki/Stato_di_sistema "Stato di sistema") discreto, quindi è un [processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico") che assume valori in uno spazio discreto e che gode della [proprietà di Markov](https://it.wikipedia.org/wiki/Propriet%C3%A0_di_Markov "Proprietà di Markov"). L'insieme $S$ di spazio degli stati può essere finito o infinito numerabile. Nel primo caso si parla di catena di Markov a stati finiti. Una catena di Markov può essere tempo-continua o tempo-discreta, in base all'insieme $T$ di appartenenza della variabile tempo (continuo o discreto).

Formalmente una catena di Markov è un processo stocastico Markoviano caratterizzato da un parametro $t_{i} \in T$, da un insieme $S$ di stati e da una [funzione probabilità di transizione](https://it.wikipedia.org/wiki/Probabilit%C3%A0_di_transizione "Probabilità di transizione")

$P:S×S×T→[0,1].$

Essendo un processo Markoviano, $P$ gode della [proprietà di Markov](https://it.wikipedia.org/wiki/Propriet%C3%A0_di_Markov "Proprietà di Markov"):

$P \left(\right. X \left(t_{n + 1}\right) = x_{n + 1} \left|\right. X \left(t_{n}\right) = x_{n} , X \left(t_{n - 1}\right) = x_{n - 1} , \ldots , X \left(t_{0}\right) = x_{0} \left.\right) = P \left(\right. X \left(t_{n + 1}\right) = x_{n + 1} \left|\right. X \left(t_{n}\right) = x_{n} \left.\right) .$

Nel caso di catena di Markov a *tempo discreto,* cioè con l'insieme $T$ discreto, la notazione si semplifica:

$P \left(\right. X_{n + 1} = x_{n + 1} \left|\right. X_{n} , X_{n - 1} , \ldots , X_{0} \left.\right) = P \left(\right. X_{n + 1} = x_{n + 1} \left|\right. X_{n} \left.\right) .$

### Catene di Markov omogenee

Una catena di Markov omogenea è un processo markoviano in cui la probabilità di transizione al tempo $t_{i}$ non dipende dal tempo stesso, ma soltanto dallo stato del sistema al tempo immediatamente precedente $S \left(t_{i - 1}\right)$. In altre parole, la probabilità di transizione è indipendente dall'origine dell'asse dei tempi e quindi dipende soltanto dalla distanza tra i due istanti temporali.

Per le catene omogenee vale la condizione

$P \left(\right. X_{n + 1} = x \left|\right. X_{n} = y \left.\right) = P \left(\right. X_{n} = x \left|\right. X_{n - 1} = y \left.\right) .$

Più in generale si dimostra che in una catena di Markov omogenea la probabilità di transizione da uno stato a un altro in $n$ passi è costante nel tempo:

$P \left(\right. X_{i + n} = x \left|\right. X_{i} = y \left.\right) = P \left(\right. X_{i - 1 + n} = x \left|\right. X_{i - 1} = y \left.\right) , \forall i = 1 , 2 , \ldots$

I sistemi reali che possono essere modellati con catene di Markov omogenee sono rari: è sufficiente pensare al sistema "tempo atmosferico" per capire come la probabilità di transizione da uno stato (per esempio "sole") a un altro stato (per esempio "pioggia") dipende dalla stagione, quindi non è possibile modellare questo sistema come catena di Markov omogenea. Tuttavia restringendo l'analisi del sistema a un determinato intervallo di tempo si può considerare il comportamento omogeneo: in questo caso l'intervallo di tempo potrebbe essere una singola stagione.

### Matrice di transizione

Una catena di Markov omogenea a stati finiti in cui l'insieme $S$ degli stati del sistema è finito e ha $N$ elementi può essere rappresentata mediante una matrice di transizione $A \in \mathbb{R}^{N \times N}$ e un vettore di probabilità iniziale $\left(\overset{\sim}{\pi}\right)_{0} \in \mathbb{R}^{N}$.

Gli elementi di $A$ rappresentano le probabilità di transizione tra gli stati della catena: una catena che si trova nello stato $i$ ha probabilità $a_{i j}$ di passare allo stato $j$ nel passo immediatamente successivo. In particolare gli elementi $a_{i i}$ sulla [diagonale principale](https://it.wikipedia.org/wiki/Diagonale_principale "Diagonale principale") di $A$ indicano le probabilità di rimanere nello stesso stato $i$. Il vettore $\left(\overset{\sim}{\pi}\right)_{0}$ definisce le probabilità che inizialmente la catena di Markov si trovi in ciascuno degli $N$ stati. Una catena di Markov omogenea è univocamente definita dalla coppia $\left(A , \left(\overset{\sim}{\pi}\right)_{0}\right)$.

Se al tempo $t_{0}$ ha la distribuzione di probabilità $\left(\overset{\sim}{\pi}\right)_{0}$ allora le probabilità $\left(\overset{\sim}{\pi}\right)_{n}$ che a un tempo $t_{n}$ il sistema si trovi in ciascuno degli $N$ stati sono date dal vettore così definito:

$\left(\right. \left(\overset{\sim}{\pi}\right)_{n} \left.\right)^{T} = \left(\right. \left(\overset{\sim}{\pi}\right)_{0} \left.\right)^{T} \cdot A^{n} ,$

dove $\left(\right. \left(\overset{\sim}{\pi}\right)_{n} \left.\right)^{T}$ indica la trasposta del vettore $\left(\overset{\sim}{\pi}\right)_{n}$.

Dalla [definizione assiomatica della probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0#Definizione_assiomatica "Probabilità") discendono le seguenti proprietà per la matrice $A$:

- $aij≥0,∀i,j∈{1…N};$
- $∑j=1Naij=1,∀i∈{1…N}.$

La seconda proprietà equivale a richiedere che la somma degli elementi su ciascuna riga sia uguale a 1, nel qual caso la matrice si dice anche [stocastica](https://it.wikipedia.org/wiki/Matrice_stocastica "Matrice stocastica").

Per esempio, $A$ e $\left(\overset{\sim}{\pi}\right)_{0}$ possono essere i seguenti:

$A = \begin{pmatrix} 0 , 3 & 0 , 5 & 0 , 2 \\ 0 , 1 & 0 , 8 & 0 , 1 \\ 0 , 5 & 0 , 5 & 0 \end{pmatrix} , \left(\overset{\sim}{\pi}\right)_{0} = \begin{pmatrix} 0 , 4 \\ 0 , 3 \\ 0 , 3 \end{pmatrix} .$

Nel caso di una *catena di Markov omogenea a stati discreti* si può adottare la notazione sintetica:

$P_{i j}^{\left(n\right)} \equiv P \left(\right. X_{m + n} = s_{j} \left|\right. X_{m} = s_{i} \left.\right) = P \left(\right. X_{n} = s_{j} \left|\right. X_{0} = s_{i} \left.\right) ,$

dove $(n)$ non è un esponente bensì un indice.

Si ha quindi $\left(\right. \left(\overset{\sim}{\pi}\right)_{n} \left.\right)_{j} = \underset{i \in S}{\sum} \left(\right. \left(\overset{\sim}{\pi}\right)_{0} \left.\right)_{i} \left(\right. P^{\left(n\right)} \left.\right)_{i j}$.

Si hanno le seguenti proprietà:

- $P_{i j} \geq 0 , \forall i , j \in S ;$
- $\underset{j \in S}{\sum} P_{i j} = 1.$

### Catene di Markov aperiodiche

Il **periodo** di uno stato $s_{i} \in S$ di una *catena di Markov a stati discreti,* con $S$ finito o infinito numerabile, è definito come il minimo numero di passi temporali affinché vi sia una probabilità diversa da zero di tornare sullo stesso stato, partendo dallo stato $s_{i}$ al tempo $t_{m}$. Formalmente il periodo $d \left(s_{i}\right)$ è definito come segue:

$d(si,tm)=MCD{n≥1:P(Xm+n=si|Xm=si)>0},$

dove $MCD$ indica il [massimo comune divisore](https://it.wikipedia.org/wiki/Massimo_comune_divisore "Massimo comune divisore").

Nel caso di una *catena di Markov omogenea a stati finiti* con numero di stati $N$, rappresentabile quindi con una matrice $A \in \mathbb{R}^{N}$, si può riformulare la definizione così:

$d(si)=MCD{n≥1:(An)ii>0}.$

Lo stato $s_{i}$ è detto aperiodico se il suo periodo è uguale a 1.

Una catena di Markov è detta aperiodica se tutti i suoi stati sono aperiodici, altrimenti è detta periodica.

### Catene di Markov irriducibili

Una catena di Markov a stati discreti è detta irriducibile se partendo da ogni stato $s_{i}$ c'è una probabilità maggiore di zero di raggiungere ogni altro stato $s_{j}$. Formalmente una catena di Markov è irriducibile se:

$\forall s_{i} , s_{j} \in S , \forall m \in \mathbb{N} , \exists n \in \mathbb{N} : P \left(\right. X_{m + n} = s_{j} \left|\right. X_{m} = s_{i} \left.\right) > 0.$

### Stati ricorrenti positivi

Sia

$Ti={min⁡{n≥1:Xn=si}se Xn=si per qualche n≥1,+∞altrimenti,$

lo stato $s_{i} \in S$ si dice ricorrente positivo se $E \left(\right. T_{i} \left|\right. X_{0} = s_{i} \left.\right) = \mu_{i} < + \infty .$

Se una catena è irriducibile e un suo stato è ricorrente positivo allora tutti i suoi stati sono ricorrenti positivi, in tale caso la catena si dice ricorrente positiva.

### Distribuzioni stazionarie

Data una catena di Markov omogenea a stati discreti, una sua distribuzione stazionaria di probabilità, detta anche distribuzione di equilibrio, $π={π1…πn…}$ è una [distribuzione discreta di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità") che soddisfa le seguenti:

- $\pi_{i} \geq 0 , \forall i \in S ;$
- $\underset{i \in S}{\sum} \pi_{i} = 1 ;$
- $\underset{i \in S}{\sum} \pi_{i} P_{i j} = \pi_{j} , \forall j \in S .$

Informalmente una distribuzione stazionaria è una distribuzione di probabilità che si mantiene costante all'evolversi nel tempo della catena di Markov.

L'importanza delle distribuzioni stazionarie per le catene di Markov omogenee a stati discreti è data dai seguenti teoremi:

- Il teorema di esistenza e unicità afferma che data una catena di Markov omogenea a stati discreti con probabilità di transizione $P_{i j}$ e spazio degli stati $S$, se la catena di Markov è irriducibile e ricorrente positiva allora esiste un'unica distribuzione stazionaria $π$ per la catena di Markov.
- Il teorema della convergenza afferma che data una catena di Markov omogenea a stati discreti con probabilità di transizione $P_{i j}$ e spazio degli stati $S$, se la catena di Markov è irriducibile, aperiodica e ricorrente positiva allora la distribuzione di probabilità $\left(\overset{\sim}{\pi}\right)_{n}$ al tempo $t_{n}$, converge alla distribuzione stazionaria $π$ per ogni distribuzione iniziale di probabilità $\left(\overset{\sim}{\pi}\right)_{0}$ scelta. Si ha cioè

$\underset{n \rightarrow \infty}{lim} \underset{i \in S}{\sum} \left(\right. \left(\overset{\sim}{\pi}\right)_{0} \left.\right)_{i} \left(\right. P^{\left(n\right)} \left.\right)_{i j} = \pi_{j} , \forall \left(\overset{\sim}{\pi}\right)_{0} , \forall i , j \in S .$

La convergenza di una catena di Markov a una distribuzione stazionaria e la possibilità di costruire una catena con una distribuzione stazionaria scelta sono alla base del funzionamento dell' [algoritmo di Metropolis-Hastings](https://it.wikipedia.org/wiki/Algoritmo_di_Metropolis-Hastings "Algoritmo di Metropolis-Hastings").

### Catene di Markov ergodiche

Una catena di Markov si definisce ergodica se e solo se per ogni istante iniziale $t_{0}$ e per ogni condizione iniziale di probabilità $\overset{\sim}{\pi} \left(t_{0}\right)$ esiste ed è indipendente da $t_{0}$ e da $\overset{\sim}{\pi} \left(t_{0}\right)$ il limite della probabilità per tempi infiniti

$P = \underset{t \rightarrow \infty}{lim} \overset{\sim}{\pi} \left(t\right) .$

## Applicazioni

![](https://it.wikipedia.org/wiki/File:PageRank-hi-res.png)

Schematizzazione del sistema PageRank

- Molti algoritmi di [Link Analysis Ranking](https://it.wikipedia.org/wiki/Link_Analysis_Ranking "Link Analysis Ranking") si basano sulla teoria di processi markoviani. Ad esempio il [PageRank](https://it.wikipedia.org/wiki/PageRank "PageRank") [inferito](https://it.wikipedia.org/wiki/Inferenza_statistica "Inferenza statistica") da [Google](https://it.wikipedia.org/wiki/Google "Google") si basa sulla frequenza a posteriori di transizione degli utenti da un [sito web](https://it.wikipedia.org/wiki/Sito_web "Sito web") A a un sito B tramite i [link](https://it.wikipedia.org/wiki/Collegamento_ipertestuale "Collegamento ipertestuale") che da A conducono a B e non sul semplice numero e tipo di collegamenti da A a B, in modo da rispecchiare la popolarità del legame per gli utenti e non l'importanza per il creatore del sito. Cioè la frequenza di un sito è un valore nell'intervallo \[0,1\] corrispondente alla quantità media di tempo spesa sul sito da un gran numero di utenti dopo un tempo abbastanza elevato: la frequenza, opportunamente riscalata, costituisce il Page Rank del sito. Dato che la frequenza di transizione approssima la probabilità di transizione si può stimare la distribuzione stazionaria di probabilità della catena di Markov formata da tutti i siti web, costruendo una [matrice di transizione](https://it.wikipedia.org/wiki/Matrice_di_transizione "Matrice di transizione").
- Fa uso di modelli statistici markoviani anche un filone di [modellistica](https://it.wikipedia.org/wiki/Modellistica_matematica "Modellistica matematica") del [linguaggio naturale](https://it.wikipedia.org/wiki/Linguaggio_naturale "Linguaggio naturale"). Ad esempio nell'ambito della [sintesi vocale](https://it.wikipedia.org/wiki/Sintesi_vocale "Sintesi vocale") lo [CSELT](https://it.wikipedia.org/wiki/CSELT "CSELT") è stato tra i precursori di questo filone, in particolare per la [lingua italiana](https://it.wikipedia.org/wiki/Lingua_italiana "Lingua italiana") e le [lingue latine](https://it.wikipedia.org/wiki/Lingue_latine "Lingue latine").[^2]
- Diversi algoritmi previsionali in ambito economico, finanziario e di [dinamica dei sistemi](https://it.wikipedia.org/wiki/Dinamica_dei_sistemi "Dinamica dei sistemi") fanno uso dei processi markoviani.

Anche gran parte della modellistica di serie temporali in finanza si basa su processi stocastici generati da catene di Markov.

## Software

- In [R](https://it.wikipedia.org/wiki/R_\(software\) "R (software)"), una libreria abbastanza completa è il pacchetto markovchain.[^3]
- Una lista di pacchetti [Python](https://it.wikipedia.org/wiki/Python "Python") può essere trovata qui.[^4]
- *[Mathematica](https://it.wikipedia.org/wiki/Mathematica "Mathematica")* ha sviluppato funzionalità [ad hoc](https://it.wikipedia.org/wiki/Ad_hoc "Ad hoc") per le catene di Markov, a partire dalla versione 9.

## Note

## Bibliografia

- (EN) Olle Häggström (2002), *Finite Markov Chains and Algorithmic Applications*, Cambridge University Press, [ISBN 0-521-81357-3](https://it.wikipedia.org/wiki/Special:BookSources/0521813573)

## Voci correlate

- [Processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico")
- [Variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale")
- [Matrice di transizione](https://it.wikipedia.org/wiki/Matrice_di_transizione "Matrice di transizione")
- [Processo di Wiener](https://it.wikipedia.org/wiki/Processo_di_Wiener "Processo di Wiener")
- [Modello di Markov nascosto](https://it.wikipedia.org/wiki/Modello_di_Markov_nascosto "Modello di Markov nascosto")
- [Algoritmo di Metropolis-Hastings](https://it.wikipedia.org/wiki/Algoritmo_di_Metropolis-Hastings "Algoritmo di Metropolis-Hastings")
- [N-gramma](https://it.wikipedia.org/wiki/N-gramma "N-gramma")
- [Teoria ergodica](https://it.wikipedia.org/wiki/Teoria_ergodica "Teoria ergodica")
- [Vacancy chain](https://it.wikipedia.org/wiki/Vacancy_chain "Vacancy chain")

## Altri progetti

Altri progetti

- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Markov_chains?uselang=it)

- contiene immagini o altri file sul **[processo markoviano](https://commons.wikimedia.org/wiki/Category:Markov_chains?uselang=it)**

## Collegamenti esterni

- (EN) [Markov chain](https://www.britannica.com/topic/Markov-chain), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Markov Chain](http://mathworld.wolfram.com/MarkovChain.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- (EN) Denis Howe, [Markov chain](https://foldoc.org/Markov%20chain "foldoc:Markov chain"), in [Free On-line Dictionary of Computing](https://it.wikipedia.org/wiki/Free_On-line_Dictionary_of_Computing "Free On-line Dictionary of Computing"). Disponibile con licenza [GFDL](https://it.wikipedia.org/wiki/GNU_Free_Documentation_License "GNU Free Documentation License")

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [19104](https://thes.bncf.firenze.sbn.it/termine.php?id=19104) · [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh85081369](http://id.loc.gov/authorities/subjects/sh85081369) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4134948-9](https://d-nb.info/gnd/4134948-9) · [BNE](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Spagna "Biblioteca nazionale di Spagna") (ES) [XX540042](https://datos.bne.es/resource/XX540042) [(data)](http://datos.bne.es/resource/XX540042) · [BNF](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Francia "Biblioteca nazionale di Francia") (FR) [cb11932425d](https://catalogue.bnf.fr/ark:/12148/cb11932425d) [(data)](https://data.bnf.fr/ark:/12148/cb11932425d) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007553386405171](https://www.nli.org.il/en/authorities/987007553386405171) |
| --- | --- |

[^1]: [Markov chain | Definition of Markov chain in US English by Oxford Dictionaries](https://web.archive.org/web/20171215001435/https://en.oxforddictionaries.com/definition/us/markov_chain), su Oxford Dictionaries | English. URL consultato il 27 novembre 2018 (archiviato dall' url originale il 15 dicembre 2017).

[^2]: Billi, R., Canavesio, F., Ciaramella, A., & Nebbia, L. (1994, September). Interactive voice technology at work: The CSELT experience. In Interactive Voice Technology for Telecommunications Applications, 1994., Second IEEE Workshop on (pp. 43-48). IEEE.

[^3]: Giorgio Alfredo Spedicato \[aut, cre e Tae Seung Kang, [markovchain: Easy Handling Discrete Time Markov Chains](https://cran.r-project.org/package=markovchain), 26 agosto 2019. URL consultato il 13 settembre 2019.

[^4]: (EN) Martin Thoma, [Python Markov Chain Packages](https://web.archive.org/web/20230324040908/https://martin-thoma.com/python-markov-chain-packages/), su Martin Thoma. URL consultato il 13 settembre 2019 (archiviato dall' url originale il 24 marzo 2023).