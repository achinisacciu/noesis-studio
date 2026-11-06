---
title: "Misura di probabilità"
source: "https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0"
author:
  - "[[Wikipedia]]"
published: 2005-01-26
created: 2026-11-06
description:
tags:
  - "clippings"
---
Nell'ambito della [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità"), **misura di probabilità** è il nome tecnico della [funzione](https://it.wikipedia.org/wiki/Funzione_\(matematica\) "Funzione (matematica)") che assegna agli esiti di un determinato esperimento la probabilità che tali esiti si realizzino. È importante osservare che la misura di probabilità non assegna la probabilità ai singoli punti dello [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario") (gli eventi elementari) bensì a sottoinsiemi di esso (gli eventi).

Se l'assegnazione di una specifica misura di probabilità sia un fatto univoco o arbitrario è stato oggetto di discussione per anni nella [comunità scientifica](https://it.wikipedia.org/wiki/Comunit%C3%A0_scientifica "Comunità scientifica"). L' [impostazione assiomatica](https://it.wikipedia.org/wiki/Probabilit%C3%A0#Definizione_assiomatica "Probabilità") dovuta a [Kolmogorov](https://it.wikipedia.org/wiki/Andrey_Nikolaevich_Kolmogorov "Andrey Nikolaevich Kolmogorov") non si cura di ciò ma si preoccupa di definire e formalizzare il concetto in modo da renderlo operativo dal punto di vista matematico.

## Definizioni formali

### Misura di probabilità

In termini più rigorosi, una **misura di probabilità**, caso particolare di [misura](https://it.wikipedia.org/wiki/Misura_\(matematica\) "Misura (matematica)"), è una funzione [sigma-additiva](https://it.wikipedia.org/wiki/Sigma-additivit%C3%A0 "Sigma-additività") definita su di uno [spazio degli eventi](https://it.wikipedia.org/wiki/Spazio_degli_eventi "Spazio degli eventi") a valori nell'intervallo $[0,1].$

Sia $𝒜$ una [sigma-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra") di sottoinsiemi di $Ω$ e $μ$ una misura di probabilità su essa definita.

In quanto misura, $μ$ deve soddisfare le proprietà:

- $∀A∈𝒜μ(A)≥0,$ (assioma di non negatività);
- $μ(∅)=0;$
- se $E_{1} , E_{2} , E_{3} , \ldots$ è una successione (una collezione al più numerabile) di insiemi mutuamente disgiunti in $𝒜$ allora

$\mu \left(\cup_{i = 1}^{+ \infty} E_{i}\right) = \sum_{i = 1}^{+ \infty} \mu \left(E_{i}\right) ,$ (assioma di $σ$ -additività).

In quanto probabilità deve soddisfare l'ulteriore proprietà:

- $μ(Ω)=1,$ (assioma di normalizzazione).

In realtà la seconda proprietà delle misure è ridondante (cioè può essere omessa), infatti, poiché $∅∪∅=∅$, e poiché si tratta di un'unione disgiunta, dalla terza proprietà delle misure si ricava $μ(∅)=μ(∅∪∅)=μ(∅)+μ(∅)$ da cui, appunto, $μ(∅)=0$

Esistono diverse nomenclature diffusamente usate ed accettate: in molti testi quella sinora chiamata *misura di probabilità* diventa più semplicemente *probabilità* e la notazione $μ(A)$ (che in letteratura matematica in genere è riservata ad una misura in generale, non per forza di probabilità) viene sostituita dalla notazione $P(A)$.

### Spazio di probabilità

Se $𝒜$ è uno [spazio degli eventi](https://it.wikipedia.org/wiki/Spazio_campionario#Spazio_campionario "Spazio campionario") ovvero una [sigma-algebra](https://it.wikipedia.org/wiki/Spazio_campionario#Sigma-algebra "Spazio campionario") definita sullo [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario") $Ω$ e $P$ è una misura di probabilità definita su $𝒜$, allora la terna $(Ω,𝒜,P)$ è detta **[spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità")**. La coppia $(Ω,𝒜)$ è invece detta **[spazio probabilizzabile](https://it.wikipedia.org/wiki/Spazio_probabilizzabile?action=edit&redlink=1 "Spazio probabilizzabile (la pagina non esiste)")**.

Un evento $A∈𝒜$ tale che $P(A)>0$ è detto **evento non trascurabile** per la probabilità di $P$.

Un evento $B∈𝒜$ tale che $P(B)=0$ è detto **evento trascurabile** per la probabilità di $P$.

Un evento $C∈𝒜$ tale che $P(C)=1$ è detto **evento quasi certo** per la probabilità di $P$.

Dal punto di vista della organizzazione di questi argomenti, lo **spazio di probabilità** è il nucleo portante del [modello matematico](https://it.wikipedia.org/wiki/Modello_matematico "Modello matematico") atto a rappresentare un [fenomeno aleatorio](https://it.wikipedia.org/wiki/Fenomeno_aleatorio "Fenomeno aleatorio").

## Assegnazione di una misura di probabilità

La teoria prevede quindi una funzione (misura) in grado di assegnare agli eventi i rispettivi valori di probabilità. La costruzione di tale funzione in genere è non banale: appena si esce dagli esempi elementari il numero di eventi che costituiscono la sigma algebra cresce "esponenzialmente". Se, poi, passiamo da uno spazio campionario finito ad uno infinito numerabile, la [cardinalità](https://it.wikipedia.org/wiki/Cardinalit%C3%A0 "Cardinalità") della sigma-algebra salta direttamente dal finito al continuo.

Come avviene allora in termini pratici la costruzione di una misura di probabilità?

In nostro aiuto arriva un teorema importante di [teoria della misura](https://it.wikipedia.org/wiki/Teoria_della_misura "Teoria della misura") noto come [teorema dell'estensione](https://it.wikipedia.org/wiki/Estensione_di_misure?action=edit&redlink=1 "Estensione di misure (la pagina non esiste)") il quale garantisce che, sotto certe condizioni, una misura di probabilità definita su una famiglia di eventi può essere estesa in un unico modo alla sigma-algebra generata dalla famiglia.

In maniera poco rigorosa ed anche leggermente inesatta (ma sufficiente a garantire il risultato in molti casi concreti) possiamo dire che come famiglia iniziale di eventi basta prendere una opportuna partizione dello spazio campionario, dove per opportuna, al solito, si intende *sufficiente a soddisfare le esigenze di rigore della corrente esposizione*. La famiglia cioè deve essere tale da garantire la distinzione degli eventi di interesse (se, nel lancio di un dado, siamo interessati esclusivamente alle uscite pari o dispari, la partizione $𝒜={{1,2},{3,4},{5,6}}$ è troppo grossolana perché non distingue i pari dai dispari, mentre la partizione $𝒜={{1},{2},{3},{4},{5},{6}}$ è troppo fine perché distingue più di quanto attualmente richiesto. In questo caso la partizione opportuna è: $𝒜={{1,3,5},{2,4,6}}$.

## Esempi

### Caso finito: il lancio di un dado

Supponiamo di voler studiare il lancio di un [dado](https://it.wikipedia.org/wiki/Dado_\(gioco\) "Dado (gioco)") d6 (ovvero a sei facce) bilanciato e, per la precisione, di essere interessati ai singoli esiti, cioè gli eventi elementari.

Gli eventi di interesse saranno rappresentati dai primi sei [numeri interi](https://it.wikipedia.org/wiki/Numero_intero "Numero intero") che formano già una partizione dello spazio campionario.

Lo **spazio di probabilità** associato al fenomeno sarà $(Ω,𝒜,P)$ dove:

- $Ω={ω∈ℕ:1≤ω≤6}$
- $𝒜=σ({{1},{2},{3},{4},{5},{6}})$
- $P({k})=16∀k∈Ω$

Si osservi che la misura di probabilità è stata assegnata solo a una partizione e che di più non è necessario.

Infatti per qualsiasi necessità pratica la probabilità di un evento composto potrà essere ottenuta sfruttando algoritmicamente le proprietà delle misure di probabilità. Ad esempio la probabilità che non esca ${4}$ è data da: $P({4}c)=1−P({4})=1−16=56$

### Caso numerabile: il bersaglio quadrato

Supponiamo di avere un bersaglio quadrato di lato unitario. Chiamiamo tale quadrato $\Omega = \mathcal{F}_{0}$.

Ora, con un taglio verticale, dividiamo il quadrato in due rettangoli uguali e chiamiamo $\mathcal{F}_{1}$ quello di sinistra.

Con un ulteriore taglio verticale dividiamo il rettangolo di destra in due rettangoli uguali. Nuovamente diamo nome a quello di sinistra che stavolta si chiamerà $\mathcal{F}_{2}$.

Sostanzialmente stiamo creando una successione ${𝒜n}$ di rettangoli, di pari altezza (unitaria) e base ognuno la metà del precedente, disgiunti a due a due, la cui unione numerabile copre l'intero quadrato. In altri termini la successione ${𝒜n}$ è una partizione del quadrato.

Supponiamo di lanciare una freccetta sul bersaglio e di essere interessati a capire quale sia la probabilità di colpire un rettangolo piuttosto che un altro.

Allora è ragionevole usare le aree come misura di probabilità:

$$
P \left(A_{k}\right) = A r e a \left(A_{k}\right) = \frac{1}{2^{k}} \forall k \in \mathbb{N}
$$

Si noti che in questo modo abbiamo assegnato una probabilità *soltanto* ad una infinità numerabile di eventi nonostante l'intera sigma-algebra abbia la [potenza del continuo](https://it.wikipedia.org/wiki/Cardinalit%C3%A0_del_continuo "Cardinalità del continuo") (perché lo spazio campionario è numerabile).

Si noti inoltre che tutto funziona bene (ovvero tutte le proprietà sono rispettate): ad esempio l'unione numerabile degli eventi della successione appartiene (per definizione) alla sigma-algebra. Intuitivamente tutti sappiamo che tale unione coincide con l'intero quadrato. Anche la proprietà di numerabile additività delle misure di probabilità è soddisfatta. Infatti:

$$
\Omega = \cup_{k = 1}^{\infty} A_{k}
$$

e

$$
P \left(\Omega\right) = P \left(\cup_{k = 1}^{\infty} A_{k}\right) = \sum_{k = 1}^{\infty} \frac{1}{2^{k}} = - 1 + \sum_{k = 0}^{\infty} \frac{1}{2^{k}} = 1
$$

essendo l'ultima [serie geometrica](https://it.wikipedia.org/wiki/Serie_geometrica "Serie geometrica") di ragione 1/2.

### Caso continuo: il segmento (0,1\]

Sia $Ω=(0,1]$ e sia $\mathcal{B}_{0}$ l'algebra delle unioni finite e disgiunte di intervalli di $Ω$ nota come [algebra di Borel](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel").

Dunque se $A \in \mathcal{B}_{0}$ allora è del tipo $A = \cup_{i = 1}^{n} I_{i}$ dove $I_{i}$ è della forma $\left(a_{i} , b_{i}\right]$.

Definiamo $P \left(A\right) := \sum_{i = 1}^{n} \left|I_{i}\right| = \sum_{i = 1}^{n} \left(b_{i} - a_{i}\right)$.

È possibile dimostrare che $P$ così costruita è una misura di probabilità su $\mathcal{B}_{0}$

Ancora una volta il teorema di esistenza e unicità dell'estensione ci garantisce che la probabilità così definita può essere estesa in un unico modo alla sigma-algebra $\mathcal{B} \left(\left(0 , 1\right]\right) = \sigma \left(\mathcal{B}_{0}\right)$.

Tale misura di probabilità viene detta [misura di Lebesgue](https://it.wikipedia.org/wiki/Misura_di_Lebesgue "Misura di Lebesgue"); la sigma-algebra $ℬ((0,1])$ viene detta sigma-algebra di Lebesgue.

La terna $(Ω,ℬ((0,1]),P)$ è uno spazio di probabilità fondamentale col quale siamo obbligati a confrontarci anche solo per occuparci di un numero **infinito** di lanci di una moneta.

Il *trait d'union* tra i lanci di una moneta e il segmento unitario è costituito dalle [espansioni diadiche](https://it.wikipedia.org/wiki/Espansione_diadica "Espansione diadica").

### La misura del conteggio

Come ultimo esempio riportiamo la misura del conteggio la cui importanza risiede nel suo utilizzo: su essa, infatti, si basa l'intera sezione della [probabilità elementare](https://it.wikipedia.org/wiki/Probabilit%C3%A0_elementare?action=edit&redlink=1 "Probabilità elementare (la pagina non esiste)") dedicata agli [spazi equiprobabili](https://it.wikipedia.org/wiki/Spazi_equiprobabili?action=edit&redlink=1 "Spazi equiprobabili (la pagina non esiste)") ovvero a quei fenomeni i cui esiti hanno tutti la medesima probabilità di realizzazione.

Sia $Ω$ uno spazio campionario al più numerabile.

Sia, inoltre $𝒫(Ω)$ la sigma-algebra generata.

Dato $A⊆Ω$, sia $\nu_{c} \left(A\right) = \# A$ la funzione che, sostanzialmente, conta il numero di elementi di A.

Tale funzione è detta **misura del conteggio**.

Ovviamente $\nu_{c}$ assume valori al finito se e solo se anche $Ω$ è finito.

Consideriamo pertanto il solo caso di $Ω$ finito e definiamo la seguente misura di probabilità:

$$
P \left(A\right) = \frac{\nu_{c} \left(A\right)}{\nu_{c} \left(\Omega\right)} = \frac{\# A}{\# \Omega}
$$

Lo spazio di probabilità $(Ω,𝒫(Ω),P)$ è, ripetiamo, atto a rappresentare tutti i fenomeni aleatori i cui eventi elementari sono equiprobabili ovvero, sostanzialmente tutti i fenomeni studiati dalla probabilità elementare (lancio di monete, lancio di dadi, estrazione di carte, estrazione di palline da un'urna, [roulette](https://it.wikipedia.org/wiki/Roulette "Roulette"), [lotto](https://it.wikipedia.org/wiki/Lotto "Lotto"), eccetera).

## Bibliografia

- (EN) [Paul Halmos](https://it.wikipedia.org/wiki/Paul_Halmos "Paul Halmos"), [Measure theory](https://archive.org/details/measuretheory00halm), Berlino, [Springer](https://it.wikipedia.org/wiki/Springer_\(azienda\) "Springer (azienda)"), 1976, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-03-87-90088-9](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-03-87-90088-9 "Speciale:RicercaISBN/978-03-87-90088-9").
- (EN) Patrick P. Billingsley, [Probability and Measure](https://archive.org/details/probabilitymeasu0000bill_a8s0), 4ª ed., Hoboken, [John Wiley & Sons](https://it.wikipedia.org/wiki/John_Wiley_&_Sons "John Wiley & Sons"), 2012, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-11-18-12237-2](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-11-18-12237-2 "Speciale:RicercaISBN/978-11-18-12237-2").
- (EN) Alan F. Karr, [Probability](https://archive.org/details/probability0000karr), New York, Springer-Verlag, 1993, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-1-4612-0891-4](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-1-4612-0891-4 "Speciale:RicercaISBN/978-1-4612-0891-4").
- (EN) [Andrey N. Kolmogorov](https://it.wikipedia.org/wiki/Andrej_Nikolaevi%C4%8D_Kolmogorov "Andrej Nikolaevič Kolmogorov"), [Foundations of the theory of probability](https://archive.org/details/foundationsofthe00kolm), New York, Chelsea Publishing Company, 1950.

## Voci correlate

- [Assiomi della probabilità](https://it.wikipedia.org/wiki/Assiomi_della_probabilit%C3%A0 "Assiomi della probabilità")
- [Capacità (matematica)](https://it.wikipedia.org/wiki/Capacit%C3%A0_\(matematica\) "Capacità (matematica)")
- [Evento (teoria della probabilità)](https://it.wikipedia.org/wiki/Evento_\(teoria_della_probabilit%C3%A0\) "Evento (teoria della probabilità)")
- [Funzione di probabilità](https://it.wikipedia.org/wiki/Funzione_di_probabilit%C3%A0 "Funzione di probabilità")
- [Indipendenza statistica](https://it.wikipedia.org/wiki/Indipendenza_statistica "Indipendenza statistica")
- [Probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità")
- [Teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità")
- [Valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso")
- [Variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale")

## Collegamenti esterni

- (EN) [probability space](https://www.britannica.com/topic/probability-space), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Probability Space](http://mathworld.wolfram.com/ProbabilitySpace.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [45875](https://thes.bncf.firenze.sbn.it/termine.php?id=45875) · [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh92001869](http://id.loc.gov/authorities/subjects/sh92001869) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4410515-0](https://d-nb.info/gnd/4410515-0) · [BNF](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Francia "Biblioteca nazionale di Francia") (FR) [cb123623831](https://catalogue.bnf.fr/ark:/12148/cb123623831) [(data)](https://data.bnf.fr/ark:/12148/cb123623831) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007553848805171](https://www.nli.org.il/en/authorities/987007553848805171) |
| --- | --- |