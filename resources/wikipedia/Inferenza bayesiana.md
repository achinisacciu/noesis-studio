---
title: "Inferenza bayesiana"
source: "https://it.wikipedia.org/wiki/Inferenza_bayesiana"
author:
  - "[[Wikipedia]]"
published: 2005-08-03
created: 2026-11-06
description:
tags:
  - "clippings"
---
L' **inferenza bayesiana** è un approccio all' [inferenza statistica](https://it.wikipedia.org/wiki/Inferenza_statistica "Inferenza statistica") in cui le [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") non sono interpretate come frequenze, proporzioni o concetti analoghi, ma piuttosto come livelli di fiducia nel verificarsi di un dato evento. Il nome deriva dal [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes"), che costituisce il fondamento di questo approccio.

Il [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") prende a sua volta il nome dal reverendo [Thomas Bayes](https://it.wikipedia.org/wiki/Thomas_Bayes "Thomas Bayes"). Ad ogni modo non è chiaro se Bayes stesso sottoscriverebbe l'interpretazione della [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità") che oggi chiamiamo *bayesiana*.

## Principi e strumenti dell'approccio bayesiano

### Evidenza empirica e metodo scientifico

Gli [statistici](https://it.wikipedia.org/wiki/Statistico "Statistico") bayesiani sostengono che i metodi dell'inferenza bayesiana rappresentano una formalizzazione del [metodo scientifico](https://it.wikipedia.org/wiki/Metodo_scientifico "Metodo scientifico"), che normalmente implica la raccolta di dati ([evidenza empirica](https://it.wikipedia.org/wiki/Evidenza_empirica "Evidenza empirica")), che corroborano o confutano una data [ipotesi](https://it.wikipedia.org/wiki/Ipotesi "Ipotesi"). In questo senso, non si possono mai avere certezze riguardo a un' [ipotesi](https://it.wikipedia.org/wiki/Ipotesi "Ipotesi"), ma con l'aumentare della disponibilità di dati il grado di fiducia cambia; con sufficiente evidenza empirica, diventerà molto alto (per esempio, tendente a 1) o molto basso (tendente a 0).

*Il sole è sorto e tramontato per miliardi di anni. Il sole è tramontato anche stanotte. Con un'elevata probabilità, il sole domani sorgerà.*

Questo esempio è ripreso da una nota argomentazione di [Pierre Simon Laplace](https://it.wikipedia.org/wiki/Pierre_Simon_Laplace "Pierre Simon Laplace"), che pare sia giunto in maniera indipendente al risultato del [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes").

Gli [statistici](https://it.wikipedia.org/wiki/Statistico "Statistico") bayesiani sostengono inoltre che l'inferenza bayesiana costituisca la base più logica per discriminare tra [ipotesi](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla") alternative/in conflitto. Tramite tale approccio, si usa una stima del grado di fiducia in una data [ipotesi](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla") prima dell'osservazione dei dati, al fine di associare un valore numerico al grado di fiducia in quella stessa [ipotesi](https://it.wikipedia.org/wiki/Ipotesi "Ipotesi") successivamente all'osservazione dei dati. Dal momento che si fonda su livelli di fiducia soggettivi, per contro, l'inferenza bayesiana non è interamente riducibile al concetto di [induzione](https://it.wikipedia.org/wiki/Induzione "Induzione"); si veda anche [metodo scientifico](https://it.wikipedia.org/wiki/Metodo_scientifico "Metodo scientifico").

### Teorema di Bayes

In termini più semplici, il [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") fornisce un metodo per modificare il livello di fiducia in una data [ipotesi](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla"), alla luce di nuova informazione. Denotando con $H_{0}$ l' [ipotesi nulla](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla"), e con $E$ il dato empirico osservato, il [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") può essere enunciato come:

$P \left(\right. H_{0} \left|\right. E \left.\right) = \frac{P \left(\right. E \left|\right. H_{0} \left.\right) P \left(H_{0}\right)}{P \left(E\right)} .$

Tralasciando l'origine dell' [ipotesi nulla](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla") (che potrà essere stata formulata *ab initio*, o dedotta da precedenti osservazioni), essa dovrà comunque essere formulata *prima* dell'osservazione $E$. Nella terminologia della [statistica bayesiana](https://it.wikipedia.org/wiki/Statistica_bayesiana "Statistica bayesiana"), inoltre:

- $P \left(H_{0}\right)$ è detta probabilità *a priori* di $H_{0}$;
- $P \left(\right. E \left|\right. H_{0} \left.\right)$ è detta *[funzione di verosimiglianza](https://it.wikipedia.org/wiki/Funzione_di_verosimiglianza "Funzione di verosimiglianza")*, ed è ciò su cui si fonda l'inferenza classica, o *frequentista*;
- $P(E)$ è detta *probabilità marginale*, la probabilità di osservare $E$, senza alcuna informazione pregressa; è una [costante di normalizzazione](https://it.wikipedia.org/wiki/Normalizzazione_\(matematica\) "Normalizzazione (matematica)");
- $P \left(\right. H_{0} \left|\right. E \left.\right)$ è detta probabilità *a posteriori* di $H_{0}$, dato $E$.

Il fattore di scala $P \left(\right. E \left|\right. H_{0} \left.\right) / P \left(E\right)$ può essere interpretato come una misura dell'impatto che l'osservazione di $E$ ha sul grado di fiducia del ricercatore nell' [ipotesi nulla](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla"), rappresentato a sua volta dalla probabilità a priori $P \left(H_{0}\right)$; se è altamente inverosimile che $E$ sia osservato, a meno che $H_{0}$ non sia proprio vera, il fattore di scala sarà elevato. La probabilità (fiducia) a posteriori, di conseguenza, combina le convinzioni che il ricercatore ha a priori con quelle derivanti dall'osservazione del dato empirico.

È facile mostrare che $P \left(\right. H_{0} \left|\right. E \left.\right)$ è sempre minore o al più uguale a 1, così che le consuete proprietà della [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") sono soddisfatte; infatti:

$P \left(E\right) \geq P \left(E \land H_{0}\right) = P \left(\right. E \left|\right. H_{0} \left.\right) P \left(H_{0}\right) ,$

dunque se $P \left(E\right) = P \left(E \land H_{0}\right)$, $P \left(\right. H_{0} \left|\right. E \left.\right) = 1$, e in qualunque altro caso la [probabilità a posteriori](https://it.wikipedia.org/wiki/Probabilit%C3%A0_a_posteriori "Probabilità a posteriori") sarà strettamente minore di 1.

### Probabilità oggettiva e soggettiva

Alcuni statistici bayesiani ritengono che se fosse possibile assegnare alle probabilità a priori un valore *oggettivo*, il [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") potrebbe essere impiegato per fornire una misura oggettiva della probabilità di un' [ipotesi](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla"). Per altri, tuttavia, non sarebbe possibile assegnare probabilità *oggettive*; in effetti, ciò sembrerebbe richiedere la capacità di assegnare probabilità a tutte le possibili [ipotesi](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla").

In alternativa (e più spesso, nel contesto della [statistica bayesiana](https://it.wikipedia.org/wiki/Statistica_bayesiana "Statistica bayesiana")), le [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") si considerano una misura del grado *soggettivo* di fiducia da parte del ricercatore, e si suppone che restringano le potenziali [ipotesi](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla") a un [insieme limitato](https://it.wikipedia.org/wiki/Insieme_limitato "Insieme limitato"), inquadrato in un [modello](https://it.wikipedia.org/wiki/Modello_statistico "Modello statistico") di riferimento. Il [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") dovrebbe allora fornire un criterio razionale per valutare fino a che punto una data osservazione dovrebbe alterare le convinzioni del ricercatore; in questo caso tuttavia la probabilità rimane soggettiva: dunque è possibile usare il teorema per giustificare razionalmente una qualche [ipotesi](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla"), ma alle spese di rifiutare l'oggettività delle affermazioni che ne derivano.

È inoltre improbabile che due individui muovano dallo stesso grado di fiducia soggettiva. I sostenitori del metodo bayesiano argomentano che, anche con probabilità a priori molto differenti, un numero sufficiente di osservazioni possa condurre a probabilità a posteriori molto vicine. Ciò presuppone che i ricercatori non rifiutino *a priori* le [ipotesi](https://it.wikipedia.org/wiki/Ipotesi_nulla "Ipotesi nulla") della loro controparte, e che assegnino probabilità condizionate ([funzioni di verosimiglianza](https://it.wikipedia.org/wiki/Funzione_di_verosimiglianza "Funzione di verosimiglianza")) simili.

La scuola della [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica") italiana ha dato importanti contributi allo sviluppo della concezione soggettiva della [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità"), tramite il lavoro di [Bruno de Finetti](https://it.wikipedia.org/wiki/Bruno_de_Finetti "Bruno de Finetti"). Sulla distinzione tra probabilità *oggettiva* e *soggettiva*, si veda anche l'articolo sulla [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità").

### Rapporto di verosimiglianza

Spesso l'impatto dell'osservazione empirica può essere sintetizzato da un rapporto di [verosimiglianza](https://it.wikipedia.org/wiki/Funzione_di_verosimiglianza "Funzione di verosimiglianza"). Quest'ultimo può essere combinato con la probabilità a priori, per rappresentare il grado di fiducia *a priori* e qualunque precedente risultato empirico. Per esempio, si consideri il rapporto di [verosimiglianza](https://it.wikipedia.org/wiki/Funzione_di_verosimiglianza "Funzione di verosimiglianza"):

$\Lambda = \frac{L \left(\right. H_{0} \left|\right. E \left.\right)}{L \left(\right. \text{not } H_{0} \left|\right. E \left.\right)} = \frac{P \left(\right. E \left|\right. H_{0} \left.\right)}{P \left(\right. E \left|\right. \text{not } H_{0} \left.\right)}$

Si può riscrivere l'enunciato del [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") come:

$P \left(\right. H_{0} \left|\right. E \left.\right) = \frac{\Lambda P \left(H_{0}\right)}{\Lambda P \left(H_{0}\right) + P \left(\text{not } H_{0}\right)} = \frac{P \left(H_{0}\right)}{P \left(H_{0}\right) + \left(1 - P \left(H_{0}\right)\right) / \Lambda} .$

Sulla base di due risultati empirici [indipendenti](https://it.wikipedia.org/wiki/Indipendenza_statistica "Indipendenza statistica") $E_{1}$, $E_{2}$, quanto sopra può essere sfruttato per computare la probabilità a posteriori sulla base di $E_{1}$, e utilizzare quest'ultima come nuova probabilità a priori per calcolare una seconda probabilità a posteriori basata su $E_{2}$. Questo procedimento è algebricamente equivalente a moltiplicare i rapporti di verosimiglianza. Dunque:

$P \left(\right. E_{1} , E_{2} \left|\right. H_{0} \left.\right) = P \left(\right. E_{1} \left|\right. H_{0} \left.\right) P \left(\right. E_{2} \left|\right. H_{0} \left.\right) \land P \left(\right. E_{1} , E_{2} \left|\right. \text{not } H_{0} \left.\right) = P \left(\right. E_{1} \left|\right. \text{not } H_{0} \left.\right) P \left(\right. E_{2} \left|\right. \text{not } H_{0} \left.\right)$

implica:

$P \left(\right. H_{0} \left|\right. E_{1} , E_{2} \left.\right) = \frac{\Lambda_{1} \Lambda_{2} P \left(H_{0}\right)}{\Lambda_{1} \Lambda_{2} P \left(H_{0}\right) + P \left(\text{not } H_{0}\right)} .$

### Funzione di perdita

La [statistica bayesiana](https://it.wikipedia.org/wiki/Statistica_bayesiana "Statistica bayesiana") presenta importanti collegamenti con la [teoria delle decisioni](https://it.wikipedia.org/wiki/Teoria_delle_decisioni "Teoria delle decisioni"); una decisione basata sul fondamento dell'inferenza bayesiana è determinata da una [funzione di perdita](https://it.wikipedia.org/wiki/Funzione_di_perdita "Funzione di perdita") ad essa associata. La [funzione di perdita](https://it.wikipedia.org/wiki/Funzione_di_perdita "Funzione di perdita") essenzialmente riflette le conseguenze negative associate alla decisione "sbagliata". Un esempio piuttosto comune, e che porta a risultati assai vicini a quelli dell'inferenza classica o frequentista, è quello della funzione di perdita quadratica.

## Particolari distribuzioni a priori e a posteriori

### La variabile casuale Beta nell'inferenza bayesiana

La [variabile casuale Beta](https://it.wikipedia.org/wiki/Variabile_casuale_Beta "Variabile casuale Beta") svolge un importante ruolo nell'ambito dell'inferenza bayesiana in quanto per alcune [variabili casuali](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") è sia la distribuzione a priori che la distribuzione a posteriori (con parametri diversi) dei parametri di tali variabili casuali.

#### Distribuzioni a priori coniugate e la variabile casuale binomiale

Se $X$ è distribuita come una [variabile casuale binomiale](https://it.wikipedia.org/wiki/Variabile_casuale_binomiale "Variabile casuale binomiale") con parametri $n$ e $π$

$f(x|π)=Binom(x|n;π)$

e il parametro $π$ è distribuito a priori come una [variabile casuale Beta](https://it.wikipedia.org/wiki/Variabile_casuale_Beta "Variabile casuale Beta") con i parametri $a$ e $b$

$g(π)=Beta(π|a;b),$

allora il parametro $π$ è distribuito a posteriori anch'esso come una variabile casuale Beta, ma con parametri $a+x$ e $b+n−x$

$g(π|x)=Beta(π|a+x;b+n−x).$

Qualora la distribuzione a priori sia una [variabile casuale rettangolare](https://it.wikipedia.org/wiki/Variabile_casuale_rettangolare "Variabile casuale rettangolare") nell'intervallo $[0;1]$ (ossia ipotizzando a priori tutti i possibili valori di $π$ equiprobabili), e pertanto $a=1$ e $b=1,$ allora la distribuzione a posteriori è una Beta con parametri $x+1$ e $n−x+1$

$g \left(\right. \pi \left|\right. x \left.\right) = \left(n + 1\right) \left(\right. \genfrac{}{}{0pt}{}{n}{x} \left.\right) \pi^{x} \left(\right. 1 - \pi \left.\right)^{n - x}$

che ha come valore modale $p$ (e dunque come valore più probabile)

$p = \frac{x}{n}$, che corrisponde alla stima usata in ambito frequentistico,

mentre il [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso"), ossia la media, coincide con il valore che [minimizza lo scarto quadratico](https://it.wikipedia.org/wiki/Metodo_dei_minimi_quadrati "Metodo dei minimi quadrati"): esso è

$p = \frac{x + 1}{n + 2}$, che per $x<n/2$ è maggiore del valore modale $\frac{x}{n} .$

#### Variabili casuali Beta, Binomiale e Beta-Binomiale

Nel caso di una variabile casuale binomiale $Binom(n;π)$ con [distribuzione a priori coniugata](https://it.wikipedia.org/wiki/Distribuzione_a_priori_coniugata "Distribuzione a priori coniugata") $Beta(a,b)$ della $π$, la variabile casuale che descrive la probabilità di ottenere $x$ eventi positivi su $n$ è distribuita come una [variabile casuale Beta-Binomiale](https://it.wikipedia.org/wiki/Variabile_casuale_Beta-Binomiale?action=edit&redlink=1 "Variabile casuale Beta-Binomiale (la pagina non esiste)") $BetaBin(n;a;b)$. La variabile casuale Beta-Binomiale entra così nella formula con la quale si determina in modo bayesiano la probabilità posteriori di un modello.

#### Distribuzioni a priori coniugate e la variabile casuale binomiale negativa

Se $X$ è distribuita come una [variabile casuale binomiale negativa](https://it.wikipedia.org/wiki/Variabile_casuale_binomiale_negativa "Variabile casuale binomiale negativa") con parametri $m$ e $θ$

$f(x|θ)=BinNeg(x|m;θ)$

e il parametro $θ$ è distribuito a priori come una variabile casuale Beta con i parametri $a$ e $b$

$g(θ)=Beta(θ|a;b)$

allora il parametro $θ$ è distribuito a posteriori anch'esso come una variabile casuale Beta, ma con parametri $a+m$ e $b+x$

$g(θ|x)=Beta(θ|a+m;b+x)$

Qualora la distribuzione a priori sia una [variabile casuale rettangolare](https://it.wikipedia.org/wiki/Variabile_casuale_rettangolare "Variabile casuale rettangolare") nell'intervallo $[0;1]$ (ossia ipotizzando a priori tutti i possibili valori di $θ$ equiprobabili), e pertanto $a=1$ e $b=1,$ allora la distribuzione a posteriori è una Beta con parametri $m+1$ e $x+1$ che ha come valore modale $t$ (e dunque come valore più probabile):

$t = \frac{m}{m + x} .$

### La variabile casuale Gamma nell'inferenza bayesiana

La [variabile casuale Gamma](https://it.wikipedia.org/wiki/Variabile_casuale_Gamma "Variabile casuale Gamma") svolge un importante ruolo nell'ambito dell'inferenza bayesiana in quanto per alcune variabili casuali è sia la distribuzione a priori che la distribuzione a posteriori (con parametri diversi) dei parametri di tali variabili casuali.

#### Distribuzioni a priori coniugate e la stessa variabile casuale Gamma

Se $X$ è distribuita come una variabile casuale Gamma con parametri $α$ e $θ$

$f(x|θ)=Gamma(x|α;θ)$

e il parametro $θ$ è distribuito a priori a sua volta come una variabile casuale Gamma con i parametri $a$ e $b$

$g(θ)=Gamma(θ|a;b),$

allora il parametro $θ$ è distribuito a posteriori anch'esso come una variabile casuale Gamma, ma con parametri $a+α$ e $b+x$

$g(θ|x)=Gamma(θ|a+α;b+x).$

#### Distribuzioni a priori coniugate e la variabile casuale di Poisson

Se $X$ è distribuita come una [variabile casuale di Poisson](https://it.wikipedia.org/wiki/Variabile_casuale_di_Poisson "Variabile casuale di Poisson") con parametro $λ$

$f(x|λ)=Poisson(x|λ)$

e il parametro $λ$ è distribuito a priori come una variabile casuale Gamma con i parametri $a$ e $b$

$g(λ)=Gamma(λ|a;b),$

allora il parametro $λ$ è distribuito a posteriori anch'esso come una variabile casuale Gamma, ma con parametri $a+x$ e $b+n$

$g(λ|x)=Gamma(θ|a+x;b+n).$

#### Variabili casuali Poissoniana, Gamma e Poisson-Gamma

Nel caso che la distribuzione a priori coniugata di una variabile casuale di Poisson sia una variabile casuale Gamma, allora la probabilità che si realizzino $x$ eventi è distribuita come una [variabile casuale Poisson-Gamma](https://it.wikipedia.org/wiki/Variabile_casuale_Poisson-Gamma "Variabile casuale Poisson-Gamma"). La Poisson-Gamma entra così nella formula con la quale si determina in modo bayesiano la probabilità di un modello dopo aver conosciuto i dati.

#### Variabili casuali esponenziale, Gamma e Gamma-Gamma

Nel caso che la distribuzione a priori coniugata di una [variabile casuale esponenziale](https://it.wikipedia.org/wiki/Variabile_casuale_esponenziale "Variabile casuale esponenziale") sia una variabile casuale Gamma, allora la [funzione di densità di probabilità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità") è distribuita come una [variabile casuale Gamma-Gamma](https://it.wikipedia.org/wiki/Variabile_casuale_Gamma-Gamma?action=edit&redlink=1 "Variabile casuale Gamma-Gamma (la pagina non esiste)").

### Distribuzioni a priori coniugate e la variabile casuale normale

#### Variabile casuale Gamma come priori coniugati della variabile casuale normale

Se $X$ è distribuita come una [variabile casuale normale](https://it.wikipedia.org/wiki/Variabile_casuale_normale "Variabile casuale normale") con parametri $μ$ e $1/θ$

$f(x|λ)=N(x|μ;1/θ)$

e il parametro $θ$ è distribuito a priori come una variabile casuale Gamma con i parametri $a$ e $b$

$g(λ)=Gamma(λ|a;b),$

allora il parametro $θ$ è distribuito a posteriori anch'esso come una variabile casuale Gamma, ma con parametri $a+1/2$ e $b + \left(\right. \mu - x \left.\right)^{2} / 2$

$g \left(\right. \theta \left|\right. x \left.\right) = G a m m a \left(\right. \theta \left|\right. a + 1 / 2 ; b + \left(\mu - x \left.\right)^{2} / 2\right) .$

#### Distribuzioni a priori coniugate normali di una normale

Se $X$ è distribuita come una [variabile casuale normale](https://it.wikipedia.org/wiki/Variabile_casuale_normale "Variabile casuale normale") con parametri $m$ e $\sigma^{2}$

$f \left(\right. x \left|\right. m \left.\right) = N \left(\right. x \left|\right. m ; 1 / r^{2} \left.\right)$

e il parametro $m$ è distribuito a priori come una variabile casuale normale con i parametri $μ$ e $\sigma^{2}$

$g \left(m\right) = N \left(\right. m \left|\right. \mu ; 1 / \sigma^{2} \left.\right) ,$

allora il parametro $m$ è distribuito a posteriori anch'esso come una variabile casuale normale, ma con parametri $\left(\sigma^{2} \mu + r^{2} x\right) / \left(\sigma^{2} + r^{2}\right)$ e $\left(\sigma^{2} r^{2}\right) / \left(\sigma^{2} + r^{2}\right)$

$g \left(\right. m \left|\right. x \left.\right) = N \left(\right. m \left|\right. \left(\sigma^{2} \mu + r^{2} x\right) / \left(\sigma^{2} + r^{2}\right) ; \left(\sigma^{2} r^{2}\right) / \left(\sigma^{2} + r^{2}\right) \left.\right) .$

#### La variabile casuale Dirichlet come distribuzione a priori coniugata della multinominale

Se $X$ è distribuita come una [variabile casuale multinomiale](https://it.wikipedia.org/wiki/Variabile_casuale_multinomiale "Variabile casuale multinomiale")

$f \left(\right. x \left|\right. \theta \left.\right) = M u l t i n o m i a l e_{k} \left(\theta_{1} , \theta_{2} , \ldots , \theta_{k}\right)$

e la distribuzione a priori di $θ$ è una [variabile casuale di Dirichlet](https://it.wikipedia.org/wiki/Variabile_casuale_di_Dirichlet "Variabile casuale di Dirichlet")

$g \left(\theta\right) = D i r i c h l e t \left(\alpha_{1} , \alpha_{2} , \ldots , \alpha_{k}\right) ,$

allora la distribuzione a posteriori di $θ$ è anch'essa una variabile casuale di Dirichlet, ma con nuovi parametri

$g \left(\right. \theta \left|\right. x \left.\right) = D i r i c h l e t \left(\alpha_{1} + x_{1} , \alpha_{2} + x_{k} , \ldots , \alpha_{k} + x_{k}\right) .$

#### L'uniforme discreta nel caso di estrazione semplice

Se $X$ è distribuita come in seguito ad una estrazione semplice di una popolazione dicotomica

$f(x|θ)=θ/n$

e il parametro $θ$ è distribuito apriori come una [variabile casuale uniforme discreta](https://it.wikipedia.org/wiki/Variabile_casuale_uniforme_discreta "Variabile casuale uniforme discreta")

$g(θ)=1/n,$

allora la distribuzione a posteriori con la funzione di probabilità

$g(θ|x)=2θ/(n+1).$

## Esempio in R

Utilizzando il [linguaggio di programmazione](https://it.wikipedia.org/wiki/Linguaggio_di_programmazione "Linguaggio di programmazione") R ed il software RStudio si vuole calcolare l' [intervallo di credibilità](https://it.wikipedia.org/wiki/Intervallo_di_credibilit%C3%A0 "Intervallo di credibilità") al 95% del reddito familiare medio degli abitanti degli Stati Uniti, cioè l'intervallo che contiene il reddito medio con probabilità del 95%. Nel seguito si utilizzerà la variabile "coninc" che all'interno del [dataset](https://it.wikipedia.org/wiki/Dataset "Dataset") "General Social Surveys (GSS)" è il reddito dichiarato dagli intervistati del sondaggio. Il dataset usato è stato ottenuto tramite Il "General Social Surveys", un questionario sottoposto a persone intervistate di 18 anni o più che parlavano in inglese all'interno degli [Stati Uniti d'America](https://it.wikipedia.org/wiki/Stati_Uniti_d'America "Stati Uniti d'America"). Tali interviste sono state fatte tra il 1972 e il 2014 e ciascuna contiene 114 variabili di cui alcune numeriche ed altre categoriali.

La funzione bayes\_inference si utilizza per costruire intervalli credibili e condurre test di ipotesi bayesiani. Il primo argomento y specifica la variabile di risposta che ci interessa: coninc (reddito). Il secondo argomento, data, specifica il dataset gss che contiene la variabile coninc. Il terzo argomento statistic è la statistica che stiamo utilizzando cioè mean (media). L'argomento type specifica il tipo di inferenza che vogliamo: intervalli credibili (type = "ci"), o [test di verifica d'ipotesi](https://it.wikipedia.org/wiki/Test_di_verifica_d'ipotesi "Test di verifica d'ipotesi") ( type = "ht" ). L'argomento prior\_family indica quale [distribuzione di probabilità a priori](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0_a_priori "Distribuzione di probabilità a priori") utilizzeremo per l'inferenza cioè JZS (Zellner-Siow Cauchy) centrata nella media del campione mu\_0 = 44503. La funzione restituisce l'intervallo di credibilità per cui possiamo affermare che c'è una probabilità del 95% che il reddito medio degli abitanti degli Stati Uniti tra il 1972 e il 2014 risulta compreso nell'intervallo di credibilità \[44.189$, 44.810$\]

```
library(statsr)

bayes_inference(y = coninc, data = gss,
               statistic = "mean", type = "ci",
               prior_family = "JZS", mu_0 = 44503, rscale = 1,
               method = "theoretical",
               cred_level = 0.95)
```

```
Single numerical variable
n = 51232, y-bar = 44503.04, s = 35936.01
(Assuming Zellner-Siow Cauchy prior:  mu | sigma^2 ~ C(44503, 1*sigma)
(Assuming improper Jeffreys prior: p(sigma^2) = 1/sigma^2
Posterior Summaries
           2.5%      25%      50%      75%     97.5%
mu    44189.674 44392.69 44501.66 44606.73  44810.59
sigma 35718.865 35861.39 35935.37 36013.54  36160.92
n_0    1000.559 11594.29 27811.80 57061.59 148919.82
95% CI for mu: (44189.6736, 44810.5948)
```

Inoltre volendo calcolare l'intervallo di credibilità al 95% della percentuale vera di nativi statunitensi tra il 1972 e il 2014, utilizzando la variabile born che può assumere i valori Yes o No, possiamo affermare che c'è una probabilità del 95% che la percentuale vera di nativi statunitensi tra il 1972 e il 2014 risulta compresa nell'intervallo di credibilità \[91,17%, 91,67%\].

```
library(statsr)

bayes_inference(y = born, data = gss,
                statistic = "proportion", type = "ci",
                prior_family = "JZS", rscale = 1,
                method = "theoretical", success = "Yes",
                cred_level = 0.95, beta_prior = c(1,1))
```

```
Single categorical variable, success: Yes
n = 47804, p-hat = 0.9143
95% CI: (0.9117 , 0.9167)
```

## Popolarità dell'inferenza bayesiana

L'inferenza bayesiana ha a lungo rappresentato una corrente minoritaria nella teoria della [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica"). Ciò è in larga parte dovuto alle difficoltà algebriche che essa pone; la computazione delle probabilità a posteriori è basata sul calcolo di [integrali](https://it.wikipedia.org/wiki/Integrale "Integrale"), per i quali spesso non si hanno espressioni analitiche.

Queste difficoltà hanno fino a pochi anni fa limitato la capacità della statistica bayesiana di produrre modelli realistici della realtà. Al fine di evitare di incorrere in problemi algebrici, gran parte dei risultati erano basati sulla teoria delle [coniugate](https://it.wikipedia.org/wiki/Coniugata?action=edit&redlink=1 "Coniugata (la pagina non esiste)"), particolari famiglie di distribuzioni per cui la probabilità a posteriori risulta avere la stessa forma di quella a priori. Chiaramente un approccio di questo tipo non andava d'accordo con l'ambizione dei bayesiani di fare statistica a partire da ipotesi meno restrittive di quelle dell'inferenza classica.

Grazie alla maggiore disponibilità di risorse informatiche a partire dagli [anni novanta](https://it.wikipedia.org/wiki/Anni_1990 "Anni 1990"), è stato possibile superare tali difficoltà. È infatti possibile risolvere gli [integrali](https://it.wikipedia.org/wiki/Integrale "Integrale") in via numerica, aggirando i problemi algebrici, nella maggior parte delle applicazioni su un qualsiasi [personal computer](https://it.wikipedia.org/wiki/Personal_computer "Personal computer"). Questa possibilità ha inoltre stimolato l'applicazione alla statistica Bayesiana di metodi numerici sviluppati in altri contesti, come quelli basati sulla simulazione ([metodo Monte Carlo](https://it.wikipedia.org/wiki/Metodo_Monte_Carlo "Metodo Monte Carlo"), algoritmi del [campionamento di Gibbs](https://it.wikipedia.org/wiki/Campionamento_di_Gibbs "Campionamento di Gibbs") e [Metropolis-Hastings](https://it.wikipedia.org/wiki/Algoritmo_di_Metropolis-Hastings "Algoritmo di Metropolis-Hastings")), nonché lo sviluppo di metodi nuovi nell'ambito della statistica bayesiana stessa (ad esempio i popolari metodi basati sulla [catena di Markov Monte Carlo](https://it.wikipedia.org/wiki/Catena_di_Markov_Monte_Carlo "Catena di Markov Monte Carlo"), o MCMC). Ciò ha notevolmente incrementato la popolarità dell'inferenza bayesiana tra gli statistici; sebbene i bayesiani costituiscano ancora una minoranza, si tratta di una minoranza in rapida crescita.

Al di là delle difficoltà algebriche che hanno a lungo reso impopolare l'inferenza bayesiana o delle problematiche epistemologiche che i metodi bayesiani sollevano, l'approccio bayesiano ha il merito di aver stimolato, nella [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica") come in altre discipline (un recente esempio è dato dall' [economia](https://it.wikipedia.org/wiki/Economia "Economia")), la riflessione su cosa sia un [modello](https://it.wikipedia.org/wiki/Modello_\(scienza\) "Modello (scienza)") e su che lettura un ricercatore ne deve dare.

## Voci correlate

- [Thomas Bayes](https://it.wikipedia.org/wiki/Thomas_Bayes "Thomas Bayes")
- [Pierre Simon Laplace](https://it.wikipedia.org/wiki/Pierre_Simon_Laplace "Pierre Simon Laplace")
- [Teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes")
- [Statistica bayesiana](https://it.wikipedia.org/wiki/Statistica_bayesiana "Statistica bayesiana")
- [Filtro bayesiano](https://it.wikipedia.org/wiki/Filtro_bayesiano "Filtro bayesiano")
- [Inferenza bayesiana in filogenesi](https://it.wikipedia.org/wiki/Inferenza_bayesiana_in_filogenesi "Inferenza bayesiana in filogenesi")

## Altri progetti

Altri progetti

- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Bayesian_inference?uselang=it)

- contiene immagini o altri file su **[inferenza bayesiana](https://commons.wikimedia.org/wiki/Category:Bayesian_inference?uselang=it)**

## Collegamenti esterni

- [International Society for Bayesian Analysis](https://www.bayesian.org/), su bayesian.org.
- (EN) Edward N. Zalta (a cura di), [Bayesian Epistemology](http://plato.stanford.edu/entries/epistemology-bayesian/), in [Stanford Encyclopedia of Philosophy](https://it.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy "Stanford Encyclopedia of Philosophy"), Center for the Study of Language and Information (CSLI), [Università di Stanford](https://it.wikipedia.org/wiki/Universit%C3%A0_di_Stanford "Università di Stanford").
- (EN) Edward N. Zalta (a cura di), [Bayes' Theorem](http://plato.stanford.edu/entries/bayes-theorem/), in [Stanford Encyclopedia of Philosophy](https://it.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy "Stanford Encyclopedia of Philosophy"), Center for the Study of Language and Information (CSLI), [Università di Stanford](https://it.wikipedia.org/wiki/Universit%C3%A0_di_Stanford "Università di Stanford").
- (EN) Edward N. Zalta (a cura di), [Interpretations of Probability](http://plato.stanford.edu/entries/probability-interpret/), in [Stanford Encyclopedia of Philosophy](https://it.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy "Stanford Encyclopedia of Philosophy"), Center for the Study of Language and Information (CSLI), [Università di Stanford](https://it.wikipedia.org/wiki/Universit%C3%A0_di_Stanford "Università di Stanford").
- (EN) Edward N. Zalta (a cura di), [Inductive logic](http://plato.stanford.edu/entries/logic-inductive/), in [Stanford Encyclopedia of Philosophy](https://it.wikipedia.org/wiki/Stanford_Encyclopedia_of_Philosophy "Stanford Encyclopedia of Philosophy"), Center for the Study of Language and Information (CSLI), [Università di Stanford](https://it.wikipedia.org/wiki/Universit%C3%A0_di_Stanford "Università di Stanford").
- (EN) A.N. Shiryaev, [Bayesian approach to statistical problems](https://www.encyclopediaofmath.org/index.php/Bayesian_approach_to_statistical_problems), in [Encyclopaedia of Mathematics](https://it.wikipedia.org/wiki/Encyclopaedia_of_Mathematics "Encyclopaedia of Mathematics"), Springer e European Mathematical Society, 2002.
- (EN) L.N. Bol'shev, [Bayesian approach, empirical](https://www.encyclopediaofmath.org/index.php/Bayesian_approach,_empirical), in [Encyclopaedia of Mathematics](https://it.wikipedia.org/wiki/Encyclopaedia_of_Mathematics "Encyclopaedia of Mathematics"), Springer e European Mathematical Society, 2002.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [36249](https://thes.bncf.firenze.sbn.it/termine.php?id=36249) · [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh85012506](http://id.loc.gov/authorities/subjects/sh85012506) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4144220-9](https://d-nb.info/gnd/4144220-9) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007282424705171](https://www.nli.org.il/en/authorities/987007282424705171) |
| --- | --- |