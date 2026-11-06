---
title: "Processo di Wiener"
source: "https://it.wikipedia.org/wiki/Processo_di_Wiener"
author:
  - "[[Wikipedia]]"
published: 2005-07-18
created: 2026-11-06
description:
tags:
  - "clippings"
---
![](https://it.wikipedia.org/wiki/File:Wiener_process_zoom.png)

Una singola traiettoria di un processo di Wiener unidimensionale

In [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica"), un **processo di Wiener**, conosciuto anche come **moto browniano**, è un [processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico") [gaussiano](https://it.wikipedia.org/wiki/Processo_gaussiano "Processo gaussiano") in tempo continuo con incrementi indipendenti, usato per modellizzare il [moto browniano](https://it.wikipedia.org/wiki/Moto_browniano "Moto browniano") stesso e diversi fenomeni casuali osservati nell'ambito della matematica applicata, della [finanza](https://it.wikipedia.org/wiki/Finanza "Finanza") e della fisica. È uno dei [processi di Lévy](https://it.wikipedia.org/wiki/Processo_di_L%C3%A9vy "Processo di Lévy") meglio conosciuti. Prende il nome dal matematico [Norbert Wiener](https://it.wikipedia.org/wiki/Norbert_Wiener "Norbert Wiener").

Il processo di Wiener ricopre un ruolo importante anche in [matematica pura](https://it.wikipedia.org/wiki/Matematica_pura "Matematica pura"), dove diede vita allo studio della [martingala](https://it.wikipedia.org/wiki/Martingala_\(matematica\) "Martingala (matematica)") a tempo continuo, che risultò fondamentale per la descrizione e la modellizzazione di processi stocastici più complessi. Per questo, questo tipo di processo ricopre un ruolo vitale nel calcolo stocastico, nei processi di diffusione e anche nella [teoria del potenziale](https://it.wikipedia.org/wiki/Teoria_del_potenziale "Teoria del potenziale").

In matematica applicata, il processo di Wiener è usato per rappresentare l'integrale del [rumore bianco](https://it.wikipedia.org/wiki/Rumore_bianco "Rumore bianco") gaussiano; ed è molto utile come modello del rumore in [ingegneria elettronica](https://it.wikipedia.org/wiki/Ingegneria_elettronica "Ingegneria elettronica"), nella teoria dei filtri e per rappresentare gli ingressi sconosciuti nella teoria dei controlli.

## Definizione

Un processo di Wiener $W_{t}$ è caratterizzato dalle seguenti condizioni:

- Il processo parte da 0, ossia $W_{0} = 0$ [quasi certamente](https://it.wikipedia.org/wiki/Quasi_certamente "Quasi certamente").
- Le traiettorie, ossia le funzioni $t \rightarrow W_{t}$ sono continue quasi certamente.
- Il processo ha incrementi indipendenti, ossia scelti quattro tempi $0 \leq s_{1} \leq t_{1} \leq s_{2} \leq t_{2}$ (gli intervalli $\left(s_{1} , t_{1}\right)$ e $\left(s_{2} , t_{2}\right)$ non si intersecano), allora

$W_{t_{1}} - W_{s_{1}}$ e $W_{t_{2}} - W_{s_{2}}$

sono [variabili casuali indipendenti](https://it.wikipedia.org/wiki/Indipendenza_stocastica "Indipendenza stocastica").

- Il processo ha incrementi gaussiani, ossia scelti due tempi $s≤t$

$W_{t} - W_{s} \sim N \left(0 , \left(t - s\right)\right) ,$

dove $N(0,(t−s))$ denota una [distribuzione normale](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale") con [media](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") $0$ e [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") $(t−s)$.

## Proprietà

Dalla definizione segue che, per ogni $t$, la [variabile aleatoria](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") $W_{t}$ ha [distribuzione normale](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale") $N(0,t)$. Da questo fatto possono essere ricavate le seguenti proprietà:

- La [funzione di densità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0 "Funzione di densità") di $W_{t}$ ha legge

$f_{W_{t}} \left(x\right) = \frac{1}{\sqrt{2 \pi t}} e^{- \frac{x^{2}}{2 t}} .$

- Il [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") è

$\mathbb{E} \left[W_{t}\right] = 0.$

- La [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") è

$Var \left(W_{t}\right) = t .$

- La [covarianza](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\) "Covarianza (probabilità)") tra $W_{s}$ e $W_{t}$ è

$Cov \left(W_{s} , W_{t}\right) = min \left(s , t\right) ,$

- La correlazione tra $W_{s}$ e $W_{t}$ è

$Cor \left(W_{s} , W_{t}\right) = \sqrt{\frac{min \left(s , t\right)}{max \left(s , t\right)}} .$

### Massimo e minimo

Sia $M_{t} = \underset{0 \leq s \leq t}{max} \left(W_{s}\right)$ il massimo raggiunto dal moto browniano nell'intervallo $[0,t]$. La densità di probabilità incondizionata di $f_{M_{t}} \left(m\right)$ è data da:

$f_{M_{t}} \left(m\right) = \sqrt{\frac{2}{\pi t}} e^{- \frac{m^{2}}{2 t}} , m \geq 0.$

Il valore atteso del massimo è

$\mathbb{E} \left[M_{t}\right] = \sqrt{\frac{2 t}{\pi}} .$

Se invece $m_{t} = \underset{0 \leq s \leq t}{min} \left(W_{s}\right)$ è il minimo raggiunto dal moto browniano in $[0,t]$, per simmetria dello stesso la densità di probabilità incondizionata di $f_{m_{t}} \left(m\right)$ è data da:

$f_{m_{t}} \left(m\right) = \sqrt{\frac{2}{\pi t}} e^{- \frac{m^{2}}{2 t}} , m \leq 0.$

Il valore atteso del minimo è:

$\mathbb{E} \left[m_{t}\right] = - \sqrt{\frac{2 t}{\pi}} .$

La distribuzione di probabilità di massimi e minimi, condizionata a un valore $W_{t}$ prefissato, è descritta in " [Distribuzione di probabilità dei punti estremanti di un processo stocastico di Wiener](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0_dei_punti_estremanti_di_un_processo_stocastico_di_Wiener "Distribuzione di probabilità dei punti estremanti di un processo stocastico di Wiener") ". Nel caso del minimo, la distribuzione di [probabilità condizionata](https://it.wikipedia.org/wiki/Probabilit%C3%A0_condizionata "Probabilità condizionata") a un valore prefissato $W_{t}$ è:

$F_{m_{W_{t}}} \left(m\right) = P r \left(\right. m_{W_{t}} = \underset{0 \leq s \leq t}{min} W \left(s\right) \leq m \left|\right. W \left(t\right) = W_{t} \left.\right) = e^{- 2 \frac{m \left(m - W_{t}\right)}{t}} , m < min \left(0 , W_{t}\right) .$

### Proprietà di scaling

Se $W_{t}$ è un moto browniano, allora:

- Il processo $V_{t} = W_{t + s} - W_{s}$ è un moto browniano.
- Il processo $V_{t} = - W_{t}$ è un moto browniano.
- Per ogni $c>0$, il processo $V_{t} = c W_{t / c^{2}}$ è un moto browniano.
- Il processo $Z_{t}$ tale che $Z_{0} = 0$ e $Z_{t} = t W_{1 / t} ,$ per $t>0,$ è un moto browniano.

### Regolarità delle traiettorie

Il moto browniano è continuo quasi certamente per definizione. Se si elimina questa condizione dalla sua caratterizzazione, si ottiene un processo non necessariamente continuo. Utilizzando il [teorema di continuità di Kolmogorov](https://it.wikipedia.org/wiki/Teorema_di_continuit%C3%A0_di_Kolmogorov "Teorema di continuità di Kolmogorov") si può però dimostrare che questo processo ha comunque una versione continua quasi certamente. In questo senso, la condizione di continuità seleziona proprio questa versione.

Utilizzando lo stesso teorema, si dimostra anche che quasi certamente ogni traiettoria del moto browniano è holderiana di esponente $γ$ solo per $\gamma < \frac{1}{2}$.

Pur essendo continua su tutto il proprio dominio, la traiettoria del moto browniano non è derivabile in nessun punto.

### Comportamento asintotico

La [legge del logaritmo iterato](https://it.wikipedia.org/wiki/Legge_del_logaritmo_iterato?action=edit&redlink=1 "Legge del logaritmo iterato (la pagina non esiste)") afferma che, se $W_{t}$ è un moto browniano, allora

$\underset{t \rightarrow + \infty}{lim sup} \frac{\left|W_{t}\right|}{\sqrt{2 t log log t}} = 1 , \text{quasi certamente} .$

### Proprietà di martingala

Il processo di Wiener è una [martingala](https://it.wikipedia.org/wiki/Martingala_\(matematica\) "Martingala (matematica)"). Più in particolare, se $W_{t}$ è un processo di Wiener e $p(x,t)$ è un [polinomio](https://it.wikipedia.org/wiki/Polinomio "Polinomio") che soddisfa

$\left(\frac{\partial}{\partial t} + \frac{1}{2} \frac{\partial^{2}}{\partial x^{2}}\right) p \left(x , t\right) = 0 ,$

allora $M_{t} := p \left(W_{t} , t\right)$ è una martingala.

## Differenziale del processo di Wiener

Se si considera il processo di Wiener in corrispondenza di un lasso di tempo sufficientemente piccolo si ottiene l'incremento [infinitesimo](https://it.wikipedia.org/wiki/Infinitesimo "Infinitesimo") di tale processo nella forma

$W_{t + d t} - W_{t} = \delta W_{t} = N \sqrt{d t} , \left(1\right)$

la quale può scriversi come

$\frac{W_{t + d t} - W_{t}}{d t} = \frac{N}{\sqrt{d t}} .$

Tale processo non è a [variazione limitata](https://it.wikipedia.org/wiki/Continuit%C3%A0_uniforme "Continuità uniforme"), e per questo non risulta differenziabile nell'ambito dell'analisi classica. Infatti la precedente tende ad infinito al tendere a zero dell'intervallo $dt$.

Accantonati in parte gli strumenti dell'analisi classica, il differenziale del processo di Wiener può essere comunque definito in senso stocastico. Infatti, essendo la varianza di tale processo

$\mathbb{E} \left[W_{t}^{2}\right] - \mathbb{E}^{2} \left[W_{t}\right] = t$

ed essendo il valore atteso di tale processo nullo

$\mathbb{E} \left[W_{t}\right] = \mathbb{E}^{2} \left[W_{t}\right] = 0 ,$

si ha che la media quadratica del processo di Wiener coincide con il tempo trascorso, ossia

$\mathbb{E} \left[W_{t}^{2}\right] = t .$

In base a ciò possiamo definire il differenziale di un processo di Wiener tramite il differenziale della media quadratica di tale processo. Ossia il differenziale di $W_{t}$ rispetto al tempo è $d W_{t}$ in quanto il differenziale di $t$ è $dt$.

In altre parole: il differenziale di un processo di Wiener è quel processo la cui media quadratica coincide con il differenziale della media quadratica del processo di Wiener da differenziare. In formule:

$\mathbb{E} \left[d W_{t}^{2}\right] = d \mathbb{E} \left[W_{t}^{2}\right] .$

In base a quanto sopra esposto si può definire il differenziale di un processo di Wiener con la formula

$d W_{t} = N \sqrt{d t} ,$

la quale, confrontata con la (1), mostra che secondo l'approccio stocastico $\delta W_{t}$ coincide proprio con $d W_{t}$, e sussistono le proprietà $\mathbb{E} \left[d W_{t}\right] = 0$ e $\text{Var} \left(d W_{t}\right) = d t$.

In termini meno formali il differenziale del processo di Wiener non è altro che un processo di Wiener considerato in un lasso di tempo infinitesimo.

Un'interessante proprietà del processo di Wiener è l'approssimativa non stocasticità del fattore $d W_{t}^{2}$ al tendere a zero del fattore temporale $dt$.

## Bibliografia

- (EN) Takeyuki Hida, Brownian Motion, Berlino, Springer, 2012, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-14-61-26032-5](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-14-61-26032-5 "Speciale:RicercaISBN/978-14-61-26032-5").
- (EN) Ioannis Karatzas e Steve E. Shreve, Brownian Motion and Stochastic Calculus, Berlino, Springer, 2004, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-03-87-97655-6](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-03-87-97655-6 "Speciale:RicercaISBN/978-03-87-97655-6").
- (EN) Daniel Revuz e Marc Yor, Continuous Martingales and Brownian Motion, Berlino, Springer, 1999, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-35-40-64325-8](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-35-40-64325-8 "Speciale:RicercaISBN/978-35-40-64325-8").
- Paolo Baldi, Equazioni differenziali stocastiche, Pitagora editrice, 2000, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-88-371-1211-0](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-88-371-1211-0 "Speciale:RicercaISBN/978-88-371-1211-0").

## Voci correlate

- [Processo di Markov](https://it.wikipedia.org/wiki/Processo_di_Markov "Processo di Markov")
- [Distribuzione di probabilità dei punti estremanti di un processo stocastico di Wiener](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0_dei_punti_estremanti_di_un_processo_stocastico_di_Wiener "Distribuzione di probabilità dei punti estremanti di un processo stocastico di Wiener")

## Altri progetti

Altri progetti

- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Wiener_process?uselang=it)

- contiene immagini o altri file su **[processo di Wiener](https://commons.wikimedia.org/wiki/Category:Wiener_process?uselang=it)**

## Collegamenti esterni

- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Wiener Process](http://mathworld.wolfram.com/WienerProcess.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- (EN) [Processo di Wiener](https://encyclopediaofmath.org/wiki/Wiener%20process), su [Encyclopaedia of Mathematics](https://it.wikipedia.org/wiki/Encyclopaedia_of_Mathematics "Encyclopaedia of Mathematics"), Springer e European Mathematical Society.
- [Un'introduzione al processo di Wiener e alle equazioni stocastiche](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxlbnJpY29wcmlvbGF8Z3g6NWY3ZmM2NWY0YjY1ZjYw) di Enrico Priola. {broken link}
- [Processi di Wiener ed applicazioni](http://www.caressa.it/pdf/000008.pdf) di Paolo Caressa.