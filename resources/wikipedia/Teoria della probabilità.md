---
title: "Teoria della probabilità"
source: "https://it.wikipedia.org/wiki/Teoria_della_probabilit%C3%A0"
author:
  - "[[Wikipedia]]"
published: 2005-03-14
created: 2026-11-06
description:
tags:
  - "clippings"
---
La **teoria della probabilità** è lo studio [matematico](https://it.wikipedia.org/wiki/Matematica "Matematica") della [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità").

I matematici si riferiscono alle probabilità come a numeri nell'intervallo da 0 a 1, assegnati ad " [eventi](https://it.wikipedia.org/wiki/Evento_\(teoria_della_probabilit%C3%A0\) "Evento (teoria della probabilità)") " la cui ricorrenza è [casuale](https://it.wikipedia.org/wiki/Caso_\(circostanza\) "Caso (circostanza)"). Le probabilità $P(E)$ sono assegnate ad eventi $E$ secondo gli [assiomi della probabilità](https://it.wikipedia.org/wiki/Assiomi_della_probabilit%C3%A0 "Assiomi della probabilità").

La probabilità che un evento $E$ avvenga *dato* il verificarsi noto di un evento $F$ è la [probabilità condizionata](https://it.wikipedia.org/wiki/Probabilit%C3%A0_condizionata "Probabilità condizionata") di $E$ *dato* $F$; il suo valore numerico è $P(E∩F)/P(F)$ (finché $P(F)$ è diverso da zero). Se la probabilità condizionale di $E$ dato $F$ è la stessa della probabilità ("non condizionale") di $E$, allora $E$ ed $F$ sono detti eventi [indipendenti](https://it.wikipedia.org/wiki/Indipendenza_statistica "Indipendenza statistica"). Che questa relazione tra $E$ e $F$ sia simmetrica, può essere visto più chiaramente osservando che è la stessa cosa che dire $P(E∩F)=P(E)P(F)$.

Due concetti cruciali nella teoria della probabilità sono quelli di [variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") e di [distribuzione probabilistica](https://it.wikipedia.org/wiki/Distribuzione_probabilistica "Distribuzione probabilistica") di una variabile casuale. In altri termini descrivere in termini probabilistici o statistici un fenomeno aleatorio nel tempo, caratterizzabile dunque da una variabile aleatoria, vuol dire descriverlo in termini di densità di distribuzione di probabilità e dei suoi parametri di media o valore atteso e varianza.

## Una visione astratta della probabilità

I matematici ritengono che la teoria della probabilità sia lo studio di uno spazio *astratto* di probabilità (su cui sono ad esempio definite le [variabili casuali](https://it.wikipedia.org/wiki/Variabili_casuali "Variabili casuali") o aleatorie), un approccio introdotto da [Kolmogorov](https://it.wikipedia.org/wiki/Andrej_Nikolaevi%C4%8D_Kolmogorov "Andrej Nikolaevič Kolmogorov") nel [1930](https://it.wikipedia.org/wiki/1930 "1930") (anche detto *approccio assiomatico*). Uno [spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità") è una terna $(Ω,𝔉,P)$, dove:

- $Ω$ è un insieme non vuoto, a volte chiamato [spazio campionario](https://it.wikipedia.org/wiki/Spazio_campionario "Spazio campionario"), in cui ognuno dei membri si può pensare come un potenziale risultato di un esperimento casuale. Per esempio, se 100 votanti devono essere estratti a caso tra tutti i votanti di un insieme e ad essi viene chiesto per chi voteranno, allora l'insieme di tutte le sequenze dei 100 votanti sarebbe lo spazio campionario $Ω$.
- $𝔉$ è una [σ-algebra](https://it.wikipedia.org/wiki/Sigma-algebra "Sigma-algebra") di insiemi di $Ω$ i cui elementi sono chiamati *eventi*. Per esempio, l'insieme di tutte le sequenze di 100 elettori di cui almeno 60 voteranno per un certo candidato viene identificato con l'"evento" che almeno 60 dei 100 elettori estratti voteranno in quel dato modo. Dire che $𝔉$ è una $σ$ -algebra implica necessariamente che il complemento di ogni evento è un evento, e l'unione di ogni sequenza (finita o infinita numerabile) di eventi è un evento.
- $P$ è una misura della probabilità in $𝔉$, cioè una [misura](https://it.wikipedia.org/wiki/Misura_\(matematica\) "Misura (matematica)") tale per cui $P(Ω)=1$.

È importante notare che $P$ è definita in $𝔉$ e non in $Ω$.

Con $Ω$ [numerabile](https://it.wikipedia.org/wiki/Numerabile "Numerabile") possiamo definire $𝔉:=$ insieme di potenza $(Ω)$ che è banalmente una $σ$ -algebra ed il più grande che si possa creare usando $Ω$. In uno spazio discreto possiamo quindi omettere $𝔉$ e scrivere solo $(Ω,P)$ per definirlo.

Se d'altra parte $Ω$ è non numerabile e si usa $𝔉=$ insieme di potenza $(Ω)$ cadiamo nella difficoltà di definire la nostra misura di probabilità $P$ perché $𝔉$ è 'immenso'. Quindi dobbiamo usare una $σ$ -algebra $𝔉$ più piccola (per esempio l' [algebra di Borel](https://it.wikipedia.org/wiki/Algebra_di_Borel "Algebra di Borel") di $Ω$). Si definisce questo tipo di spazio probabilistico uno spazio probabilistico continuo e ci porta alcuni problemi nella [teoria della misura](https://it.wikipedia.org/wiki/Teoria_della_misura "Teoria della misura") quando proviamo a definire $P$.

Una [variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") è una [funzione misurabile](https://it.wikipedia.org/wiki/Funzione_misurabile "Funzione misurabile") da $Ω$ nei reali. Per esempio, il numero di elettori che voteranno per un dato candidato nel campione di 100 dell'esempio precedente è una variabile casuale.

Se $X$ è una variabile casuale, l'insieme ${ω∈Ω:X(ω)≥60}$ è un "evento", e la notazione $P(X≥60)$ è un'abbreviazione di $P({ω∈Ω:X(ω)≥60})$.

## Filosofia delle applicazioni della probabilità

Alcuni statistici assegneranno delle probabilità solo agli eventi che si pensano essere casuali, in base alle loro frequenze relative, o a sottoinsiemi di popolazione in relazione al tutto; questi sono *frequentisti*. Altri assegnano probabilità a proposizioni incerte o secondo gradi [soggettivi](https://it.wikipedia.org/wiki/Probabilit%C3%A0_soggettiva?action=edit&redlink=1 "Probabilità soggettiva (la pagina non esiste)") di confidenza nella loro verità, o a livelli logicamente giustificabili di confidenza nella loro verità. Tali persone sono *bayesiani*. Un bayesiano può assegnare una probabilità alla proposizione che c'era vita su [Marte](https://it.wikipedia.org/wiki/Marte_\(astronomia\) "Marte (astronomia)") un miliardo di anni fa, dal momento che questo è incerto; un frequentista non assegnerebbe una probabilità a tale proposizione, poiché non si tratta di un evento casuale che abbia una frequenza relativa a lungo termine.

## Bibliografia

- (EN) Patrick P. Billingsley, [Probability and measure](https://archive.org/details/probabilitymeasu0000bill), 3ª ed., New York, John Wiley & Sons, 1995, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-471-00710-2](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-471-00710-2 "Speciale:RicercaISBN/0-471-00710-2").
- (EN) [Harold Jeffreys](https://it.wikipedia.org/wiki/Harold_Jeffreys "Harold Jeffreys"), The Theory of Probability, Oxford and Clarendon Press, 1939.
- (DE) [Andrej N. Kolmogorov](https://it.wikipedia.org/wiki/Andrej_Nikolaevi%C4%8D_Kolmogorov "Andrej Nikolaevič Kolmogorov"), Grundbegriffe der Wahrscheinlichkeitsrechnung, 1939.
- (FR) [Pierre Simon Laplace](https://it.wikipedia.org/wiki/Pierre_Simon_Laplace "Pierre Simon Laplace"), Theorie Analytique des Probabilités, Parigi, Courcier, 1812.
- (EN) [Edward Nelson](https://it.wikipedia.org/wiki/Edward_Nelson_\(matematico\)?action=edit&redlink=1 "Edward Nelson (matematico) (la pagina non esiste)"), [Radically Elementary Probability Theory](https://archive.org/details/radicallyelement0000nels), 1987, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-06-91-08474-9](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-06-91-08474-9 "Speciale:RicercaISBN/978-06-91-08474-9").
- (EN) Yuri A. Rozanov, Probability Theory, Random Processes and Mathematical statistics, Kluwer, 1995, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-7923-3764-6](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-7923-3764-6 "Speciale:RicercaISBN/0-7923-3764-6").
- [Andrei N. Kolmogorov](https://it.wikipedia.org/wiki/Andrej_Nikolaevi%C4%8D_Kolmogorov "Andrej Nikolaevič Kolmogorov"), *Teoria delle probabilità*, a cura di Luigi Accardi; Roma, Edizioni Teknos, 1995.
- Andrea Pascucci, Teoria della Probabilità, Springer, 2020, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-88-470-3999-5](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-88-470-3999-5 "Speciale:RicercaISBN/978-88-470-3999-5").
- (EN) Richard von Mises, [Probability, Statistics and Truth](https://archive.org/details/probabilitystati0000vonm), Dover Publications, 1981, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-0486242149](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-0486242149 "Speciale:RicercaISBN/978-0486242149").

## Voci correlate

- [Probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità")
- [Misura di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità")
- [Funzione di probabilità](https://it.wikipedia.org/wiki/Funzione_di_probabilit%C3%A0 "Funzione di probabilità")
- [Valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso")
- [Evento (teoria della probabilità)](https://it.wikipedia.org/wiki/Evento_\(teoria_della_probabilit%C3%A0\) "Evento (teoria della probabilità)")
- [Assiomi della probabilità](https://it.wikipedia.org/wiki/Assiomi_della_probabilit%C3%A0 "Assiomi della probabilità")
- [Variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale"), [distribuzione di probabilità](https://it.wikipedia.org/wiki/Variabile_casuale#Distribuzione_di_probabilit%C3%A0 "Variabile casuale")
- [Indipendenza statistica](https://it.wikipedia.org/wiki/Indipendenza_statistica "Indipendenza statistica")
- [Uso sbagliato della statistica](https://it.wikipedia.org/wiki/Uso_sbagliato_della_statistica "Uso sbagliato della statistica")
- [Criterio di Kelly](https://it.wikipedia.org/wiki/Criterio_di_Kelly "Criterio di Kelly")
- [Geometria dell'informazione](https://it.wikipedia.org/wiki/Information_geometry "Information geometry")

## Altri progetti

Altri progetti

- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Probability_theory?uselang=it)

- contiene immagini o altri file sulla **[teoria della probabilità](https://commons.wikimedia.org/wiki/Category:Probability_theory?uselang=it)**

## Collegamenti esterni

- Eugenio Regazzini, [La seconda rivoluzione scientifica: matematica e logica. La probabilità](https://www.treccani.it/enciclopedia/la-seconda-rivoluzione-scientifica-matematica-e-logica-la-probabilita_\(Storia-della-Scienza\)), su Treccani.it – Enciclopedie on line, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2004.
- (EN) David O. Siegmund, [probability theory](https://www.britannica.com/topic/probability-theory), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4079013-7](https://d-nb.info/gnd/4079013-7) · [NDL](https://it.wikipedia.org/wiki/Biblioteca_della_Dieta_nazionale_del_Giappone "Biblioteca della Dieta nazionale del Giappone") (EN, JA) [00564753](https://id.ndl.go.jp/auth/ndlna/00564753) |
| --- | --- |