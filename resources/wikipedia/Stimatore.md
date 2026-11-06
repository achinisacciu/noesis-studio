---
title: "Stimatore"
source: "https://it.wikipedia.org/wiki/Stimatore"
author:
  - "[[Wikipedia]]"
published: 2002-11-08
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica") uno **stimatore** (puntuale) è una funzione che associa ad ogni possibile [campione](https://it.wikipedia.org/wiki/Campione_\(statistica\) "Campione (statistica)") un valore del parametro da stimare. È una funzione di un campione di dati estratti casualmente da una [popolazione](https://it.wikipedia.org/wiki/Popolazione_statistica "Popolazione statistica").

Il valore assunto dallo stimatore in corrispondenza di un particolare campione è detto *stima*.

Uno stimatore puntuale è dunque una [variabile casuale](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") funzione del campione, a valori nello spazio parametrico (ossia nell'insieme dei possibili valori del parametro).

## Proprietà desiderabili per uno stimatore

In generale, non si dispone di un criterio per determinare quale stimatore per una data quantità sia il *migliore*. Nell'ambito della statistica classica, tuttavia, è stata proposta una serie di proprietà considerate desiderabili per uno stimatore.

In primo luogo, un *buono* stimatore dovrebbe fornire stime che si *avvicinano* al valore del parametro da stimare, ossia l'errore che commettiamo assumendo che il valore del parametro sia eguale alla stima dev'essere *piccolo*. Non conoscendo il valore del parametro non siamo in grado di quantificare l'errore commesso per una particolare stima, possiamo però quantificare lo scostamento medio tra la variabile casuale *stimatore* e il parametro. La bontà di uno stimatore è infatti valutata sulla base di proprietà quali la [correttezza](https://it.wikipedia.org/wiki/Correttezza_\(statistica\) "Correttezza (statistica)"), la correttezza asintotica, la [consistenza](https://it.wikipedia.org/wiki/Consistenza_\(statistica\) "Consistenza (statistica)") e l' [efficienza](https://it.wikipedia.org/wiki/Efficienza_\(statistica\) "Efficienza (statistica)") che sono legate a tale scostamento medio.

In termini più precisi, se con $μ$ indichiamo il parametro da stimare e con $\overset{̂}{\mu} \left(Y\right)$ lo stimatore, funzione del campione $Y,$ possiamo calcolare il [valore atteso](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") dello scostamento tra stimatore e parametro, detta distorsione (anche detta, con termine [inglese](https://it.wikipedia.org/wiki/Lingua_inglese "Lingua inglese"), *[bias](https://it.wikipedia.org/wiki/Bias_\(statistica\) "Bias (statistica)")*):

$\text{E} \left[\overset{̂}{\mu} \left(Y\right)\right] - \mu$

e l'errore quadratico medio

$\text{E} \left[\right. \left(\overset{̂}{\mu} \left(Y\right) - \mu \left.\right)^{2}\right]$.

Queste sono le principali quantità usate per valutare la bontà di uno stimatore nel senso che quanto più piccole sono, tanto migliore è lo stimatore.

Più in generale, le proprietà desiderabili per uno stimatore sono:

- [Correttezza](https://it.wikipedia.org/wiki/Correttezza_\(statistica\) "Correttezza (statistica)")
- [Consistenza](https://it.wikipedia.org/wiki/Consistenza_\(statistica\) "Consistenza (statistica)")
- [Efficienza](https://it.wikipedia.org/wiki/Efficienza_\(statistica\) "Efficienza (statistica)")
- [Sufficienza](https://it.wikipedia.org/wiki/Sufficienza_\(statistica\) "Sufficienza (statistica)")
- [Completezza](https://it.wikipedia.org/wiki/Completezza_\(statistica\) "Completezza (statistica)")
- [Ancillarità](https://it.wikipedia.org/wiki/Ancillarit%C3%A0_\(statistica\)?action=edit&redlink=1 "Ancillarità (statistica) (la pagina non esiste)")

## Esempio

Siamo interessati a conoscere la statura media della popolazione residente femminile italiana adulta (con ciò intendendo le persone di età maggiore di 18 anni). La popolazione è pertanto l'insieme degli $N$ individui di genere femminile residenti in Italia aventi età maggiore di 18 anni. Se $x_{1} , \ldots , x_{N}$ sono le loro altezze, il parametro da stimare è $\mu = \text{E} \left[x_{i}\right]$.

Non potendo osservare l'intera popolazione non conosciamo il valore di $μ$, quindi per inferire su tale valore osserviamo un sottoinsieme di 1000 unità dalla popolazione (campione) scelte in modo che ciascun individuo nella popolazione abbia la stessa probabilità di essere incluso nel campione. Per ciascuna unità del campione misuriamo l'altezza, ottenendo così la sequenza $y_{1} , \ldots , y_{1000}$.

Uno stimatore ragionevole per $μ$ è allora la media aritmetica delle $y_{i}$:

$\overset{̂}{\mu} = \frac{1}{1000} \sum_{i = 1}^{1000} y_{i}$.

## Bibliografia

- James Stock, Mark Watson, Introduzione all'econometria, Milano, Pearson Education, 2005, p. 59, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-88-7192-267-6](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-88-7192-267-6 "Speciale:RicercaISBN/978-88-7192-267-6").

## Voci correlate

- [Funzione di verosimiglianza](https://it.wikipedia.org/wiki/Funzione_di_verosimiglianza "Funzione di verosimiglianza")
- [Metodo dei minimi quadrati](https://it.wikipedia.org/wiki/Metodo_dei_minimi_quadrati "Metodo dei minimi quadrati")
- [Metodo dei momenti (statistica)](https://it.wikipedia.org/wiki/Metodo_dei_momenti_\(statistica\) "Metodo dei momenti (statistica)")
- [Metodo della massima verosimiglianza](https://it.wikipedia.org/wiki/Metodo_della_massima_verosimiglianza "Metodo della massima verosimiglianza")
- [Correttezza (statistica)](https://it.wikipedia.org/wiki/Correttezza_\(statistica\) "Correttezza (statistica)")
- [Consistenza (statistica)](https://it.wikipedia.org/wiki/Consistenza_\(statistica\) "Consistenza (statistica)")
- [Efficienza (statistica)](https://it.wikipedia.org/wiki/Efficienza_\(statistica\) "Efficienza (statistica)")
- [Sufficienza (statistica)](https://it.wikipedia.org/wiki/Sufficienza_\(statistica\) "Sufficienza (statistica)")
- [Completezza (statistica)](https://it.wikipedia.org/wiki/Completezza_\(statistica\) "Completezza (statistica)")

## Altri progetti

Altri progetti

- [Wikizionario](https://it.wiktionary.org/wiki/stimatore "wikt:stimatore")

- [Wikizionario](https://it.wiktionary.org/wiki/ "wikt:") contiene il lemma di dizionario « **[stimatore](https://it.wiktionary.org/wiki/stimatore "wikt:stimatore")** »

## Collegamenti esterni

- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Estimator](http://mathworld.wolfram.com/Estimator.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [61564](https://thes.bncf.firenze.sbn.it/termine.php?id=61564) |
| --- | --- |