---
title: "Variabile casuale multivariata"
source: "https://it.wikipedia.org/wiki/Variabile_casuale_multivariata"
author:
  - "[[Wikipedia]]"
published: 2016-06-10
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica"), [probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità") e [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica"), una **variabile casuale multivariata** o *vettore casuale* è una lista di [variabili](https://it.wikipedia.org/wiki/Variabile_\(matematica\) "Variabile (matematica)") matematiche ciascuna di valore ignoto, o perché il valore non è ancora stato determinato o perché c'è una conoscenza imperfetta di tale valore. Le singole variabili in un vettore casuale sono raggruppate insieme perché ci possono essere [correlazioni](https://it.wikipedia.org/wiki/Correlazione_\(statistica\) "Correlazione (statistica)") tra loro — spesso esse rappresentano differenti proprietà di una singola [unità statistica](https://it.wikipedia.org/wiki/Unit%C3%A0_statistica?action=edit&redlink=1 "Unità statistica (la pagina non esiste)"). Per esempio, poiché una data persona ha una specifica età, altezza e peso, la rappresentazione di *qualsiasi persona* all'interno di un gruppo può essere un vettore casuale. Normalmente ogni elemento di un vettore casuale è un [numero reale](https://it.wikipedia.org/wiki/Numero_reale "Numero reale").

I vettori casuali sono spesso usati come l'implementazione sottostante di [variabili casuali](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") aggregate, come una [matrice casuale](https://it.wikipedia.org/wiki/Matrice_casuale?action=edit&redlink=1 "Matrice casuale (la pagina non esiste)"), un [albero casuale](https://it.wikipedia.org/wiki/Albero_casuale?action=edit&redlink=1 "Albero casuale (la pagina non esiste)"), una [successione casuale](https://it.wikipedia.org/wiki/Successione_casuale?action=edit&redlink=1 "Successione casuale (la pagina non esiste)"), un [processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico"), ecc.

PIù formalmente, una variabile casuale multivariata è un [vettore colonna](https://it.wikipedia.org/wiki/Vettore_colonna "Vettore colonna") $\mathbf{X} = \left(\right. X_{1} , \ldots , X_{n} \left.\right)^{T}$ (il cui [trasposto](https://it.wikipedia.org/wiki/Matrice_trasposta "Matrice trasposta") è un [vettore riga](https://it.wikipedia.org/wiki/Vettore_riga "Vettore riga")) le cui componenti sono [variabili casuali](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") a valori [scalari](https://it.wikipedia.org/wiki/Scalare_\(matematica\) "Scalare (matematica)") sullo stesso [spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità") $(Ω,ℱ,P)$, dove $Ω$ è lo [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario"), $ℱ$ è la [sigma-algebra](https://it.wikipedia.org/wiki/%CE%A3-algebra "Σ-algebra") (la collezione di tutti gli eventi) e $P$ è la [misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità") (una funzione che restituisce la [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") di ogni evento).

## Distribuzione di probabilità

Ogni vettore casuale dà luogo ad una misura di probabilità su $\mathbb{R}^{n}$ con l' [algebra di Borel](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel") come la sottostante sigma-algebra. Questa misura è anche conosciuta come la [distribuzione congiunta](https://it.wikipedia.org/wiki/Distribuzione_congiunta "Distribuzione congiunta") di probabilità, la distribuzione congiunta, o la distribuzione multivariata del vettore casuale.

Le [distribuzioni](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0 "Distribuzione di probabilità") di tutte le variabili casuali componenti $X_{i}$ sono chiamate [distribuzioni marginali](https://it.wikipedia.org/wiki/Distribuzione_marginale "Distribuzione marginale"). La [distribuzione di probabilità condizionata](https://it.wikipedia.org/wiki/Distribuzione_condizionata "Distribuzione condizionata") di $X_{i}$, data $X_{j}$, è la distribuzione di probabilità di $X_{i}$ quando è noto che $X_{j}$ assume un particolare valore.

## Operazioni sui vettori casuali

Ai vettori casuali si possono applicare gli stessi tipi di operazioni algebriche applicabili ai [vettori non casuali](https://it.wikipedia.org/wiki/Vettore_\(matematica\) "Vettore (matematica)"): addizione, sottrazione, moltiplicazione per uno [scalare](https://it.wikipedia.org/wiki/Scalare_\(matematica\) "Scalare (matematica)") e l'introduzione di [prodotti interni](https://it.wikipedia.org/wiki/Prodotto_interno "Prodotto interno").

Analogamente, un nuovo vettore casuale $𝐘$ può essere definito applicando una trasformazione affine $g : \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$ a un vettore casuale $𝐗$:

$𝐘=𝒜𝐗+b$, dove $𝒜$ è una matrice $n×n$ e $b$ è un vettore colonna $n×1$.

Se $𝒜$ è invertibile e la densità di probabilità di $𝐗$ è $f_{\mathbf{X}}$, allora la densità di probabilità di $𝐘$ è

$f_{\mathbf{Y}} \left(y\right) = \frac{f_{\mathbf{X}} \left(\mathcal{A}^{- 1} \left(y - b\right)\right)}{\left|det \mathcal{A}\right|}$.

## Valore atteso, covarianza e cross-covarianza

Il [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") o la media di un vettore casuale $𝐗$ è un vettore fissato $E⁡[𝐗]$ i cui elementi sono i valori attesi delle rispettive variabili casuali.

La [matrice delle covarianze](https://it.wikipedia.org/wiki/Matrice_delle_covarianze "Matrice delle covarianze") (detta anche matrice di varianza e covarianza) di un vettore casuale $n×1$ è una [matrice](https://it.wikipedia.org/wiki/Matrice "Matrice") $n×n$ il cui elemento $i,j$ è la [covarianza](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\) "Covarianza (probabilità)") tra le variabili casuali $i$ -esima e $j$ -esima. La matrice delle covarianze è il valore atteso, elemento per elemento, della matrice $n×n$ [calcolata come](https://it.wikipedia.org/wiki/Moltiplicazione_di_matrici "Moltiplicazione di matrici") $\left[\mathbf{X} - E \left[\mathbf{X}\right]\right] \left[\right. \mathbf{X} - E \left[\mathbf{X}\right] \left]\right.^{T}$, dove la sovrascritta T si riferisce alla trasposizione del vettore indicato:

$Var \left[\mathbf{X}\right] = E \left[\right. \left(\mathbf{X} - E \left[\mathbf{X}\right]\right) \left(\mathbf{X} - E \left[\mathbf{X}\right] \left.\right)^{T}\right] .$

Per estensione, la [matrice delle cross-covarianze](https://it.wikipedia.org/wiki/Matrice_delle_cross-covarianze "Matrice delle cross-covarianze") tra due vettori casuali $𝐗$ e $𝐘$ ($𝐗$ avente $n$ elementi e $𝐘$ aventi $p$ elementi) è la matrice $n×p$

$Cov \left[\mathbf{X} , \mathbf{Y}\right] = E \left[\right. \left(\mathbf{X} - E \left[\mathbf{X}\right]\right) \left(\mathbf{Y} - E \left[\mathbf{Y}\right] \left.\right)^{T}\right] ,$

dove, nuovamente, il valore atteso indicata nella matrice è presa elemento per elemento. La matrice delle cross-covarianze $Cov⁡[𝐘,𝐗]$ è, semplicemente, la trasposta della matrice $Cov⁡[𝐗,𝐘]$.

## Ulteriori proprietà

### Valore atteso di una forma quadratica

È possibile prendere il valore atteso di una [forma quadratica](https://it.wikipedia.org/wiki/Forma_quadratica "Forma quadratica") nel vettore casuale $𝐗$ come segue:[^1]

$E \left(\mathbf{X}^{'} A \mathbf{X}\right) = \left[\right. E \left(\mathbf{X}\right) \left]\right.^{'} A \left[E \left(\mathbf{X}\right)\right] + tr \left(A C\right) ,$

dove $C$ è la matrice delle covarianze di $𝐗$ e $tr$ si riferisce alla [traccia](https://it.wikipedia.org/wiki/Traccia_\(matrice\) "Traccia (matrice)") di una matrice, cioè alla somma degli elementi della sua [diagonale principale](https://it.wikipedia.org/wiki/Diagonale_principale "Diagonale principale") (dall'alto a sinistra al basso a destra). Poiché la forma quadratica è uno scalare, tale è il suo valore atteso.

**Dimostrazione**: Sia $𝐳$ un vettore casuale $m×1$ con $E⁡[𝐳]=μ$ e $Cov⁡[𝐳]=V$ e sia $A$ una matrice non stocastica $m×m$.

Applicando la [formula della covarianza](https://it.wikipedia.org/wiki/Formula_computazionale_per_la_varianza#Generalizzazione_per_la_covarianza "Formula computazionale per la varianza"), se poniamo $𝐳^{'} = \mathbf{X}$ e $𝐳^{'} A^{'} = \mathbf{Y}$, vediamo che:

$Cov \left[\mathbf{X} , \mathbf{Y}\right] = E \left[\mathbf{X} \mathbf{Y}^{'}\right] - E \left[\mathbf{X}\right] E \left[\right. \mathbf{Y} \left]\right.^{'}$

Quindi

$\begin{matrix}E \left(\mathbf{X} \mathbf{Y}^{'}\right) & = Cov \left(\mathbf{X} , \mathbf{Y}\right) + E \left(\mathbf{X}\right) E \left(\right. \mathbf{Y} \left.\right)^{'} \\ E \left(z^{'} A z\right) & = Cov \left(z^{'} , z^{'} A^{'}\right) + E \left(z^{'}\right) E \left(\right. z^{'} A^{'} \left.\right)^{'} \\ = Cov \left(z^{'} , z^{'} A^{'}\right) + \mu^{'} \left(\right. \mu^{'} A^{'} \left.\right)^{'} \\ = Cov \left(z^{'} , z^{'} A^{'}\right) + \mu^{'} A \mu ,\end{matrix}$

che ci permette di mostrare che

$Cov \left(z^{'} , z^{'} A^{'}\right) = tr \left(A V\right) .$

Questo è vero in base al fatto che è possibile [permutare ciclicamente le matrici mentre si considera la traccia](https://it.wikipedia.org/wiki/Traccia_\(matrice\)#Propriet%C3%A0 "Traccia (matrice)") senza che cambi il risultato finale (ossia: $tr⁡(AB)=tr⁡(BA)$).

Allora, [come si vede](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\)#Definizione "Covarianza (probabilità)"),

$\begin{matrix}Cov \left(z^{'} , z^{'} A^{'}\right) & = E \left[\left(z^{'} - E \left(z^{'}\right)\right) \left(z^{'} A^{'} - E \left(z^{'} A^{'}\right)\right)^{'}\right] \\ = E \left[\right. \left(z^{'} - \mu^{'}\right) \left(z^{'} A^{'} - \mu^{'} A^{'} \left.\right)^{'}\right] \\ = E \left[\right. \left(z - \mu \left.\right)^{'} \left(A z - A \mu\right)\right] .\end{matrix}$

e, poiché

$\left(z - \mu\right)^{'} \left(A z - A \mu\right)$

è un numero fissato, si ha

$\left(\right. z - \mu \left.\right)^{'} \left(A z - A \mu\right) = tr \left[\left(\right. z - \mu \left.\right)^{'} \left(A z - A \mu\right)\right] = tr \left[\right. \left(z - \mu \left.\right)^{'} A \left(z - \mu\right)\right]$

banalmente. Usando la [permutazione](https://it.wikipedia.org/wiki/Permutazione "Permutazione"), abbiamo:

$tr \left[\left(\right. z - \mu \left.\right)^{'} A \left(z - \mu\right)\right] = tr \left[A \left(z - \mu\right) \left(\right. z - \mu \left.\right)^{'}\right] ,$

e, ponendo ciò nella formula originale, abbiamo:

$\begin{matrix}Cov \left(z^{'} , z^{'} A^{'}\right) & = E \left[\left(z - \mu\right)^{'} \left(A z - A \mu\right)\right] \\ = E \left[tr \left[\right. A \left(z - \mu\right) \left(z - \mu \left.\right)^{'}\right]\right] \\ = tr \left[A \cdot E \left[\right. \left(z - \mu\right) \left(z - \mu \left.\right)^{'}\right]\right] \\ = tr \left[A V\right] .\end{matrix}$

### Valore atteso del prodotto di due differenti forme quadratiche

È possibile considerare l'aspettazione del prodotto di due differenti forme quadratiche in un vettore casuale [gaussiano](https://it.wikipedia.org/wiki/Distribuzione_normale_multivariata "Distribuzione normale multivariata") $𝐗$ con media zero, come segue:[^1]

$E \left[\mathbf{X}^{'} A \mathbf{X}\right] \left[\mathbf{X}^{'} B \mathbf{X}\right] = 2 tr \left(A C B C\right) + tr \left(A C\right) tr \left(B C\right)$

dove, nuovamente, $C$ è la matrice delle covarianze di $𝐗$. Di nuovo, poiché entrambe le forme quadratiche sono scalari e quindi il loro prodotto è uno scalare, il valore atteso del loro prodotto è ancora uno scalare.

## Applicazioni

### Teoria dei portafogli

In [teoria dei portafogli](https://it.wikipedia.org/wiki/Frontiera_dei_portafogli "Frontiera dei portafogli") in [finanza](https://it.wikipedia.org/wiki/Finanza "Finanza"), spesso un obiettivo è quello di scegliere un portafoglio di attività rischiose tali che la distribuzione del rendimento casuale di portafoglio abbia proprietà desiderabili. Per esempio, si potrebbe voler scegliere il rendimento di portafoglio avente la varianza più bassa per un dato valore atteso. In tal caso, il vettore casuale è il vettore *r* dei rendimenti casuali sulle attività individuali e il rendimento di portafoglio *p* (uno scalare casuale) è il prodotto interno del vettore dei rendimenti casuali con un vettore *w* dei pesi di portafoglio — le frazioni di portafoglio poste nelle rispettive attività. Poiché *p* = *w* <sup>T</sup> *r*, il valore atteso del rendimento del portafoglio è *w* <sup>T</sup> E(*r*) e si può dimostrare che la varianza del rendimento del portafoglio è *w* <sup>T</sup> C *w*, dove C è la matrice delle covarianze di *r*.

### Regressione lineare

In teoria delle [regressioni lineari](https://it.wikipedia.org/wiki/Regressione_lineare "Regressione lineare"), abbiamo i dati su *n* osservazioni su una variabile dipendente *y* e *n* osservazioni su ciascuna di *k* variabili indipendenti *x <sub>j</sub>*. Le osservazioni sulla variabile dipendente vengono scritte in un vettore colonna *y*; le osservazioni su ciascuna variabile indipendente sono pure scritte in vettori colonna e tali vettori colonna sono combinati in una matrice *X* di osservazioni sulle variabili indipendenti. La seguente equazione di regressione viene quindi postulata come la descrizione del processo che ha generato i dati:

$y=Xβ+e,$

dove $β$ è un vettore fissato postulato ma non noto di *k* coefficienti di risposta ed *e* è un vettore casuale non noto che riflette le influenze casuali sulla variabile dipendente. Con alcune tecniche, come i [minimi quadrati ordinari](https://it.wikipedia.org/wiki/Minimi_quadrati_ordinari "Minimi quadrati ordinari"), un vettore $\overset{̂}{\beta}$ è scelto come una stima di β e la stima del vettore *e*, denotata $\overset{̂}{e}$, è calcolata come

$\overset{̂}{e} = y - X \overset{̂}{\beta} .$

A questo punto l'esperto di statistica deve analizzare le proprietà di $\overset{̂}{\beta}$ e $\overset{̂}{e}$, che sono visti come vettori casuali poiché una selezione casualmente differente di *n* casi da osservare avrebbe comportato valori diversi per essi.

## Note

## Voci correlate

- [Distribuzione normale multivariata](https://it.wikipedia.org/wiki/Distribuzione_normale_multivariata "Distribuzione normale multivariata")

## Collegamenti esterni

- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Variabile casuale multivariata](http://mathworld.wolfram.com/RandomVariable.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.

[^1]: Kendrick, David, *Stochastic Control for Economic Models*, McGraw-Hill, 1981.