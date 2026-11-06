---
title: "Algebra di Borel"
source: "https://it.wikipedia.org/wiki/Algebra_di_Borel"
author:
  - "[[Wikipedia]]"
published: 2006-06-05
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica") l' **algebra di Borel**, o più propriamente la **σ-algebra di Borel**, è la più piccola [σ-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra") su un insieme dotato di [struttura topologica](https://it.wikipedia.org/wiki/Spazio_topologico "Spazio topologico") che sia compatibile con la topologia stessa, ossia che contenga tutti gli aperti della [topologia](https://it.wikipedia.org/wiki/Topologia "Topologia").

Lo [spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile") così definito prende il nome di **spazio boreliano**, gli insiemi contenuti nella σ-algebra di Borel sono detti **insiemi boreliani** o **insiemi di Borel** ed una [misura](https://it.wikipedia.org/wiki/Misura_\(matematica\) "Misura (matematica)") definita su una σ-algebra di Borel è detta **misura di Borel**.

La nozione di algebra di Borel è stata introdotta da [Émile Borel](https://it.wikipedia.org/wiki/%C3%89mile_Borel "Émile Borel") nell'ambito dei [numeri reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale"), ed in seguito generalizzata a spazi topologici arbitrari.[^1]

## Definizione

Sia $(X,T)$ uno spazio topologico. L'algebra di Borel di $X$ rispetto a $T$ è la più piccola σ-algebra $𝔉:=σ(T)$ contenente la topologia $T$, ossia contenente ogni [sottoinsieme aperto](https://it.wikipedia.org/wiki/Insieme_aperto "Insieme aperto") di $(X,T)$.[^2]

La definizione data è motivata dal fatto che, dal momento che l' [intersezione](https://it.wikipedia.org/wiki/Intersezione_\(insiemistica\) "Intersezione (insiemistica)") di una famiglia di [σ-algebre](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra") è ancora una σ-algebra, data una generica collezione di insiemi si dimostra che esiste una più piccola σ-algebra che contiene la collezione. Più precisamente, se $X$ è un insieme non vuoto e $𝔊$ una famiglia di sottoinsiemi di $X$, allora è ben definita $σ(𝔊)$, la più piccola σ-algebra su $X$ contenente $𝔊$.[^2]

Dati due spazi topologici $X$ e $Y$ e una [funzione continua](https://it.wikipedia.org/wiki/Funzione_continua "Funzione continua") $f:X→Y$, allora tale funzione è [misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") rispetto alla σ-algebra di Borel. Infatti $f^{- 1} \left(V\right)$ è contenuta nella σ-algebra di Borel per ogni insieme aperto $V$ di $Y$. Se $Y$ è l'asse reale del [piano complesso](https://it.wikipedia.org/wiki/Piano_complesso "Piano complesso"), le funzioni misurabili rispetto alla σ-algebra di Borel sono dette *funzioni di Borel*.[^3]

Ogni misura definita su una σ-algebra di Borel si dice *misura di Borel*, ed alcuni autori richiedono che $μ(K)<∞$ per ogni compatto $K$. Una misura caratterizzata da regolarità interna ed esterna si dice *regolare*, mentre se è caratterizzata da regolarità interna ed è localmente finita prende il nome di [misura di Radon](https://it.wikipedia.org/wiki/Misura_di_Radon "Misura di Radon").

### Terminologia

In alcuni casi si utilizza il termine "algebra di Borel" per indicare la σ-algebra generata dai [compatti](https://it.wikipedia.org/wiki/Insieme_compatto "Insieme compatto") della topologia $T$ di $X$. Poiché in uno [spazio di Hausdorff](https://it.wikipedia.org/wiki/Spazio_di_Hausdorff "Spazio di Hausdorff") ogni compatto è chiuso, in questo caso la σ-algebra di Borel definita in esso è *più fine* di quella generata dai compatti. Risulta che esse coincidono se lo spazio topologico di partenza è uno [spazio metrizzabile](https://it.wikipedia.org/wiki/Spazio_metrico "Spazio metrico") [separabile](https://it.wikipedia.org/wiki/Spazio_separabile "Spazio separabile") e [localmente compatto](https://it.wikipedia.org/wiki/Spazio_localmente_compatto "Spazio localmente compatto"). Questa seconda definizione di algebra di Borel si utilizza ad esempio per costruire la [misura di Haar](https://it.wikipedia.org/wiki/Misura_di_Haar "Misura di Haar").

Talvolta, "algebra di Borel" identifica anche l' [algebra di insiemi](https://it.wikipedia.org/wiki/Algebra_di_insiemi "Algebra di insiemi") generata dagli aperti di uno spazio topologico, e non la σ-algebra. Questa dicitura è tuttavia meno comune. Ad esempio, intesa con questo significato, l'algebra di Borel dei [numeri reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale"), equipaggiati con la usuale [topologia euclidea](https://it.wikipedia.org/wiki/Topologia_euclidea "Topologia euclidea"), è costituita semplicemente dalle unioni finite di intervalli.

A volte si utilizza, inoltre, il termine "spazio boreliano" come abbreviazione di spazio boreliano standard. Uno spazio boreliano è detto *standard* se lo spazio topologico $(X,T)$, che genera lo spazio boreliano stesso, è uno [spazio polacco](https://it.wikipedia.org/wiki/Spazio_polacco "Spazio polacco").

## Principali risultati

Nella [teoria delle categorie](https://it.wikipedia.org/wiki/Teoria_delle_categorie "Teoria delle categorie"), gli spazi boreliani formano una [categoria](https://it.wikipedia.org/wiki/Categoria_\(matematica\) "Categoria (matematica)") i cui morfismi sono le [funzioni misurabili](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile"). Essa è una sottocategoria della categoria degli [spazi misurabili](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile").

Due spazi boreliani $(X,𝔉)$ e $(Y,𝔊)$ sono detti [isomorfi](https://it.wikipedia.org/wiki/Isomorfismo "Isomorfismo") se esiste una funzione $f:X→Y$ [biiettiva](https://it.wikipedia.org/wiki/Funzione_biiettiva "Funzione biiettiva") tale che $f , f^{- 1}$ siano entrambe misurabili.

### Lemma di misurabilità di funzioni continue

Siano $(Ω,T)$ e $(Ψ,Υ)$ due spazi topologici, e siano $(Ω,𝔉)$ e $(Ψ,𝔊)$ i relativi spazi boreliani. Se un'applicazione $f:Ω→Ψ$ è [continua](https://it.wikipedia.org/wiki/Funzione_continua "Funzione continua") rispetto a $T$ e $Υ$ allora essa è [misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") rispetto a $𝔉$ e $𝔊$.

Questo risultato è importante, ed è utilizzato, ad esempio, per mostrare che le funzioni continue su un compatto di $\mathbb{R}^{n}$ sono [integrabili](https://it.wikipedia.org/wiki/Funzione_integrabile "Funzione integrabile") rispetto alla [misura di Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue"), o più in generale per compatti di [gruppi topologici](https://it.wikipedia.org/wiki/Gruppo_topologico "Gruppo topologico") [localmente compatti](https://it.wikipedia.org/wiki/Spazio_localmente_compatto "Spazio localmente compatto") rispetto alla [misura di Haar](https://it.wikipedia.org/wiki/Misura_di_Haar "Misura di Haar"). Ne segue anche che se due spazi topologici sono [omeomorfi](https://it.wikipedia.org/wiki/Omeomorfismo "Omeomorfismo"), allora i relativi spazi boreliani sono isomorfi.

### Teorema di Kuratowski

Sia $(X,T)$ uno [spazio polacco](https://it.wikipedia.org/wiki/Spazio_polacco "Spazio polacco"), e $𝔉$ la relativa σ-algebra di Borel. Allora lo spazio boreliano $(X,𝔉)$ è [isomorfo](https://it.wikipedia.org/wiki/Isomorfismo "Isomorfismo") ad uno dei seguenti insiemi:

- L'insieme dei numeri reali $ℝ$ equipaggiato con la usuale algebra di Borel.
- L'insieme dei [numeri interi](https://it.wikipedia.org/wiki/Numero_intero "Numero intero") equipaggiato con la σ-algebra dell'insieme delle parti, che è semplicemente la σ-algebra di Borel generata dalla topologia discreta.
- Un [insieme finito](https://it.wikipedia.org/wiki/Insieme_finito "Insieme finito") equipaggiato con la σ-algebra dell'insieme delle parti, che è semplicemente la σ-algebra di Borel generata dalla topologia discreta.

Questo teorema, importante in molti ambiti della matematica ed in particolare in [teoria descrittiva degli insiemi](https://it.wikipedia.org/wiki/Teoria_descrittiva_degli_insiemi "Teoria descrittiva degli insiemi") ed in [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità"), è dovuto al matematico [polacco](https://it.wikipedia.org/wiki/Polonia "Polonia") [Kazimierz Kuratowski](https://it.wikipedia.org/wiki/Kazimierz_Kuratowski "Kazimierz Kuratowski").

## Costruzione esplicita della σ-algebra di Borel

Nel caso in cui $(X,T)$ sia metrizzabile (ossia, nel caso in cui sia possibile considerare la topologia $T$ come indotta da una [distanza](https://it.wikipedia.org/wiki/Spazio_metrico "Spazio metrico")), si può dare una descrizione abbastanza esplicita della σ-algebra di Borel.

Data una famiglia $𝔗$ di sottoinsiemi di $X$, si definiscono:

- $\mathfrak{T}_{\sigma}$ la famiglia di sottoinsiemi di $X$ costituita da tutte le [unioni](https://it.wikipedia.org/wiki/Unione_\(insiemistica\) "Unione (insiemistica)") [numerabili](https://it.wikipedia.org/wiki/Insieme_numerabile "Insieme numerabile") di elementi di $𝔗$.
- $\mathfrak{T}_{\delta}$ la famiglia di sottoinsiemi di $X$ costituita da tutte le [intersezioni](https://it.wikipedia.org/wiki/Intersezione_\(insiemistica\) "Intersezione (insiemistica)") [numerabili](https://it.wikipedia.org/wiki/Insieme_numerabile "Insieme numerabile") di elementi di $𝔗$.

dove con la notazione $\mathfrak{T}_{\delta , \sigma}$ si intende semplicemente $\left(\right. \mathfrak{T}_{\delta} \left.\right)_{\sigma}$.

Si costruisce la σ-algebra di Borel per [induzione transfinita](https://it.wikipedia.org/wiki/Induzione_transfinita "Induzione transfinita") definendo una famiglia di insiemi $\mathfrak{G}^{i} \subset 𝟐^{X}$, parametrizzata dai [numeri ordinali](https://it.wikipedia.org/wiki/Numero_ordinale "Numero ordinale") $i$.

- Base dell'induzione: si definisce $\mathfrak{G}^{0} := T$, la topologia di $X$.
- Passo induttivo: si distinguono i due casi, quello in cui $i$ sia un [ordinale limite](https://it.wikipedia.org/wiki/Ordinale_limite "Ordinale limite"), e quello in cui non lo sia. Se $i$ *non* è un ordinale limite, allora ammette un ordinale $i−1$ che lo precede, e si pone:

$\mathfrak{G}^{i} := \mathfrak{G}_{\delta , \sigma}^{i - 1} .$

Se $i$ è un ordinale limite, allora si pone:

$\mathfrak{G}^{i} := \underset{j < i}{\cup} \mathfrak{G}^{j} .$

Con queste definizioni, la σ-algebra di Borel è data da $\mathfrak{F} = \mathfrak{G}^{\omega_{1}}$, dove $\omega_{1}$ è il primo ordinale non numerabile. Infatti, in uno spazio metrico ogni aperto è l'unione dei chiusi in esso contenuti, da cui segue facilmente che $\mathfrak{G}^{\omega_{1}}$ è una σ-algebra. La proprietà di minimalità di $\mathfrak{G}^{\omega_{1}}$ (ossia il fatto che essa sia la più piccola σ-algebra contenente gli aperti) segue invece da un'osservazione più sottile. Infatti è possibile mostrare che per ogni insieme boreliano $B$ esiste un ordinale numerabile $i$ tale che $B \in \mathfrak{G}^{i}$. Tuttavia, al variare del boreliano $B$ tale indice numerabile diviene arbitrariamente grande, ed approccia il primo ordinale non numerabile.

## Esempi

La maggior parte degli spazi misurabili che si utilizzano in [analisi matematica](https://it.wikipedia.org/wiki/Analisi_matematica "Analisi matematica") sono boreliani.

- Sia $X$ un insieme non vuoto, e siano $𝔉0={∅,X}$ la [topologia banale](https://it.wikipedia.org/wiki/Topologia_banale "Topologia banale") e $\mathfrak{F}_{\mathcal{P}} = 𝟐^{X}$ la [topologia discreta](https://it.wikipedia.org/wiki/Topologia_discreta "Topologia discreta") di $X$ (qui e nel seguito $𝟐^{X}$ indica l' [insieme delle parti](https://it.wikipedia.org/wiki/Insieme_delle_parti "Insieme delle parti") di $X$). $\mathfrak{F}_{0}$ e $\mathfrak{F}_{\mathcal{P}}$ sono anche due σ-algebre,[^4] e quindi *le* σ-algebre generate dalle medesime $\mathfrak{F}_{0}$ e $\mathfrak{F}_{\mathcal{P}}$. Ne segue che esse sono delle algebre di Borel, e $\left(X , \mathfrak{F}_{0}\right)$ e $\left(X , \mathfrak{F}_{\mathcal{P}}\right)$ sono i più semplici esempi di spazi boreliani.
- Dato un qualunque insieme non vuoto $X$, la famiglia composta da tutti i sottoinsiemi di $X$ che hanno [cardinalità](https://it.wikipedia.org/wiki/Cardinalit%C3%A0 "Cardinalità") numerabile o il cui complementare abbia cardinalità numerabile è una σ-algebra. È immediato verificare che questa σ-algebra è quella generata dalla [topologia cofinita](https://it.wikipedia.org/wiki/Topologia_cofinita "Topologia cofinita") su $X$, ed è pertanto un'algebra boreliana.
- L'algebra di Borel utilizzata più di frequente in matematica, è la σ-algebra di Borel sui numeri reali (o più in generale sugli [spazi euclidei](https://it.wikipedia.org/wiki/Spazio_euclideo "Spazio euclideo")). Questa è la più piccola σ-algebra contenente tutti gli [intervalli](https://it.wikipedia.org/wiki/Intervallo_\(matematica\) "Intervallo (matematica)") reali, ed è generalmente utilizzata per definire le [funzioni misurabili](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") e le [variabili aleatorie](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") a valori reali, la [misura di Borel](https://it.wikipedia.org/wiki/Misura_di_Borel "Misura di Borel"), ed in alcune delle possibili costruzioni della [misura di Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue"). Essa può essere costruita induttivamente seguendo il procedimento generale indicato sotto. Si può dimostrare che questa σ-algebra ha la [cardinalità del continuo](https://it.wikipedia.org/wiki/Cardinalit%C3%A0_del_continuo "Cardinalità del continuo"), e dunque solo *pochi* sottoinsiemi dei numeri reali sono boreliani. Tuttavia, tutti i sottoinsiemi di $ℝ$ che ricorrono più spesso sono boreliani, ad esempio:
	- Gli insiemi numerabili, come gli [interi](https://it.wikipedia.org/wiki/Numero_intero "Numero intero"), i [razionali](https://it.wikipedia.org/wiki/Numero_razionale "Numero razionale") o loro sottoinsiemi.
		- Gli intervalli aperti e chiusi, ma anche *semiaperti*, e le semirette aperte e chiuse. Ad esempio l'intervallo $[0,1)$ è boreliano.
		- Le [unioni](https://it.wikipedia.org/wiki/Unione_\(insiemistica\) "Unione (insiemistica)") ed [intersezioni](https://it.wikipedia.org/wiki/Intersezione_\(insiemistica\) "Intersezione (insiemistica)") di insiemi dei tipi appena descritti.
- Un esempio di σ-algebra *non boreliana*, è dato dalla [σ-algebra di Lebesgue](https://it.wikipedia.org/wiki/Sigma-algebra_di_Lebesgue "Sigma-algebra di Lebesgue"). Questa può ad esempio definirsi come il *completamento* della σ-algebra boreliana dei reali rispetto alla misura di Borel (il completamento di una σ-algebra si ottiene aggiungendo agli insiemi che la compongono gli insiemi di misura nulla).

## Note

## Bibliografia

- (EN) Walter Rudin, [Real and Complex Analysis](https://archive.org/details/realcomplexanaly0000rudi), Mladinska Knjiga, McGraw-Hill, 1970, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-07-054234-1](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-07-054234-1 "Speciale:RicercaISBN/0-07-054234-1").
- (EN) Carl B. Boyer, [History of Mathematics](https://archive.org/details/historyofmathema0000boye_y4y8), 2nd edition, New York, [John Wiley & Sons](https://it.wikipedia.org/wiki/John_Wiley_&_Sons "John Wiley & Sons"), 1989, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-471-54397-7](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-471-54397-7 "Speciale:RicercaISBN/0-471-54397-7").
- (EN) Donald L. Cohn, [Measure Theory](https://archive.org/details/measuretheory0000cohn), Boston, Birkhäuser, 1980, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-8493-7157-0](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-8493-7157-0 "Speciale:RicercaISBN/0-8493-7157-0").
- (EN) [Paul R. Halmos](https://it.wikipedia.org/wiki/Paul_Halmos "Paul Halmos"), [Measure Theory](https://archive.org/details/measuretheory00halm), New York, Springer-Verlag, 1974, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-387-90088-8](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-387-90088-8 "Speciale:RicercaISBN/0-387-90088-8").

## Voci correlate

- [Algebra di Baire](https://it.wikipedia.org/wiki/Algebra_di_Baire?action=edit&redlink=1 "Algebra di Baire (la pagina non esiste)")
- [Funzione continua](https://it.wikipedia.org/wiki/Funzione_continua "Funzione continua")
- [Funzione misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile")
- [Insieme analitico](https://it.wikipedia.org/wiki/Insieme_analitico?action=edit&redlink=1 "Insieme analitico (la pagina non esiste)")
- [Sigma-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra")
- [Spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile")

## Collegamenti esterni

- [Borel, algebra di](https://www.treccani.it/enciclopedia/algebra-di-borel_\(Enciclopedia-della-Matematica\)/), in Enciclopedia della Matematica, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2013.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Borel Sigma-Algebra](http://mathworld.wolfram.com/BorelSigma-Algebra.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- (EN) V.A. Skvortsov, [Borel set](https://www.encyclopediaofmath.org/index.php/Borel_set), in [Encyclopaedia of Mathematics](https://it.wikipedia.org/wiki/Encyclopaedia_of_Mathematics "Encyclopaedia of Mathematics"), Springer e European Mathematical Society, 2002.

[^1]: Un breve resoconto dello sviluppo storico della teoria della misura e delle sue strutture insiemistiche si trova in Boyer, *History of Mathematics*, cap. 28.

[^2]: [W. Rudin](#CITEREFrudin), Pag. 12.

[^3]: [W. Rudin](#CITEREFrudin), Pag. 13.

[^4]: Queste due σ-algebre sono dette *improprie*.