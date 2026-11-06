---
title: "Spazio campionario"
source: "https://it.wikipedia.org/wiki/Spazio_campionario"
author:
  - "[[Wikipedia]]"
published: 2005-01-23
created: 2026-11-06
description:
tags:
  - "clippings"
---
Nel [calcolo delle probabilità](https://it.wikipedia.org/wiki/Calcolo_delle_probabilit%C3%A0 "Calcolo delle probabilità") lo **spazio campionario** o **insieme universo** (generalmente indicato dalle lettere $S$, $Ω$ o $U$) è l' [insieme](https://it.wikipedia.org/wiki/Insieme "Insieme") dei possibili risultati di un esperimento casuale. Ad esempio, nel lancio di un dado a sei facce, lo spazio campionario è l'insieme ${1,2,3,4,5,6}$, nel lancio di una moneta è l'insieme $Ω≡{testa,croce}$ (escludendo che la moneta possa rimanere in bilico sul bordo), e così via. Lo spazio campionario può anche avere infiniti elementi: se, ad esempio, siamo interessati allo studio della caduta di una pallina su un pavimento, lo spazio campionario corrisponderà all'insieme dei punti del pavimento, considerati tutti come possibili punti di impatto della pallina.

## Definizioni formali

### Spazio campionario

Dato un esperimento casuale, è detto evento elementare $ω$ (*sample point* nella letteratura anglosassone) uno dei possibili esiti dell'esperimento stesso. L'insieme di tutti gli eventi elementari $Ω≡{ω1,…,ωn,…}$ viene detto spazio campionario (*sample space* nella letteratura anglosassone); gli eventi elementari rappresentano i punti di questo spazio.

I concetti di spazio campionario ed evento elementare sono [concetti primitivi](https://it.wikipedia.org/wiki/Concetto_primitivo "Concetto primitivo") in [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità"), come quelli di punto o linea in [geometria](https://it.wikipedia.org/wiki/Geometria "Geometria"), e non vengono ulteriormente definiti a partire da altri concetti. Non vi sono quindi indicazioni o limitazioni sulla natura degli eventi elementari; nel seguito della voce si daranno alcuni esempi nei quali gli eventi elementari assumono una specifica natura matematica.

### Eventi

Mentre con evento elementare si indica uno dei possibili esiti di un esperimento casuale, si dice [evento](https://it.wikipedia.org/wiki/Evento_\(teoria_della_probabilit%C3%A0\) "Evento (teoria della probabilità)") un qualsiasi sottoinsieme $A⊆Ω$ dello spazio campionario $Ω$ degli eventi elementari. Dunque un evento non è altro che un raggruppamento di uno o più eventi elementari. Pertanto, le espressioni evento elementare ed evento senza ulteriori specificazioni si riferiscono ad enti di natura diversa: i primi sono punti di uno spazio, la cui natura non è ulteriormente definita in generale, mentre i secondi sono insiemi, quindi trattabili con tutti gli strumenti della [omonima teoria](https://it.wikipedia.org/wiki/Teoria_degli_insiemi "Teoria degli insiemi").

L'insieme corrispondente all'intero spazio campionario $Ω$ è esso stesso un evento, in quanto insieme di eventi elementari; è detto evento certo poiché comprende tutti gli eventi elementari, cioè tutti i possibili risultati di un esperimento. L'evento corrispondente all'insieme vuoto $∅$, che non comprende alcun evento elementare, è detto evento impossibile.

Dato uno spazio campionario associato a un esperimento, può darsi che l'analisi da condurre non coinvolga tutti i possibili eventi, ma solo una parte di essi. Gli eventi che hanno un ruolo in una specifica analisi vengono detti eventi di interesse.

### Sigma-algebra

Sia $Ω$ uno spazio arbitrario purché non vuoto. Una famiglia $𝒜$ di eventi di $Ω$ (cioè una qualsiasi collezione di sottoinsiemi $A_{i} \subseteq \Omega$) è detta $σ$ -algebra ([sigma](https://it.wikipedia.org/wiki/Sigma_\(lettera_greca\) "Sigma (lettera greca)") -algebra) se contiene $Ω$ ed è [chiusa](https://it.wikipedia.org/wiki/Chiusura "Chiusura") rispetto alle operazioni insiemistiche di [unione](https://it.wikipedia.org/wiki/Unione_\(insiemistica\) "Unione (insiemistica)") numerabile e [complementazione](https://it.wikipedia.org/wiki/Complementazione "Complementazione"), ovvero se soddisfa le seguenti tre proprietà:

1. $Ω∈𝒜$
2. $A \in \mathcal{A} \Rightarrow A^{c} \in \mathcal{A}$
3. $A_{i} \in \mathcal{A} \forall i \in \mathbb{N} \Rightarrow \cup_{i = 1}^{\infty} A_{i} \in \mathcal{A}$

Pertanto: (1) l'evento certo è un evento (come dire: "succede qualcosa"); (2) la negazione di un qualsiasi evento è essa stessa un evento; (3) qualsiasi unione di eventi è un evento (per esempio l'evento "si verifica $E$ o $F$ " è l'unione dell'evento "si verifica $E$ " con l'evento "si verifica $F$ ").

La proprietà 1. è del tutto equivalente a:

1'. $∅∈𝒜$

La proprietà 3. è del tutto equivalente a:

3'. $A_{i} \in \mathcal{A} \forall i \in \mathbb{N} \Rightarrow \cap_{i = 1}^{\infty} A_{i} \in \mathcal{A}$

cioè una sigma-algebra è anche chiusa rispetto a [intersezioni](https://it.wikipedia.org/wiki/Intersezione_\(insiemistica\) "Intersezione (insiemistica)") numerabili.

Una sigma-algebra è il metodo più appropriato per descrivere un insieme di eventi a partire da un insieme di eventi elementari, e viene anche detta spazio degli eventi. Essa rappresenta un concetto ampiamente trattato in [teoria della misura](https://it.wikipedia.org/wiki/Teoria_della_misura "Teoria della misura") e deriva da una generalizzazione dell' [algebra di insiemi](https://it.wikipedia.org/wiki/Algebra_di_insiemi "Algebra di insiemi"). Questa, che richiede la stabilità solo per unioni finite (e non per quelle numerabili), non è tuttavia adeguata a descrivere tutti i possibili eventi, quali quelli del tipo "prima o poi piove". Infatti, questo evento è traducibile in linguaggio insiemistico come "piove oggi" oppure "piove domani" oppure " piove dopodomani", eccetera; ovvero l'evento $E$ è descritto dall'unione di infiniti eventi, $E = \cup_{i = 1}^{\infty} E_{i}$, da cui deriva che per la definizione di algebra potrebbe essere $\cup_{i = 1}^{\infty} E_{i} \notin \mathcal{A}$; quindi $E$ non sarebbe un evento compreso in un modello basato sull'algebra di insiemi. Per ovviare a ciò si introduce la nozione di sigma-algebra.

Dato uno spazio arbitrario $Ω$ e una famiglia $𝒜$ di suoi sottoinsiemi è possibile, sempre e in vari modi, *estendere* la famiglia sino a renderla una sigma-algebra. La più piccola sigma-algebra contenente la famiglia $𝒜$ viene indicata con $σ(𝒜)$ e detta sigma-algebra generata dalla famiglia.

### Spazio di probabilità

I concetti di spazio campionario $Ω$ e di spazio degli eventi $𝒜$ sin qui definiti, considerati assieme a quello di una [misura](https://it.wikipedia.org/wiki/Misura "Misura") $ℙ(A)$, detta appunto [misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità"), concorrono a definire il concetto di [spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità") $(Ω,𝒜,ℙ)$, che rappresenta la base per lo [sviluppo assiomatico della teoria della probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0#Definizione_assiomatica "Probabilità").

## Osservazioni

Gli elementi dell' [insieme delle parti](https://it.wikipedia.org/wiki/Insieme_delle_parti "Insieme delle parti") di $Ω$ sono i sottoinsiemi di $Ω$; quindi una famiglia $𝒜$ di sottoinsiemi di $Ω$ è un sottoinsieme dell'insieme delle parti di $Ω$, $𝒫(Ω)$.

Un evento $A$ è un sottoinsieme di $Ω$, e non un suo elemento. Quindi un evento, in quanto insieme, non appartiene allo spazio campionario, ma è incluso nello spazio campionario. Di converso, un evento elementare $ω$, in quanto punto, appartiene allo spazio campionario, e l'evento ${ω}$, insieme costituito da un singolo punto (e perciò detto [singoletto](https://it.wikipedia.org/wiki/Singoletto "Singoletto")), è incluso nello spazio campionario. Si può quindi scrivere $ω∈Ω$, mentre la scrittura $A∈Ω$ è priva di significato.

Se la cardinalità di $Ω$ è finita, allora la $σ$ -algebra può coincidere con l'insieme delle parti; non è detto però che sia necessario considerare una famiglia di eventi così grande.

Ovviamente nulla vieta di prendere come spazio degli eventi proprio l'insieme delle parti. Questo perché, nel caso di [cardinalità](https://it.wikipedia.org/wiki/Cardinalit%C3%A0 "Cardinalità") finita, è sempre possibile prendere come $σ$ -algebra l'intero insieme delle parti, senza rischiare di incappare in eventi $A$ ai quali non sia possibile attribuire una [probabilità](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0 "Distribuzione di probabilità") $P(A)$.

Se invece la [cardinalità](https://it.wikipedia.org/wiki/Cardinalit%C3%A0 "Cardinalità") di $Ω$ è infinita, non è detto che sia possibile definire $P(A)∀A∈𝒫(Ω)$. In tale caso, può darsi che la scelta dell'insieme delle parti come sigma-algebra non sia felice: in virtù della terza proprietà delle sigma-algebre, quando passiamo alla probabilità vengono coinvolte delle [serie](https://it.wikipedia.org/wiki/Serie_\(matematica\) "Serie (matematica)") che non è detto convergano.

In generale, si cerca sempre di scegliere una sigma-algebra piccola, in quanto più semplice da usare. Il fatto che una sigma-algebra sia non coincidente con l'intero insieme delle parti non vuol dire che alcuni eventi elementari ne possano restare esclusi; infatti, per definizione di sigma-algebra, dev'essere $∀ω∈Ω∃A∈𝒜:ω∈A$. In altri termini, le sigma-algebre definite su $Ω$ sono una copertura di $Ω$.

## Tipi di spazio campionario

La scelta dello spazio campionario per un determinato [fenomeno aleatorio](https://it.wikipedia.org/wiki/Fenomeno_aleatorio "Fenomeno aleatorio") deve in qualche modo equilibrare la necessità di essere fedele alla realtà fisica esaminata con la convenienza matematica.

In pratica, la maggior parte degli spazi campionari rientra nelle seguenti tipologie:

### Finito

I più semplici esperimenti aleatori consistono nel lancio di una moneta o di un dado, o nell'estrazione di una pallina da un'urna. In ogni caso lo spazio campionario sarà un insieme costituito da un numero finito di eventi elementari. In genere, ma non necessariamente, essi saranno rappresentati dai primi n [numeri interi](https://it.wikipedia.org/wiki/Numero_intero "Numero intero"): ${0,1,…,n−1}$ oppure ${1,…,n}$.

### Numerabile

Molti importanti modelli probabilistici, come ad esempio quello poissoniano utilizzato per contare il numero di accadimenti che si verificano in un intervallo di tempo fissato, si basano su uno spazio campionario numerabile e coincidente, quindi con tutto $ℕ$ o con $ℤ$.

### Continuo

Solitamente il modello continuo per eccellenza è la [retta reale](https://it.wikipedia.org/wiki/Retta_dei_numeri_reali "Retta dei numeri reali"), come nel caso degli errori di misura nelle osservazioni scientifiche il cui studio sistematico è stato avviato da [Karl Friedrich Gauss](https://it.wikipedia.org/wiki/Karl_Friedrich_Gauss "Karl Friedrich Gauss") nel 1809. Altri modelli, utili per rappresentare i tempi di vita di componenti elettronici, hanno come modello la [semiretta](https://it.wikipedia.org/wiki/Semiretta "Semiretta") reale positiva.

### Vettoriale finito

Spesso un esperimento è costituito da una sequenza finita di altri esperimenti come, ad esempio, il lancio di un dado ripetuto n volte. In tale caso, se $Ω0≡{ω∈ℕ:1≤ω≤6}$ è lo spazio campionario del singolo lancio, lo spazio campionario complessivo sarà dato dal [prodotto cartesiano](https://it.wikipedia.org/wiki/Prodotto_cartesiano "Prodotto cartesiano") dei singoli spazi: $Ω=Ω0×⋯×Ω0≡{(ω1,…,ωn):ωi∈Ω0∀i=1,…,n}$.

Lo spazio campionario del singolo esperimento potrà essere sia finito che numerabile che continuo.

### Vettoriale numerabile

Come nel caso vettoriale finito con l'unica differenza che la sequenza dei singoli esperimenti non è finita ma numerabile dunque: $Ω=Ω0×Ω0×⋯≡{(ω1,ω2,…):ωi∈Ω0∀i∈ℕ}$.

Tale modello compare, ad esempio, nelle analisi di qualità dei pezzi uscenti da una linea di produzione con $Ω0={0,1}$ o nella [passeggiata aleatoria](https://it.wikipedia.org/wiki/Passeggiata_aleatoria "Passeggiata aleatoria") (random walk) con $Ω0={−1,1}$.

### Funzionale

In alcuni esperimenti aleatori della fisica, gli esiti dell'esperimento sono i percorsi o le traiettorie di una particella in un certo intervallo di tempo. Quindi ogni esito, in questo caso, è una funzione. Tale modello emerge insistentemente nei [processi stocastici](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico").

## Esempi

Per molti esperimenti può esistere più di una scelta plausibile sia per lo spazio campionario che per lo spazio degli eventi, e la loro scelta rappresenta una parte fondamentale nella costruzione di un modello probabilistico. Una scelta corretta in questa fase conferisce un vantaggio che diviene chiaro in fase di assegnazione di una [misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità"). Sono elencati qui alcuni esempi.

### Un mazzo di carte

Per esempio, nel caso dell'estrazione di una carta da un mazzo, si potrebbe scegliere di rappresentare nello spazio campionario il punteggio ($Ω≡$ {Asso, Due, Tre,..., Re}), oppure il seme ($Ω≡$ {Cuori, Quadri, Fiori, Picche}), o ancora la scelta $Ω≡$ {Faccia in alto, Faccia in basso} se si vuole considerare l'eventuale rovesciamento di alcune carte nel mazzo. Una descrizione più completa dei risultati potrebbe poi specificare tutti questi elementi costruendo uno spazio campionario come prodotto cartesiano degli esempi prima fatti.

### Un foglio in pezzi

Prendiamo un qualsiasi foglio: nella sua interezza rappresenterà il nostro spazio campionario. Le singole particelle del foglio corrisponderanno ai punti dello spazio campionario ovvero agli eventi elementari. Se ora strappiamo in pezzi il foglio, ognuno dei pezzi rappresenterà un evento che, in quanto aggregato di particelle, sarà un sottoinsieme del foglio originale e, in quanto pezzo, sarà un elemento dell'insieme dei pezzi del foglio (l'insieme delle parti). Osserviamo che un foglio strappato in pezzi costituisce una partizione del foglio originale. I pezzi in cui abbiamo strappato il foglio non esauriscono tutto l'insieme delle parti ma ne costituiscono solo una sua famiglia. Tale famiglia può essere estesa ad una sigma-algebra aggiungendo ad essa anche tutte le possibili composizioni ottenibili con le operazioni insiemistiche di unione numerabile, intersezione numerabile e complementazione. Ad esempio dovremo aggiungere alla famiglia l'unione di tutti i pezzi (l'intero foglio). Accanto ad ogni pezzo della famiglia dovremo aggiungere il suo complementare (ovvero l'unione di tutti gli altri pezzi), e via dicendo.

Notiamo che questo procedimento ci conduce ad una sigma-algebra ma non all'insieme delle parti, per arrivare al quale dovremmo ripetere il procedimento anche per tutti gli altri modi in cui possiamo strappare il foglio originale.

### Lancio di un dado equilibrato

Consideriamo un esperimento che consiste nel lanciare un comune dado (un cubo le cui facce sono numerate da $1$ a $6$) su una superficie piana dotata di attrito e delimitata da pareti atte a contenere il movimento del dado (ovvero una scatola!) e supponiamo che il dado sia bilanciato (ovvero che la sua distribuzione di massa sia uniforme e non privilegi una faccia rispetto alle altre).

Gli esiti di tale esperimento sono misurabili. Infatti, spesa la sua energia, il dado si fermerà inesorabilmente poggiando sulla superficie una delle sue facce e mostrando, quindi, all'esperimentatore la faccia opposta a quella di appoggio.

Il numero impresso sulla faccia esposta potrà essere utilizzato per rappresentare l'esito dell'esperimento che, complessivamente, avrà sei possibili esiti distinti (tanti quanti le facce del dado). Codificheremo tali esiti con i primi sei numeri interi.

Allora gli eventi elementari saranno i primi sei numeri interi e lo spazio campionario associato a questo esperimento sarà $Ω≡{ω∈ℕ:1≤ω≤6}$ che ha [cardinalità](https://it.wikipedia.org/wiki/Cardinalit%C3%A0 "Cardinalità") $#Ω=6$ evidentemente finita.

Poiché ogni evento è un sottoinsieme dello spazio campionario ovvero un elemento dell'insieme delle parti di $Ω$ ci sono $2^{6}$ possibili eventi tra i quali, ovviamente, l'insieme vuoto, l'intero $Ω$, i sei singoletti, le $\left(\right. \genfrac{}{}{0pt}{}{6}{2} \left.\right)$ possibili coppie, i pari ${2,4,6}$ e via dicendo.

La scelta della $σ$ -algebra da usare dipende dagli obiettivi. Se, ad esempio, siamo interessati a calcolare la probabilità che esca un [numero pari](https://it.wikipedia.org/wiki/Numeri_pari_e_dispari "Numeri pari e dispari"), gli unici eventi di interesse saranno $A$ ="è uscito un pari" e il suo complementare. La più piccola sigma-algebra contenente l'evento $A$ sarà: ${∅,A,Ac,Ω}$. Non è l'unica ma, tra tutte le sigma algebre contenenti l'evento $A$, è la più piccola dunque quella che genera meno lavoro e meno problemi.

### Sigma-algebra di Borel su (0,1\]

[Questa sigma-algebra](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel"), che prende nome dal matematico francese [Émile Borel](https://it.wikipedia.org/wiki/%C3%89mile_Borel "Émile Borel"), non rappresenta un caso intuitivo, ma è qui riportato perché celebre, perché riveste un ruolo fondamentale in gran parte della teoria della probabilità e perché, nonostante la sua semplicità (è sufficiente investigare su un numero infinito di lanci di una moneta per incappare in una sigma-algebra di Borel), ha messo in crisi la teoria classica della probabilità, richiedendone la rivisitazione assiomatica di [Kolmogorov](https://it.wikipedia.org/wiki/Andrej_Kolmogorov "Andrej Kolmogorov").

Sia $Ω=(0,1]$ l'intervallo reale unitario aperto a sinistra e chiuso a destra. Sia, inoltre, $ℐ$ la famiglia degli intervalli di $Ω$, della forma $(a,b]$ con $a<b.$ Aggiungiamo poi ad $ℐ$ gli intervalli $A_{i} = \left(a_{i} , b_{i}\right]$, tutte le loro unioni finite e disgiunte $A = \cup_{i = 1}^{n} A_{i} = \cup_{i = 1}^{n} \left(a_{i} , b_{i}\right]$ ed, infine, anche l'insieme vuoto.

L' *algebra di Borel* $\mathcal{B}_{0}$ così ottenuta, nonostante sia assai numerosa, non è ancora una sigma-algebra; ad esempio ne sono esclusi i singoletti ${x}$ che, in virtù della proprietà 3', dovrebbero invece essere presenti. Ognuno di essi è infatti intersezione numerabile di insiemi della famiglia, in quanto ${x}=⋂n=1∞(x−1n,x]$

L'insieme $ℬ$ ottenuto dall'unione di $\mathcal{B}_{0}$ con i singoletti è una sigma-algebra; inoltre, esso non coincide con l'insieme delle parti di $Ω$, $𝒫(Ω)$, e non è quindi banale, come sarà dimostrato da [Giuseppe Vitali](https://it.wikipedia.org/wiki/Giuseppe_Vitali_\(matematico\) "Giuseppe Vitali (matematico)").

### Costruzione di una sigma-algebra

Riprendiamo ancora l'esempio del lancio di un dado. Abbiamo già visto che, se siamo interessati a valutare la probabilità che esca pari, dovremo considerare l'evento $A$ ={è uscito pari}. Ma $A$ preso singolarmente non basta; per completare la partizione occorrerà aggiungere ad $A$ il suo complementare. Ora ${A,Ac}$ è una partizione, in quanto chiusa rispetto alla complementazione.

Ovviamente ci sono altre partizioni possibili, quali ${{1,2},{3,4},{5,6}}$ o ${A,{1},{3},{5}}$. Tuttavia la prima non distingue tra pari e dispari, mentre la seconda aggiunge dettagli non di nostro interesse, come l'informazione se il dispari uscito sia $1$ o $3$ o $5$. Quindi ${A,Ac}$ rappresenta la migliore partizione rispetto al problema in esame.

Se, per qualche motivo, dobbiamo esaminare tutte e sei le possibili configurazioni, allora la partizione che dovremo costruire sarà la più fine possibile: ${{1},{2},{3},{4},{5},{6}}$. Una volta assegnato questo spazio campionario, per generare la sua sigma-algebra si considerano tutte le possibili unioni tra i suoi elementi e i loro complementari (procedimento valido per ogni [insieme finito](https://it.wikipedia.org/wiki/Insieme_finito "Insieme finito")). La sigma-algebra conterrà quindi, ad esempio: ${5}∪{6},{1}∪{2}∪{3},{1}c∪{4},…$

## Bibliografia

- P. Halmos (1950): *Measure theory*, D. van Nostrand and Co.
- [W. Feller](https://it.wikipedia.org/wiki/William_Feller "William Feller") (1967): *An Introduction to Probability Theory and its Applications*, vol. I, III ed, J. Wiley & Sons
- P. Billingsley (1995): *Probability and Measure*, [John Wiley & Sons](https://it.wikipedia.org/wiki/John_Wiley_&_Sons "John Wiley & Sons")
- A. F. Karr (1993): *Probability*, Springer-Verlag
- G. Dall'Aglio (2003): *Calcolo delle probabilità*, III ed, Zanichelli, [ISBN 978-8808176769](https://it.wikipedia.org/wiki/Special:BookSources/9788808176769)

## Voci correlate

- [Misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità")
- [Spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità")
- [Variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale")

## Altri progetti

Altri progetti

- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Sample_space?uselang=it)

- contiene immagini o altri file sullo **[spazio campionario](https://commons.wikimedia.org/wiki/Category:Sample_space?uselang=it)**

## Collegamenti esterni

- (EN) [sample space](https://www.britannica.com/topic/sample-space), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Sample Space](http://mathworld.wolfram.com/SampleSpace.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.