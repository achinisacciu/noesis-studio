---
title: "Filtro bayesiano"
source: "https://it.wikipedia.org/wiki/Filtro_bayesiano"
author:
  - "[[Wikipedia]]"
published: 2006-02-06
created: 2026-11-06
description:
tags:
  - "clippings"
---
Un **filtro bayesiano** (dal nome del noto matematico [Bayes](https://it.wikipedia.org/wiki/Thomas_Bayes "Thomas Bayes") vissuto nel [XVIII secolo](https://it.wikipedia.org/wiki/XVIII_secolo "XVIII secolo")) è una forma di filtraggio dello [spam](https://it.wikipedia.org/wiki/Spam "Spam") che si basa sull'analisi del contenuto delle [email](https://it.wikipedia.org/wiki/Email "Email"). Questa tecnica (di grande efficacia) è complementare ai sistemi di blocco basati su [indirizzo IP](https://it.wikipedia.org/wiki/Indirizzo_IP "Indirizzo IP"), le cosiddette [liste nere](https://it.wikipedia.org/wiki/Lista_nera_\(informatica\) "Lista nera (informatica)").

Il filtro bayesiano applica all'analisi delle [email](https://it.wikipedia.org/wiki/Email "Email") un [teorema](https://it.wikipedia.org/wiki/Teorema "Teorema"), espresso per l'appunto da Bayes, secondo il quale ogni [evento](https://it.wikipedia.org/wiki/Evento_\(teoria_della_probabilit%C3%A0\) "Evento (teoria della probabilità)") cui è attribuita una [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") è valutabile in base all'analisi degli eventi già verificatisi. Nel caso dell'analisi antispam, se in un numero *n* delle mail analizzate in precedenza, l'utente ha marcato come spam quelle che contenevano la parola "sesso", il filtro ne dedurrà che la presenza di quella parola innalza la probabilità che le mail seguenti contenenti quella parola siano a loro volta spam. In questo modo, il sistema è in grado di adattarsi in maniera dinamica e veloce alle nuove tipologie di spam.[^1] [^2]

Gran parte dei software di analisi delle email antispam, ormai, adotta questo genere di tecnologia.

## Client di posta elettronica con filtro bayesiano

- [Mozilla Thunderbird](https://it.wikipedia.org/wiki/Mozilla_Thunderbird "Mozilla Thunderbird") [^3] [^4]
- [Evolution](https://it.wikipedia.org/wiki/Evolution_\(software\) "Evolution (software)") [^5]

## Note

## Voci correlate

- [SpamAssassin](https://it.wikipedia.org/wiki/SpamAssassin "SpamAssassin")
- [Teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes")
- [Filtro di Kalman](https://it.wikipedia.org/wiki/Filtro_di_Kalman "Filtro di Kalman")

[^1]: Paolo Attivissimo, [Filtri bayesiani, arma letale antispam](https://www.apogeonline.com/articoli/filtri-bayesiani-arma-letale-antispam-paolo-attivissimo/), su Apogeo Editore. URL consultato il 10 febbraio 2021.

[^2]: Joli Ballew e Jeff Duntemann, [Windows che funziona. Trucchi e tecniche per migliorare le prestazioni del PC](https://books.google.it/books?id=ccoZcXDtjwEC&pg=PA117). URL consultato il 10 febbraio 2021.

[^3]: (EN) [Junk Mail Controls](https://kb.mozillazine.org/Junk_Mail_Controls), su kb.mozillazine.org. URL consultato il 10 febbraio 2021.

[^4]: [Thunderbird e la Posta indesiderata/Spam](https://support.mozilla.org/it/kb/thunderbird-posta-indesiderata-spam), su support.mozilla.org. URL consultato il 10 febbraio 2021.

[^5]: (EN) [Stopping Junk Mail (Spam)](https://www.novell.com/documentation/evolution24/?page=/documentation/evolution24/evolution24/data/usage-mail-organize-spam.html), su novell.com.