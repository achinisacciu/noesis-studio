---
title: "Processo stocastico"
source: "https://it.wikipedia.org/wiki/Processo_stocastico"
author:
  - "[[Wikipedia]]"
published: 2003-04-17
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica"), più precisamente nella [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità"), un **processo stocastico** (o **processo aleatorio**) è la versione probabilistica del concetto di [sistema dinamico](https://it.wikipedia.org/wiki/Sistema_dinamico "Sistema dinamico"). Un processo stocastico è un insieme ordinato di [funzioni](https://it.wikipedia.org/wiki/Funzione_\(matematica\) "Funzione (matematica)") reali di un certo parametro (in genere il [tempo](https://it.wikipedia.org/wiki/Tempo "Tempo")) che gode di determinate proprietà [statistiche](https://it.wikipedia.org/wiki/Statistica "Statistica"). In generale è possibile identificare questo processo come una famiglia con un parametro di [variabili casuali](https://it.wikipedia.org/wiki/Variabili_casuali "Variabili casuali") reali $X(t)$ rappresentanti le trasformazioni dallo stato iniziale allo stato dopo un certo tempo $t$. In termini più precisi questo si basa su una variabile casuale che supera il limite dei [numeri reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale") (come ad esempio, $\mathbb{R}^{n}$, o [spazi funzionali](https://it.wikipedia.org/wiki/Spazio_funzionale "Spazio funzionale"), o [successioni](https://it.wikipedia.org/wiki/Successione_\(matematica\) "Successione (matematica)") di numeri reali). I processi aleatori sono un'estensione del concetto di variabile aleatoria quando viene preso in considerazione anche il parametro tempo.

## Descrizione

Da un punto di vista pratico, un processo stocastico è una forma di rappresentazione di una grandezza che varia nel tempo in modo casuale (ad esempio un [segnale elettrico](https://it.wikipedia.org/wiki/Segnale_elettrico "Segnale elettrico") contenente [informazione](https://it.wikipedia.org/wiki/Informazione "Informazione") ovvero [modulato](https://it.wikipedia.org/wiki/Modulazione "Modulazione"), il numero di autovetture che transitano su un ponte, ecc.) e con certe caratteristiche. Facendo delle prove (o osservazioni) ripetute dello stesso processo, si ottengono diversi andamenti nel tempo (realizzazioni del processo); osservando le diverse realizzazioni a un istante $t$ si ottiene una variabile aleatoria $X(t)$ che comprende i diversi valori che il processo può assumere in quell'istante. Tali valori avranno un valore medio, che, nel caso di variabile aleatoria gaussiana, costituiranno il valore al centro della "campana" gaussiana all'istante $t$. Quindi per ciascun istante si può definire una variabile aleatoria, una gaussiana o altra, che rappresenti il valore più probabile del processo con il relativo indice di scostamento o deviazione standard.

### Concetti e definizioni

Si definisce processo stocastico una famiglia di [variabili aleatorie](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") ${X(t),t∈T⊆ℝ+}$ dipendenti dal tempo, definite su uno [spazio campione](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario") $Ω$ e che assumono valori in un insieme definito *spazio degli stati del processo*. Un processo stocastico è quindi un insieme di funzioni che evolvono nel tempo (le cosiddette *funzioni campione* o *realizzazioni*), ognuna delle quali è associata ad un determinato elemento dello spazio campione, così che il risultato di un esperimento casuale corrisponde di fatto all'estrazione di una di queste funzioni.

Fissando un istante di tempo $\overset{\sim}{t}$, è possibile individuare valori generalmente differenti, ognuno relativo a una determinata realizzazione e quindi ad un elemento dello spazio campione: $X \left(\overset{\sim}{t}\right)$ è allora una variabile aleatoria e rappresenta la "fotografia" del processo stocastico in un determinato istante; quindi, rispetto a una semplice variabile aleatoria, esso fornisce anche un'informazione relativa all'evoluzione temporale.

Per descrivere un processo aleatorio è sufficiente utilizzare la [funzione di densità di probabilità congiunta](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità"), o, analogamente, la [funzione di distribuzione di probabilità congiunta](https://it.wikipedia.org/wiki/Variabile_casuale#Distribuzione_di_probabilit.C3.A0 "Variabile casuale"), delle variabili aleatorie ${X(t1),X(t2),…,X(tn)}$.

Lo spazio della variabile tempo, cioè l'insieme $T={ti,i=1,2,…,n}$, può essere continuo o discreto: nel primo caso si parla di processo stocastico "continuo nel tempo" (o processo stocastico tempo-continuo), mentre nel secondo caso si parla di processo stocastico "discreto nel tempo" (o processo stocastico tempo-discreto). In alternativa si usa la formulazione "processo stocastico a parametro discreto" o "continuo".

L'insieme dei valori che possono assumere le realizzazioni costituisce il suddetto [spazio degli stati](https://it.wikipedia.org/wiki/Stato_di_sistema "Stato di sistema") del processo e rappresenta le "situazioni" descritte dalle variabili casuali e indicate per esempio con $s_{0} , s_{1} , s_{2} , \ldots$. Tale insieme può essere continuo o discreto: in quest'ultimo caso, che implica la numerabilità degli stati, il processo aleatorio viene definito catena.

Se la variabile casuale è [discreta](https://it.wikipedia.org/wiki/Variabile_casuale_discreta "Variabile casuale discreta") allora si parla di " [processo stocastico discreto](https://it.wikipedia.org/wiki/Processo_stocastico_discreto "Processo stocastico discreto") ", se invece è una [variabile casuale continua](https://it.wikipedia.org/wiki/Variabile_casuale_continua "Variabile casuale continua") allora si parla di " [processo stocastico continuo](https://it.wikipedia.org/wiki/Processo_stocastico_continuo?action=edit&redlink=1 "Processo stocastico continuo (la pagina non esiste)") " (sottinteso "nello spazio degli eventi").

I processi stocastici si distinguono in [markoviani](https://it.wikipedia.org/wiki/Processo_markoviano "Processo markoviano") e non markoviani a seconda che la legge di probabilità che determina il passaggio da uno stato all'altro (probabilità di transizione) dipenda unicamente dallo stato di partenza ([processo markoviano](https://it.wikipedia.org/wiki/Processo_markoviano "Processo markoviano")) o anche dagli stati ad esso precedenti (processo non markoviano).

Se la probabilità di transizione dipende dagli stati precedenti ma non dipende esplicitamente dal tempo *t*, allora si parla di [processo stocastico omogeneo](https://it.wikipedia.org/wiki/Processo_stocastico_omogeneo?action=edit&redlink=1 "Processo stocastico omogeneo (la pagina non esiste)").

I [processi stocastici ciclostazionari](https://it.wikipedia.org/wiki/Processi_stocastici_ciclostazionari "Processi stocastici ciclostazionari") servono per descrivere processi generati da fenomeni periodici.

### Esempio introduttivo

Si supponga di voler definire matematicamente la dinamica di un punto che si muove su una retta con una data legge probabilistica. Si può definire un processo stocastico come la collezione delle variabili casuali ${St,t∈ℝ}$, dove per ogni valore del tempo $t$, $S_{t}$ è la variabile casuale (reale) che esprime la legge probabilistica del punto considerato al tempo $t$. Se si definisce $S_{t}$ come la soluzione all'equazione differenziale stocastica

$d S_{t} = - \mu S_{t} d t + \sigma d W_{t} ,$

dove $μ∈ℝ$, $\sigma \in \mathbb{R}_{> 0}$ e $W_{t}$ denota il processo di Wiener, allora $\left(\right. S_{t} \left.\right)_{t}$ definisce il [processo di Ornstein-Uhlenbeck](https://it.wikipedia.org/wiki/Processo_di_Ornstein-Uhlenbeck?action=edit&redlink=1 "Processo di Ornstein-Uhlenbeck (la pagina non esiste)").

## Bibliografia

- (EN) Malempati Madhusudana Rao (1995): *Stochastic Processes: General Theory*, Kluwer, [ISBN 0-7923-3725-5](https://it.wikipedia.org/wiki/Special:BookSources/0792337255)
- (EN) [Kiyoshi Itō](https://it.wikipedia.org/wiki/Kiyoshi_It%C5%8D "Kiyoshi Itō") (2004): *Stochastic Processes*, Springer, [ISBN 3-540-20482-2](https://it.wikipedia.org/wiki/Special:BookSources/3540204822)
- (EN) [G. E. Uhlenbeck](https://it.wikipedia.org/wiki/George_Uhlenbeck "George Uhlenbeck") e [L. S. Ornstein](https://it.wikipedia.org/wiki/Leonard_Ornstein "Leonard Ornstein"), [On the theory of Brownian Motion](https://archive.org/details/sim_physical-review_1930-09-01_36_5/page/n31), in Phys. Rev., vol. 36, 1930, pp. 823-841, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1103/PhysRev.36.823](https://dx.doi.org/10.1103%2FPhysRev.36.823).

## Voci correlate

- [Variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale")
- [Spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità")
- [Processo stazionario](https://it.wikipedia.org/wiki/Processo_stazionario "Processo stazionario")
- [Ergodicità](https://it.wikipedia.org/wiki/Ergodicit%C3%A0 "Ergodicità")
- [Processo markoviano](https://it.wikipedia.org/wiki/Processo_markoviano "Processo markoviano")
- [Processo gaussiano](https://it.wikipedia.org/wiki/Processo_gaussiano "Processo gaussiano")
- [Processo di Wiener](https://it.wikipedia.org/wiki/Processo_di_Wiener "Processo di Wiener")
- [Funzione càdlàg](https://it.wikipedia.org/wiki/Funzione_c%C3%A0dl%C3%A0g "Funzione càdlàg")
- [Matrice aleatoria](https://it.wikipedia.org/wiki/Matrice_aleatoria "Matrice aleatoria")

## Altri progetti

Altri progetti

- [Wikizionario](https://it.wiktionary.org/wiki/processo%20stocastico "wikt:processo stocastico")
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Stochastic_processes?uselang=it)

- [Wikizionario](https://it.wiktionary.org/wiki/ "wikt:") contiene il lemma di dizionario « **[processo stocastico](https://it.wiktionary.org/wiki/processo%20stocastico "wikt:processo stocastico")** »
- contiene immagini o altri file sul **[processo stocastico](https://commons.wikimedia.org/wiki/Category:Stochastic_processes?uselang=it)**

## Collegamenti esterni

- Luigi Accardi e Roberto Monte, [Stocastici, processi](https://www.treccani.it/enciclopedia/processi-stocastici_\(Enciclopedia-Italiana\)/), in [Enciclopedia Italiana](https://it.wikipedia.org/wiki/Enciclopedia_Treccani "Enciclopedia Treccani"), VI Appendice, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2000.
- [Processo stocastico](https://www.treccani.it/enciclopedia/processo-stocastico_\(Enciclopedia-della-Matematica\)/), in Enciclopedia della Matematica, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2013.
- Flavio Pressacco, [Processo aleatorio (processo stocastico)](https://www.treccani.it/enciclopedia/processo-aleatorio_\(Dizionario-di-Economia-e-Finanza\)/), in Dizionario di Economia e Finanza, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2012.
- (EN) [stochastic process](https://www.britannica.com/topic/stochastic-process), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Stochastic Process](http://mathworld.wolfram.com/StochasticProcess.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- (DE) [Quantenphysik und Indeterminismus](https://web.archive.org/web/20120523154754/http://philo.at/wiki/index.php/Quantenphysik_und_Indeterminismus), su philo.at. URL consultato il 22 dicembre 2009 (archiviato dall' url originale il 23 maggio 2012).
- (EN) [The problem of indeterminism](http://www.informationphilosopher.com/freedom/indeterminism.html), su informationphilosopher.com.
- [Indeterminismo](https://web.archive.org/web/20160304100711/http://indeterminismo.bravehost.com/), su indeterminismo.bravehost.com. URL consultato il 6 novembre 2018 (archiviato dall' url originale il 4 marzo 2016).

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [20545](https://thes.bncf.firenze.sbn.it/termine.php?id=20545) · [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh85128181](http://id.loc.gov/authorities/subjects/sh85128181) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4057630-9](https://d-nb.info/gnd/4057630-9) · [BNE](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Spagna "Biblioteca nazionale di Spagna") (ES) [XX4576445](https://datos.bne.es/resource/XX4576445) [(data)](http://datos.bne.es/resource/XX4576445) · [BNF](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Francia "Biblioteca nazionale di Francia") (FR) [cb119326416](https://catalogue.bnf.fr/ark:/12148/cb119326416) [(data)](https://data.bnf.fr/ark:/12148/cb119326416) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007536303605171](https://www.nli.org.il/en/authorities/987007536303605171) · [NDL](https://it.wikipedia.org/wiki/Biblioteca_della_Dieta_nazionale_del_Giappone "Biblioteca della Dieta nazionale del Giappone") (EN, JA) [00564752](https://id.ndl.go.jp/auth/ndlna/00564752) |
| --- | --- |