---
title: "Funzione di probabilità"
source: "https://it.wikipedia.org/wiki/Funzione_di_probabilit%C3%A0"
author:
  - "[[Wikipedia]]"
published: 2006-10-27
created: 2026-11-06
description:
tags:
  - "clippings"
---
![](https://thumb.wikimedia.org/wikipedia/commons/thumb/8/85/Discrete_probability_distrib.svg/250px-Discrete_probability_distrib.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Grafico di una funzione di probabilità. Ciascun valore della funzione deve essere positivo e gli elementi del codominio devono sommare a 1.

In [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità"), una **funzione di probabilità** (talvolta chiamata **funzione di massa di probabilità** o **densità discreta**) è una [funzione di variabile reale](https://it.wikipedia.org/wiki/Funzione_di_variabile_reale "Funzione di variabile reale") che rappresenta la probabilità che una [variabile casuale discreta](https://it.wikipedia.org/wiki/Variabile_casuale_discreta "Variabile casuale discreta") assuma esattamente un determinato valore.

Nel caso in cui la variabile casuale sia [continua](https://it.wikipedia.org/wiki/Variabile_casuale_continua "Variabile casuale continua"), cioè l'insieme dei possibili valori ha la [potenza del continuo](https://it.wikipedia.org/wiki/Potenza_del_continuo "Potenza del continuo"), allora tale probabilità è sempre nulla. Nel caso continuo si utilizza pertanto la [funzione di ripartizione](https://it.wikipedia.org/wiki/Funzione_di_ripartizione "Funzione di ripartizione") e la sua derivata, la [funzione di densità di probabilità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità").

La funzione di massa di probabilità è spesso lo strumento principale per definire una [distribuzione di probabilità discreta](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") e tali funzioni esistono per variabili casuali sia scalari sia multivariate il cui dominio è discreto.

Una funzione di massa di probabilità differisce da una [funzione di densità di probabilità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità") continua in quanto quest'ultima è associata a variabili casuali continue anziché discrete. Una funzione di densità di probabilità continua deve essere [integrata](https://it.wikipedia.org/wiki/Integrale "Integrale") su un intervallo per ottenere una probabilità.

Il valore della variabile casuale che possiede la massa di probabilità maggiore è chiamato [moda](https://it.wikipedia.org/wiki/Moda_\(statistica\) "Moda (statistica)").

## Definizione

Data una variabile casuale discreta $X:S→ℝ$, la funzione di probabilità è la funzione

$pX(x)=P(X=x)=P({s∈S:X(s)=x})$

che associa ad ogni valore $x$ assunto dalla variabile casuale $X$ la probabilità che la variabile $X$ assuma esattamente quel valore. Inoltre, deve essere soddisfatta la seguente equazione:

$\sum_{i = 1}^{\infty} p_{X} \left(x_{i}\right) = 1.$

Per estendere tale definizione a tutta la [retta reale](https://it.wikipedia.org/wiki/Numero_reale "Numero reale"), si assume che per ogni valore $x$ che $X$ non può assumere (cioè non contenuto nel supporto di $X$) essa vale 0, cioè:

$pX:ℝ⟶[0,1],pX(x)={P(X=x),x∈S,0,x∈ℝ∖S.$

Dato che $S$, il supporto di $X$, è un [insieme numerabile](https://it.wikipedia.org/wiki/Insieme_numerabile "Insieme numerabile"), la $p_{X} \left(x\right)$ è una funzione nulla [quasi ovunque](https://it.wikipedia.org/wiki/Quasi_ovunque "Quasi ovunque").

Nel caso di variabili multivariate discrete (cioè con supporto un sottoinsieme discreto di $\mathbb{R}^{n}$) $X = \left(X_{1} , X_{2} , \ldots , X_{n}\right)$, la *funzione di probabilità congiunta* è definita come segue:

$p_{X} \left(x_{1} , x_{2} , \ldots , x_{n}\right) = P \left(\left(X_{1} = x_{1}\right) \cap \left(X_{2} = x_{2}\right) \cap \ldots \cap \left(X_{n} = x_{n}\right)\right) .$

Il secondo membro spesso, per comodità di notazione, si scrive più semplicemente $P \left(X_{1} = x_{1} , X_{2} = x_{2} , \ldots , X_{n} = x_{n}\right) .$

La *funzione di probabilità marginale* della $i$ -esima componente si ricava grazie al [teorema della probabilità assoluta](https://it.wikipedia.org/wiki/Teorema_della_probabilit%C3%A0_assoluta "Teorema della probabilità assoluta"). Sia $n=2$ per semplicità; allora da $(X=t)=(X=t)∩Ω$ ne deriva

$p_{X} \left(t\right) = P \left(X = t , Y \in \mathbb{R}\right) = \underset{y \in R_{Y}}{\sum} P \left(X = t , Y = y\right) .$

## Relazioni con la funzione di ripartizione

Se indichiamo con $F_{X}$ la [funzione di ripartizione](https://it.wikipedia.org/wiki/Funzione_di_ripartizione "Funzione di ripartizione") di $X$, allora

- $p_{X} \left(x\right) = F_{X} \left(x\right) - F_{X} \left(x^{-}\right)$, dove con $F_{X} \left(x^{-}\right)$ si indica il [limite sinistro](https://it.wikipedia.org/wiki/Limite_di_una_funzione#Limite_destro,_sinistro,_per_eccesso,_per_difetto "Limite di una funzione") della $F_{X}$ in $x.$

Da ciò si deduce che, se $X$ è una [variabile casuale continua](https://it.wikipedia.org/wiki/Variabile_casuale_continua "Variabile casuale continua"), tale valore è nullo in ogni punto, poiché la sua funzione di ripartizione è continua. Dunque ha senso definire tale funzione solo per variabili aleatorie discrete.

- $F_{X} \left(x\right) = \underset{\xi \leq x}{\sum} p_{X} \left(\xi\right) .$

## Un caso molto particolare di densità

La funzione di probabilità può essere pensata come una densità, cioè in termini [integrali](https://it.wikipedia.org/wiki/Integrale "Integrale"), grazie all'approccio assiomatico di [Kolmogorov](https://it.wikipedia.org/wiki/Kolmogorov "Kolmogorov") che si basa sulla [teoria della misura](https://it.wikipedia.org/wiki/Teoria_della_misura "Teoria della misura"): se si pensa infatti di munire lo [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario") $ℝ$ della [misura del conteggio](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0#La_misura_del_conteggio "Misura di probabilità") (*counting measure* in [inglese](https://it.wikipedia.org/wiki/Lingua_inglese "Lingua inglese")) $c$ risulta:

$P(X∈A)=∑x∈ApX(x)=∑x∈ApX(x)⋅1=∑x∈ApX(x)⋅c({x})=∫⋃x∈A{x}p(x)dc=∫Ap(x)dc,$

cioè la funzione di probabilità risulta essere una densità rispetto alla misura del conteggio, diversa da quella di [Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue").

Questa osservazione permette innanzitutto di unificare, quando conveniente, le due grandi classi di variabili discrete e continue in un'unica trattazione in termini di densità (per una opportuna misura) e poi evita di far nascere problemi di natura teorica quando si vanno a considerare variabili casuali vettoriali del tipo $(X,Y)$, dove una delle due è discreta e l'altra è continua: basta fornire lo spazio campionario [prodotto](https://it.wikipedia.org/wiki/Prodotto_cartesiano "Prodotto cartesiano") della misura $c×μ$ (nel caso $X$ discreta), dove $μ$ sarà l'usuale misura di Lebesgue.

## Collegamenti esterni

- (EN) [probability mass function](https://www.britannica.com/topic/probability-mass-function) / [mass function](https://www.britannica.com/topic/mass-function), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4514608-1](https://d-nb.info/gnd/4514608-1) |
| --- | --- |