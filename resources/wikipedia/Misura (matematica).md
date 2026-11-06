---
title: "Misura (matematica)"
source: "https://it.wikipedia.org/wiki/Misura_(matematica)"
author:
  - "[[Wikipedia]]"
published: 2004-11-06
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [analisi matematica](https://it.wikipedia.org/wiki/Analisi_matematica "Analisi matematica"), una **misura**, talvolta detta **misura positiva**, è una funzione che assegna un numero reale a taluni sottoinsiemi di un dato [insieme](https://it.wikipedia.org/wiki/Insieme "Insieme") per rendere quantitativa la nozione della loro estensione. In particolare, si assegnano lunghezze a segmenti di curva, [aree](https://it.wikipedia.org/wiki/Area "Area") a superfici, [volumi](https://it.wikipedia.org/wiki/Volume "Volume") a figure tridimensionali e [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") ad [eventi](https://it.wikipedia.org/wiki/Evento_\(teoria_della_probabilit%C3%A0\) "Evento (teoria della probabilità)").

La **teoria della misura** è la branca dell' [analisi reale](https://it.wikipedia.org/wiki/Analisi_reale "Analisi reale") e [complessa](https://it.wikipedia.org/wiki/Analisi_complessa "Analisi complessa") che studia [sigma-algebre](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra"), [spazi misurabili](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile"), [insiemi misurabili](https://it.wikipedia.org/wiki/Insieme_misurabile "Insieme misurabile"), misure, [funzioni misurabili](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") ed [integrali](https://it.wikipedia.org/wiki/Integrale "Integrale"). La teoria astratta della misura ha come casi particolari la [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità"), e trova numerose applicazioni in diversi settori della [matematica pura](https://it.wikipedia.org/wiki/Matematica_pura "Matematica pura") ed applicata.

La nozione di misura, e quelle ad essa correlate, sono nate a cavallo tra il [XIX secolo](https://it.wikipedia.org/wiki/XIX_secolo "XIX secolo") ed il [XX secolo](https://it.wikipedia.org/wiki/XX_secolo "XX secolo"), nell'ambito appunto della formalizzazione della *teoria della misura*.[^1]

## Definizione

Sia $𝔉$ una [σ-algebra](https://it.wikipedia.org/wiki/%CE%A3-algebra "Σ-algebra") definita su un insieme $X$. Si definisce *misura* una [funzione](https://it.wikipedia.org/wiki/Funzione_\(matematica\) "Funzione (matematica)") $μ:𝔉→[0,+∞]$ (vedi [retta reale estesa](https://it.wikipedia.org/wiki/Retta_reale_estesa "Retta reale estesa")), con $μ(E)<+∞$ per almeno un $E∈𝔉$, tale da essere [σ-additiva](https://it.wikipedia.org/wiki/Sigma_additivit%C3%A0 "Sigma additività").[^2]

La σ-additività, o additività numerabile, significa che se $E_{1} , E_{2} , \ldots \in \mathfrak{F}$ è una successione di insiemi mutuamente disgiunti, allora:

$\mu \left(\cup_{i = 1}^{+ \infty} E_{i}\right) = \sum_{i = 1}^{+ \infty} \mu \left(E_{i}\right) .$

Gli elementi di $𝔉$ sono detti [insiemi misurabili](https://it.wikipedia.org/wiki/Insieme_misurabile "Insieme misurabile"), e la [struttura](https://it.wikipedia.org/wiki/Struttura_\(matematica\) "Struttura (matematica)") $(X,𝔉,μ)$ viene detta [spazio di misura](https://it.wikipedia.org/wiki/Spazio_di_misura "Spazio di misura").

Una [misura complessa](https://it.wikipedia.org/wiki/Misura_complessa "Misura complessa") è una funzione numerabilmente additiva a valori [complessi](https://it.wikipedia.org/wiki/Numero_complesso "Numero complesso") definita su una σ-algebra.

## Proprietà

Dalla definizione possono essere derivate le seguenti proprietà:

- L'insieme vuoto ha [misura nulla](https://it.wikipedia.org/wiki/Insieme_di_misura_nulla "Insieme di misura nulla"):

$μ(∅)=0.$

- Se $E_{1}$ ed $E_{2}$ sono insiemi misurabili, allora se $E_{1} \subseteq E_{2}$ si ha $\mu \left(E_{1}\right) \leq \mu \left(E_{2}\right)$.
- Se $E_{1} , E_{2} , \ldots$ sono insiemi misurabili e $\forall n \in \mathbb{N} E_{n} \subseteq E_{n + 1}$, allora l'unione degli insiemi $E_{n}$ è misurabile:

$\mu \left(\cup_{i = 1}^{+ \infty} E_{i}\right) = \underset{i \rightarrow + \infty}{lim} \mu \left(E_{i}\right) .$

- Se $E_{1} , E_{2} , \ldots$ sono insiemi misurabili e $\forall n \in \mathbb{N} E_{n + 1} \subseteq E_{n}$, allora l'intersezione degli insiemi $E_{n}$ è misurabile. Inoltre, se almeno uno di tali insiemi ha misura finita, allora

$\mu \left(\cap_{i = 1}^{+ \infty} E_{i}\right) = \underset{i \rightarrow + \infty}{lim} \mu \left(E_{i}\right) .$

## Misure prodotto

Siano $(X,𝔉,μ)$ e $(Y,𝔊,λ)$ due [spazi di misura](https://it.wikipedia.org/wiki/Spazio_di_misura "Spazio di misura"). Ad ogni funzione $f$ definita su $X×Y$ e ad ogni $x∈X$ si può associare la funzione $f_{x} \left(y\right) = f \left(x , y\right)$ definita in $Y$, e per ogni $y∈Y$ si può associare la funzione $f_{y} \left(x\right) = f \left(x , y\right)$.[^3] Per ogni insieme aperto $V∈𝔊×𝔉$ si definisce inoltre:

$Q={(x,y):f(x,y)∈V},Qx={y:fx(y)∈V}.$

Si dimostra che se

$\phi \left(x\right) = \lambda \left(Q_{x}\right) , \psi \left(y\right) = \mu \left(Q_{y}\right) , \forall x \in X , \forall y \in Y ,$

allora $ϕ$ è $𝔉$ -misurabile e $ψ$ è $𝔊$ -misurabile, e si ha:[^4]

$\int_{X} \phi d \mu = \int_{Y} \psi d \lambda .$

Si definisce la misura $μ×λ$ prodotto delle due misure $μ$ e $λ$ l'integrale:[^5]

$\left(\mu \times \lambda\right) \left(Q\right) = \int_{X} \lambda \left(Q_{x}\right) d \mu \left(x\right) = \int_{Y} \mu \left(Q_{y}\right) d \lambda \left(y\right) .$

## Continuità assoluta

Se $μ$ e $ν$ sono misure sulla stessa [sigma-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra"), la misura $μ$ si dice assolutamente continua rispetto a $ν$ se $μ(A)=0$ per ogni insieme $A$ per il quale $ν(A)=0$. Questa situazione viene presentata con la scrittura $μ≪ν$.[^6]

Se esiste inoltre un insieme $B$ tale per cui:

$μ(E)=μ(B∩E),$

per ogni insieme $E$ della sigma-algebra, allora tale misura si dice *concentrata su $B$*. Misure concentrate su insiemi rispettivamente disgiunti sono dette *mutuamente singolari*. In particolare, se $\mu_{1}$ e $\mu_{2}$ sono mutuamente singolari si scrive $\mu_{1} \bot \mu_{2}$.

Un teorema di particolare importanza nell'ambito della continuità assoluta delle misure afferma che se $μ$ e $ν$ sono due misure limitate, allora esiste un'unica coppia di misure positive $\mu_{1} \bot \mu_{2}$ tali che:

$\mu = \mu_{1} + \mu_{2} , \mu_{1} \ll \nu , \mu_{2} \bot \nu .$

Il [teorema di Radon-Nikodym](https://it.wikipedia.org/wiki/Teorema_di_Radon-Nikodym "Teorema di Radon-Nikodym") afferma inoltre che esiste un'unica funzione $h \in L^{1} \left(\nu\right)$ tale che:

$\mu_{1} \left(E\right) = \int_{E} h d \nu ,$

per ogni insieme $E$ della sigma-algebra. La decomposizione

$\mu = \mu_{1} + \mu_{2}$

è detta *decomposizione di Lebesgue* di $μ$ relativamente a $ν$, ed è unica.[^7] La funzione $h$ si dice inoltre *derivata di Radon-Nikodym* di $\mu_{1}$ rispetto $ν$.

Il teorema può essere esteso al caso più generale in cui $μ$ è una [misura complessa](https://it.wikipedia.org/wiki/Misura_complessa "Misura complessa") e $ν$ è sigma-finita e positiva.[^8]

## Differenziabilità di una misura

Sia $μ$ una [misura complessa](https://it.wikipedia.org/wiki/Misura_complessa "Misura complessa") di [Borel](https://it.wikipedia.org/wiki/Misura_di_Borel "Misura di Borel") su $\mathbb{R}^{k}$. Si consideri una famiglia di insiemi $E$ di $\mathbb{R}^{k}$ tale che il diametro di $E$ sia inferiore a $δ$ e tale che esiste una palla $B$ contenente $E$ la cui misura di Lebesgue sia inferiore alla misura di $E$ moltiplicata per una costante finita.

Sia $A$ un numero complesso. Si dice che $μ$ è differenziabile in $x \in \mathbb{R}^{k}$ e si scrive:[^9]

$(Dμ)(x)=A$

se, detta $m$ la [misura di Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue"), per ogni $ϵ>0$ esiste $δ>0$ tale che

$\left|\frac{\mu \left(E\right)}{m \left(E\right)} - A\right| < \epsilon , x \in E .$

Tale espressione è equivalente al [limite](https://it.wikipedia.org/wiki/Limite_\(matematica\) "Limite (matematica)") in cui il diametro dell'insieme $E$ si annulla, ossia il limite in cui l'insieme coincide con il punto $x$.

Si definiscono inoltre la *derivata superiore*:

$\left(\bar{D} \mu\right) \left(x\right) = \underset{\delta \rightarrow 0}{lim} sup \left[\frac{\mu \left(E\right)}{m \left(E\right)}\right]$

e la *derivata inferiore*, ottenuta considerando l'estremo inferiore nella relazione precedente. La misura $μ$ è differenziabile se le derivate superiore e inferiore coincidono e sono finite, e in tal caso sono uguali a $(Dμ)(x)$.[^10]

### Integrale indefinito

Si dimostra che in $\mathbb{R}^{k}$ la misura $μ$ è differenziabile [quasi ovunque](https://it.wikipedia.org/wiki/Quasi_ovunque "Quasi ovunque") rispetto a $m$ e che la sua derivata è [integrabile secondo Lebesgue](https://it.wikipedia.org/wiki/Integrale_di_Lebesgue "Integrale di Lebesgue"). Inoltre, si può definire una misura $\mu_{s}$ tale che

$\mu_{s} \bot m , \left(D \mu_{s}\right) \left(x\right) = 0 ,$

dove $\mu_{s} \bot m$ indica che le misure sono mutuamente singolari. Per ogni insieme di Borel $E$ si ha allora:[^11]

$\mu \left(E\right) = \mu_{s} \left(E\right) + \int_{E} \left(D \mu\right) \left(x\right) d x .$

Come conseguenza di questo fatto, una [condizione necessaria e sufficiente](https://it.wikipedia.org/wiki/Condizione_necessaria_e_sufficiente "Condizione necessaria e sufficiente") alla mutua singolarità $μ⊥m$ è il fatto che $\left(D \mu_{s}\right) \left(x\right) = 0$ quasi ovunque. In generale, due misure sono mutuamente singolari se la derivata di una rispetto all'altra è nulla quasi ovunque.[^12]

Inoltre $(Dμ)(x)$ coincide quasi ovunque con la [derivata di Radon-Nikodym](https://it.wikipedia.org/wiki/Teorema_di_Radon-Nikodym "Teorema di Radon-Nikodym") se e solo se $μ$ è [assolutamente continua](https://it.wikipedia.org/wiki/Continuit%C3%A0_assoluta "Continuità assoluta") rispetto a $m$, ed in tal caso:[^13]

$\left(D \mu\right) \left(x\right) = \frac{d \mu}{d m} , \mu \left(E\right) = \int_{E} \left(D \mu\right) \left(x\right) d x .$

Se si definisce infine *integrale indefinito* di $f \in L^{1} \left(\mathbb{R}^{k}\right)$ l'espressione:[^14]

$\mu \left(E\right) = \int_{E} \left(D \mu\right) \left(x\right) d x ,$

allora la derivata di un integrale indefinito coincide con la funzione integranda, ed inoltre ogni misura $μ$ che è assolutamente continua rispetto a $m$ coincide con l'integrale della sua derivata.

In generale, se $f \in L^{1} \left(\mathbb{R}^{k}\right)$, allora

$f \left(x_{0}\right) = \underset{\delta \rightarrow 0}{lim} \left[\frac{1}{m \left(E\right)} \int_{E} \left(D \mu\right) \left(x\right) d x\right] , x_{0} \in E ,$

per quasi tutti i punti $x_{0} \in \mathbb{R}^{k}$.

## Sigma-finitezza

Uno spazio di misura $(X,𝔉,μ)$ si dice *finito* se $μ(X)$ è un numero reale finito, mentre si dice *σ-finito* se $X$ è l' [unione](https://it.wikipedia.org/wiki/Unione_\(insiemistica\) "Unione (insiemistica)") numerabile di insiemi misurabili di misura finita. Un insieme in uno spazio di misura si dice avere misura σ-finita se è una [unione](https://it.wikipedia.org/wiki/Unione_\(insiemistica\) "Unione (insiemistica)") numerabile di insiemi di misura finita.

Ad esempio, i [numeri reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale") con la usuale [misura di Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue") sono σ-finiti ma non finiti. Si considerino gli [intervalli chiusi](https://it.wikipedia.org/wiki/Intervallo_chiuso "Intervallo chiuso") $[k,k+1]$ per tutti gli [interi](https://it.wikipedia.org/wiki/Numero_intero "Numero intero") $k$: vi è una quantità numerabile di tali intervalli, ciascuno avente misura 1, e la loro unione è l'intera retta reale. Alternativamente, si considerino i [numeri reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale") con la [misura di conteggio](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0#La_misura_del_conteggio "Misura di probabilità"), che assegna ad ogni [insieme finito](https://it.wikipedia.org/wiki/Insieme_finito "Insieme finito") di numeri reali il numero di punti nell'insieme. Questa misura non è σ-finita, in quanto ogni insieme con misura finita contiene solo un insieme finito di punti e sarebbe necessario una quantità non numerabile di tali insiemi per coprire l'intera retta reale. Gli spazi di misura σ-finita risultano avere alcune proprietà molto apprezzabili, e la σ-finitezza può essere confrontata alla [separabilità](https://it.wikipedia.org/wiki/Separabilit%C3%A0 "Separabilità") degli spazi topologici.

## Completezza

Una misura $μ$ si dice *completa* se ogni sottoinsieme di un [insieme di misura nulla](https://it.wikipedia.org/wiki/Insieme_di_misura_nulla "Insieme di misura nulla") è misurabile. Il teorema che sta alla base della definizione afferma che se $(X,𝔉,μ)$ è uno [spazio di misura](https://it.wikipedia.org/wiki/Spazio_di_misura "Spazio di misura") e $\mathfrak{F}^{*}$ l'insieme di tutti gli insiemi $E⊂X$ per i quali esistano due insiemi $A$ e $B$ di $𝔉$ tali che

$μ(B−A)=0,A⊂E⊂B,$

allora, definendo $μ(E)=μ(A)$, $\mathfrak{F}^{*}$ è una σ-algebra e $μ$ una misura su di essa.[^15]

La misura $μ$ estesa in tal modo si dice completa, e $\mathfrak{F}^{*}$ prende il nome di $μ$ -completamento di $𝔉$. Dal teorema segue che ogni misura può essere completata.

## Regolarità

## Generalizzazioni

In alcuni ambiti risulta utile disporre di varianti della misura definita in precedenza che possano assumere valori infiniti o non ristretti al campo reale.

- Le funzioni su insiemi numerabilmente additive che assumono valori dati da numeri reali sono chiamate [misure con segno](https://it.wikipedia.org/wiki/Misura_con_segno "Misura con segno").
- Funzioni su insiemi numerabilmente additive che possono assumere valori complessi si dicono [misure complesse](https://it.wikipedia.org/wiki/Misura_complessa "Misura complessa").
- Le misure con codominio in uno [spazio di Banach](https://it.wikipedia.org/wiki/Spazio_di_Banach "Spazio di Banach") sono chiamate [misure spettrali](https://it.wikipedia.org/wiki/Misura_spettrale "Misura spettrale"), e vengono usate principalmente in [analisi funzionale](https://it.wikipedia.org/wiki/Analisi_funzionale "Analisi funzionale") nell'ambito della [teoria spettrale](https://it.wikipedia.org/wiki/Teoria_spettrale "Teoria spettrale").
- Le *misure finitamente additive* sono misure che, invece della additività numerabile, posseggono soltanto la additività finita. Storicamente questa definizione di misura è stata usata per prima, ma non si è rivelata sufficientemente utile. In generale, le misure finitamente additive sono collegate a nozioni come quella dei [limiti di Banach](https://it.wikipedia.org/wiki/Limite_di_Banach?action=edit&redlink=1 "Limite di Banach (la pagina non esiste)"), duale dello [spazio *L* <sup>∞</sup>](https://it.wikipedia.org/wiki/Spazio_Lp "Spazio Lp") e della [compattificazione di Stone-Čech](https://it.wikipedia.org/wiki/Compattificazione_di_Stone-%C4%8Cech "Compattificazione di Stone-Čech").

Per distinguere una usuale misura a valori positivi dalle sue possibili generalizzazioni si utilizza frequentemente il termine *misura positiva*.

Un importante risultato della [geometria integrale](https://it.wikipedia.org/wiki/Geometria_integrale "Geometria integrale"), noto come [teorema di Hadwiger](https://it.wikipedia.org/wiki/Teorema_di_Hadwiger?action=edit&redlink=1 "Teorema di Hadwiger (la pagina non esiste)"), stabilisce che lo spazio delle funzioni di insieme non necessariamente non negative, invarianti per traslazione e finitamente additive che sono definite nell'insieme delle unioni finite di insiemi compatti [convessi](https://it.wikipedia.org/wiki/Insieme_convesso "Insieme convesso") in $\mathbb{R}^{n}$ consiste (a meno di multipli scalari) di una misura che è omogenea di grado $k$ per qualsiasi $k=0,1,2,…,n$ e di [combinazioni lineari](https://it.wikipedia.org/wiki/Combinazione_lineare "Combinazione lineare") di tali misure. La specificazione "omogeneo di grado $k$ " significa che riscalando di un qualsiasi fattore $c>0$ tutti gli insiemi si moltiplica la misura di insieme per $c^{k}$. La misura omogenea di grado $n$ è l'ordinario volume $n$ -dimensionale, quella omogenea di grado $n−1$ è il volume di superficie, quella omogenea di grado 1 è una funzione chiamata "ampiezza media" mentre la misura omogenea di grado 0 è infine la [caratteristica di Eulero](https://it.wikipedia.org/wiki/Caratteristica_di_Eulero "Caratteristica di Eulero").

## Esempi

- La [misura di conteggio](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0#La_misura_del_conteggio "Misura di probabilità") è definita da $μ(S)≡$ numero di elementi nell'insieme $S$.
- La [misura di Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue") è l'unica misura completa invariante per traslazione sopra una sigma algebra contenente gli [intervalli](https://it.wikipedia.org/wiki/Intervallo_\(matematica\) "Intervallo (matematica)") in $ℝ$ tale che $μ([0,1])=1$.
- La [misura di Haar](https://it.wikipedia.org/wiki/Misura_di_Haar "Misura di Haar") per un [gruppo topologico](https://it.wikipedia.org/wiki/Gruppo_topologico "Gruppo topologico") [localmente compatto](https://it.wikipedia.org/wiki/Spazio_localmente_compatto "Spazio localmente compatto") è una generalizzazione della misura di Lebesgue ed ha una proprietà di unicità simile alla precedente.
- La misura zero è definita da $μ(S)≡0$ per ogni insieme $S$.
- Ad ogni [spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità") si associa una misura che assume il valore 1 sull'intero spazio (e di conseguenza assume tutti i suoi valori nell' [intervallo unitario](https://it.wikipedia.org/wiki/Intervallo_unitario "Intervallo unitario") $[0,1]$). Questa misura viene detta [misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità") (si veda anche [assiomi della probabilità](https://it.wikipedia.org/wiki/Assiomi_della_probabilit%C3%A0 "Assiomi della probabilità")).

## Note

## Bibliografia

- (EN) Walter Rudin, [Real and Complex Analysis](https://archive.org/details/realcomplexanaly0000rudi), Mladinska Knjiga, McGraw-Hill, 1970, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-07-054234-1](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-07-054234-1 "Speciale:RicercaISBN/0-07-054234-1").
- (EN) Patrick Billingsley, [Probability and measure](https://archive.org/details/probabilitymeasu0000bill), 3rd edition, New York, [John Wiley & Sons](https://it.wikipedia.org/wiki/John_Wiley_&_Sons "John Wiley & Sons"), 1995, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-471-00710-2](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-471-00710-2 "Speciale:RicercaISBN/0-471-00710-2"),..
- (EN) Carl B. Boyer, [History of Mathematics](https://archive.org/details/historyofmathema0000boye_y4y8), 2nd edition, New York, [John Wiley & Sons](https://it.wikipedia.org/wiki/John_Wiley_&_Sons "John Wiley & Sons"), 1989, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-471-54397-7](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-471-54397-7 "Speciale:RicercaISBN/0-471-54397-7").
- (EN) Donald L. Cohn, [Measure Theory](https://archive.org/details/measuretheory0000cohn), Boston, Birkhäuser, 1980, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-8493-7157-0](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-8493-7157-0 "Speciale:RicercaISBN/0-8493-7157-0").
- (EN) [Paul R. Halmos](https://it.wikipedia.org/wiki/Paul_Halmos "Paul Halmos"), [Measure Theory](https://archive.org/details/measuretheory00halm), New York, Springer-Verlag, 1974, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-387-90088-8](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-387-90088-8 "Speciale:RicercaISBN/0-387-90088-8").
- (EN) Eric M. Verstrup, [The Theory of Measures and Integration](https://archive.org/details/theoryofmeasures0000vest), Hoboken, [John Wiley & Sons](https://it.wikipedia.org/wiki/John_Wiley_&_Sons "John Wiley & Sons"), 2003, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-471-24977-7](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-471-24977-7 "Speciale:RicercaISBN/0-471-24977-7").

## Voci correlate

- [Funzione misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile")
- [Misura di Borel](https://it.wikipedia.org/wiki/Misura_di_Borel "Misura di Borel")
- [Misura di Haar](https://it.wikipedia.org/wiki/Misura_di_Haar "Misura di Haar")
- [Misura di Hausdorff](https://it.wikipedia.org/wiki/Misura_di_Hausdorff "Misura di Hausdorff")
- [Misura di Jordan](https://it.wikipedia.org/wiki/Misura_di_Jordan "Misura di Jordan")
- [Misura di Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue")
- [Misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità")
- [Misura esterna](https://it.wikipedia.org/wiki/Misura_esterna "Misura esterna")
- [Misura regolare](https://it.wikipedia.org/wiki/Misura_regolare "Misura regolare")
- [Sigma-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra")
- [Spazio di misura](https://it.wikipedia.org/wiki/Spazio_di_misura "Spazio di misura")
- [Spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile")

## Altri progetti

Altri progetti

- [Wikizionario](https://it.wiktionary.org/wiki/misura "wikt:misura")
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Measures_\(measure_theory\)?uselang=it)

- [Wikizionario](https://it.wiktionary.org/wiki/ "wikt:") contiene il lemma di dizionario « **[misura](https://it.wiktionary.org/wiki/misura "wikt:misura")** »
- contiene immagini o altri file su **[misura](https://commons.wikimedia.org/wiki/Category:Measures_\(measure_theory\)?uselang=it)**

## Collegamenti esterni

- (EN) [measure](https://www.britannica.com/topic/measure-mathematics), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Measure](http://mathworld.wolfram.com/Measure.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- (EN) [Misura](https://encyclopediaofmath.org/wiki/measure), su [Encyclopaedia of Mathematics](https://it.wikipedia.org/wiki/Encyclopaedia_of_Mathematics "Encyclopaedia of Mathematics"), Springer e European Mathematical Society.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [24181](https://thes.bncf.firenze.sbn.it/termine.php?id=24181) |
| --- | --- |

[^1]: Un breve resoconto dello sviluppo storico della teoria della misura e dell'integrazione si trova testo di Boyer *History of Mathematics*

[^2]: [W. Rudin](#CITEREFrudin), Pag. 16.

[^3]: [W. Rudin](#CITEREFrudin), Pag. 138.

[^4]: [W. Rudin](#CITEREFrudin), Pag. 139.

[^5]: [W. Rudin](#CITEREFrudin), Pag. 140.

[^6]: [W. Rudin](#CITEREFrudin), Pag. 121.

[^7]: [W. Rudin](#CITEREFrudin), Pag. 122.

[^8]: [W. Rudin](#CITEREFrudin), Pag. 124.

[^9]: [W. Rudin](#CITEREFrudin), Pag. 153.

[^10]: [W. Rudin](#CITEREFrudin), Pag. 152.

[^11]: [W. Rudin](#CITEREFrudin), Pag. 154.

[^12]: [W. Rudin](#CITEREFrudin), Pag. 156.

[^13]: [W. Rudin](#CITEREFrudin), Pag. 155.

[^14]: [W. Rudin](#CITEREFrudin), Pag. 157.

[^15]: [W. Rudin](#CITEREFrudin), Pag. 27.