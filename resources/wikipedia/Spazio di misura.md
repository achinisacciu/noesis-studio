---
title: "Spazio di misura"
source: "https://it.wikipedia.org/wiki/Spazio_di_misura#Spazio_di_probabilit%C3%A0"
author:
  - "[[Wikipedia]]"
published: 2006-05-09
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [analisi matematica](https://it.wikipedia.org/wiki/Analisi_matematica "Analisi matematica") uno **spazio di misura** (o **spazio mensurale**, o **spazio di Lebesgue**) è una struttura astratta utilizzata per formalizzare il concetto di [misura](https://it.wikipedia.org/wiki/Misura_\(matematica\) "Misura (matematica)"), come generalizzazione delle idee elementari di lunghezza di una curva o area di una superficie [^1].

## Definizione

Si definisce spazio di misura uno [spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile") $(X,𝔉)$ dotato di una [misura](https://it.wikipedia.org/wiki/Misura_\(matematica\) "Misura (matematica)") $μ$ positiva definita sulla [σ-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra") $𝔉$ costituita da sottoinsiemi misurabili di $X$.[^2] Un tale spazio si rappresenta con una terna $(X,𝔉,μ)$.

Quando lo spazio misurabile $(X,𝔉)$ è uno [spazio boreliano](https://it.wikipedia.org/wiki/Spazio_boreliano "Spazio boreliano"), talvolta lo spazio di misura $(X,𝔉,μ)$ è detto *spazio di misura boreliano*. Dato uno spazio di misura $(X,𝔉,μ)$, in genere si denota con $|μ|$ la [variazione totale](https://it.wikipedia.org/wiki/Misura_complessa#Variazione_totale "Misura complessa") di $μ$ su $(X,𝔉)$.

Se $|μ|(X)<∞$ lo spazio di misura si dice *finito*. Se inoltre $X$ può scriversi come [unione](https://it.wikipedia.org/wiki/Unione_\(insiemistica\) "Unione (insiemistica)") [numerabile](https://it.wikipedia.org/wiki/Insieme_numerabile "Insieme numerabile") di insiemi:

$X = \underset{i \in \mathbb{N}}{\cup} X_{i}$

di misura finita, cioè tali che $\left|\mu\right| \left(X_{i}\right) < \infty$, allora lo spazio misurabile si dice *σ-finito*.

## Spazio di probabilità

Uno **spazio di probabilità** $(Ω,ℱ,P)$ è uno spazio di misura tale che $P(E)≥0$ per ogni $E∈ℱ$ e $P(Ω)=1$. In questo contesto $P$ è detta [misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità"). Dalla definizione stessa, segue che uno spazio di probabilità è sempre uno spazio di misura finita.

La struttura di spazio di probabilità è stata introdotta da [Andrey Nikolaevich Kolmogorov](https://it.wikipedia.org/wiki/Andrey_Nikolaevich_Kolmogorov "Andrey Nikolaevich Kolmogorov") negli [anni trenta](https://it.wikipedia.org/wiki/Anni_1930 "Anni 1930"), nell'ambito di una serie di lavori del matematico russo che hanno posto i fondamenti dell'intera [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità").

## Completamento di uno spazio di misura

Uno spazio di misura si dice **completo** se ogni insieme contenuto in un [insieme nullo](https://it.wikipedia.org/wiki/Insieme_nullo_\(teoria_della_misura\) "Insieme nullo (teoria della misura)") è misurabile (avendo ovviamente in questo caso misura nulla). In generale, da un punto di vista pratico, è conveniente utilizzare spazi completi.[^3] Tuttavia, dato uno spazio di misura non completo, è sempre possibile estenderlo ad uno [spazio completo](https://it.wikipedia.org/wiki/Spazio_metrico_completo "Spazio metrico completo") nel seguente senso.

Sia $(X,𝔉,μ)$ uno spazio di misura. Esiste un unico spazio di misura completo $\left(X , \mathfrak{F}^{'} , \mu^{'}\right)$, detto **completamento** di $(X,𝔉,μ)$, sullo stesso insieme $X$ con le seguenti proprietà:

1. la σ-algebra $\mathfrak{F}^{'}$ è più fine (cioè contiene) $𝔉$.
2. la misura $\mu^{'}$ ristretta ad $𝔉$ coincide con $μ$, ossia per ogni [sottoinsieme misurabile](https://it.wikipedia.org/wiki/Insieme_misurabile "Insieme misurabile") di $X$ $E∈𝔉$ accade $\mu \left(E\right) = \mu^{'} \left(E\right)$.
3. se $(X,𝔊,ν)$ è un altro spazio con tale proprietà, allora $𝔊$ è più fine di $\mathfrak{F}^{'}$ (o equivalentemente, $\mathfrak{F}^{'}$ è la meno fine tra tutte le σ-algebre su cui sia possibile effettuare tale costruzione).

Evidentemente, se $(X,𝔉,μ)$ è completo, esso coincide col suo completamento. In generale è possibile costruire in maniera esplicita il completamento di uno spazio non completo. Ne illustriamo qui la procedura.

Consideriamo l'insieme $𝔑$ di tutti gli insiemi contenuti in insiemi nulli (tali insiemi sono talvolta detti [trascurabili](https://it.wikipedia.org/wiki/Insieme_trascurabile "Insieme trascurabile")). Sia $\mathfrak{F}^{'} = \sigma \left(\mathfrak{N} \cup \mathfrak{F}\right)$ la più piccola σ-algebra contenente sia gli elementi di $𝔉$ che quelli di $𝔑$ [^4]. Poiché l'unione e l'intersezione numerabili di insiemi trascurabili è trascurabile, si vede facilmente che ogni elemento $E^{'}$ di $\mathfrak{F}^{'}$ può essere ottenuto da un elemento $E$ di $𝔉$ unendovi o sottraendovi un insieme trascurabile. Sarà allora sufficiente estendere $μ$ ad una nuova misura su $\left(X , \mathfrak{F}^{'}\right)$ semplicemente ponendo $\mu^{'} \left(E^{'}\right) := \mu \left(E\right)$.

Un caso notevole, è quello dello spazio di misura di Lebesgue (il secondo esempio sopra), che è il completamento dello spazio di Borel (il primo esempio sopra).

## La categoria degli spazi di misura

L'insieme degli spazi di misura forma una [categoria](https://it.wikipedia.org/wiki/Teoria_delle_categorie_\(matematica\) "Teoria delle categorie (matematica)"), dove i [morfismi](https://it.wikipedia.org/wiki/Morfismo "Morfismo") sono dati dalle [funzioni misurabili](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") che *conservano* la misura. Più precisamente, dati due spazi di misura $(X,𝔉,μ)$, $(Y,𝔊,ν)$ un morfismo è naturalmente associato ad una [funzione](https://it.wikipedia.org/wiki/Funzione_\(matematica\) "Funzione (matematica)") $f:X↦Y$ tale che:

- $f$ sia $(𝔉,𝔊)$ -misurabile [^5].
- Per ogni insieme $F∈𝔊$ accade $\mu \left(f^{- 1} \left(F\right)\right) = \nu \left(F\right)$.

In particolare, i due spazi di misura si diranno [isomorfi](https://it.wikipedia.org/wiki/Isomorfismo "Isomorfismo") se esiste una [funzione biiettiva](https://it.wikipedia.org/wiki/Funzione_biiettiva "Funzione biiettiva") $f:X↦Y$ misurabile e con inversa misurabile, tale che per ogni $E∈𝔉$ accada $μ(E)=ν(f(E))$.

Dato uno spazio misurabile $(X,𝔉)$, e due misure $μ,ν$ su di esso, $ν$ si dice **[assolutamente continua](https://it.wikipedia.org/wiki/Misura_assolutamente_continua "Misura assolutamente continua")** rispetto a $μ$ se ogni insieme $E∈𝔉$ che ha [misura nulla](https://it.wikipedia.org/wiki/Insieme_di_misura_nulla "Insieme di misura nulla") rispetto a $μ$ ha misura nulla anche rispetto a $ν$: $μ(E)=0⇒ν(E)=0$ Due misure assolutamente continue l'una rispetto all'altra si dicono **[equivalenti](https://it.wikipedia.org/wiki/Misure_equivalenti?action=edit&redlink=1 "Misure equivalenti (la pagina non esiste)")**.

### Isomorfismi di spazi misurabili

Dal [teorema di Radon-Nikodym](https://it.wikipedia.org/wiki/Teorema_di_Radon-Nikodym "Teorema di Radon-Nikodym") si può allora dedurre la seguente preposizione: siano $(X,𝔉,μ)$ e $(X,𝔉,ν)$ due spazi di misura σ-finiti costruiti sopra il medesimo spazio misurabile $(X,𝔉)$. Se $μ,ν$ sono equivalenti, allora i due spazi sono isomorfi.

## Applicazioni

- Naturalmente, l'applicazione più naturale della nozione di spazio di misura si ha proprio nella teoria della misura, in quanto essa costituisce un oggetto fondamentale di tale teoria.
- Se $(X,𝔉)$ è uno spazio misurabile ed $S$ un [semigruppo](https://it.wikipedia.org/wiki/Semigruppo "Semigruppo"), un'azione misurabile di $S$ su $X$ è una famiglia (indicizzata dal parametro $s∈S$) di mappe misurabili $T_{s} : X \mapsto X$ tali che $T_{s} \circ T_{t} = T_{s t}$ per ogni $s,t∈S$. Un [sistema dinamico conservativo](https://it.wikipedia.org/wiki/Sistema_dinamico_conservativo "Sistema dinamico conservativo") è una quadrupla $(X,𝔉,μ,S)$, dove $(X,𝔉,μ)$ è uno spazio di misura, e $T$ è un'azione misurabile di un semigruppo $S$ su $X$, che *conserva* la misura: $\mu \left(T_{s}^{- 1} \left(E\right)\right) = \mu \left(E\right)$ per ogni $E∈𝔉,s∈S$. La [teoria dei sistemi](https://it.wikipedia.org/wiki/Teoria_dei_sistemi "Teoria dei sistemi") dinamici conservativi è -nonostante la sua generalità- molto ricca. Da essa si possono ad esempio derivare con semplicità e generalità molte delle proprietà della [meccanica classica](https://it.wikipedia.org/wiki/Meccanica_classica "Meccanica classica"). Infatti, i [sistemi hamiltoniani](https://it.wikipedia.org/wiki/Meccanica_hamiltoniana "Meccanica hamiltoniana") rientrano nella classe dei [sistemi dinamici](https://it.wikipedia.org/wiki/Sistema_dinamico "Sistema dinamico") conservativi.

## Esempi

- La terna $(ℝ,𝔅,μ)$, dove $ℝ$ è la retta reale, $𝔅$ è la relativa [σ-algebra boreliana](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel"), e $μ$ è la [misura di Borel](https://it.wikipedia.org/wiki/Misura_di_Borel "Misura di Borel") è uno spazio di misura boreliano. Questo non è uno spazio finito, in quanto la misura (in questo caso *lunghezza*) dell'intera retta reale è infinita. Tuttavia tale spazio è σ-finito, in quanto ogni [intervallo](https://it.wikipedia.org/wiki/Intervallo_\(matematica\) "Intervallo (matematica)") del tipo $[n,n+1]$ ha misura $1$, ed $\mathbb{R} = \underset{n}{\cup} \left[n , n + 1\right]$.
- La terna $(ℝ,𝔏,λ)$, dove $𝔏$ è la [σ-algebra di Lebesgue](https://it.wikipedia.org/wiki/Sigma-algebra_di_Lebesgue "Sigma-algebra di Lebesgue"), e $λ$ è la [misura di Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue") è uno spazio di misura non boreliano. Questo spazio di misura è pure σ-finito, per la stessa motivazione data sopra.
- Lo spazio discreto $Ω={1,…,n}$, con la convenzione che ogni sottoinsieme di $Ω$ è misurabile e la misura di un sottoinsieme è data da $\mathbb{P} \left(A\right) = \frac{\left|A\right|}{n}$, è uno spazio di probabilià.
- Se $Ω$ è uno spazio di misura finita, allora si può ottenere uno spazio di probabilità introducendo la misura $\mathbb{P} \left(A\right) = \frac{\mu \left(A\right)}{\mu \left(\Omega\right)}$.

## Note

## Bibliografia

- Walter Rudin, [Real and Complex Analysis](https://archive.org/details/realcomplexanaly0000rudi), Mladinska Knjiga, McGraw-Hill, 1970, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-07-054234-1](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-07-054234-1 "Speciale:RicercaISBN/0-07-054234-1").
- Carl B. Boyer, [History of Mathematics](https://archive.org/details/historyofmathema0000boye_y4y8), 2nd edition, New York, [John Wiley & Sons](https://it.wikipedia.org/wiki/John_Wiley_&_Sons "John Wiley & Sons"), 1989, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-471-54397-7](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-471-54397-7 "Speciale:RicercaISBN/0-471-54397-7").
- Donald L. Cohn, [Measure Theory](https://archive.org/details/measuretheory0000cohn), Boston, Birkhäuser, 1980, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-8493-7157-0](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-8493-7157-0 "Speciale:RicercaISBN/0-8493-7157-0").
- [Paul R. Halmos](https://it.wikipedia.org/wiki/Paul_Halmos "Paul Halmos"), [Measure Theory](https://archive.org/details/measuretheory00halm), New York, Springer-Verlag, 1974, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-387-90088-8](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-387-90088-8 "Speciale:RicercaISBN/0-387-90088-8").

## Voci correlate

- [Algebra di Borel](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel")
- [Algebra di Baire](https://it.wikipedia.org/wiki/Algebra_di_Baire?action=edit&redlink=1 "Algebra di Baire (la pagina non esiste)")
- [Funzione misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile")
- [Insieme misurabile](https://it.wikipedia.org/wiki/Insieme_misurabile "Insieme misurabile")
- [Sigma-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra")
- [Spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile")
- [Teoria della misura](https://it.wikipedia.org/wiki/Teoria_della_misura "Teoria della misura")
- [Teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità")

## Collegamenti esterni

- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Measure Space](http://mathworld.wolfram.com/MeasureSpace.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- (EN) [Spazio di misura](https://encyclopediaofmath.org/wiki/Measure_space), su [Encyclopaedia of Mathematics](https://it.wikipedia.org/wiki/Encyclopaedia_of_Mathematics "Encyclopaedia of Mathematics"), Springer e European Mathematical Society.

[^1]: Rimandiamo alla voce *[teoria della misura](https://it.wikipedia.org/wiki/Teoria_della_misura "Teoria della misura")* per un'introduzione storica e qualitativa alle nozioni della teoria della misura. Un'introduzione storica si trova anche in Boyer, *History of Mathematics*.

[^2]: [W. Rudin](#CITEREFrudin), Pag. 16.

[^3]: Uno dei vantaggi di lavorare con spazi completi è il seguente: gli insiemi di misura nulla, in un certo senso, contano poco. Molte interessanti proprietà matematiche relative a spazi di misura sono verificate *[quasi ovunque](https://it.wikipedia.org/wiki/Quasi_ovunque "Quasi ovunque")* (ossia, a meno di un insieme di misura nulla). Se vogliamo dimostrare che una data proprietà è valida *quasi ovunque*, in uno spazio completo sarà sufficiente dimostrare che essa è valida *almeno* per tutti i punti al di fuori di un qualunque insieme di misura nulla. Invece, per uno spazio non completo, dovremo dimostrare che l'insieme di punti per cui essa non è valida, è misurabile ed ha misura nulla (questa seconda asserzione è in generale più difficile da mostrare).

[^4]: Si veda la sezione [Principali risultati](https://it.wikipedia.org/wiki/Sigma-algebra#Principali_risultati "Sigma-algebra") della voce *σ-algebra* per approfondire la nozione di σ-algebra generata da una famiglia di insiemi.

[^5]: Si veda la voce [funzione misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") per eventuali chiarimenti su questa notazione.