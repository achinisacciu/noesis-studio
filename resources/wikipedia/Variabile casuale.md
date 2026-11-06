---
title: "Variabile casuale"
source: "https://it.wikipedia.org/wiki/Variabile_casuale"
author:
  - "[[Wikipedia]]"
published: 2003-04-17
created: 2026-11-06
description:
tags:
  - "clippings"
---
![Questo grafico mostra come la variabile casuale è una funzione da tutti i possibili risultati a valori reali.](https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d2/Variabile_aleatoria_funzione.svg/500px-Variabile_aleatoria_funzione.svg.png?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Questo grafico mostra come la variabile casuale è una funzione da tutti i possibili risultati a valori reali.

In [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica"), e in particolare nella [teoria della probabilità](https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0 "Teoria della probabilità"), una **variabile casuale** (detta anche **variabile aleatoria** o **variabile stocastica**) è una formalizzazione matematica di una quantità o di un oggetto che dipende da eventi casuali.

Il termine, tuttavia, non deve confondere. Non si tratta né di una [variabile](https://it.wikipedia.org/wiki/Variabile_\(statistica\) "Variabile (statistica)") né di un insieme casuale di elementi, bensì di una [funzione matematica](https://it.wikipedia.org/wiki/Funzione_\(matematica\) "Funzione (matematica)") con caratteristiche proprie:

- il **dominio** è l'insieme dei possibili esiti in uno [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario") (ad esempio l'insieme ${T,C}$, ovvero le possibili facce rivolte verso l'alto di una moneta lanciata, testa $T$ o croce $C$, come risultato del lancio di una moneta).
- il **codominio** è uno spazio misurabile (seguendo l'esempio precedente, il codominio potrebbe essere l'insieme ${−1,1}$ se, supponiamo, testa $T$ fosse associata a $1$ e croce $C$ fosse associata a $−1$). Tipicamente, il codominio di una variabile casuale è un sottoinsieme dei numeri reali.

Il grafico mostra come una variabile casuale sia una funzione da tutti i possibili esiti a valori reali. Mostra inoltre come una variabile casuale venga utilizzata per definire le [funzioni di massa di probabilità](https://it.wikipedia.org/wiki/Funzione_di_probabilit%C3%A0 "Funzione di probabilità").

Il termine «aleatorio» deriva dal latino *alea* (*gioco di dadi* [^1]) ed esprime il concetto di rischio calcolato. La denominazione alternativa *stocastico* è stata introdotta da [Bruno de Finetti](https://it.wikipedia.org/wiki/Bruno_de_Finetti "Bruno de Finetti") [^2]. Il termine «casuale» deriva dal latino *casualis*.

Nel linguaggio matematico formale della [teoria della misura](https://it.wikipedia.org/wiki/Misura_\(matematica\) "Misura (matematica)"), una variabile casuale è definita come una funzione misurabile da uno spazio con misura di probabilità (chiamato [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario")) a uno [spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile"). Questo permette di considerare la misura immagine (o *pushforward*), che prende il nome di distribuzione di variabile casuale; la distribuzione è quindi una misura di probabilità sull'insieme di tutti i possibili valori della variabile casuale. È possibile che due variabili casuali abbiano distribuzioni identiche ma differiscano in modo significativo; per esempio, potrebbero essere indipendenti tra loro.

## Storia

Ancorché non formalizzato, il concetto della distribuzione statistica attorno ad una media era noto fin dall'antichità. Leggiamo infatti nel *[Fedone](https://it.wikipedia.org/wiki/Fedone "Fedone")* di [Platone](https://it.wikipedia.org/wiki/Platone "Platone"):

««E non è ingiusto, questo? Non è forse vero che chi si comporta così, evidentemente vive tra gli uomini senza averne nessuna esperienza? Se, infatti, li conoscesse appena, saprebbe che son pochi quelli veramente buoni o completamente malvagi e che per la maggior parte, invece, sono dei mediocri.»  

«In che senso?» feci.  
«È lo stesso delle cose molto piccole e molto grandi. Credi forse che sia tanto facile trovare un uomo o un cane o un altro essere qualunque molto grande o molto piccolo o, che so io, uno molto veloce o molto lento o molto brutto o molto bello o tutto bianco o tutto nero? Non ti sei mai accorto che in tutte le cose gli estremi sono rari mentre gli aspetti intermedi sono frequenti, anzi numerosi?»»

## Definizione

Più formalmente, dato uno [spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_misura#Spazio_di_probabilit%C3%A0 "Spazio di misura") $(Ω,ℱ,ν)$ (dove $Ω$ è un [insieme](https://it.wikipedia.org/wiki/Insieme "Insieme") detto [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario") o insieme degli [eventi](https://it.wikipedia.org/wiki/Evento_\(teoria_della_probabilit%C3%A0\) "Evento (teoria della probabilità)"), $ℱ$ è una [sigma-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra") su $Ω$ e $ν$ è una [misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità")) e dato uno [spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile") $(E,ℰ)$, una $(E,ℰ)$ -variabile aleatoria è una [funzione misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") $X:Ω→E$ dallo spazio campionario ad $E$.

In questa definizione si intende che una [funzione](https://it.wikipedia.org/wiki/Funzione_\(matematica\) "Funzione (matematica)") $X$ è misurabile se per ogni $A∈ℰ$ si ha che $X^{- 1} \left(A\right) \in \mathcal{F}$. Questa definizione di misurabilità è una generalizzazione di quella definita da [Lindgren](https://it.wikipedia.org/wiki/Bernard_Lindgren?action=edit&redlink=1 "Bernard Lindgren (la pagina non esiste)") ([1976](https://it.wikipedia.org/wiki/1976 "1976")): una funzione $X$ definita sullo spazio campionario $Ω$ si dice misurabile rispetto al [campo di Borel](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel") $ℬ$ se e solo se l'evento ${ω∈Ω:X(ω)≤λ}$ appartiene a $ℬ$ per ogni $λ$.

Se $E$ è uno [spazio topologico](https://it.wikipedia.org/wiki/Spazio_topologico "Spazio topologico") e $ℰ$ è la [sigma-algebra di Borel](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel") allora $X$ è detta anche $E$ -variabile aleatoria. Inoltre se $E = \mathbb{R}^{n}$ allora $X$ è detta semplicemente variabile aleatoria.

In altre parole una variabile aleatoria $X$ è un modo per indurre una [misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità") sullo [spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile") di arrivo $E$ a partire dalla misura di probabilità definita sull'insieme degli eventi $Ω$.

- Le variabili casuali a una dimensione (cioè a valori in $ℝ$) si dicono semplici o univariate.
- Le variabili casuali a più dimensioni si dicono multiple o multivariate (doppie, triple, $k$ -uple).
- Le variabili casuali a valori matriciali si dicono [matrici aleatorie](https://it.wikipedia.org/wiki/Matrice_aleatoria "Matrice aleatoria").

Variabili casuali che dipendono da un parametro $t$ (dove $t$ sta solitamente per "tempo") vengono considerate [processi stocastici](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico").

## Esempio

Riportiamo un esempio nell'ambito della probabilità discreta. Immaginiamo di effettuare tre esperimenti distinti, come il lancio successivo di tre monete. Lo [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario") risultante di [cardinalità](https://it.wikipedia.org/wiki/Cardinalit%C3%A0 "Cardinalità") $2^{3}$ è composto da tutte le possibili terne di facce ottenibili.

Fanno parte di questo insieme:

$(C,C,C)$; $(C,C,T)$; $(C,T,C)$; $(C,T,T)$; $(T,C,C)$; $(T,C,T)$; $(T,T,C)$; $(T,T,T).$

Una possibile variabile casuale potrebbe associare a ciascuna terna il numero di croci che essa contiene. Pertanto la variabile casuale in questo esempio ha per dominio l'insieme di tutte le terne (ossia l'intero spazio campionario) e per codominio l'insieme misurabile ${0,1,2,3}$.

Essa è la funzione che associa

$(C,C,C)↦3,$

$(C,C,T);(C,T,C);(T,C,C)↦2,$

$(T,T,C);(T,C,T);(C,T,T)↦1,$

$(T,T,T)↦0.$

Possiamo poi applicare una funzione di massa di probabilità a ciascun valore del codominio di questa variabile casuale. La probabilità di ottenere $n$ croci con tre lanci equivale alla cardinalità della contrimmagine di $n$ attraverso la variabile casuale diviso la cardinalità dello spazio campionario di partenza:

$P \left(3\right) = \frac{1}{8} ;$

$P \left(2\right) = \frac{3}{8} ;$

$P \left(1\right) = \frac{3}{8} ;$

$P \left(0\right) = \frac{1}{8} .$

## Distribuzione di probabilità

La [misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità") indotta sullo [spazio misurabile](https://it.wikipedia.org/wiki/Spazio_misurabile "Spazio misurabile") di arrivo $(E,ℰ)$ da una variabile aleatoria $X$, a partire dalla misura di probabilità $ν$ su $(Ω,ℱ)$, è detta la distribuzione, o legge, di probabilità, di $X$, è indicata con $P_{X}$ ed è definita nel seguente modo

$P_{X} \left(A\right) := \nu \left(X^{- 1} \left(A\right)\right) ,$

per ogni $A∈ℰ$. Essa è ben definita proprio perché $X^{- 1} \left(A\right) \in \mathcal{F}$ per ogni $A∈ℰ$. Quando la variabile aleatoria è chiara dal contesto spesso si omette il pedice $X$. Per brevità, invece di scrivere $\nu \left(X^{- 1} \left(A\right)\right)$ o $ν({ω∈Ω:X(ω)∈A})$ spesso si usa la notazione

$P_{X} \left(A\right) = P \left(X \in A\right) .$

Per variabili aleatorie a valori [reali](https://it.wikipedia.org/wiki/Numero_reale "Numero reale"), la legge di probabilità della variabile casuale $X$ è chiamata *[funzione di ripartizione](https://it.wikipedia.org/wiki/Funzione_di_ripartizione "Funzione di ripartizione")* ed è definita come $F(x)=P(X≤ x)$.

In generale le distribuzioni di probabilità sono divise in due classi:

- se la variabile casuale $X$ è discreta, cioè l'insieme dei possibili valori (il rango o immagine di $X$) è [finito](https://it.wikipedia.org/wiki/Insieme_finito "Insieme finito") o [numerabile](https://it.wikipedia.org/wiki/Insieme_numerabile "Insieme numerabile"), la distribuzione di probabilità è una [distribuzione discreta](https://it.wikipedia.org/wiki/Distribuzione_discreta "Distribuzione discreta") ed è chiamata *[funzione di massa](https://it.wikipedia.org/wiki/Funzione_di_probabilit%C3%A0 "Funzione di probabilità")* (o *funzione massa di probabilità* o *densità discreta*):

$p(x)=P(X=x);$

- se la variabile casuale $X$ è continua, cioè l'insieme dei possibili valori ha la [potenza del continuo](https://it.wikipedia.org/wiki/Cardinalit%C3%A0_del_continuo "Cardinalità del continuo"), la distribuzione di probabilità è una [distribuzione continua](https://it.wikipedia.org/wiki/Distribuzione_continua "Distribuzione continua") ed è definita come:

$P \left(X \in A\right) = \int_{A} f \left(x\right) d x ,$

dove $f$ è una funzione non negativa chiamata *[funzione di densità di probabilità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità")*.

Descrivere un fenomeno aleatorio, cioè un fenomeno che sia caratterizzabile da una variabile aleatoria, vuol dire descriverlo in termini di distribuzione di probabilità e dei suoi parametri, come il [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") e la [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza").

## Alcune variabili casuali utilizzate in statistica

Le variabili casuali si dividono principalmente in due grandi classi, [discrete](https://it.wikipedia.org/wiki/Distribuzione_discreta "Distribuzione discreta") e [continue](https://it.wikipedia.org/wiki/Distribuzione_continua "Distribuzione continua") (o assolutamente continue): Esempi del primo tipo:

- [variabile casuale uniforme discreta](https://it.wikipedia.org/wiki/Distribuzione_discreta_uniforme "Distribuzione discreta uniforme")
- [variabile casuale bernoulliana](https://it.wikipedia.org/wiki/Distribuzione_di_Bernoulli "Distribuzione di Bernoulli"), caso particolare della Binomiale
- [variabile casuale binomiale](https://it.wikipedia.org/wiki/Distribuzione_binomiale "Distribuzione binomiale")
- [variabile casuale poissoniana](https://it.wikipedia.org/wiki/Distribuzione_di_Poisson "Distribuzione di Poisson") detta pure "legge degli eventi rari"
- [variabile casuale geometrica](https://it.wikipedia.org/wiki/Distribuzione_geometrica "Distribuzione geometrica"), caso particolare della [distribuzione di Pascal](https://it.wikipedia.org/wiki/Distribuzione_di_Pascal "Distribuzione di Pascal")
- [variabile casuale ipergeometrica](https://it.wikipedia.org/wiki/Distribuzione_ipergeometrica "Distribuzione ipergeometrica")
- [variabile casuale degenere](https://it.wikipedia.org/wiki/Distribuzione_degenere "Distribuzione degenere")

Esempi del secondo tipo:

- [variabile casuale normale o gaussiana](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale")
- [variabile casuale Gamma o Erlanghiana](https://it.wikipedia.org/wiki/Distribuzione_Gamma "Distribuzione Gamma")
- [variabile casuale t di Student](https://it.wikipedia.org/wiki/Distribuzione_t_di_Student "Distribuzione t di Student")
- [variabile casuale di Fisher-Snedecor](https://it.wikipedia.org/wiki/Distribuzione_di_Fisher-Snedecor "Distribuzione di Fisher-Snedecor")
- [variabile casuale esponenziale negativa](https://it.wikipedia.org/wiki/Distribuzione_esponenziale "Distribuzione esponenziale"), caso particolare della v.c. Gamma
- [variabile casuale Chi Quadrato χ²](https://it.wikipedia.org/wiki/Distribuzione_chi_quadrato "Distribuzione chi quadrato"), caso particolare della v.c. Gamma
- [variabile casuale Beta](https://it.wikipedia.org/wiki/Distribuzione_Beta "Distribuzione Beta")
- [variabile casuale rettangolare o uniforme continua](https://it.wikipedia.org/wiki/Distribuzione_continua_uniforme "Distribuzione continua uniforme")
- [variabile casuale di Cauchy](https://it.wikipedia.org/wiki/Distribuzione_di_Cauchy "Distribuzione di Cauchy")

Tali classi non sono però esaustive della famiglia delle variabili casuali; esiste anche una terza classe, delle [variabili casuali singolari](https://it.wikipedia.org/wiki/Distribuzione_singolare "Distribuzione singolare") o *continue singolari*, come la [variabile casuale di Cantor](https://it.wikipedia.org/wiki/Distribuzione_di_Cantor "Distribuzione di Cantor").

Il teorema di rappresentazione di [Lebesgue](https://it.wikipedia.org/wiki/Henri_Lebesgue "Henri Lebesgue") ci assicura che ogni funzione di ripartizione (e dunque ogni variabile casuale) è rappresentabile come [combinazione convessa](https://it.wikipedia.org/wiki/Combinazione_convessa "Combinazione convessa") di una funzione di ripartizione discreta, una continua e una singolare. Variabili casuali che non appartengono a nessuna delle tre classi vengono dette *[miste](https://it.wikipedia.org/wiki/Mistura_di_distribuzioni "Mistura di distribuzioni")*.

Si può comunque dimostrare che le classi delle variabili casuali discrete e delle variabili casuali continue sono dense nella classe di tutte le variabili casuali rispetto alla [convergenza in distribuzione](https://it.wikipedia.org/wiki/Convergenza_di_variabili_casuali#Convergenza_in_distribuzione "Convergenza di variabili casuali"), cioè per ogni variabile casuale esiste una successione di v.c. discrete (rispettivamente continue) che converge in distribuzione alla variabile data.

## Note

## Bibliografia

- Remo Cacciafesta, Lezioni di calcolo delle probabilità, Roma, Veschi, 1983.
- Giorgio Dall'Aglio, Calcolo delle probabilità, Bologna, Zanichelli, 2003.
- (EN) Bert Lawrence Fristedt Gray, [A modern approach to probability theory](http://books.google.com/books/about/A_Modern_Approach_to_Probability_Theory.html?id=5D5O8xyM-kMC), Boston, Birkhäuser, 1996, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [3-7643-3807-5](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/3-7643-3807-5 "Speciale:RicercaISBN/3-7643-3807-5").
- (EN) [Olav Kallenberg](https://it.wikipedia.org/wiki/Olav_Kallenberg?action=edit&redlink=1 "Olav Kallenberg (la pagina non esiste)"), [Random Measures](http://books.google.com/books/about/Random_measures.html?id=bBnvAAAAMAAJ), 4ª ed., Berlin, Akademie Verlag, 1986, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-12-394960-2](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-12-394960-2 "Speciale:RicercaISBN/0-12-394960-2"), [MR](https://it.wikipedia.org/wiki/Mathematical_Reviews "Mathematical Reviews") [MR0854102](http://www.ams.org/mathscinet-getitem?mr=MR0854102).
- (EN) Olav Kallenberg, [Foundations of Modern Probability](http://books.google.de/books/about/Foundations_of_Modern_Probability.html?hl=de&id=L6fhXh13OyMC), 2ª ed., Berlin, Springer Verlag, 2001, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-387-95313-2](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-387-95313-2 "Speciale:RicercaISBN/0-387-95313-2").
- (EN) [Athanasios Papoulis](https://it.wikipedia.org/wiki/Athanasios_Papoulis?action=edit&redlink=1 "Athanasios Papoulis (la pagina non esiste)"), [Probability, Random Variables, and Stochastic Processes](http://www.mhhe.com/engcs/electrical/papoulis/), 9ª ed., Tokyo, McGraw–Hill, 1965, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-07-119981-0](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-07-119981-0 "Speciale:RicercaISBN/0-07-119981-0").

## Voci correlate

- [Mistura di distribuzioni](https://it.wikipedia.org/wiki/Mistura_di_distribuzioni "Mistura di distribuzioni")
- [Variabile casuale multivariata](https://it.wikipedia.org/wiki/Variabile_casuale_multivariata "Variabile casuale multivariata")
- [Misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità")
- [Processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico")
- [Winsorizzazione](https://it.wikipedia.org/wiki/Winsorizzazione "Winsorizzazione")
- [Matrice aleatoria](https://it.wikipedia.org/wiki/Matrice_aleatoria "Matrice aleatoria")

## Altri progetti

Altri progetti

- [Wikiversità](https://it.wikiversity.org/wiki/Variabili%20casuali "v:Variabili casuali")
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Random_variable?uselang=it)

- [Wikiversità](https://it.wikiversity.org/wiki/ "v:") contiene risorse sulle **[variabili casuali](https://it.wikiversity.org/wiki/Variabili%20casuali "v:Variabili casuali")**
- contiene immagini o altri file sulle **[variabili casuali](https://commons.wikimedia.org/wiki/Category:Random_variable?uselang=it)**

## Collegamenti esterni

- [Variabile aleatoria](https://www.treccani.it/enciclopedia/variabile-aleatoria_\(Enciclopedia-della-Matematica\)/), in Enciclopedia della Matematica, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2013.
- [Variabile casuale](https://www.treccani.it/enciclopedia/variabile-casuale_\(Enciclopedia-della-Matematica\)/), in Enciclopedia della Matematica, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2013.
- Samantha Leorato, [Variabile aleatoria](https://www.treccani.it/enciclopedia/variabile-aleatoria_\(Dizionario-di-Economia-e-Finanza\)/), in Dizionario di Economia e Finanza, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2012.
- (EN) [random variable](https://www.britannica.com/topic/random-variable), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Random Variable](http://mathworld.wolfram.com/RandomVariable.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [27896](https://thes.bncf.firenze.sbn.it/termine.php?id=27896) · [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh85111355](http://id.loc.gov/authorities/subjects/sh85111355) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4129514-6](https://d-nb.info/gnd/4129514-6) · [BNF](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Francia "Biblioteca nazionale di Francia") (FR) [cb121355344](https://catalogue.bnf.fr/ark:/12148/cb121355344) [(data)](https://data.bnf.fr/ark:/12148/cb121355344) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007563129305171](https://www.nli.org.il/en/authorities/987007563129305171) |
| --- | --- |

[^1]: [Definizione di Aleatorio](http://www.treccani.it/vocabolario/aleatorio/), su treccani.it. URL consultato il 9 febbraio 2015.

[^2]: DELI, Dizionario etimologico della lingua italiana, Zanichelli, 2009.