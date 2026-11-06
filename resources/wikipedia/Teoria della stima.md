---
title: "Teoria della stima"
source: "https://it.wikipedia.org/wiki/Teoria_della_stima"
author:
  - "[[Wikipedia]]"
published: 2009-02-23
created: 2026-11-06
description:
tags:
  - "clippings"
---
La **teoria della stima** è un ramo della [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica") e dell' [elaborazione numerica dei segnali](https://it.wikipedia.org/wiki/Elaborazione_numerica_dei_segnali "Elaborazione numerica dei segnali") che ha come obiettivo la stima di parametri, scalari o vettoriali, a partire da dati misurati/empirici, la cui distribuzione è influenzata dai valori effettivi assunti da tali parametri. Uno [stimatore](https://it.wikipedia.org/wiki/Stimatore "Stimatore") è una funzione deterministica dei dati misurati, che, in relazione ad un determinato criterio di ottimalità, assume il valore del parametro stimato.

Un classico problema di stima, in ambito [radar](https://it.wikipedia.org/wiki/Radar "Radar"), è quello di stimare la posizione di un bersaglio analizzando il segnale ricevuto, influenzato non solo dagli echi di ritorno dal bersaglio, ma anche dal [rumore termico](https://it.wikipedia.org/wiki/Rumore_termico "Rumore termico") o da altri fenomeni aleatori di disturbo. Tali disturbi introducono incertezza, senza la quale il problema sarebbe deterministico e non vi sarebbe alcuna necessità di stima.

La teoria della stima si divide in due branche: [stima puntuale](https://it.wikipedia.org/wiki/Stima_puntuale "Stima puntuale") e [stima intervallare](https://it.wikipedia.org/wiki/Stima_intervallare?action=edit&redlink=1 "Stima intervallare (la pagina non esiste)").

Esempi di stimatori sono: la media campionaria $\bar{x}$ (stimatore della media della popolazione), la varianza campionaria $S^{2}$ (stimatore della varianza della popolazione)...

## Processo di stima

L'intero obiettivo della teoria della stima è di arrivare ad uno stimatore, e preferibilmente di implementarne uno che sia realmente utilizzabile. Lo [stimatore](https://it.wikipedia.org/wiki/Stimatore "Stimatore") è una funzione deterministica che a partire dai dati misurati produce una stima del parametro.

È preferibile derivare uno stimatore che esibisca proprietà di [ottimalità](https://it.wikipedia.org/wiki/Ottimizzazione_\(matematica\) "Ottimizzazione (matematica)").

Questi sono i passi generali per determinare uno stimatore:

- Determinazione di un modello per il sistema, che includa sia la dipendenza dal parametro che le componenti aleatorie di disturbo.
- Determinazione dei limiti a cui deve sottostare uno stimatore. Tali limiti, ad esempio possono esser trovati attraverso la [disuguaglianza di Cramér-Rao](https://it.wikipedia.org/wiki/Disuguaglianza_di_Cram%C3%A9r-Rao "Disuguaglianza di Cramér-Rao").
- Sviluppo di uno stimatore.
- Analisi delle performance dello stimatore, attraverso simulazioni/esperimenti.

## Stimatori

Gli stimatori o metodi di stima più usati sono i seguenti:

- [Metodo della massima verosimiglianza](https://it.wikipedia.org/wiki/Metodo_della_massima_verosimiglianza "Metodo della massima verosimiglianza")
- [Metodo dei momenti](https://it.wikipedia.org/wiki/Metodo_dei_momenti_\(statistica\) "Metodo dei momenti (statistica)")
- Stimatore dei [minimi quadrati](https://it.wikipedia.org/wiki/Minimi_quadrati "Minimi quadrati")

## Bibliografia

- (EN) John Rice, Mathematical Statistics and Data Analysis, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-534-20934-3](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-534-20934-3 "Speciale:RicercaISBN/0-534-20934-3").
- (EN) Steven M. Kay, Fundamentals of Statistical Signal Processing: Estimation Theory, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-13-345711-7](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-13-345711-7 "Speciale:RicercaISBN/0-13-345711-7").
- (EN) H. Vincent Poor, An Introduction to Signal Detection and Estimation, [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [0-387-94173-8](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/0-387-94173-8 "Speciale:RicercaISBN/0-387-94173-8").

## Voci correlate

- [Teoria della rivelazione](https://it.wikipedia.org/wiki/Teoria_della_rivelazione "Teoria della rivelazione")
- [Stimatore](https://it.wikipedia.org/wiki/Stimatore "Stimatore")
- [Disuguaglianza di Cramér-Rao](https://it.wikipedia.org/wiki/Disuguaglianza_di_Cram%C3%A9r-Rao "Disuguaglianza di Cramér-Rao")
- [Efficienza (statistica)](https://it.wikipedia.org/wiki/Efficienza_\(statistica\) "Efficienza (statistica)")
- [Sufficienza (statistica)](https://it.wikipedia.org/wiki/Sufficienza_\(statistica\) "Sufficienza (statistica)")
- [Consistenza (statistica)](https://it.wikipedia.org/wiki/Consistenza_\(statistica\) "Consistenza (statistica)")
- [Filtro di Wiener](https://it.wikipedia.org/wiki/Filtro_di_Wiener "Filtro di Wiener")
- [Filtro di Kalman](https://it.wikipedia.org/wiki/Filtro_di_Kalman "Filtro di Kalman")