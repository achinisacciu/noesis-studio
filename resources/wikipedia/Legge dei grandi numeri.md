---
title: "Legge dei grandi numeri"
source: "https://it.wikipedia.org/wiki/Legge_dei_grandi_numeri"
author:
  - "[[Wikipedia]]"
published: 2003-04-18
created: 2026-11-06
description:
tags:
  - "clippings"
---
![Legge dei grandi numeri](https://thumb.wikimedia.org/wikipedia/commons/thumb/c/c9/Lawoflargenumbers.svg/250px-Lawoflargenumbers.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Legge dei grandi numeri

La **legge dei grandi numeri**, detta anche **teorema di Bernoulli** (in quanto la sua prima formulazione è dovuta a [Jakob Bernoulli](https://it.wikipedia.org/wiki/Jakob_Bernoulli "Jakob Bernoulli")), descrive il comportamento della media di una sequenza di $n$ prove di una [variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale"), indipendenti e caratterizzate dalla stessa [distribuzione di probabilità](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0 "Distribuzione di probabilità") ($n$ misure della stessa grandezza, $n$ lanci della stessa moneta, ecc.), al tendere a infinito della numerosità $n$ della sequenza stessa.

Secondo la legge dei grandi numeri è ragionevolmente sicuro che la media, che determiniamo a partire da un numero sufficiente di campioni, sia sufficientemente vicina alla media vera, ovvero quella calcolabile teoricamente. Che cosa significhi "ragionevolmente sicuri" dipende da quanto vogliamo essere precisi nel nostro test: con dieci prove, avremmo una stima grossolana, con cento, ne otterremmo una molto più precisa, con mille, ancora di più, e così via: il valore di $n$ che siamo disposti ad accettare come sufficiente dipende dal grado di casualità che riteniamo necessario per il dato in questione.

In termini generici, per la legge dei grandi numeri si può dire che:

- la media della sequenza è un'approssimazione, che migliora al crescere di $n,$ della media della distribuzione;
- viceversa, si può prevedere che sequenze siffatte mostreranno una media tanto più spesso e tanto più precisamente prossima alla media della distribuzione quanto più grande sarà $n$.

Un caso particolare di applicazione della legge dei grandi numeri è la previsione probabilistica della proporzione di successi in una successione di $n$ realizzazioni indipendenti di un evento $E,$ ossia la frequenza di $E$ nelle $n$ misurazioni: per $n$ che tende a infinito, la proporzione di successi converge alla probabilità di $E$.

Unita a questa si ha un'altra nozione interessante, ossia la legge dei piccoli numeri, che va al di là del concetto di equiprobabilità e considera la dimensione del campione rispetto ai possibili eventi e conseguenti esiti. In particolare, a seguito di esperimenti ripetuti considerando un campione più piccolo, è molto più semplice allontanarsi dal [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso"), banalmente perché avendo meno valori da considerare vi è più probabilità che essa si approssimi a un certo valore, sottostimando il numero di campioni per stime accurate. Essa fu teorizzata da Kahneman.[^1]

## Legge forte dei grandi numeri

Se, data una successione di variabili casuali $X_{1} , X_{2} , \ldots , X_{n} , \ldots$ indipendenti e identicamente distribuite con media (finita) $μ$, si considera la [media campionaria](https://it.wikipedia.org/wiki/Media_campionaria "Media campionaria")

$\left(\bar{X}\right)_{n} = \frac{X_{1} + X_{2} + \hdots + X_{n}}{n}$

la legge (forte) dei grandi numeri afferma che

$P \left(\underset{n \rightarrow \infty}{lim} \left(\bar{X}\right)_{n} = \mu\right) = 1 ,$

ossia lo [stimatore](https://it.wikipedia.org/wiki/Stimatore "Stimatore") media campionaria [converge](https://it.wikipedia.org/wiki/Convergenza_di_variabili_casuali "Convergenza di variabili casuali") [quasi certamente](https://it.wikipedia.org/wiki/Quasi_certamente "Quasi certamente") al valore atteso comune delle $X_{i}$.

## Legge debole dei grandi numeri

Se, data una successione di variabili casuali $X_{1} , X_{2} , \ldots , X_{n} , \ldots$ aventi la stessa media $μ$, la stessa varianza finita e indipendenti, si considera la [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") campionaria

$\left(\bar{X}\right)_{n} = \frac{X_{1} + X_{2} + \hdots + X_{n}}{n}$

la legge (debole) dei grandi numeri afferma che per ogni $ε>0$:

$\underset{n \rightarrow \infty}{lim} P \left(\left|\left(\bar{X}\right)_{n} - \mu\right| < \epsilon\right) = 1.$

ossia la media campionaria [converge in probabilità](https://it.wikipedia.org/wiki/Convergenza_di_variabili_casuali "Convergenza di variabili casuali") al valore atteso comune alle $X_{i}$.

## Con maggior rigore

Sia ${(Ωi,𝒜i,Pi)}i∈ℕ$ una [successione](https://it.wikipedia.org/wiki/Successione_\(matematica\) "Successione (matematica)") di spazi di [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità"). Si consideri lo spazio prodotto $(Ω,𝒜,P⁡)$ e in esso una successione [bernoulliana](https://it.wikipedia.org/wiki/Variabile_casuale_bernoulliana "Variabile casuale bernoulliana") di eventi ([stocasticamente indipendenti](https://it.wikipedia.org/wiki/Indipendenza_stocastica "Indipendenza stocastica") e con probabilità costante $p$) ${Ek}k∈ℕ⊆𝒜$. Assegnato un elemento $ω∈Ω$ si definisce la frequenza di successo in $n$ prove $\phi_{n} \left(\omega\right) = \frac{N_{n}}{n}$, dove $\phi_{n} : \Omega \rightarrow \mathbb{R}$ e $Nn=#{i:ω∈Ei}i=1n$ indica il numero di successi ottenuti in $n$ prove.

### Dimostrazione della legge debole dei grandi numeri

Nelle condizioni sopra enunciate, si vuole dimostrare che:

$∀ε∈ℝ0+,limn→∞P⁡{ω∈Ω:|ϕn(ω)−p|>ε}=0$.

Fissato $ε$, si consideri la [disuguaglianza di Bienaymé-Čebyšëv](https://it.wikipedia.org/wiki/Disuguaglianza_di_%C4%8Ceby%C5%A1%C3%ABv "Disuguaglianza di Čebyšëv"):

$P⁡{ω∈Ω:|ϕn(ω)−E⁡(ϕn)|>ε}≤var⁡(ϕn)ε2$;

poiché $N_{n}$ è distribuito in modo [binomiale](https://it.wikipedia.org/wiki/Distribuzione_binomiale "Distribuzione binomiale"), il suo [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") è

$E \left(N_{n}\right) = n p ,$

e la sua [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") è

$var \left(N_{n}\right) = n p \left(1 - p\right) ;$

abbiamo allora che il valore atteso e la varianza di $\phi_{n}$ sono, rispettivamente:

$E \left(\phi_{n}\right) = E \left(\frac{N_{n}}{n}\right) = \frac{E \left(N_{n}\right)}{n} = p ,$

$var \left(\phi_{n}\right) = var \left(\frac{N_{n}}{n}\right) = \frac{var \left(N_{n}\right)}{n^{2}} = \frac{p \left(1 - p\right)}{n} .$

Sostituendo nella disuguaglianza, si ottiene:

$P⁡{ω∈Ω:|ϕn(ω)−p|>ε}≤p(1−p)nε2,$

e, passando al limite per $n→+∞$,

$limn→∞P⁡{ω∈Ω:|ϕn(ω)−p|>ε}≤0.$

Ma la [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") non può essere negativa:

$P⁡:𝒜→[0,1],$

da cui la tesi.

#### Osservazioni

La legge debole dei grandi numeri non assicura che, comunque scelto $ε>0$, [quasi certamente](https://it.wikipedia.org/wiki/Quasi_certamente "Quasi certamente") a partire da un certo $n_{\epsilon}$ il valore $\left|\phi_{n} - p\right|$ si mantenga minore o uguale a $ε$, ossia che l'insieme

${ω∈Ω:∃nε:∀n>nε,|ϕn(ω)−p|>ε}$

sia $P$ -trascurabile. Infatti, esplicitando la definizione di limite, si trova:

$∀ε>0,∀η>0,∃nε,η:∀n≥nε,η,P⁡{ω∈Ω:|ϕn(ω)−p|>ε}≤η,$

ma niente sembra assicurare che $n_{\epsilon , \eta}$ non diverga per $η→0$.

### Dimostrazione della legge forte dei grandi numeri

Ciò è invece assicurato, nelle medesime condizioni, dalla proposizione:

$P⁡{ω∈Ω:limn→∞ϕn(ω)=p}=1,$

che, in effetti, implica sia

$∀ε∈ℝ0+,P⁡{ω∈Ω:∃nε:∀n>nε,|ϕn(ω)−p|>ε}=0$

sia la legge debole dei grandi numeri.

Dimostrazione delle due implicazioni

La legge forte può essere formulata, esplicitando la definizione di limite e passando al complementare, come:

$P⁡{ω∈Ω:∃ε∈ℝ0+:∀nε∈ℕ,∃n>nε:|ϕn(ω)−p|>ε}=0$

che a sua volta è equivalente, trasformando il [quantificatore](https://it.wikipedia.org/wiki/Quantificatore "Quantificatore") esistenziale in un'unione, a:

$P⁡(⋃ε∈ℝ0+{ω∈Ω:∀nε∈ℕ,∃n>nε:|ϕn(ω)−p|>ε})=0$

e per monotonia di $P$

$∀ε∈ℝ0+,P⁡{ω∈Ω:∃nε∈ℕ:∀n>nε,|ϕn(ω)−p|>ε}≤$

$≤P⁡(⋃ε∈ℝ0+{ω∈Ω:∀nε∈ℕ,∃n>nε:|ϕn(ω)−p|>ε})$

da cui, per confronto, la prima implicazione. Trasformando anche gli altri due quantificatori in operazioni insiemistiche, si ha:

$0=P⁡{ω∈Ω:∃nε∈ℕ:∀n>nε,|ϕn(ω)−p|>ε}=$

$=P⁡(⋂nε∈ℕ⋃n>nε{ω∈Ω:|ϕn(ω)−p|>ε})=$

ma, si è in presenza dell'intersezione di una successione non crescente di insiemi, dunque per monotonia di $P$, si ha:

$=limnε→∞P⁡(⋃n>nε{ω∈Ω:|ϕn(ω)−p|>ε})≥$

e ancora:

$≥limn→∞{ω∈Ω:|ϕn(ω)−p|>ε}$

da cui anche la seconda implicazione, ricordando che questo è valido per ogni $ε$.

Dimostrazione della legge forte

Si è già visto che l'asserto è equivalente a:

$P⁡(⋃ε∈ℝ0+{ω∈Ω:∀nε∈ℕ,∃n>nε:|ϕn(ω)−p|>ε})=0$

Discretizzando, come consueto nel caso dei limiti, si ha:

$P⁡(⋃k∈ℕ0{ω∈Ω:∀nk∈ℕ,∃n>nk:|ϕn(ω)−p|>1k})=0$

Per [subadditività](https://it.wikipedia.org/wiki/Subadditivit%C3%A0 "Subadditività")

$P⁡(⋃k∈ℕ0{ω∈Ω:∀nk∈ℕ,∃n>nk:|ϕn(ω)−p|>1k})≤$

$≤∑k∈ℕ0P⁡{ω∈Ω:∀nk∈ℕ,∃n>nε:|ϕn(ω)−p|>1k}$

Dunque, se quest'ultima espressione sarà nulla, si sarà dimostrata la legge forte. Essendo $P$ non negativa, si dovrà avere:

$∀k∈ℕ0,P⁡(lim supn→∞{ω∈Ω:|ϕn(ω)−p|>1k})=0$

si vuole mostrare che questo è vero considerando la [sottosuccessione](https://it.wikipedia.org/wiki/Sottosuccessione "Sottosuccessione") $\phi_{n^{2}}$. Si vuole applicare il [lemma di Borel-Cantelli](https://it.wikipedia.org/wiki/Lemma_di_Borel-Cantelli "Lemma di Borel-Cantelli"), pertanto si verifica che converga l'espressione

$∑n=1∞P⁡{ω∈Ω:|ϕn2(ω)−p|>1k}$

Per la [disuguaglianza di Bienaymé-Čebyšëv](https://it.wikipedia.org/wiki/Disuguaglianza_di_%C4%8Ceby%C5%A1%C3%ABv "Disuguaglianza di Čebyšëv") si trova:

$∀k,∀n,P⁡{ω∈Ω:|ϕn2(ω)−p|>1k}≤var(ϕn2)k2=k2p(1−p)n2$

da cui:

$∑n=1∞P⁡{ω∈Ω:|ϕn2(ω)−p|>1k}≤p(1−p)k2∑n=1∞1n2$

Ma questa serie è notoriamente convergente. Pertanto,

$∀k∈ℕ0,P⁡(lim supn→∞{ω∈Ω:|ϕn2(ω)−p|>1k})=0$

Si noti ora che ogni [numero naturale](https://it.wikipedia.org/wiki/Numero_naturale "Numero naturale") *n* è compreso tra due quadrati consecutivi:

$\forall n \in \mathbb{N} , \exists q \in \mathbb{N} : q^{2} \leq n < \left(\right. q + 1 \left.\right)^{2}$

da cui

$\frac{N_{n}}{\left(\right. q + 1 \left.\right)^{2}} \leq \phi_{n} \leq \frac{N_{n}}{q^{2}}$

si noti ora che $n - q^{2}$ è la massima differenza possibile tra $N_{q^{2}}$ e $N_{n}$, da cui:

$N_{q^{2}} \leq N_{n} \leq N_{q^{2}} + \left(n - q^{2}\right)$

pertanto:

$\frac{N_{q^{2}}}{\left(\right. q + 1 \left.\right)^{2}} \leq \frac{N_{n}}{\left(\right. q + 1 \left.\right)^{2}} \leq \phi_{n} \leq \frac{N_{n}}{q^{2}} \leq \frac{N_{q^{2}} + \left(n - q^{2}\right)}{q^{2}}$

ora però si ha $n - q^{2} \leq \left(\right. q + 1 \left.\right)^{2} - q^{2}$, dunque:

$\frac{N_{q^{2}}}{q^{2}} \frac{q^{2}}{\left(\right. q + 1 \left.\right)^{2}} \leq \phi_{n} \leq \frac{N_{q^{2}}}{q^{2}} + \frac{\left(\right. q + 1 \left.\right)^{2} - q^{2}}{q^{2}}$

passando al limite ($n→∞⇒q→∞$) e applicando il risultato ottenuto per $\phi_{n^{2}}$, si ottiene che, quasi certamente:

$p \cdot 1 = p \underset{q \rightarrow \infty}{lim} \frac{q^{2}}{\left(\right. q + 1 \left.\right)^{2}} \leq \underset{n \rightarrow \infty}{lim} \phi_{n} \leq p + \underset{q \rightarrow \infty}{lim} \frac{q^{2} + 2 q + 1 - q^{2}}{q^{2}} = p + 0$

il che conclude la dimostrazione.

## Note

## Voci correlate

- [Campionamento statistico](https://it.wikipedia.org/wiki/Campionamento_statistico "Campionamento statistico")
- [Distribuzione di Bernoulli](https://it.wikipedia.org/wiki/Distribuzione_di_Bernoulli "Distribuzione di Bernoulli")
- [Probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità")
- [Statistica](https://it.wikipedia.org/wiki/Statistica "Statistica")
- [Quasi certamente](https://it.wikipedia.org/wiki/Quasi_certamente "Quasi certamente")
- [Teorema della scimmia instancabile](https://it.wikipedia.org/wiki/Teorema_della_scimmia_instancabile "Teorema della scimmia instancabile")
- [Paradosso di Cantor](https://it.wikipedia.org/wiki/Paradosso_di_Cantor "Paradosso di Cantor")

## Altri progetti

Altri progetti

- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Law_of_large_numbers?uselang=it)

- contiene immagini o altri file su **[legge dei grandi numeri](https://commons.wikimedia.org/wiki/Category:Law_of_large_numbers?uselang=it)**

## Collegamenti esterni

- (EN) Richard Routledge, [law of large numbers](https://www.britannica.com/science/law-of-large-numbers), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Law of Large Numbers](http://mathworld.wolfram.com/LawofLargeNumbers.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [34822](https://thes.bncf.firenze.sbn.it/termine.php?id=34822) · [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh85075318](http://id.loc.gov/authorities/subjects/sh85075318) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4157077-7](https://d-nb.info/gnd/4157077-7) · [BNF](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Francia "Biblioteca nazionale di Francia") (FR) [cb11978788d](https://catalogue.bnf.fr/ark:/12148/cb11978788d) [(data)](https://data.bnf.fr/ark:/12148/cb11978788d) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007558155705171](https://www.nli.org.il/en/authorities/987007558155705171) |
| --- | --- |

[^1]: [Articolo Kahneman](http://www.econ.yale.edu/~shiller/behfin/2000-05/rabin.pdf) (PDF), su econ.yale.edu.