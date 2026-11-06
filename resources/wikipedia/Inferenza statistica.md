---
title: "Inferenza statistica"
source: "https://it.wikipedia.org/wiki/Inferenza_statistica"
author:
  - "[[Wikipedia]]"
published: 2004-12-10
created: 2026-11-06
description:
tags:
  - "clippings"
---
L' **inferenza statistica** (o **statistica inferenziale**) è il procedimento per cui si [inducono](https://it.wikipedia.org/wiki/Induzione "Induzione") le [caratteristiche](https://it.wikipedia.org/wiki/Variabile_\(statistica\) "Variabile (statistica)") di una [popolazione](https://it.wikipedia.org/wiki/Popolazione_statistica "Popolazione statistica") dall' [osservazione](https://it.wikipedia.org/wiki/Campionamento_statistico "Campionamento statistico") di una parte di essa (detta " [campione](https://it.wikipedia.org/wiki/Campionamento_statistico "Campionamento statistico") "), selezionata solitamente mediante un [esperimento](https://it.wikipedia.org/wiki/Esperimento "Esperimento") casuale (aleatorio). Da un punto di vista [filosofico](https://it.wikipedia.org/wiki/Filosofia "Filosofia"), si tratta di tecniche [matematiche](https://it.wikipedia.org/wiki/Matematica "Matematica") per quantificare il processo di [apprendimento](https://it.wikipedia.org/wiki/Apprendimento "Apprendimento") tramite l' [esperienza](https://it.wikipedia.org/wiki/Esperienza "Esperienza").

Si considereranno principalmente campioni casuali semplici di dimensione *n* > 1, che possono venire interpretati come *n* realizzazioni indipendenti di un esperimento di base, nelle medesime condizioni. Dal momento che si considera un esperimento casuale, si coinvolge il [calcolo delle probabilità](https://it.wikipedia.org/wiki/Calcolo_delle_probabilit%C3%A0 "Calcolo delle probabilità"). Nell'inferenza statistica c'è, in un certo senso, un rovesciamento del punto di vista rispetto al calcolo delle probabilità.

Nell'ambito di quest'ultimo, noto il processo di generazione dei dati sperimentali (modello probabilistico) siamo in grado di valutare la probabilità dei diversi possibili risultati di un esperimento. Nella statistica il processo di generazione dei dati sperimentali non è noto in modo completo (il processo in questione è, in definitiva, l'oggetto di indagine) e le tecniche statistiche si prefiggono di indurre le caratteristiche di tale processo sulla base dell'osservazione dei dati sperimentali da esso generati.

## Storia

Nella [storia della statistica](https://it.wikipedia.org/wiki/Storia_della_statistica "Storia della statistica"), l'inferenza ha conosciuto due grandi periodi. Il primo cominciò alla fine dell'Ottocento e si sviluppò in maniera decisiva nella prima metà del XX secolo con i lavori di [R. Fisher](https://it.wikipedia.org/wiki/Ronald_Fisher "Ronald Fisher"), [K. Pearson](https://it.wikipedia.org/wiki/Karl_Pearson "Karl Pearson"), [Jerzy Neyman](https://it.wikipedia.org/wiki/Jerzy_Neyman "Jerzy Neyman"), [Egon Pearson](https://it.wikipedia.org/wiki/Egon_Pearson "Egon Pearson") e [Abraham Wald](https://it.wikipedia.org/wiki/Abraham_Wald "Abraham Wald") con le fondamentali idee riguardanti la [verosomiglianza](https://it.wikipedia.org/wiki/Verosomiglianza "Verosomiglianza"), la potenza dei test di verifica d'ipotesi, gli [intervalli di confidenza](https://it.wikipedia.org/wiki/Intervallo_di_confidenza "Intervallo di confidenza") e altre.

Il secondo grande periodo, tuttora in corso, è stato possibile grazie alla crescente potenza di calcolo dei computer, disponibili a prezzi sempre più abbordabili. Ciò ha permesso di allontanarsi da ipotesi comode dal punto di vista matematico ma non sempre adeguate alla realtà mettendo in pratica idee anche *antiche* come quella [bayesiana](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") che trova applicazioni pratiche solo in presenza della potenza di calcolo dei computer, come pure le tecniche di [ricampionamento](https://it.wikipedia.org/wiki/Ricampionamento "Ricampionamento") dei dati come il [metodo Monte Carlo](https://it.wikipedia.org/wiki/Metodo_Monte_Carlo "Metodo Monte Carlo"), [bootstraping](https://it.wikipedia.org/wiki/Metodo_bootstrap "Metodo bootstrap"), [metodo jackknife](https://it.wikipedia.org/wiki/Metodo_jackknife "Metodo jackknife") ecc. legati a personaggi quali [John von Neumann](https://it.wikipedia.org/wiki/John_von_Neumann "John von Neumann"), [Stanisław Marcin Ulam](https://it.wikipedia.org/wiki/Stanis%C5%82aw_Marcin_Ulam "Stanisław Marcin Ulam"), [Bradley Efron](https://it.wikipedia.org/wiki/Bradley_Efron "Bradley Efron"), [Richard von Mises](https://it.wikipedia.org/wiki/Richard_von_Mises "Richard von Mises") e altri.

## Descrizione

### Due approcci

Nell'ambito dell'inferenza statistica, si distinguono due scuole di pensiero, legate a diverse concezioni, o interpretazioni, del significato della [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità"):

- Inferenza *classica*, o *frequentista*;
- [Inferenza bayesiana](https://it.wikipedia.org/wiki/Inferenza_bayesiana "Inferenza bayesiana").

La prima è legata agli storici contributi di [R. Fisher](https://it.wikipedia.org/wiki/Ronald_Fisher "Ronald Fisher"), [K. Pearson](https://it.wikipedia.org/wiki/Karl_Pearson "Karl Pearson"), e rappresenta la posizione maggioritaria. La seconda è fondata sull'uso del risultato del [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") ai fini dell'inferenza statistica.

Esiste per il vero un terzo approccio, che però è una contestazione del concetto di inferenza, ovvero il soggettivismo statistico propugnato dall'ingegnere e matematico [Bruno De Finetti](https://it.wikipedia.org/wiki/Bruno_de_Finetti "Bruno de Finetti"). In particolare De Finetti contestando la possibilità ontologica che esistano casi ripetibili, contesta l'attendibilità della [statistica frequentista](https://it.wikipedia.org/wiki/Statistica_frequentista "Statistica frequentista"). Emblematico di questa posizione è il seguente passo di De Finetti " *Vi sono certo delle differenze fra i diversi casi, ad esempio, per il lotto, due palline diverse differiscono di certo almeno per il fatto che portano due numeri diversi e che, al momento dell’estrazione, occupano nell’urna due posizioni diverse. Perché queste condizioni non si prendono in considerazione?*" (così a pag.12 in Bruno de Finetti *Probabilismo. Saggio critico sulla teoria delle probabilità e sul valore della scienza*, Editrice F. Perrella, Napoli 1931)

### Inferenza frequentista e bayesiana a confronto

Sia l'approccio frequentista che l'approccio bayesiano hanno in comune anzitutto gli assiomi della [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità") nonché tutta la struttura statistico-matematica. Anche il [teorema di Bayes](https://it.wikipedia.org/wiki/Teorema_di_Bayes "Teorema di Bayes") ha validità per entrambi gli approcci così come il fatto che in entrambi i casi si parla solitamente di [statistica parametrica](https://it.wikipedia.org/wiki/Statistica_parametrica "Statistica parametrica"). Ciò che cambia è il significato da dare al concetto di probabilità, all'atteggiamento nel confronto dell'idea di una probabilità soggettiva e di conseguenza l'utilizzo e l'importanza che si dà al teorema di Bayes.

Nell'ambito dell'inferenza statistica queste differenze si manifestano, da un lato, sul come e se utilizzare informazioni note prima di "vedere" i dati e di come quantificare tali informazioni e, dall'altro, vi sono approcci differenti sul come interpretare i risultati.

Un esempio sul come lo stesso esperimento venga visto dai due approcci può essere il seguente problema scolastico.

In un'urna contenente palline identiche tra di loro salvo per il colore, una ignota percentuale π è di colore nero. Estraendo 100 volte una pallina che viene subito dopo riposta nell'urna succede ad esempio che per 30 volte la pallina fosse nera.

In entrambi gli approcci si suppone una [distribuzione binomiale](https://it.wikipedia.org/wiki/Distribuzione_binomiale "Distribuzione binomiale"):

Il tipico approccio frequentista basato sull' [intervallo di confidenza](https://it.wikipedia.org/wiki/Intervallo_di_confidenza "Intervallo di confidenza") derivante dalle idee di Neyman porta a stabilire per il valore ignoto di π un intervallo di confidenza p.es. al 95% compreso tra 0,21 e 0,39. La confidenza al 95% **non** sta ad indicare che π è compreso con una probabilità del 95% tra 0,21 e 0,39 (si tratterebbe di una affermazione tipicamente bayesiana), ma indica che a partire dalle ipotesi, il metodo utilizzato, nel 95% dei casi fa delle affermazioni corrette, nel senso che il vero valore sarà veramente nell'intervallo calcolato. Questo approccio sottolinea che il valore ignoto π o è compreso nell'intervallo oppure non lo è, ma non dà valori probabilistici a questo *essere compreso*. Una stima puntuale sia dei minimi quadrati che della [massima verosimiglianza](https://it.wikipedia.org/wiki/Metodo_della_massima_verosimiglianza "Metodo della massima verosimiglianza") porterebbe a stimare il valore di π con la stima p=30/100=0,3.

L'approccio bayesiano invece formalizza anzitutto l'idea che si ha su come potrebbe essere forse, probabilmente il vero valore π, supponendo una distribuzione discreta o continua sui possibili valori di π. Nel caso particolare che ci si voglia mettere in condizione di totale ignoranza, verrebbe considerata una [distribuzione discreta uniforme](https://it.wikipedia.org/wiki/Distribuzione_discreta_uniforme "Distribuzione discreta uniforme") o, vista la numerosità campionaria relativamente elevata (100 estrazioni), una [distribuzione continua uniforme](https://it.wikipedia.org/wiki/Distribuzione_continua_uniforme "Distribuzione continua uniforme") nell'intervallo compreso tra zero e uno. Scegliendo *a priori* la distribuzione di tipo del parametro π si ottiene:

$f \left(\right. \pi \left|\right. n = 100 ; k = 30 \left.\right) = \left(n + 1\right) \left(\right. \genfrac{}{}{0pt}{}{n}{k} \left.\right) \pi^{k} \left(\right. 1 - \pi \left.\right)^{n - k}$

Il valore massimo, e dunque il più probabile, è dato anche in questo caso da k/n=30/100=0,3, valore già visto nell'approccio frequentista, con la differenza che questo è *a posteriori* il valore più probabile, vista le nostre idee *a priori* e i risultati dell'esperimento. Utilizzando la distribuzione *a posteriori* si può affermare che la probabilità che l'ignoto parametro π abbia un valore tra 0,216 e 0,393 è pari a 0.95 vale a dire a 95%, mentre i valori compresi nell'intervallo tra 0,21 e 0.39 hanno la probabilità del 95,3%.

Riassumendo questo esempio: nell'approccio frequentista si fanno affermazioni su quante volte si dice il vero usando la tecnica usata, mentre nell'approccio bayesiano si attribuisce una probabilità di verità direttamente ad un intervallo. Questa differenza è a livello pratico spesso ignorata, ma dal punto di vista teorico è sostanziale. Si aggiunga il fatto che l'approccio bayesiano è in grado di utilizzare informazioni già in possesso, modificando la probabilità a priori e ottenendo così delle [probabilità a posteriori](https://it.wikipedia.org/wiki/Probabilit%C3%A0_a_posteriori "Probabilità a posteriori") diverse.

### Temi legati all'inferenza statistica

I seguenti temi costituiscono una lista, non necessariamente esaustiva, di argomenti ricompresi nell'inferenza statistica:

- [Stima](https://it.wikipedia.org/wiki/Teoria_della_stima "Teoria della stima"), per punti o per intervalli;
- [Test di verifica d'ipotesi](https://it.wikipedia.org/wiki/Test_di_verifica_d'ipotesi "Test di verifica d'ipotesi");
- [Previsione](https://it.wikipedia.org/wiki/Previsione?action=edit&redlink=1 "Previsione (la pagina non esiste)").

### Esempio

Data un'urna con composizione nota di 6 palline bianche e 4 palline rosse, utilizzando le regole del calcolo delle probabilità possiamo dedurre che se estraiamo una pallina a caso dall'urna, la probabilità che essa sia rossa è 0,4. Si ha invece un problema di inferenza statistica quando abbiamo un'urna di cui non conosciamo la composizione, estraiamo *n* palline a caso, ne osserviamo il colore e, a partire da questo, cerchiamo di inferire la composizione dell'urna.

## Bibliografia

- A. Rizzi (1992): *Inferenza Statistica*, Torino, UTET, [ISBN 88-7750-014-X](https://it.wikipedia.org/wiki/Special:BookSources/887750014X).

## Voci correlate

- [Statistica](https://it.wikipedia.org/wiki/Statistica "Statistica")
- [Statistica descrittiva](https://it.wikipedia.org/wiki/Statistica_descrittiva "Statistica descrittiva")
- [Probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità")
- [Inferenza bayesiana](https://it.wikipedia.org/wiki/Inferenza_bayesiana "Inferenza bayesiana")
- [Winsorizzazione](https://it.wikipedia.org/wiki/Winsorizzazione "Winsorizzazione")
- [Geometria dell'informazione](https://it.wikipedia.org/wiki/Geometria_dell'informazione "Geometria dell'informazione")

## Altri progetti

Altri progetti

- [Wikizionario](https://it.wiktionary.org/wiki/ "wikt:") contiene il lemma di dizionario « **[inferenza statistica](https://it.wiktionary.org/wiki/inferenza%20statistica "wikt:inferenza statistica")** »
- contiene immagini o altri file sull' **[inferenza statistica](https://commons.wikimedia.org/wiki/Category:Statistical_inference?uselang=it)**

## Collegamenti esterni

- (EN) [inference](https://www.britannica.com/science/inference-statistics), su [Enciclopedia Britannica](https://it.wikipedia.org/wiki/Enciclopedia_Britannica "Enciclopedia Britannica"), Encyclopædia Britannica, Inc.
- [Corso di statistica applicata alla microbiologia](https://web.archive.org/web/20060620022904/http://www.iperserver.it/mediawiki/index.php/Pagina_Principale), su iperserver.it. URL consultato il 24 maggio 2006 (archiviato dall' url originale il 20 giugno 2006).

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [Thesaurus BNCF](https://it.wikipedia.org/wiki/Nuovo_soggettario "Nuovo soggettario") [7894](https://thes.bncf.firenze.sbn.it/termine.php?id=7894) · [GND](https://it.wikipedia.org/wiki/Gemeinsame_Normdatei "Gemeinsame Normdatei") (DE) [4182963-3](https://d-nb.info/gnd/4182963-3) |
| --- | --- |