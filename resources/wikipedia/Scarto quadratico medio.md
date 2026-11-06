---
title: "Scarto quadratico medio"
source: "https://it.wikipedia.org/wiki/Scarto_quadratico_medio"
author:
  - "[[Wikipedia]]"
published: 2003-01-02
created: 2026-11-06
description:
tags:
  - "clippings"
---
![](https://upload.wikimedia.org/wikipedia/commons/7/7e/Standard_deviation_illustration.gif?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail_unscaled)

Una serie di dati con una media di 50 (in blu) e uno scarto quadratico medio (σ) di 20.

Lo **scarto quadratico medio**, più nota come **deviazione standard** (o **scarto tipo**, o **scostamento quadratico medio**), è un [indice di dispersione](https://it.wikipedia.org/wiki/Indice_di_dispersione "Indice di dispersione") [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica"), vale a dire un [indicatore](https://it.wikipedia.org/wiki/Indicatore_statistico "Indicatore statistico") usato per fornire una stima sintetica della variabilità di una [popolazione](https://it.wikipedia.org/wiki/Popolazione_\(statistica\) "Popolazione (statistica)") di dati o di una [variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale").

È uno dei modi per esprimere la dispersione dei dati intorno a un [indice di posizione](https://it.wikipedia.org/wiki/Indice_di_posizione "Indice di posizione"), quale può essere, ad esempio, la [media aritmetica](https://it.wikipedia.org/wiki/Media_aritmetica "Media aritmetica") o una sua stima. Ha pertanto la stessa [unità di misura](https://it.wikipedia.org/wiki/Unit%C3%A0_di_misura "Unità di misura") dei valori osservati (al contrario della [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") che ha come unità di misura il quadrato dell'unità di misura dei valori di riferimento). In [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica"), la [precisione](https://it.wikipedia.org/wiki/Precisione "Precisione") si può esprimere come lo scarto quadratico medio.

Il termine " *standard deviation* " è stato introdotto in statistica nel 1894 da [Karl Pearson](https://it.wikipedia.org/wiki/Karl_Pearson "Karl Pearson") [^1], assieme alla lettera greca $σ$ ([sigma](https://it.wikipedia.org/wiki/Sigma_\(lettera_greca\) "Sigma (lettera greca)")) che lo rappresenta. Il termine italiano "deviazione standard" ne è la traduzione più usata nel linguaggio comune; il termine dell' [Ente italiano di normazione](https://it.wikipedia.org/wiki/Ente_italiano_di_normazione "Ente italiano di normazione") è tuttavia "scarto tipo".[^2]

Lo scarto quadratico medio $σ$ è la radice quadrata della [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") [^3], la quale viene coerentemente rappresentata con il quadrato di sigma, $\sigma^{2}$.

## Statistica descrittiva

In [statistica descrittiva](https://it.wikipedia.org/wiki/Statistica_descrittiva "Statistica descrittiva") lo scarto quadratico medio di un [carattere](https://it.wikipedia.org/wiki/Carattere_\(statistica\) "Carattere (statistica)") $X$ rilevato su una [popolazione](https://it.wikipedia.org/wiki/Popolazione_\(statistica\) "Popolazione (statistica)") di $N$ unità statistiche si definisce nel seguente modo:[^4]

$\sigma_{X} = \sqrt{\frac{1}{N} \sum_{i = 1}^{N} \left(\right. x_{i} - \mu_{X} \left.\right)^{2}} ,$

dove $\mu_{X} = \frac{1}{N} \sum_{i = 1}^{N} x_{i}$ è la [media aritmetica](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") di $X$. Ossia lo scarto quadratico medio è la radice quadrata della [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza").

A partire dallo scarto quadratico medio si definisce anche il [coefficiente di variazione](https://it.wikipedia.org/wiki/Coefficiente_di_variazione "Coefficiente di variazione") [^5] o la *deviazione standard relativa* come il rapporto tra lo scarto tipo $\sigma_{X}$ e il [valore assoluto](https://it.wikipedia.org/wiki/Valore_assoluto "Valore assoluto") della media aritmetica della variabile in esame sempreché quella media sia non nulla:

$\sigma_{X}^{*} = \frac{\sigma_{X}}{\left|\mu_{X}\right|} .$

Questo indice relativo (che viene spesso espresso in termini percentuali [^6]) consente di effettuare confronti tra dispersioni di dati di tipo diverso, indipendentemente dalle loro quantità assolute.

### Formulazioni equivalenti

Lo scarto quadratico medio può essere espresso in una forma equivalente, ricalcolando come segue la [sommatoria](https://it.wikipedia.org/wiki/Sommatoria "Sommatoria") dei quadrati degli scarti:

$\begin{matrix}\sum_{i = 1}^{N} \left(\right. x_{i} - \mu_{X} \left.\right)^{2} & = \sum_{i = 1}^{N} \left(x_{i}^{2} - 2 x_{i} \mu_{X} + \mu_{X}^{2}\right) = \sum_{i = 1}^{N} x_{i}^{2} - 2 \mu_{X} \sum_{i = 1}^{N} x_{i} + N \mu_{X}^{2} \\ = \sum_{i = 1}^{N} x_{i}^{2} - 2 \mu_{X} \left(N \mu_{X}\right) + N \mu_{X}^{2} = \sum_{i = 1}^{N} x_{i}^{2} - 2 N \mu_{X}^{2} + N \mu_{X}^{2} = \sum_{i = 1}^{N} x_{i}^{2} - N \mu_{X}^{2} .\end{matrix}$

Applicando questo risultato alla formula originale per lo scarto quadratico medio, si ottiene:

$\sigma_{X} = \sqrt{\frac{1}{N} \left(\sum_{i = 1}^{N} x_{i}^{2} - N \mu_{X}^{2}\right)} = \sqrt{\frac{1}{N} \sum_{i = 1}^{N} x_{i}^{2} - \mu_{X}^{2}} .$

Nelle applicazioni informatiche, è a volte conveniente modificare la formula precedente:

$\sigma_{X} = \sqrt{\frac{1}{N} \left(\sum_{i = 1}^{N} x_{i}^{2} - N \mu_{X}^{2}\right)} = \frac{1}{N} \sqrt{N \sum_{i = 1}^{N} x_{i}^{2} - \left(N \mu_{X}\right)^{2}} = \frac{1}{N} \sqrt{N \sum_{i = 1}^{N} x_{i}^{2} - \left(\sum_{i = 1}^{N} x_{i}\right)^{2}}$

che consente, con sole tre variabili $\left(N , \sum x_{i} , \sum x_{i}^{2}\right)$, di calcolare lo scarto quadratico medio, oltre che la [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)"), di una successione di numeri di lunghezza $N$ senza dover ricorrere ad una memorizzazione degli stessi.

## Statistica inferenziale

Nell'ambito della [statistica inferenziale](https://it.wikipedia.org/wiki/Statistica_inferenziale "Statistica inferenziale") (dove è noto solo un campione, di numerosità $n$, dell'intera popolazione), soprattutto nel contesto della [teoria della stima](https://it.wikipedia.org/wiki/Teoria_della_stima "Teoria della stima"), uno stimatore per lo scarto quadratico medio di un [carattere](https://it.wikipedia.org/wiki/Carattere_\(statistica\) "Carattere (statistica)") $X$ è dato dallo scarto quadratico medio campionario:

$s_{X} = \sqrt{\frac{1}{n} \sum_{i = 1}^{n} \left(\right. x_{i} - \bar{x} \left.\right)^{2}} ,$

dove $\bar{x} = \frac{1}{n} \sum_{i = 1}^{n} x_{i}$ è la [media campionaria](https://it.wikipedia.org/wiki/Media_campionaria "Media campionaria") di $X$ (ossia la media aritmetica del carattere calcolata sul campione considerato).

Valgono i limiti $\underset{n \rightarrow N}{lim} \bar{x} = \mu_{X}$ e $\underset{n \rightarrow N}{lim} s_{X} = \sigma_{X}$, dove $N$ indica la numerosità della popolazione di riferimento, quindi $N$ è un intero positivo oppure $N=+∞$ a seconda dei casi.

Poiché il precedente stimatore $s_{X}$ è [distorto](https://it.wikipedia.org/wiki/Bias_\(statistica\) "Bias (statistica)"), per ottenerne uno non distorto si rimpiazza il denominatore $n$ con $n−1$ ottenendo:

$\left(\bar{s}\right)_{X} = \sqrt{\frac{1}{n - 1} \sum_{i = 1}^{n} \left(\right. x_{i} - \bar{x} \left.\right)^{2}} .$

Sostanzialmente, poiché non è nota la media dell'intera popolazione $\mu_{X}$, ma solo una sua stima (la media del campione $\bar{x}$), bisogna utilizzare $n−1$ per ottenere uno [stimatore corretto](https://it.wikipedia.org/wiki/Stimatore_corretto "Stimatore corretto") $\left(\bar{s}\right)_{X}^{2}$ della [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") incognita $\sigma_{X}^{2}$ di $X$ sull'intera popolazione a partire dai dati del campione. La sua radice quadrata diviene lo scarto quadratico medio campionario "corretto".

Questa correzione al denominatore fa sì che $\left(\bar{s}\right)_{X}$ sia maggiore rispetto a $s_{X}$, correggendo così la tendenza di $s_{X}$ a sottostimare le incertezze, soprattutto nel caso in cui si lavori con pochi dati ($n$ "piccolo"; nelle applicazioni pratiche, si considera "piccolo" un campione formato da meno di 30 elementi).

Osserviamo il caso limite di $n=1$, cioè quando si ha un campione di un solo elemento. Si ha $s_{X} = 0$, che non è molto ragionevole nell'ambito della statistica inferenziale. Invece $\left(\bar{s}\right)_{X} = 0 / 0$ non è definito, rispecchiando così la totale ignoranza inerente all'incertezza su una singola misura. In questo senso, si afferma che $\left(\bar{s}\right)_{X}$ non dice nulla sul singolo caso.

La differenza tra $s_{X}$ e $\left(\bar{s}\right)_{X}$ per campioni molto estesi diventa numericamente insignificante.

## Probabilità

Sia $X$ una [variabile aleatoria](https://it.wikipedia.org/wiki/Variabile_aleatoria "Variabile aleatoria"), lo scarto quadratico medio è definito come la radice quadrata della [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") di $X$

$\sigma_{X} = \sqrt{\sigma_{X}^{2}} .$

Formalmente lo scarto quadratico medio di una variabile aleatoria può essere calcolato a partire dalla [funzione generatrice dei momenti](https://it.wikipedia.org/wiki/Funzione_generatrice_dei_momenti "Funzione generatrice dei momenti"), in particolare è la radice quadrata della differenza tra il momento secondo ed il momento primo elevato al quadrato, cioè

$\sigma_{X} = \sqrt{\mathbb{E} \left[x^{2}\right] - \left(\right. \mathbb{E} \left[x\right] \left.\right)^{2}} ,$

dove $𝔼[X]$ è il [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") di $X$.

## Applicazioni

In [fisica](https://it.wikipedia.org/wiki/Fisica "Fisica"), lo scarto quadratico medio è un ottimo indice dell' [errore casuale](https://it.wikipedia.org/wiki/Errore_casuale "Errore casuale") della misurazione di una grandezza fisica.

In ingegneria, è uno dei parametri da considerare per valutare la [capacità di un processo](https://it.wikipedia.org/wiki/Capacit%C3%A0_di_un_processo "Capacità di un processo") produttivo, o più in generale, l'affidabilità di una campagna di test per determinare il [tasso di guasto](https://it.wikipedia.org/wiki/Tasso_di_guasto "Tasso di guasto") di un dato componente.

In ambito [finanziario](https://it.wikipedia.org/wiki/Matematica_finanziaria "Matematica finanziaria"), viene usato per indicare la variabilità di un'attività finanziaria e dei suoi payoff ([rendimenti](https://it.wikipedia.org/wiki/Rendimento_\(economia\) "Rendimento (economia)")). Esso fornisce quindi, implicitamente, una misura della [volatilità](https://it.wikipedia.org/wiki/Volatilit%C3%A0_\(economia\) "Volatilità (economia)") dell'attività, quindi del suo [rischio](https://it.wikipedia.org/wiki/Rischio "Rischio").

In ambito sportivo è utilizzato per valutare la prestazione di un giocatore di [bowling](https://it.wikipedia.org/wiki/Bowling "Bowling") in riferimento ad un certo numero di partite. Il valore trovato non incide sul punteggio ma sintetizza le capacità e i miglioramenti del giocatore.[^7]

## Note

## Bibliografia

- M. Ross Sheldon, [Introduzione alla statistica](https://books.google.it/books?id=Fnv1AwAAQBAJ), 2ª ed., Maggioli Editore, 2014, [ISBN 88-916-0267-1](https://it.wikipedia.org/wiki/Special:BookSources/8891602671).
- Thomas H. Wannacott, Introduzione alla statistica, 19ª ed., Franco Angeli, 2009, [ISBN 978-88-568-1260-2](https://it.wikipedia.org/wiki/Special:BookSources/9788856812602).

## Voci correlate

- [Root sum squared](https://it.wikipedia.org/wiki/Root_sum_squared "Root sum squared")
- [Coefficiente di variazione](https://it.wikipedia.org/wiki/Coefficiente_di_variazione "Coefficiente di variazione")
- [Scarto interquartile](https://it.wikipedia.org/wiki/Scarto_interquartile "Scarto interquartile")
- [Varianza](https://it.wikipedia.org/wiki/Varianza "Varianza")
- [Stimatore corretto#Esempio: stimatore della varianza](https://it.wikipedia.org/wiki/Stimatore_corretto#Esempio:_stimatore_della_varianza "Stimatore corretto")
- [Precisione](https://it.wikipedia.org/wiki/Precisione "Precisione")
- [Median absolute deviation](https://it.wikipedia.org/wiki/Median_absolute_deviation "Median absolute deviation")
- [Regola 68-95-99,7](https://it.wikipedia.org/wiki/Regola_68-95-99,7 "Regola 68-95-99,7")

## Altri progetti

Altri progetti

- [Wikizionario](https://it.wiktionary.org/wiki/deviazione%20standard "wikt:deviazione standard")
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Standard_deviation?uselang=it)

- [Wikizionario](https://it.wiktionary.org/wiki/ "wikt:") contiene il lemma di dizionario « **[deviazione standard](https://it.wiktionary.org/wiki/deviazione%20standard "wikt:deviazione standard")** »
- contiene immagini o altri file sulla **[deviazione standard](https://commons.wikimedia.org/wiki/Category:Standard_deviation?uselang=it)**

## Collegamenti esterni

- [scarto²](https://www.sapere.it/enciclopedia/scarto%C2%B2.html), su sapere.it, [De Agostini](https://it.wikipedia.org/wiki/De_Agostini "De Agostini").
- [Deviazione standard](https://www.treccani.it/enciclopedia/deviazione-standard_\(Enciclopedia-della-Matematica\)/), in Enciclopedia della Matematica, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2013.
- [Deviazione standard](https://www.treccani.it/enciclopedia/deviazione-standard_\(Dizionario-di-Economia-e-Finanza\)/), in Dizionario di Economia e Finanza, [Istituto dell'Enciclopedia Italiana](https://it.wikipedia.org/wiki/Istituto_dell'Enciclopedia_Italiana "Istituto dell'Enciclopedia Italiana"), 2012.
- (EN) [Opere riguardanti Standard deviations](https://openlibrary.org/subjects/standard_deviations), su [Open Library](https://it.wikipedia.org/wiki/Open_Library "Open Library"), [Internet Archive](https://it.wikipedia.org/wiki/Internet_Archive "Internet Archive").
- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Standard Deviation](http://mathworld.wolfram.com/StandardDeviation.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- (EN) [Quadratic deviation](https://encyclopediaofmath.org/wiki/Quadratic_deviation), su [Encyclopaedia of Mathematics](https://it.wikipedia.org/wiki/Encyclopaedia_of_Mathematics "Encyclopaedia of Mathematics"), Springer e European Mathematical Society.
- (EN) Denis Howe, [standard deviation](https://foldoc.org/standard%20deviation "foldoc:standard deviation"), in [Free On-line Dictionary of Computing](https://it.wikipedia.org/wiki/Free_On-line_Dictionary_of_Computing "Free On-line Dictionary of Computing"). Disponibile con licenza [GFDL](https://it.wikipedia.org/wiki/GNU_Free_Documentation_License "GNU Free Documentation License")
- (EN) [Scarto quadratico medio](http://goldbook.iupac.org/D01650.html), su goldbook.iupac.org.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh85127303](http://id.loc.gov/authorities/subjects/sh85127303) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4767332-1](https://d-nb.info/gnd/4767332-1) |
| --- | --- |

[^1]: [Karl Pearson](https://it.wikipedia.org/wiki/Karl_Pearson "Karl Pearson"), *On the dissection of asymmetrical frequency curves*, 1894

[^2]: [UNI](https://it.wikipedia.org/wiki/Ente_nazionale_italiano_di_unificazione "Ente nazionale italiano di unificazione"), Norma italiana [UNI ISO 3534-1](https://it.wikipedia.org/wiki/UNI_ISO_3534-1 "UNI ISO 3534-1"):2000, *Statistica - Vocabolario e simboli, Probabilità e termini statistici generali*, Milano: UNI, 2000, definizione 1.23.

[^3]: [Glossario Istat](https://web.archive.org/web/20111231130402/http://www3.istat.it/servizi/studenti/binariodie/CorsoExcel/Glossario.htm), su www3.istat.it (archiviato dall' url originale il 31 dicembre 2011).

[^4]: [Sheldon](#CITEREFSheldon), p. 96.

[^5]: [UNI](https://it.wikipedia.org/wiki/Ente_nazionale_italiano_di_unificazione "Ente nazionale italiano di unificazione"), Norma italiana [UNI ISO 3534-1](https://it.wikipedia.org/wiki/UNI_ISO_3534-1 "UNI ISO 3534-1"):2000, *Statistica - Vocabolario e simboli, Probabilità e termini statistici generali*, Milano: UNI, 2000, definizione 1.24 e 2.35.

[^6]: Domenico Piccolo, *Statistica*, Il Mulino, Bologna, 1998, p. 123.

[^7]: (EN) Joan L. Martin, [Notes: Bowling Norms for College Men and Women](https://www.tandfonline.com/doi/full/10.1080/10671188.1960.10613082), in Research Quarterly. American Association for Health, Physical Education and Recreation, vol. 31, n. 1, 1960-03, pp. 113-116, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1080/10671188.1960.10613082](https://dx.doi.org/10.1080%2F10671188.1960.10613082). URL consultato il 12 giugno 2024.