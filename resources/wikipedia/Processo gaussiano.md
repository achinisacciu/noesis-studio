---
title: "Processo gaussiano"
source: "https://it.wikipedia.org/wiki/Processo_gaussiano"
author:
  - "[[Wikipedia]]"
published: 2009-08-12
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [teoria delle probabilità](https://it.wikipedia.org/wiki/Teoria_delle_probabilit%C3%A0 "Teoria delle probabilità") un **processo gaussiano** è un [processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico") *f(**x**)*, ossia una collezione di [variabili aleatorie](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") indicizzate (in base al tempo o allo spazio), tale che ogni insieme finito di tali variabili abbia una [distribuzione di probabilità](https://it.wikipedia.org/wiki/Misura_di_probabilit%C3%A0 "Misura di probabilità") [gaussiana](https://it.wikipedia.org/wiki/Variabile_casuale_normale "Variabile casuale normale") multivariata.

La distribuzione del processo gaussiano è la [distribuzione congiunta](https://it.wikipedia.org/wiki/Distribuzione_congiunta "Distribuzione congiunta") di tutte le sue (infinite) variabili e, come tale, è una distribuzione su funzioni dal dominio continuo (ad es. il tempo o lo spazio). Quindi un processo gaussiano può essere considerato la generalizzazione a dimensioni infinite della distribuzione normale multivariata.

## Definizione

Un processo gaussiano è specificato interamente dalla sua [media](https://it.wikipedia.org/wiki/Valore_atteso "Valore atteso") *$m_{f}$ (**x**)* e dalla [covarianza](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\) "Covarianza (probabilità)") *$k_{f}$ (**x**,**x'**)*, e viene indicato nel modo seguente:

$f \left(𝐱\right) \sim \mathcal{N} \left(m_{f} \left(𝐱\right) , k_{f} \left(𝐱 , 𝐱^{'}\right)\right)$

Talvolta si assume che la media sia pari a zero e spesso si sceglie come insieme indice quello temporale cosicché il processo gaussiano risulti definito sul [tempo](https://it.wikipedia.org/wiki/Tempo "Tempo") [^1]. Accade di frequente nell'ambito delle [telecomunicazioni](https://it.wikipedia.org/wiki/Telecomunicazioni "Telecomunicazioni"), dove vari segnali vengono interpretati come processi gaussiani (ad esempio il [rumore gaussiano](https://it.wikipedia.org/wiki/Rumore_gaussiano "Rumore gaussiano")).

## Alcune applicazioni

Un processo gaussiano può essere usato come [distribuzione di probabilità a priori](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0_a_priori "Distribuzione di probabilità a priori") sulle funzioni nell' [inferenza bayesiana](https://it.wikipedia.org/wiki/Inferenza_bayesiana "Inferenza bayesiana"). L'inferenza per valori continui che fa uso di processi gaussiani è nota come [regressione](https://it.wikipedia.org/wiki/Analisi_di_regressione "Analisi di regressione") gaussiana e trova utilizzo in svariati campi, dall' [automazione](https://it.wikipedia.org/wiki/Automazione "Automazione") alla [geostatistica](https://it.wikipedia.org/wiki/Geostatistica "Geostatistica") ([Kriging](https://it.wikipedia.org/wiki/Kriging "Kriging")). I processi gaussiani sono, inoltre, un potente strumento per l' [interpolazione](https://it.wikipedia.org/wiki/Interpolazione_\(matematica\) "Interpolazione (matematica)") non lineare.

Nell'ambito dell' [apprendimento supervisionato](https://it.wikipedia.org/wiki/Apprendimento_supervisionato "Apprendimento supervisionato"), i processi gaussiani sono impiegati in metodi [non parametrici](https://it.wikipedia.org/wiki/Statistica_non_parametrica "Statistica non parametrica") basati su [kernel](https://it.wikipedia.org/wiki/Kernel_definito_positivo "Kernel definito positivo") utili a risolvere problemi di classificazione e regressione.[^2]

## Note

## Bibliografia

- (EN) C.E. Rasmussen, C.K.I Williams, [Gaussian Processes for Machine Learning](https://www.gaussianprocess.org/gpml/), MIT Press, 2006, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-262-18253-X](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-262-18253-X "Speciale:RicercaISBN/0-262-18253-X").
- (EN) N. Benvenuto, R. Corvaja; T. Erseghe; N. Laurenti, Communication Systems: Fundamentals and Design Methods, Wiley, 2007, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-470-01822-4](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-470-01822-4 "Speciale:RicercaISBN/0-470-01822-4").

## Voci correlate

- [Processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico")
- [Processo di Wiener](https://it.wikipedia.org/wiki/Processo_di_Wiener "Processo di Wiener")
- [Processo di Markov](https://it.wikipedia.org/wiki/Processo_di_Markov "Processo di Markov")

## Collegamenti esterni

- [The Gaussian Processes Web Site](http://www.gaussianprocess.org/), su GaussianProcess.org.
- [Classificazione e regressione basate su processi gaussiani](https://scikit-learn.org/stable/modules/gaussian_process.html) in Scikit-Learn

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [45384](https://thes.bncf.firenze.sbn.it/termine.php?id=45384) · [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh85053558](http://id.loc.gov/authorities/subjects/sh85053558) · [BNF](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Francia "Biblioteca nazionale di Francia") (FR) [cb119469389](https://catalogue.bnf.fr/ark:/12148/cb119469389) [(data)](https://data.bnf.fr/ark:/12148/cb119469389) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007560462305171](https://www.nli.org.il/en/authorities/987007560462305171) · [NDL](https://it.wikipedia.org/wiki/Biblioteca_della_Dieta_nazionale_del_Giappone "Biblioteca della Dieta nazionale del Giappone") (EN, JA) [01180243](https://id.ndl.go.jp/auth/ndlna/01180243) |
| --- | --- |

[^1]: David J. C. MacKay, [Information theory, inference, and learning algorithms](https://www.inference.org.uk/mackay/itila/), 22nd printing, Cambridge University Press, 2003, p. 540, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-0-521-64298-9](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-0-521-64298-9 "Speciale:RicercaISBN/978-0-521-64298-9").

[^2]: Kevin P. Murphy, Probabilistic machine learning: an introduction, collana Adaptive computation and machine learning, The MIT Press, 2022, p. 574, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-0-262-04682-4](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-0-262-04682-4 "Speciale:RicercaISBN/978-0-262-04682-4").