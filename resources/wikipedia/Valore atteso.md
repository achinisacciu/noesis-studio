---
title: "Valore atteso"
source: "https://it.wikipedia.org/wiki/Valore_atteso"
author:
  - "[[Wikipedia]]"
published: 2003-04-13
created: 2026-11-06
description:
tags:
  - "clippings"
---
![Questo grafico mostra la convergenza della successione del valor medio dei risultati di un dado a sei facce al valore atteso 3,5 al crescere del numero di tiri.](https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f9/Largenumbers.svg/250px-Largenumbers.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Questo grafico mostra la convergenza della successione del valor medio dei risultati di un dado a sei facce al valore atteso 3,5 al crescere del numero di tiri.

In [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità") il **valore atteso** (chiamato anche **media** o **speranza matematica**) di una [variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") $X$ è un numero indicato con $𝔼[X]$ (da *expected value* o *expectation* in inglese o dal francese *espérance*) che formalizza l'idea euristica di *valore medio* di un fenomeno aleatorio.

In generale il valore atteso di una [variabile casuale discreta](https://it.wikipedia.org/wiki/Variabile_casuale_discreta "Variabile casuale discreta") (che assuma cioè solo un numero [finito](https://it.wikipedia.org/wiki/Insieme_finito "Insieme finito") o una infinità [numerabile](https://it.wikipedia.org/wiki/Insieme_numerabile "Insieme numerabile") di valori) è dato dalla somma dei possibili valori di tale variabile, ciascuno moltiplicato per la probabilità di essere assunto (ossia di verificarsi), cioè è la [media ponderata](https://it.wikipedia.org/wiki/Media_ponderata "Media ponderata") dei possibili risultati. Per una [variabile casuale continua](https://it.wikipedia.org/wiki/Variabile_casuale_continua "Variabile casuale continua") la questione è più delicata e si deve ricorrere alla [teoria della misura](https://it.wikipedia.org/wiki/Misura_\(matematica\) "Misura (matematica)") e all' [integrale di Lebesgue-Stieltjes](https://it.wikipedia.org/wiki/Integrale_di_Lebesgue-Stieltjes "Integrale di Lebesgue-Stieltjes").

Per esempio, nel celebre gioco [testa o croce](https://it.wikipedia.org/wiki/Testa_o_croce "Testa o croce"), se scegliamo "testa" e ipotizziamo un valore di 100 per la vittoria (testa) e di zero per la sconfitta (croce), il valore atteso del gioco è 50, ovvero la media delle vincite e perdite pesata in base alle probabilità (50% per entrambi i casi): $100⋅0,5+0⋅0,5=50$, cioè il valore di "testa" per la sua probabilità e il valore di "croce" per la sua probabilità.

## Definizione matematica

Sia $(Ω,𝔉,ℙ)$ uno [spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità") e $X$ una variabile aleatoria a [valori reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale") su tale spazio (ossia una [funzione misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") $X:Ω→ℝ$, dove i numeri reali si intendono equipaggiati con la loro [σ-algebra boreliana](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel")). Il valore atteso di $X$ è l'integrale di $X$ rispetto alla misura di probabilità $ℙ$:

$\mathbb{E} \left(X\right) := \int_{\Omega} X \left(\omega\right) d \mathbb{P} \left(\omega\right) .$

### Calcolare il valore atteso di variabili aleatorie discrete

Nel caso di [variabile casuale discreta](https://it.wikipedia.org/wiki/Variabile_casuale_discreta "Variabile casuale discreta") che ammette [funzione di probabilità](https://it.wikipedia.org/wiki/Funzione_di_probabilit%C3%A0 "Funzione di probabilità") $p_{i}$ è definita come

$\mathbb{E} \left[X\right] = \sum_{i = 1}^{\infty} x_{i} p_{i} .$

### Calcolare il valore atteso di variabili aleatorie assolutamente continue

Nel caso di [variabile casuale continua](https://it.wikipedia.org/wiki/Variabile_casuale_continua "Variabile casuale continua") che ammette [funzione di densità di probabilità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità") $f(x)$ la definizione diventa

$\mathbb{E} \left[X\right] = \int_{- \infty}^{\infty} x f \left(x\right) d x .$

### Speranza matematica finita

Si dice che $X$ ha speranza finita nel discreto se

$\mathbb{E} \left[\left|X\right|\right] = \sum_{i = 1}^{\infty} \left|x_{i}\right| p_{i} < + \infty ,$

mentre nel continuo se

$\mathbb{E} \left[\left|X\right|\right] = \int_{- \infty}^{\infty} \left|x\right| f \left(x\right) d x < + \infty .$

## Proprietà

### Media di una costante

La media di una costante $c$ (cioè di una variabile casuale che assume il valore $c$ con probabilità 1) è la costante stessa:

$𝔼[c]=c$.

### Linearità

Un'importante caratteristica del valore atteso è la [linearità](https://it.wikipedia.org/wiki/Operatore_lineare "Operatore lineare"): ovvero per ogni variabile casuale X e coppia di [numeri reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale") $a$ e $b$ si ha

$𝔼[aX+b]=a𝔼[X]+b.$

Questa proprietà è facilmente dimostrabile: per esempio, nel caso di una variabile casuale discreta, si ha

$\mathbb{E} \left[a X + b\right] = \sum_{i = 1}^{\infty} \left(a x_{i} + b\right) P \left(X = x_{i}\right) = a \sum_{i = 1}^{\infty} x_{i} P \left(X = x_{i}\right) + b \sum_{i = 1}^{\infty} P \left(X = x_{i}\right) = a \mathbb{E} \left[X\right] + b ,$

perché la somma delle probabilità è 1, in quanto consideriamo la somma di tutti i possibili eventi.

Questa proprietà ha la conseguenza importante che date due variabili casuali qualsiasi $X$ e $Y$ (non necessariamente [indipendenti](https://it.wikipedia.org/wiki/Indipendenza_\(probabilit%C3%A0\) "Indipendenza (probabilità)")) si ha

$𝔼[X+Y]=𝔼[X]+𝔼[Y].$

Questa proprietà non vale per il prodotto: in generale, $𝔼[XY]$ è diverso da $𝔼[X]𝔼[Y].$ Quando queste due quantità sono uguali, si dice che $X$ e $Y$ sono [non correlate](https://it.wikipedia.org/wiki/Correlazione_\(statistica\) "Correlazione (statistica)"). In particolare, due variabili casuali indipendenti sono non correlate.

### Monotonia

Se i valori che assume una variabile casuale $X$ sono compresi tra due estremi $a$ e $b$, così sarà la media di $X$; infatti

$\mathbb{E} \left[X\right] = \sum_{i = 1}^{\infty} x_{i} P \left(X = x_{i}\right) > a \sum_{i = 1}^{\infty} P \left(X = x_{i}\right) = a ,$

e allo stesso modo si dimostra nel caso continuo. Da questo si deduce che se due variabili casuali verificano $X≥Y$ (ossia, per ogni evento $E,$ il valore di $X$ in corrispondenza di quell'evento è maggiore o uguale di quello di $Y$), allora

$𝔼[X]≥𝔼[Y].$

## Stime del valore atteso

In [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica"), la stima del valore atteso assume un ruolo centrale, in quanto principale parametro usato nella [statistica inferenziale](https://it.wikipedia.org/wiki/Statistica_inferenziale "Statistica inferenziale"). Comunemente esso verrà stimato dalla [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") dei valori del campione (ad esempio la media aritmetica) o, nelle applicazioni, dalla cosiddetta [trimmed mean](https://it.wikipedia.org/wiki/Trimmed_mean "Trimmed mean"), ossia la media che tiene conto solo dei valori più centrali del campione (ad esempio solo del 50% dei valori più centrali). La trimmed mean viene spesso preferita alla rispettiva media poiché è considerato un dato statistico più robusto, ossia meno suscettibile di variazioni in presenza di valori anomali del campione.

## Calcolo del valore atteso nel gioco

### Gioco dei dadi

Nel [gioco dei dadi](https://it.wikipedia.org/wiki/Dado_\(gioco\) "Dado (gioco)"), rappresentando il risultato del tiro del dado con una variabile casuale che possa assumere i valori $1,2,3,4,5,6$, ciascuno con probabilità $1/6,$ intuitivamente, la *media* di questa variabile casuale sarà $3,5$, dal momento che $1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + 3 \cdot \frac{1}{6} + 4 \cdot \frac{1}{6} + 5 \cdot \frac{1}{6} + 6 \cdot \frac{1}{6} = 3 , 5.$

### Gioco del lotto

- Nel [gioco del lotto](https://it.wikipedia.org/wiki/Gioco_del_lotto "Gioco del lotto") vengono estratti $5$ numeri tra $1$ e $90$, e un giocatore può *puntare* una certa posta sul verificarsi di vari eventi. Calcoliamo il valore atteso del ricavo di uno scommettitore che punti $10$ [euro](https://it.wikipedia.org/wiki/Euro "Euro") sulle cinque possibili *giocate*.
	- *Numero secco* (si punta sull'uscita di un determinato numero; la vincita paga circa undici volte la posta): la probabilità che il giocatore vinca è data dal rapporto da $5/90$ (rapporto tra i numeri vincenti e tutti i numeri che possono essere estratti), e in tal caso il giocatore vincerà $11⋅10−10=100$ euro; la probabilità di perdita è $85/90,$ e in tal caso il giocatore perderà i $10$ euro di puntata. Il ricavo medio sarà quindi $\frac{5}{90} \cdot 100 - \frac{85}{90} \cdot 10 = - \frac{35}{9} \simeq - 3 , 89.$ Ossia, in media il giocatore perderà $3,89$ euro per ogni $10$ euro giocati.
		- *Ambo* (si punta sull'uscita di una determinata coppia di numeri; la vincita paga $250$ volte la posta): vi sono $\left(\right. \genfrac{}{}{0pt}{}{90}{2} \left.\right) = 4005$ possibili coppie di numeri. Poiché sulla ruota vengono estratti $5$ numeri, gli ambi estratti sono $\left(\right. \genfrac{}{}{0pt}{}{5}{2} \left.\right) = 10$ e pertanto il giocatore vincerà con probabilità $10/4005,$ e in questo caso egli guadagnerà $250⋅10−10=2490$ euro; la probabilità di perdita è $3995/4005,$ e in tal caso il giocatore perderà i $10$ euro di puntata. Il guadagno medio sarà quindi $\frac{10}{4005} \cdot 2490 - \frac{3995}{4005} \cdot 10 \simeq - 3 , 76.$ Ossia, in media il giocatore perderà $3,76$ euro per ogni $10$ euro giocati.
		- *Terno* (si punta sull'uscita di una determinata terna di numeri; la vincita paga $4500$ volte la posta): ci sono $117480$ possibili terne distinte di numeri.
		- *Quaterna* (si punta sull'uscita di una determinata quaterna di numeri; la vincita paga $120000$ volte la posta): ci sono $2555190$ possibili quaterne distinte di numeri.
		- *Cinquina* (si punta sull'uscita di una determinata cinquina di numeri; la vincita paga $6$ milioni di volte la posta): Ci sono $43949268$ possibili cinquine distinte di numeri.

La tabella seguente mostra un riepilogo delle perdite medie per una giocata di importo pari a $1$ euro.

|  | Probabilità di vincita | Quote di vincita per $1$ euro giocato | Perdita media in centesimi |
| --- | --- | --- | --- |
| Numero secco | 1/18 | 11 | 38,9 |
| Ambo | 2/801 | 250 | 37,6 |
| Terna | 1/11748 | 4500 | 61,7 |
| Quaterna | 1/511038 | 120000 | 76,5 |
| Cinquina | 1/43949268 | 6 milioni | 86,3 |

### Poker

Il valore atteso è l'aspettativa, positiva o negativa che sia (ecco perché vedrete spesso le sigle EV- o EV+), che abbiamo ogniqualvolta prendiamo una decisione; cercare di prendere quante più decisioni a valore atteso positivo è fondamentale per vincere nel lungo termine.

Nel poker, ogni volta che scegliamo di fare un **bet**, un **fold** o un **raise**, abbiamo a che fare con un EV positivo o negativo. Alla fine della nostra carriera avremo guadagnato tanto più quante più scelte a EV positivo avremo preso e perso tanto meno quante più scelte a EV negativo avremo evitato.

A volte nel poker capita che sia un bet sia un raise **abbiano entrambi EV positivo**, in questo caso il giocatore con esperienza deve sapere individuare quale sia la mossa con EV maggiore. Quando si gioca a poker non si ha il tempo di calcolare precisamente quale sia l'EV di una determinata mossa e spesso non si sa neanche se la mossa che si è fatta sia vantaggiosa o no, cioè se abbia EV positivo o negativo.

Questo perché il poker è un gioco a informazioni incomplete e quindi, anche volendo, non potremmo calcolare precisamente in ogni momento l'EV di un particolare bet o fold perché non abbiamo a disposizione i dati numerici per effettuare il calcolo. Spesso i giocatori professionisti, lontano dal tavolo da gioco cercano di valutare l'EV di una determinata giocata facendo delle ipotesi sul comportamento degli avversari e sulle carte che hanno in mano.

Queste analisi (spesso molto utili) richiedono tempo e non potrebbero mai essere effettuate durante una partita. Nell'hold'em si presentano continuamente nuovi contesti di gioco, ma spesso è possibile individuare una situazione che è simile a un'altra analizzata precedentemente. Tanto più si ha dimestichezza nell'individuare queste situazioni, tanto più ci si troverà a proprio agio al tavolo da gioco.

Concludendo, l'EV nel poker non è visibilmente presente, ma ogni sforzo che il giocatore fa per “vincere” non è altro che uno sforzo (consapevole o no) per fare scelte con il più elevato EV possibile.

## Bibliografia

- Giorgio Dall'Aglio, Calcolo delle probabilità, Bologna, Zanichelli, 2003, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-88-08-17676-9](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-88-08-17676-9 "Speciale:RicercaISBN/978-88-08-17676-9").
- [Probabilità e lotto](http://www.unipa.it/giuseppe.sanfilippo/pub/sigad/lotto.pdf) (PDF), su unipa.it.

## Voci correlate

- [Teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità")
- [Media (statistica)](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)")
- [Funzione generatrice dei momenti](https://it.wikipedia.org/wiki/Funzione_generatrice_dei_momenti "Funzione generatrice dei momenti")
- [Funzione di densità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0 "Funzione di densità")
- [Funzione di ripartizione](https://it.wikipedia.org/wiki/Funzione_di_ripartizione "Funzione di ripartizione")
- [Valore atteso condizionato](https://it.wikipedia.org/wiki/Valore_atteso_condizionato "Valore atteso condizionato")

## Collegamenti esterni

- (EN) Ken Stewart, [expected value](https://www.britannica.com/topic/expected-value), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Expectation Value](http://mathworld.wolfram.com/ExpectationValue.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4152930-3](https://d-nb.info/gnd/4152930-3) |
| --- | --- |