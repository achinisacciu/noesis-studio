---
title: "Classificatore bayesiano"
source: "https://it.wikipedia.org/wiki/Classificatore_bayesiano"
author:
  - "[[Wikipedia]]"
published: 2009-03-08
created: 2026-11-06
description:
tags:
  - "clippings"
---
Un **classificatore *bayesiano*** è un [classificatore](https://it.wikipedia.org/wiki/Classificatore_\(matematica\) "Classificatore (matematica)") basato sull'applicazione del [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") [^1].

Il classificatore *bayesiano* richiede la conoscenza delle probabilità a priori e condizionali relative al problema, quantità che in generale non sono note ma sono tipicamente stimabili. Se è possibile ottenere delle stime affidabili delle probabilità coinvolte nel teorema, il classificatore *bayesiano* risulta generalmente affidabile e potenzialmente compatto. Spesso viene detto "classificatore *bayesiano* completo" (*full Bayes classifier* o anche *belief network*). Per costruzione, il classificatore *bayesiano* minimizza il rischio di classificazione [^1].

Nel gergo della [classificazione di testi](https://it.wikipedia.org/wiki/Text_categorization "Text categorization"), con il termine "classificatore *bayesiano* " ci si riferisce convenzionalmente al cosiddetto "classificatore *bayesiano* ingenuo" (*naïve Bayes classifier*) [^1] [^2], ossia un classificatore *bayesiano* semplificato con un modello di [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") sottostante che fa l'ipotesi di [indipendenza](https://it.wikipedia.org/wiki/Indipendenza_\(probabilit%C3%A0\) "Indipendenza (probabilità)") delle *[caratteristiche](https://it.wikipedia.org/wiki/Caratteristica_\(apprendimento_automatico\) "Caratteristica (apprendimento automatico)")*, cioè assume che la presenza o l'assenza di un particolare attributo in un documento testuale non è correlata alla presenza o assenza di altri attributi.

In queste ipotesi semplificate (dette appunto "ingenue", in inglese anche *idiot*), il modello è realizzabile con molta maggiore facilità. L'esperienza dimostra che il metodo funziona in molti problemi pratici [^3], come per esempio il filtraggio anti-spam adattivo [^4].

## Note

## Voci correlate

- [Teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes")
- [Apprendimento supervisionato](https://it.wikipedia.org/wiki/Apprendimento_supervisionato "Apprendimento supervisionato")

[^1]: Duda, R. O. & P. E. Hart (1973), *Pattern Classification and Scene Analysis*, New York: John Wiley & Sons

[^2]: Langley, P., W. Iba, & K. Thompson (1992), *An analysis of Bayesian classifiers*, da *Proceedings, Tenth National Conference on Artificial Intelligence* (pp. 223–228). Menlo Park, CA: AAAI Press

[^3]: N. Friedman, D. Geiger, & M. Goldszmit (1997), *Bayesian Network Classifiers*, in *Machine Learning*, 29, 131–163

[^4]: M. Sahami, S. Dumais, D. Heckerman, E. Horvitz (1998), *A Bayesian approach to filtering junk e-mail*, AAAI'98 *Workshop on Learning for Text Categorization*