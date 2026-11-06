---
title: "Funzione di densità di probabilità"
source: "https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0"
author:
  - "[[Wikipedia]]"
published: 2004-08-17
created: 2026-11-06
description:
tags:
  - "clippings"
---
![](https://it.wikipedia.org/wiki/File:Grafico_v.c.Rettangolare.png)

Funzione di densità di probabilità di una variabile aleatoria con distribuzione uniforme

In [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica"), una **funzione di densità di probabilità** (o PDF dall'inglese *probability density function*) è l'analogo della [funzione di probabilità](https://it.wikipedia.org/wiki/Funzione_di_probabilit%C3%A0 "Funzione di probabilità") di una [variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale"), con la condizione che la variabile casuale $X$ sia [continua](https://it.wikipedia.org/wiki/Distribuzione_continua "Distribuzione continua"), cioè l'insieme dei possibili valori abbia la [potenza del continuo](https://it.wikipedia.org/wiki/Potenza_del_continuo "Potenza del continuo"). Essa descrive la "densità" di probabilità in ogni punto nello [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario").

## Definizione

La funzione di densità di probabilità di una variabile casuale $X$ è un'applicazione $p_{X} \left(x\right)$ non negativa [integrabile secondo Lebesgue](https://it.wikipedia.org/wiki/Integrale_di_Lebesgue "Integrale di Lebesgue") e [reale di variabile reale](https://it.wikipedia.org/wiki/Funzione_di_variabile_reale "Funzione di variabile reale") tale che la probabilità dell'insieme *A* sia data da

$P \left(X \in A\right) = \int_{A} p_{X} \left(x\right) d x$

per tutti i sottinsiemi *A* dello [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario"). Intuitivamente, se una distribuzione di probabilità ha densità $p_{X} \left(x\right)$, allora l' [intervallo](https://it.wikipedia.org/wiki/Intervallo_\(matematica\) "Intervallo (matematica)") $[x,x+dx]$ ha probabilità $p_{X} \left(x\right) d x$. Da ciò deriva che la funzione $p_{X} \left(x\right)$ è un'applicazione definita come

$p_{X} \left(\bar{x}\right) : \bar{x} \mapsto \underset{d x \rightarrow 0}{lim} \frac{P \left(x < \bar{x} < x + d x\right)}{d x}$

Assumendo $x \equiv \bar{x}$, ciò corrisponde al limite della probabilità che $\bar{x}$ si trovi nell'intervallo $[x,x+dx]$ per $dx$ che tende a zero. Di cui il nome di funzione di 'densità', in quanto essa rappresenta il rapporto tra una probabilità e un'ampiezza.

Per la [condizione di normalizzazione](https://it.wikipedia.org/wiki/Normalizzazione_\(matematica\) "Normalizzazione (matematica)") l'integrale su tutto lo spazio di $p_{X} \left(x\right)$ deve essere 1. Di conseguenza ogni funzione non negativa, integrabile secondo Lebesgue, con integrale su tutto lo spazio uguale a 1, è la funzione densità di probabilità di una ben definita distribuzione di probabilità. Una variabile casuale che possiede densità si dice " [variabile casuale continua](https://it.wikipedia.org/wiki/Variabile_casuale_continua "Variabile casuale continua") ".

Per le variabili casuali multivariate (o vettoriali) la trattazione formale è assolutamente identica: $\left(X_{1} , \ldots , X_{n}\right)$ si dice assolutamente continua se esiste una funzione a valori reali definita in $\mathbb{R}^{n}$, detta **densità congiunta**, tale che per ogni sottoinsieme *A* dello spazio campionario

$P \left(X \in A\right) = \int_{A} p_{X_{1} , \ldots , X_{n}} \left(x_{1} , \ldots , x_{n}\right) d x_{1} \ldots d x_{n}$

Essa conserva tutte le proprietà di una densità scalare: è una funzione non negativa a integrale unitario su tutto lo spazio. Una proprietà importante è che se $\left(X_{1} , \ldots , X_{n}\right)$ è assolutamente continua allora lo è ogni sua componente; il viceversa invece non vale. La densità di una componente, detta **densità marginale**, si ottiene con un ragionamento analogo al [teorema della probabilità assoluta](https://it.wikipedia.org/wiki/Teorema_della_probabilit%C3%A0_assoluta "Teorema della probabilità assoluta"), cioè fissando l'insieme di suoi valori di cui si vuole determinare la probabilità e lasciando libere di variare tutte le altre componenti. Infatti (nel caso bivariato per semplicità) l'evento $(X∈A)$ è l'evento $(X∈A,Y∈ℝ)$, dunque

$P \left(X \in A\right) = \int_{A \times \mathbb{R}} p_{X , Y} \left(x , y\right) d x d y = \int_{A} \left(\int_{\mathbb{R}} p_{X , Y} \left(x , y\right) d y\right) d x$

utilizzando il [teorema di Fubini](https://it.wikipedia.org/wiki/Teorema_di_Fubini "Teorema di Fubini"). La densità marginale di $X$ è data dunque da

$p_{X} \left(x\right) = \int_{\mathbb{R}} p_{X , Y} \left(x , y\right) d y$.

## Esempi

![](https://it.wikipedia.org/wiki/File:Grafico_v.c.Gaussiana.png)

Esempio di gaussiana

La funzione di densità della [variabile casuale normale](https://it.wikipedia.org/wiki/Variabile_casuale_normale "Variabile casuale normale") di [media](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") 0 e [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") 1 (detta *normale standard*), di cui a destra è riportato il grafico e l'espressione analitica della corrispondente densità nel caso generico (media $μ$ e varianza $\sigma^{2}$).

Un altro esempio può essere dato dalla densità di probabilità uniforme su un segmento (0,1). Si può verificare immediatamente che è densità di probabilità facendo l'integrale tra (0,1).

## Voci correlate

- [Funzione di ripartizione](https://it.wikipedia.org/wiki/Funzione_di_ripartizione "Funzione di ripartizione")
- [Funzione di probabilità](https://it.wikipedia.org/wiki/Funzione_di_probabilit%C3%A0 "Funzione di probabilità")
- [Funzione caratteristica (teoria della probabilità)](https://it.wikipedia.org/wiki/Funzione_caratteristica_\(teoria_della_probabilit%C3%A0\) "Funzione caratteristica (teoria della probabilità)")
- [Lemma di Scheffé](https://it.wikipedia.org/wiki/Lemma_di_Scheff%C3%A9 "Lemma di Scheffé")
- [Variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale")
- [Teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità")
- [Statistica](https://it.wikipedia.org/wiki/Statistica "Statistica")
- [Integrale](https://it.wikipedia.org/wiki/Integrale "Integrale")
- [Percentile](https://it.wikipedia.org/wiki/Percentile "Percentile")
- [Quantile](https://it.wikipedia.org/wiki/Quantile "Quantile")

## Collegamenti esterni

- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Probability Density Function](http://mathworld.wolfram.com/ProbabilityDensityFunction.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- (EN) [IUPAC Gold Book, "probability density"](http://goldbook.iupac.org/P04856.html), su goldbook.iupac.org.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4139581-5](https://d-nb.info/gnd/4139581-5) |
| --- | --- |