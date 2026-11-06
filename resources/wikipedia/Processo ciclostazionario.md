---
title: "Processo ciclostazionario"
source: "https://it.wikipedia.org/wiki/Processo_ciclostazionario"
author:
  - "[[Wikipedia]]"
published: 2008-01-21
created: 2026-11-06
description:
tags:
  - "clippings"
---
Un **processo ciclostazionario** è un [segnale](https://it.wikipedia.org/wiki/Segnale_elettrico "Segnale elettrico") avente proprietà statistiche che variano nel tempo. I processi stocastici ciclostazionari servono per descrivere processi generati da fenomeni periodici, come ne esistono molti in natura. Tali processi, sebbene non siano descritti in termini di funzioni periodiche del tempo, producono dati che possono essere descritti attraverso parametri statistici che variano periodicamente nel tempo (statistiche di primo e secondo ordine). Ad esempio, nelle [telecomunicazioni](https://it.wikipedia.org/wiki/Telecomunicazioni "Telecomunicazioni"), la periodicità dei dati è dovuta alla [modulazione](https://it.wikipedia.org/wiki/Modulazione "Modulazione"), al [campionamento](https://it.wikipedia.org/wiki/Campionamento_statistico "Campionamento statistico"), alla [codifica](https://it.wikipedia.org/wiki/Codifica "Codifica"); in [meccanica](https://it.wikipedia.org/wiki/Meccanica_\(fisica\) "Meccanica (fisica)") è dovuta alla rotazione dei meccanismi, mentre in [radioastronomia](https://it.wikipedia.org/wiki/Radioastronomia "Radioastronomia") la periodicità è generata ad esempio dai [moti di rotazione](https://it.wikipedia.org/wiki/Rotazione "Rotazione") e [rivoluzione dei pianeti](https://it.wikipedia.org/wiki/Moto_di_rivoluzione "Moto di rivoluzione") e dalla pulsazione delle stelle.

## Definizione

Vi sono due approcci differenti allo studio dei processi ciclostazionari: uno [probabilistico](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità"), che considera i segnali come realizzazioni di un [processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico"); l'altro, di tipo deterministico, in cui i segnali vengono modellati come una singola funzione del tempo (serie temporale), piuttosto che come una realizzazione di un processo stocastico. Tale approccio è usato quando non esiste un insieme di realizzazioni, e si utilizza la serie temporale, con un ragionamento al limite, proprio per creare un modello matematico del processo stesso (approccio F.O.T. = *fraction-of-time*).

In entrambi i casi, il processo o la serie temporale vengono detti ciclostazionari se le statistiche ad essi associate variano periodicamente col tempo.

## Processi ciclostazionari in senso lato

Segnali che esibiscano ciclostazionarietà nelle statistiche del secondo ordine (funzioni [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") e [autocorrelazione](https://it.wikipedia.org/wiki/Autocorrelazione "Autocorrelazione")) vengono detti **ciclostazionari in senso lato**. Indicando con $E$ l'operatore di [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)"), un processo ciclostazionario $x(t)$ di periodo $T_{0}$ soddisfa quindi le seguenti relazioni:

$E \left[x \left(t\right)\right] = E \left[x \left(t + T_{0}\right)\right] \forall t$

$R_{x} \left(t ; \tau\right) = R_{x} \left(t + T_{0} ; \tau\right) \forall t , \tau .$

In particolare, la funzione di autocorrelazione, essendo una funzione periodica in *t*, può essere espansa in [serie di Fourier](https://it.wikipedia.org/wiki/Serie_di_Fourier "Serie di Fourier"):

$R_{x} \left(t ; \tau\right) = \sum_{n = - \infty}^{\infty} R_{x}^{n / T_{0}} \left(\tau\right) e^{j 2 \pi \frac{n}{T_{0}} t}$

dove $R_{x}^{n / T_{0}} \left(\tau\right)$ è chiamata **funzione di autocorrelazione ciclica**, ed è uguale a:

$R_{x}^{n / T_{0}} \left(\tau\right) = \frac{1}{T_{0}} \int_{- T_{0} / 2}^{T_{0} / 2} R_{x} \left(t , \tau\right) e^{- j 2 \pi \frac{n}{T_{0}} t} d t .$

Le frequenze $n / T_{0} , n \in \mathbb{Z} ,$ sono chiamate **frequenze cicliche**.

I processi stazionari in senso lato possono essere visti come casi particolari di processi ciclostazionari in senso lato con soltanto $R_{x}^{0} \left(\tau\right) \neq 0$.

### Serie temporali ciclostazionarie

Un segnale funzione del tempo che non sia in generale una realizzazione di un processo stocastico può esibire ciclostazionarietà nel contesto della teoria FOT. Secondo tale interpretazione, la funzione di autocorrelazione ciclica può essere definita nel seguente modo:

$\left(\overset{̂}{R}\right)_{x}^{n / T_{0}} \left(\tau\right) = \underset{T \rightarrow + \infty}{lim} \frac{1}{T} \int_{t - T / 2}^{t + T / 2} x \left(t + \tau\right) x^{*} \left(t\right) e^{- j 2 \pi \frac{n}{T_{0}} t} d t .$

Se la serie temporale è una realizzazione di un processo stocastico, allora $R_{x}^{n / T_{0}} \left(\tau\right) = E \left[\left(\overset{̂}{R}\right)_{x}^{n / T_{0}} \left(\tau\right)\right]$. Se, inoltre, il segnale è anche [ergodico](https://it.wikipedia.org/wiki/Ergodico "Ergodico"), allora tutte le realizzazioni esibiscono le stesse medie temporali, per cui $R_{x}^{n / T_{0}} \left(\tau\right) = \left(\overset{̂}{R}\right)_{x}^{n / T_{0}} \left(\tau\right)$ in [errore quadratico medio](https://it.wikipedia.org/wiki/Errore_quadratico_medio "Errore quadratico medio").

### Comportamento nel dominio della frequenza

La [trasformata di Fourier](https://it.wikipedia.org/wiki/Trasformata_di_Fourier "Trasformata di Fourier") della funzione di autocorrelazione ciclica alla frequenza ciclica α è detta **spettro ciclico** o **funzione di densità spettrale di correlazione**. Tale funzione è pari a:

$S_{x}^{\alpha} \left(f\right) = \int_{- \infty}^{+ \infty} R_{x}^{\alpha} \left(\tau\right) e^{- j 2 \pi \alpha \tau} d \tau .$

Lo spettro ciclico alla frequenza ciclica zero è anche chiamato [densità spettrale di potenza](https://it.wikipedia.org/wiki/Densit%C3%A0_spettrale_di_potenza "Densità spettrale di potenza") media.

Si noti che un processo ciclostazionario $x(t)$ con trasformata di Fourier $X(f)$ può avere componenti frequenziali correlate quando queste sono spaziate di multipli di $1 / T_{0}$. In particolare:

$E \left[X \left(f_{1}\right) X^{*} \left(f_{2}\right)\right] = \sum_{n = - \infty}^{\infty} S_{x}^{n / T_{0}} \left(f_{1}\right) \delta \left(f_{1} - f_{2} + \frac{n}{T_{0}}\right)$

dove $δ(f)$ indica la funzione [delta di Dirac](https://it.wikipedia.org/wiki/Delta_di_Dirac "Delta di Dirac"). Le frequenze $f_{1} \neq f_{2}$ sono invece sempre incorrelate per un [processo stazionario](https://it.wikipedia.org/wiki/Processo_stazionario "Processo stazionario") in senso lato, essendo $S_{x}^{n / T_{0}} \left(f\right) \neq 0$ solo per $n=0$.

### Esempio: Segnale digitale modulato linearmente

Un esempio di segnale ciclostazionario è un segnale digitale modulato linearmente:

$x \left(t\right) = \sum_{k = - \infty}^{\infty} a_{k} p \left(t - k T_{0}\right)$

dove $a_{k} \in \mathbb{C}$ sono variabili casuali [i.i.d](https://it.wikipedia.org/wiki/Variabili_indipendenti_e_identicamente_distribuite "Variabili indipendenti e identicamente distribuite"). Il segnale $p(t)$, con trasformata di Fourier $P(f)$, è l'impulso di supporto della modulazione.

Assumendo $E \left[a_{k}\right] = 0$ e $E \left[\left|a_{k}\right|^{2}\right] = \sigma_{a}^{2}$, la funzione di autocorrelazione è:

$\begin{matrix}R_{x} \left(t , \tau\right) & = E \left[x \left(t + \tau\right) x^{*} \left(t\right)\right] \\ = \underset{k , n}{\sum} E \left[a_{k} a_{n}^{*}\right] p \left(t + \tau - k T_{0}\right) p^{*} \left(t - n T_{0}\right) \\ = \sigma_{a}^{2} \underset{k}{\sum} p \left(t + \tau - k T_{0}\right) p^{*} \left(t - k T_{0}\right) .\end{matrix}$

L'ultima sommatoria è una sommatoria periodica, quindi un segnale periodico in *t*. Di conseguenza, $x(t)$ è un segnale ciclostazionario con periodo $T_{0}$ e funzione di autocorrelazione ciclica:

$Rxn/T0(τ)=1T0∫−T0T0Rx(t,τ)e−j2πnT0tdt=1T0∫−T0T0σa2∑k=−∞∞p(t+τ−kT0)p∗(t−kT0)e−j2πnT0tdt=σa2T0∑k=−∞∞∫−T0−kT0T0−kT0p(λ+τ)p∗(λ)e−j2πnT0(λ+kT0)dλ=σa2T0∫−∞∞p(λ+τ)p∗(λ)e−j2πnT0λdλ=σa2T0p(τ)∗{p∗(−τ)ej2πnT0τ}.$

dove $∗$ indica l'operatore di [convoluzione](https://it.wikipedia.org/wiki/Convoluzione "Convoluzione"). Lo spettro ciclico è:

$S_{x}^{n / T_{0}} \left(f\right) = \frac{\sigma_{a}^{2}}{T_{0}} P \left(f\right) P^{*} \left(f - \frac{n}{T_{0}}\right) .$

Tipici impulsi a [coseno rialzato](https://it.wikipedia.org/wiki/Filtro_a_coseno_rialzato "Filtro a coseno rialzato") normalmente utilizzati in comunicazioni digitali hanno quindi solo le frequenze cicliche $n=−1,0,1$.

## Bibliografia

- William A. Gardner, Antonio Napolitano, and Luigi Paura, [Cyclostationarity: Half a century of research](https://oadoi.org/10.1016%2Fj.sigpro.2005.06.016), in Signal Processing, vol. 86, n. 4, Elsevier, 2006, pp. 639-697, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1016/j.sigpro.2005.06.016](https://dx.doi.org/10.1016%2Fj.sigpro.2005.06.016).