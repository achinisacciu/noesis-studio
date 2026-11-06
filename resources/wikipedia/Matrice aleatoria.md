---
title: "Matrice aleatoria"
source: "https://it.wikipedia.org/wiki/Matrice_aleatoria"
author:
  - "[[Wikipedia]]"
published: 2025-07-07
created: 2026-11-06
description:
tags:
  - "clippings"
---
In [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica"), e in particolare in [probabilità](https://it.wikipedia.org/wiki/Probabilit%C3%A0 "Probabilità"), con **matrice aleatoria** si intende una [matrice](https://it.wikipedia.org/wiki/Matrice "Matrice") in cui una parte o tutti i suoi ingressi sono [variabili aleatorie](https://it.wikipedia.org/wiki/Variabili_aleatorie "Variabili aleatorie") estratte in modo casuale da una [distribuzione di probabilità](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0 "Distribuzione di probabilità"). In altre parole, è una [variabile aleatoria](https://it.wikipedia.org/wiki/Variabile_aleatoria "Variabile aleatoria") a valori matriciali.[^1] Talvolta è utilizzata anche l’espressione **matrice casuale** come sinonimo, tuttavia tale dizione è non preferibile in contesti matematici [^1].

La teoria delle matrici aleatorie studia le proprietà delle [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") aleatorie, focalizzandosi sul calcolo e la stima di quantità, come [traccia](https://it.wikipedia.org/wiki/Traccia_\(matrice\) "Traccia (matrice)"), [determinante](https://it.wikipedia.org/wiki/Determinante_\(algebra\) "Determinante (algebra)"), [norma](https://it.wikipedia.org/wiki/Norma_matriciale "Norma matriciale") e [spettro](https://it.wikipedia.org/wiki/Spettro_\(matematica\) "Spettro (matematica)"), in particolare per il limite di matrici a dimensionalità elevata [^2]. La teoria si avvale di strumenti come la [teoria di campo medio](https://it.wikipedia.org/wiki/Teoria_di_campo_medio "Teoria di campo medio"), i metodi diagrammatici e il metodo delle cavità. Getta le sue basi nella seconda metà del [XX secolo](https://it.wikipedia.org/wiki/XX_secolo "XX secolo"), grazie ai fondamentali contributi di [Wigner](https://it.wikipedia.org/wiki/Eugene_Wigner "Eugene Wigner") [^3], [Dyson](https://it.wikipedia.org/wiki/Freeman_Dyson "Freeman Dyson") [^4] e Lal Mehta [^5]. L'importanza dell'argomento è giustificata dal fatto che numerosi fenomeni fisici e non, come lo [spettro](https://it.wikipedia.org/wiki/Spettro_\(fisica\) "Spettro (fisica)") dei nuclei di [atomi](https://it.wikipedia.org/wiki/Atomo "Atomo") pesanti, la [conducibilità termica](https://it.wikipedia.org/wiki/Conducibilit%C3%A0_termica "Conducibilità termica") di un reticolo o l’emergere del caos quantistico, i [mercati azionari](https://it.wikipedia.org/wiki/Mercato_azionario "Mercato azionario") e lo studio della forma delle [proteine](https://it.wikipedia.org/wiki/Proteine "Proteine") possono essere modellati matematicamente come problemi relativi a matrici grandi e aleatorie [^6].

## Storia

### Fisica nucleare e nascita delle matrici aleatorie

[Enrico Fermi](https://it.wikipedia.org/wiki/Enrico_Fermi "Enrico Fermi") e collaboratori furono i primi che, tramite esperimenti, mostrarono che i [nucleoni](https://it.wikipedia.org/wiki/Nucleone "Nucleone") all’interno di un [nucleo atomico](https://it.wikipedia.org/wiki/Nucleo_atomico "Nucleo atomico") non possono essere modellati come particelle che si muovono indipendentemente. Dunque questa osservazione indusse [Niels Bohr](https://it.wikipedia.org/wiki/Niels_Bohr "Niels Bohr") alla formulazione del concetto di *nucleo composto* [^7], secondo il quale le interazioni tra [nucleoni](https://it.wikipedia.org/wiki/Nucleone "Nucleone"), prima di decadere, danno luogo a stati intermedi. Fu questa teoria, nell’ambito della [fisica nucleare](https://it.wikipedia.org/wiki/Fisica_nucleare "Fisica nucleare"), la prima ad utilizzare gli strumenti delle matrici aleatorie, al di fuori della letteratura matematica [^3].

«Anche se potessimo sperimentare con neutroni o protoni di energie superiori a cento milioni di volt, dobbiamo comunque aspettarci che l’energia in eccesso di tali particelle venga in primo luogo distribuita tra le particelle nucleari \[…\]. \[Possiamo\] tuttavia in tali casi aspettarci che in generale non una, ma diverse particelle cariche o non cariche lasceranno infine il nucleo a seguito dell'urto. Per impatti ancora più violenti, con particelle di energie dell’ordine di mille milioni di volt, dobbiamo addirittura prepararci al fatto che l’urto possa portare all’esplosione dell’intero nucleo.»

In assenza di una conoscenza dettagliata delle interazioni dirette tra [nucleoni](https://it.wikipedia.org/wiki/Nucleone "Nucleone"), [Eugene Wigner](https://it.wikipedia.org/wiki/Eugene_Wigner "Eugene Wigner") propose di modellare l’ [Hamiltoniana](https://it.wikipedia.org/wiki/Hamiltoniana_\(funzione\) "Hamiltoniana (funzione)") nucleare come una matrice aleatoria [^3]. Per [atomi](https://it.wikipedia.org/wiki/Atomo "Atomo") con un numero elevato di [nucleoni](https://it.wikipedia.org/wiki/Nucleone "Nucleone"), la [distribuzione](https://it.wikipedia.org/wiki/Distribuzione_\(matematica\) "Distribuzione (matematica)") degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") dell’ [Hamiltoniana](https://it.wikipedia.org/wiki/Meccanica_hamiltoniana "Meccanica hamiltoniana") poteva essere utilizzata per stimare le sezioni d’urto dei processi di [scattering](https://it.wikipedia.org/wiki/Scattering "Scattering"), facendo ricorso alla [distribuzione di Wishart](https://it.wikipedia.org/wiki/Distribuzione_di_Wishart "Distribuzione di Wishart") [^3].

### Dyson e gli ensemble classici

![](https://thumb.wikimedia.org/wikipedia/commons/thumb/9/94/Random_matrix_eigenvalues.gif/500px-Random_matrix_eigenvalues.gif?utm_source=it.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)

Distribuzione degli autovalori di una matrice aleatoria complessa durante un'evoluzione dinamica.

Negli anni successivi, [Freeman Dyson](https://it.wikipedia.org/wiki/Freeman_Dyson "Freeman Dyson") formalizzò ulteriormente il quadro teorico introducendo il concetto di *ensemble di matrici aleatorie*, in particolare classificando i cosiddetti *ensemble classici* (gaussiano ortogonale, unitario e simplettico), noti con l’acronimo inglese GOE, GUE e GSE [^4]. Tali ensemble descrivono differenti simmetrie fisiche associate all’ [Hamiltoniana](https://it.wikipedia.org/wiki/Meccanica_hamiltoniana "Meccanica hamiltoniana"), e si distinguono per il comportamento statistico degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") [^4].

Oltre alla [fisica nucleare](https://it.wikipedia.org/wiki/Fisica_nucleare "Fisica nucleare"), la teoria delle matrici aleatorie ha trovato applicazioni in numerosi altri contesti, tra cui la [fisica delle particelle](https://it.wikipedia.org/wiki/Fisica_delle_particelle "Fisica delle particelle"), i sistemi disordinati (come la teoria della localizzazione di Anderson), la [teoria dei numeri](https://it.wikipedia.org/wiki/Teoria_dei_numeri "Teoria dei numeri"), la [finanza](https://it.wikipedia.org/wiki/Finanza "Finanza") quantitativa, e più recentemente, l’ [apprendimento automatico](https://it.wikipedia.org/wiki/Apprendimento_automatico "Apprendimento automatico") [^6].

### Sviluppi recenti

In particolare, sviluppi recenti nel campo del *[deep learning](https://it.wikipedia.org/wiki/Deep_learning "Deep learning")* hanno mostrato che modelli di reti neurali profonde possono essere analizzati utilizzando strumenti della teoria delle matrici aleatorie [^8]. Le [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") dei pesi nelle [reti neurali](https://it.wikipedia.org/wiki/Rete_neurale_artificiale "Rete neurale artificiale"), soprattutto dopo l’addestramento, presentano [spettro](https://it.wikipedia.org/wiki/Spettro_\(matematica\) "Spettro (matematica)") e proprietà statistiche che possono essere descritte in termini di [distribuzioni di Wigner](https://it.wikipedia.org/wiki/Distribuzione_di_Wigner "Distribuzione di Wigner") o Marčenko–Pastur. Tali osservazioni hanno portato alla nascita di una nuova disciplina, talvolta chiamata “ *Random Matrix Theory for Deep Learning* ”, che fornisce una cornice teorica per analizzare generalizzazione, dinamiche di apprendimento e stabilità nei modelli neurali complessi [^8] [^9].

## Trattazione matematica

### Definizione formale

Una matrice aleatoria è una funzione misurabile definita su uno [spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità"), i cui valori sono [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") a coefficienti reali o [complessi](https://it.wikipedia.org/wiki/Numero_complesso "Numero complesso"). Formalmente, data una tripla $(Ω,ℱ,ℙ)$ che rappresenta uno [spazio di probabilità](https://it.wikipedia.org/wiki/Spazio_di_probabilit%C3%A0 "Spazio di probabilità"), una matrice aleatoria è una [funzione](https://it.wikipedia.org/wiki/Funzione_\(matematica\) "Funzione (matematica)") [^1]

 $X : \Omega \rightarrow \mathbb{K}^{n \times n}$

dove $𝕂=ℝ$ oppure $ℂ$, e ogni elemento $X_{i j} \left(\omega\right)$ della matrice è una [variabile aleatoria](https://it.wikipedia.org/wiki/Variabile_aleatoria "Variabile aleatoria"). La distribuzione congiunta degli elementi (oppure degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore")) della matrice è specificata da un modello probabilistico, detto *ensemble* [^1] [^2] [^10].

Tra i casi più studiati si trovano:[^2]

- le matrici di Wigner, [simmetriche](https://it.wikipedia.org/wiki/Matrice_simmetrica "Matrice simmetrica") o [hermitiane](https://it.wikipedia.org/wiki/Matrice_hermitiana "Matrice hermitiana"), con elementi indipendenti a [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") nulla;
- le matrici di Wishart, definite come $W = X X^{\top}$ a partire da [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") [gaussiane](https://it.wikipedia.org/wiki/Gaussiana "Gaussiana");
- l'ensemble di Ginibre, costituito da matrici non [hermitiane](https://it.wikipedia.org/wiki/Matrice_hermitiana "Matrice hermitiana") con entrate [gaussiane](https://it.wikipedia.org/wiki/Gaussiana "Gaussiana") indipendenti.

In molti casi, l'interesse principale non risiede negli elementi della matrice, ma nel comportamento statistico degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore"), ad esempio mediante la misura spettrale empirica

 $\mu_{X} := \frac{1}{n} \sum_{i = 1}^{n} \delta_{\lambda_{i}} ,$

dove $\lambda_{1} , \ldots , \lambda_{n}$ sono gli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") della matrice $X$. Tale approccio è alla base della moderna teoria delle matrici aleatorie e delle sue applicazioni in [fisica teorica](https://it.wikipedia.org/wiki/Fisica_teorica "Fisica teorica"), [statistica multivariata](https://it.wikipedia.org/wiki/Statistica_multivariata "Statistica multivariata"), [teoria dei numeri](https://it.wikipedia.org/wiki/Teoria_dei_numeri "Teoria dei numeri") e [apprendimento automatico](https://it.wikipedia.org/wiki/Apprendimento_automatico "Apprendimento automatico") [^6].

### Ensemble classici

Nel contesto della teoria delle matrici aleatorie, un ensemble è una famiglia di matrici aleatorie dotata di una [distribuzione di probabilità](https://it.wikipedia.org/wiki/Distribuzione_di_probabilit%C3%A0 "Distribuzione di probabilità") specifica, spesso determinata da proprietà di [simmetria](https://it.wikipedia.org/wiki/Simmetria_\(matematica\) "Simmetria (matematica)"). Gli *ensemble classici* più studiati sono tre, introdotti e classificati da [Freeman J. Dyson](https://it.wikipedia.org/wiki/Freeman_Dyson "Freeman Dyson") nel [1962](https://it.wikipedia.org/wiki/1962 "1962") sulla base delle simmetrie fondamentali dei sistemi fisici e del comportamento sotto [trasformazioni ortogonali](https://it.wikipedia.org/wiki/Trasformazioni_ortogonali "Trasformazioni ortogonali"), unitarie o simplettiche [^4].

I principali ensemble gaussiani sono [^4]:

- GOE (*Gaussian Orthogonal Ensemble*): comprende [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") reali simmetriche, i cui elementi sono distribuiti secondo [leggi gaussiane](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale") indipendenti, con simmetria $A = A^{\top}$. Rilevante per sistemi con simmetria temporale e senza spin.
- GUE (*Gaussian Unitary Ensemble*): comprende matrici [hermitiane](https://it.wikipedia.org/wiki/Matrice_hermitiana "Matrice hermitiana") complesse, ovvero $A = A^{\dagger}$, con elementi complessi gaussiani. Rilevante per sistemi senza simmetria temporale, come quelli con [campo magnetico](https://it.wikipedia.org/wiki/Campo_magnetico "Campo magnetico") esterno.
- GSE (*Gaussian Symplectic Ensemble*): comprende matrici [hermitiane](https://it.wikipedia.org/wiki/Matrice_hermitiana "Matrice hermitiana") [quaternioniche](https://it.wikipedia.org/wiki/Quaternione "Quaternione") (o rappresentazioni matriciali $2×2$), associate a sistemi con simmetria temporale e spin.

Questi ensemble condividono una densità di probabilità del tipo:

$P \left(A\right) \propto exp \left(- \frac{\beta}{2} T r \left(A^{2}\right)\right)$

dove $β=1$ (GOE), $β=2$ (GUE), $β=4$ (GSE), e $Tr$ indica la [traccia](https://it.wikipedia.org/wiki/Traccia_\(matrice\) "Traccia (matrice)") della matrice. $A$ è una [matrice](https://it.wikipedia.org/wiki/Matrice "Matrice") aleatoria e $T r \left(A^{2}\right)$ è la [traccia](https://it.wikipedia.org/wiki/Traccia_\(matrice\) "Traccia (matrice)") del quadrato della [matrice](https://it.wikipedia.org/wiki/Matrice "Matrice"), ovvero la somma dei quadrati dei suoi [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore"). Il parametro $β$ codifica invece il tipo di simmetria. Dunque, $P(A)$ è una densità: descrive quanto è probabile che la matrice aleatoria $A$ assuma certi valori spettrali. Il parametro $β$ ha anche interpretazione fisica in termini di temperatura nella [meccanica statistica](https://it.wikipedia.org/wiki/Meccanica_statistica "Meccanica statistica") [^4].

| Sigla | **Denominazione** | **Tipologia** | **$β$** | **Sistema** |
| --- | --- | --- | --- | --- |
| GOE | Ortogonale | Reale simmetrica | 1 | Sistemi con simmetria temporale |
| GUE | Unitaria | Complessa hermitiana | 2 | Sistemi senza simmetria temporale |
| GSE | Simplettica | Quaternionica hermitiana | 4 | Sistemi con spin e simmetria temporale |

### Matrici di Wishart

Un'importante classe di matrici aleatorie non [gaussiane](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale") è costituita dalle matrici di Wishart. Introdotte da [John Wishart](https://it.wikipedia.org/wiki/John_Wishart "John Wishart") nel 1928 in ambito statistico, esse emergono naturalmente nel contesto dell’analisi multivariata, della [teoria dell’informazione](https://it.wikipedia.org/wiki/Teoria_dell'informazione "Teoria dell'informazione") e della [fisica statistica](https://it.wikipedia.org/wiki/Fisica_statistica "Fisica statistica") [^10].

Sia $X$ una matrice rettangolare di dimensione $n×p$ i cui elementi sono [variabili aleatorie](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") [gaussiane](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale") reali, indipendenti e identicamente distribuite, con [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") zero e [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") unitaria. La matrice

$W = X^{\top} X$

è detta matrice di Wishart. Si tratta di una matrice simmetrica semi-definita positiva di dimensione $p×p$, che segue una [distribuzione di Wishart](https://it.wikipedia.org/wiki/Distribuzione_di_Wishart "Distribuzione di Wishart"). Più in generale, se le righe di $X$ sono distribuite secondo una legge normale multivariata $\mathcal{N}_{p} \left(0 , \Sigma\right)$, allora $W = X^{\top} X$ segue la [distribuzione di Wishart](https://it.wikipedia.org/wiki/Distribuzione_di_Wishart "Distribuzione di Wishart") con parametro di scala $Σ$ e $n$ gradi di libertà [^10].

Le matrici di Wishart svolgono un ruolo cruciale in numerosi contesti. Per esempio [^10]:

- In statistica, per stimare matrici di [covarianza](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\) "Covarianza (probabilità)") campionarie.
- In fisica teorica e reti complesse, per modellare la struttura spettrale di sistemi non hermitiani o con [correlazioni](https://it.wikipedia.org/wiki/Correlazioni_statistiche "Correlazioni statistiche").

Un ensemble importante associato a queste matrici è detto ensemble di Wishart–Laguerre, in quanto la densità spettrale degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") segue, nel [limite](https://it.wikipedia.org/wiki/Limite_di_una_funzione "Limite di una funzione") asintotico, la legge di Marchenko–Pastur:

$\rho \left(\lambda\right) = \frac{1}{2 \pi \lambda} \sqrt{\left(\lambda_{+} - \lambda\right) \left(\lambda - \lambda_{-}\right)}$

dove $\lambda_{\pm} = \left(\right. 1 \pm \sqrt{c} \left.\right)^{2}$ e $c = \frac{p}{n}$ nel limite $n,p→∞$ con $c$ costante [^10] [^11].

![](https://it.wikipedia.org/wiki/File:Distribuzione_spettrale_di_matrici_di_Wishart_per_diversi_rapporti.png)

Densità empirica degli autovalori di matrici di Wishart generate da matrici gaussiane rettangolari X ∈ ℝ n × p per diversi valori del rapporto γ = /. Al crescere di, il supporto della distribuzione si allarga e si assottiglia, secondo la previsione della legge di Marčenko–Pastur. Le curve teoriche (non mostrate) corrispondono alla densità ρ ( λ ) supportata in \[ 1 − 2, + \] per ≥.

### Matrici sparse e non gaussiane

Al di fuori del regime classico degli ensemble gaussiani densi, esiste un ampio interesse per le matrici aleatorie sparse e non gaussiane, che modellano sistemi fisici e reti con connettività limitata o distribuzioni di probabilità non standard [^12].

Una matrice aleatoria [sparsa](https://it.wikipedia.org/wiki/Matrice_sparsa "Matrice sparsa") è una matrice $A = \left(a_{i j}\right)$ in cui la maggior parte degli elementi è nulla, e solo una frazione $ρ≪1$ di essi è diversa da zero. Tipicamente, gli indici non nulli sono scelti in modo casuale, e i valori associati seguono una certa distribuzione ([gaussiana](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale"), di Bernoulli, uniforme, ecc.).

Queste matrici emergono in [^6]:

- modelli di [vetri di spin](https://it.wikipedia.org/wiki/Vetro_di_spin "Vetro di spin") e [transizioni di fase](https://it.wikipedia.org/wiki/Transizione_di_fase "Transizione di fase"),
- reti complesse e [teoria dei grafi](https://it.wikipedia.org/wiki/Teoria_dei_grafi "Teoria dei grafi"),
- teoria della localizzazione di Anderson e trasporto quantistico,
- [apprendimento automatico](https://it.wikipedia.org/wiki/Apprendimento_automatico "Apprendimento automatico") e compressive sensing.

Diversamente dagli ensemble gaussiani, gli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") delle matrici sparse possono mostrare localizzazione spettrale, comportamento non universale nei bordi dello spettro e assenza di legge semicircolare nei limiti di densità spettrale. Le distribuzioni degli elementi non devono essere [gaussiane](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale"): studi recenti hanno esaminato matrici con elementi di tipo sub-gaussiano, di Lévy, o appartenenti a leggi a coda pesante (*heavy-tailed*) [^13].

Questi ensemble richiedono metodi differenti per l’analisi teorica, come il metodo delle cavità, il formalismo di replica e la teoria dei grafi aleatori.[^12] [^13]

## Spettro e densità degli autovalori

Una delle principali questioni nello studio delle matrici aleatorie riguarda il comportamento dello [spettro](https://it.wikipedia.org/wiki/Spettro_\(matematica\) "Spettro (matematica)"), ovvero l'insieme degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore"), e in particolare la loro distribuzione in limiti asintotici. Per [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") di grandi dimensioni, si osservano regolarità notevoli e universali nel modo in cui gli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") si distribuiscono [^2].

Sia $A_{N}$ una matrice casuale $N×N$ con [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") reali $\lambda_{1} , \ldots , \lambda_{N}$. La densità empirica degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") è definita come [^2]

$\rho_{N} \left(\lambda\right) = \frac{1}{N} \sum_{i = 1}^{N} \delta \left(\lambda - \lambda_{i}\right)$

Nel limite $N→∞$, la densità [converge](https://it.wikipedia.org/wiki/Convergenza_di_variabili_casuali "Convergenza di variabili casuali") (in senso debole) a una [densità di probabilità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità") deterministica $ρ(λ)$, che dipende dalla classe di ensemble considerato [^2].

Le proprietà dello spettro includono [^6]:

- la forma globale della [densità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità") degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") (es. legge semicircolare, legge di Marčenko–Pastur),
- il comportamento degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") estremi (es. distribuzione di Tracy–Widom),
- la localizzazione o delocalizzazione degli [autovettori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") associati.

Questi risultati sono fondamentali sia in [matematica](https://it.wikipedia.org/wiki/Matematica "Matematica") pura sia in applicazioni a [fisica](https://it.wikipedia.org/wiki/Fisica "Fisica"), [statistica](https://it.wikipedia.org/wiki/Statistica "Statistica"), [finanza](https://it.wikipedia.org/wiki/Finanza "Finanza") e [machine learning](https://it.wikipedia.org/wiki/Apprendimento_automatico "Apprendimento automatico") [^6].

### Legge di Wigner

Nel contesto degli ensemble gaussiani simmetrici (come il GOE), la distribuzione limite degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") è descritta dalla [legge semicircolare di Wigner](https://it.wikipedia.org/wiki/Distribuzione_di_Wigner "Distribuzione di Wigner") [^3].

Sia $W_{N}$ una matrice simmetrica di dimensione $N×N$ i cui elementi $W_{i j}$ sono [variabili aleatorie](https://it.wikipedia.org/wiki/Variabile_casuale "Variabile casuale") indipendenti (fatta eccezione per la simmetria), con media nulla e varianza $\sigma^{2} / N$. Allora, nel limite $N→∞$, la [densità](https://it.wikipedia.org/wiki/Funzione_di_densit%C3%A0_di_probabilit%C3%A0 "Funzione di densità di probabilità") degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") [converge](https://it.wikipedia.org/wiki/Convergenza_di_variabili_casuali "Convergenza di variabili casuali") a

$ρsc(λ)={12πσ24σ2−λ2se |λ|≤2σ0altrimenti$

Questa distribuzione è supportata sull'intervallo $[−2σ,2σ]$ ed è detta *legge semicircolare* per via della forma del suo grafico. Il risultato, scoperto da [Eugene Wigner](https://it.wikipedia.org/wiki/Eugene_Wigner "Eugene Wigner") negli anni '50, è uno dei primi esempi di comportamento universale nella teoria delle matrici aleatorie: la forma semicircolare emerge indipendentemente dalla distribuzione precisa degli elementi (purché soddisfino ipotesi di momenti) [^3].

![](https://it.wikipedia.org/wiki/File:Spectral_density_of_gaussian_ensembels,_N_=_1_to_32.png)

Distribuzione spettrale per GOE, GUE e GSE al crescere della dimensione N. Le densità convergono alla legge semicircolare di Wigner.

È possibile derivare la distribuzione congiunta degli autovalori reali di una matrice casuale (GOE, GUE, GSE) mediante un cambiamento di base. La densità di probabilità congiunta ha la forma:

$$
P \left(\lambda_{1} , \ldots , \lambda_{N}\right) = C_{N} exp \left(- g \underset{i}{\sum} \lambda_{i}^{2}\right) \underset{i < j}{\prod} \left|\lambda_{i} - \lambda_{j}\right|^{\beta}
$$

dove $\lambda_{i}$ sono gli autovalori, $C_{N}$ è una costante di normalizzazione, $g>0$ un parametro di scala, e $β=1,2,4$ corrisponde rispettivamente agli ensemble GOE, GUE e GSE. Questa [distribuzione](https://it.wikipedia.org/wiki/Distribuzione_probabilistica "Distribuzione probabilistica") implica una repulsione tra gli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore"): la probabilità che due autovalori siano molto vicini ($s→0$) tende a zero, in netto contrasto con il comportamento di un [processo di Poisson](https://it.wikipedia.org/wiki/Processo_di_Poisson "Processo di Poisson"). Questa proprietà è nota come repulsione dei livelli [^3].

### Legge di Marčenko–Pastur

La legge di Marčenko–Pastur descrive il comportamento asintotico dello [spettro](https://it.wikipedia.org/wiki/Spettro_\(matematica\) "Spettro (matematica)") delle [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") di [covarianza](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\) "Covarianza (probabilità)") campionarie, ed è la controparte della legge semicircolare per [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") rettangolari [^14].

Sia $X$ una matrice $n×p$ con elementi reali indipendenti e identicamente distribuiti, a [media](https://it.wikipedia.org/wiki/Media_\(statistica\) "Media (statistica)") zero e [varianza](https://it.wikipedia.org/wiki/Varianza "Varianza") $\sigma^{2}$. Si considera la [matrice](https://it.wikipedia.org/wiki/Matrice "Matrice") di [covarianza](https://it.wikipedia.org/wiki/Covarianza_\(probabilit%C3%A0\) "Covarianza (probabilità)") non normalizzata

$W = \frac{1}{n} X^{\top} X$

che è una matrice di Wishart. Se $n,p→∞$ con rapporto $c = \frac{p}{n} \in \left(0 , + \infty\right)$ fisso, allora la densità empirica degli autovalori di $W$ converge (quasi sicuramente) alla distribuzione di Marčenko–Pastur [^14]:

$ρMP(λ)={12πσ2cλ(λ+−λ)(λ−λ−)se λ∈[λ−,λ+]0altrimenti$

dove i bordi dello spettro sono

$\lambda_{\pm} = \sigma^{2} \left(\right. 1 \pm \sqrt{c} \left.\right)^{2}$

Per $c<1$, la [distribuzione](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale") presenta un atomo di [Dirac](https://it.wikipedia.org/wiki/Paul_Dirac "Paul Dirac") in zero con peso $1−c$.

La legge di Marčenko–Pastur trova applicazioni in [statistica multivariata](https://it.wikipedia.org/wiki/Statistica_multivariata "Statistica multivariata") (analisi delle componenti principali), [fisica teorica](https://it.wikipedia.org/wiki/Fisica_teorica "Fisica teorica") (spettro delle matrici di tipo Wishart) ed [apprendimento automatico](https://it.wikipedia.org/wiki/Apprendimento_automatico "Apprendimento automatico") e random feature models [^14].

### Comportamento degli autovalori estremi (Tracy–Widom)

Oltre alla distribuzione globale degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore"), grande interesse teorico e applicativo riguarda il comportamento degli autovalori estremi, in particolare il massimo (o minimo) autovalore di [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") aleatorie di grande dimensione.

![](https://it.wikipedia.org/wiki/File:Tracy-widom.png)

Distribuzione di Tracy-widom confrontata con una Normale standard.

Per molte classi di matrici (come l’ensemble gaussiano ortogonale – GOE, unitario – GUE, o simmetrico reale), si dimostra che l’ [autovalore](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") più grande $\lambda_{\text{max}}$ non cresce indefinitamente con $N$, ma fluttua intorno a un valore deterministico, con fluttuazioni descritte da una legge non gaussiana, detta legge di Tracy–Widom.[^15]

Sia $W_{N}$ una matrice del GUE di dimensione $N×N$, allora vale [^15]:

$\mathbb{P} \left(\frac{\lambda_{\text{max}} - 2 \sigma \sqrt{N}}{N^{- 1 / 6}} \leq s\right) \rightarrow F_{2} \left(s\right)$

dove $F_{2} \left(s\right)$ è la distribuzione di Tracy–Widom di tipo 2. Analogamente, per il GOE si ottiene $F_{1} \left(s\right)$. Queste distribuzioni sono legate alle soluzioni dell’equazione di Painlevé II e non hanno espressioni chiuse elementari. Tuttavia, esse descrivono in modo universale le fluttuazioni dell’autovalore massimo per un’ampia classe di matrici, anche al di fuori dei modelli [gaussiani](https://it.wikipedia.org/wiki/Distribuzione_normale "Distribuzione normale") [^15].

La legge di Tracy–Widom compare in numerosi ambiti [^6] [^15]:

- statistica multivariata (massimo autovalore in PCA),
- [combinatoria](https://it.wikipedia.org/wiki/Combinatoria "Combinatoria") (problema della sottosequenza crescente massima),
- [fisica statistica](https://it.wikipedia.org/wiki/Fisica_statistica "Fisica statistica") (interfacce aleatorie, crescita stocastica – KPZ),
- [teoria delle code](https://it.wikipedia.org/wiki/Teoria_delle_code "Teoria delle code") e [teoria dei numeri](https://it.wikipedia.org/wiki/Teoria_dei_numeri "Teoria dei numeri").

### Localizzazione e delocalizzazione degli autovettori

Nello studio delle [matrici](https://it.wikipedia.org/wiki/Matrice "Matrice") aleatorie non solo gli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") sono oggetto di analisi, ma anche le proprietà strutturali degli [autovettori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") associati. Una questione centrale è se un autovettore associato a un certo autovalore sia localizzato (concentrato su poche componenti) oppure delocalizzato (distribuito uniformemente su tutte le componenti) [^16].

Formalmente, dati gli autovettori $v^{\left(1\right)} , \ldots , v^{\left(N\right)}$ di una matrice aleatoria simmetrica $A_{N}$, si definisce un indice di partecipazione come:

$\text{IPR} \left(v\right) = \sum_{i = 1}^{N} \left|v_{i}\right|^{4}$

Un valore piccolo di $IPR(v)$ indica che il vettore è distribuito su molte componenti (delocalizzato), mentre un valore grande segnala localizzazione. Per le matrici gaussiane dense (GOE, GUE), è noto che gli [autovettori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") sono fortemente delocalizzati: ciascuna componente ha modulo quadrato dell’ordine di $1/N$ con alta probabilità. Viceversa, in modelli sparsi o con disordine forte (es. matrici a banda o matrici con struttura casuale), può emergere localizzazione. In tali casi, solo un [sottoinsieme](https://it.wikipedia.org/wiki/Inclusione_\(matematica\) "Inclusione (matematica)") ristretto delle componenti dell'autovettore è significativamente diverso da zero.[^16]

La transizione tra comportamento localizzato e delocalizzato è legata a fenomeni di transizione di Anderson [^16], con implicazioni nella:[^16]

- [fisica della materia condensata](https://it.wikipedia.org/wiki/Fisica_della_materia_condensata "Fisica della materia condensata") (conduzione elettronica nei solidi disordinati),
- [informazione quantistica](https://it.wikipedia.org/wiki/Informazione_quantistica "Informazione quantistica") (stati entangled),
- [analisi numerica](https://it.wikipedia.org/wiki/Analisi_numerica "Analisi numerica") e teoria del disordine.
![](https://it.wikipedia.org/wiki/File:Matrice_di_Wigner_densa_vs_sparsa.png)

Mappa di calore delle componenti al quadrato degli autovettori corrispondenti agli autovalori più alti di due matrici aleatorie simmetriche: una matrice di Wigner (a sinistra) e una matrice sparsa (a destra).Nella matrice densa gli autovettori appaiono delocalizzati, con valori distribuiti su tutte le componenti; nella matrice sparsa si osservano invece fenomeni di localizzazione, in cui pochi componenti dominano.Questo effetto è centrale nella teoria della localizzazione di Anderson e nella comprensione della transizione delocalizzazione/localizzazione in sistemi disordinati.

## Articoli fondanti

I fondamenti della teoria delle matrici aleatorie sono stati gettati nella seconda metà del [XX secolo](https://it.wikipedia.org/wiki/XX_secolo "XX secolo") attraverso una serie di lavori pionieristici che ne hanno definito il quadro concettuale e metodologico. Tra i contributi più influenti si annoverano:

- [Eugene P. Wigner](https://it.wikipedia.org/wiki/Eugene_Wigner "Eugene Wigner") [^3] (anni 1950): introdusse l’uso di matrici aleatorie per modellizzare gli spettri degli operatori hamiltoniani nei [nuclei atomici](https://it.wikipedia.org/wiki/Nucleo_atomico "Nucleo atomico"). Il cosiddetto semicerchio di Wigner rappresenta uno dei primi risultati universali della teoria, descrivendo la densità degli [autovalori](https://it.wikipedia.org/wiki/Autovettore_e_autovalore "Autovettore e autovalore") in certi limiti asintotici.
- [Freeman J. Dyson](https://it.wikipedia.org/wiki/Freeman_Dyson "Freeman Dyson") [^4] (1962): sviluppò una classificazione dei modelli di matrici aleatorie basata sulle simmetrie fondamentali dei sistemi fisici, introducendo i cosiddetti ensemble di Dyson (Gaussian Orthogonal, Unitary e Symplectic Ensembles, GOE, GUE, GSE). Il suo approccio formale permise di connettere la teoria delle matrici aleatorie con l’algebra delle simmetrie e la [meccanica quantistica](https://it.wikipedia.org/wiki/Meccanica_quantistica "Meccanica quantistica").
- Madan Lal Mehta [^5] (dal [1967](https://it.wikipedia.org/wiki/1967 "1967")): sistematizzò e ampliò i risultati precedenti in una trattazione organica e rigorosa, culminata nell’opera “Random Matrices” (prima edizione [1967](https://it.wikipedia.org/wiki/1967 "1967"), con successive edizioni aggiornate). Il testo di Mehta è considerato una referenza standard della disciplina e ha svolto un ruolo centrale nella sua diffusione e formalizzazione.

## Note

## Bibliografia

- (EN) Terence Tao, Topics in Random Matrix Theory, collana Graduate Studies in Mathematics, vol. 132, Providence, RI, American Mathematical Society, 2012, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1090/gsm/132](https://dx.doi.org/10.1090%2Fgsm%2F132), [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-0-8218-7430-1](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-0-8218-7430-1 "Speciale:RicercaISBN/978-0-8218-7430-1").
- (EN) Giacomo Livan, Marcel Novaes e Pierpaolo Vivo, Introduction to Random Matrices: Theory and Practice, collana SpringerBriefs in Mathematical Physics, vol. 26, Cham, Springer, 2018, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1007/978-3-319-70885-0](https://dx.doi.org/10.1007%2F978-3-319-70885-0), [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-3-319-70883-6](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-3-319-70883-6 "Speciale:RicercaISBN/978-3-319-70883-6").
- (EN) Greg W. Anderson, Alice Guionnet e Ofer Zeitouni, An Introduction to Random Matrices, collana Cambridge Studies in Advanced Mathematics, vol. 118, Cambridge, Cambridge University Press, 2010, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1017/CBO9780511801334](https://dx.doi.org/10.1017%2FCBO9780511801334), [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-0-521-19452-5](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-0-521-19452-5 "Speciale:RicercaISBN/978-0-521-19452-5").

## Voci correlate

- [Matrice hermitiana](https://it.wikipedia.org/wiki/Matrice_hermitiana "Matrice hermitiana")
- [Processo stocastico](https://it.wikipedia.org/wiki/Processo_stocastico "Processo stocastico")
- [Spettro di operatori](https://it.wikipedia.org/wiki/Spettro_\(matematica\) "Spettro (matematica)")
- [Metodo di Monte Carlo](https://it.wikipedia.org/wiki/Metodo_Monte_Carlo "Metodo Monte Carlo")
- [Ipotesi di Riemann](https://it.wikipedia.org/wiki/Ipotesi_di_Riemann "Ipotesi di Riemann")
- [Polinomi ortogonali](https://it.wikipedia.org/wiki/Polinomi_ortogonali "Polinomi ortogonali")

## Collegamenti esterni

- (EN) [Eric W. Weisstein](https://it.wikipedia.org/wiki/Eric_W._Weisstein "Eric W. Weisstein"), [Random Matrix](http://mathworld.wolfram.com/RandomMatrix.html), su [MathWorld](https://it.wikipedia.org/wiki/MathWorld "MathWorld"), Wolfram Research.
- Eric W. Weisstein, [Random Matrix](http://mathworld.wolfram.com/RandomMatrix.html), su mathworld.wolfram.com, Wolfram MathWorld.
- Alan Edelman et N. Raj Rao; [*Random Matrix Theory*](http://www.mit.edu/~raj/Acta05rmt.pdf), *Acta Numerica* 14: 233-297 (2005)
- Alan Edelman et Moe Win; [*Random Matrix Theory and Its Applications*](http://ocw.mit.edu/OcwWeb/Mathematics/18-996Spring2004/CourseHome/index.htm), MIT Opencourseware (2004).
- Alan Edelman et Moe Win; [*Infinite Random Matrix Theory*](http://ocw.mit.edu/OcwWeb/Mathematics/18-338JFall-2004/CourseHome/index.htm), MIT Opencourseware (2004).
- Matthew R. Watkins; [*Random matrices and the Riemann zeta function*](https://web.archive.org/web/20060925092113/http://www.maths.ex.ac.uk/~mwatkins/zeta/random.htm), Exeter University.
- [Alice Guionnet](https://it.wikipedia.org/wiki/Alice_Guionnet "Alice Guionnet"), [Large deviations and stochastic calculus for large random matrices](http://projecteuclid.org/Dienst/UI/1.0/Summarize/euclid.ps/1099928649), *[Probability Surveys](https://it.wikipedia.org/wiki/Probability_Surveys "Probability Surveys")* 1: 72-172 (2004)
- Zhidong Bai, [Methodologies in spectral analysis of large dimensional random matrices, a review](http://www3.stat.sinica.edu.tw/statistica/j9n3/j9n31/j9n31.htm), *Statistica Sinica* 9: 611-677 (1999)

| [Controllo di autorità](https://it.wikipedia.org/wiki/Aiuto:Controllo_di_autorit%C3%A0 "Aiuto:Controllo di autorità") | [LCCN](https://it.wikipedia.org/wiki/Library_of_Congress_Control_Number "Library of Congress Control Number") (EN) [sh86001920](http://id.loc.gov/authorities/subjects/sh86001920) · [J9U](https://it.wikipedia.org/wiki/Biblioteca_nazionale_di_Israele "Biblioteca nazionale di Israele") (EN, HE) [987007543966505171](https://www.nli.org.il/en/authorities/987007543966505171) |
| --- | --- |

[^1]: (EN) Terence Tao, Topics in Random Matrix Theory, collana Graduate Studies in Mathematics, vol. 132, American Mathematical Society, 2012, p. 282, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1090/gsm/132](https://dx.doi.org/10.1090%2Fgsm%2F132), [ISBN](https://it.wikipedia.org/wiki/ISBN "ISBN") [978-0-8218-7430-1](https://it.wikipedia.org/wiki/Speciale:RicercaISBN/978-0-8218-7430-1 "Speciale:RicercaISBN/978-0-8218-7430-1").

[^2]: Giacomo Livan, Marcel Novaes e Pierpaolo Vivo, *Introduction to Random Matrices: Theory and Practice*, collana *SpringerBriefs in Mathematical Physics*, vol. 26, Springer, 2018, p. 133, [ISBN 978-3-319-70883-6](https://it.wikipedia.org/wiki/Special:BookSources/9783319708836), [DOI:10.1007/978-3-319-70885-0](https://doi.org/10.1007/978-3-319-70885-0 "doi:10.1007/978-3-319-70885-0").

[^3]: Eugene P. Wigner, [Characteristic Vectors of Bordered Matrices with Infinite Dimensions](https://archive.org/details/sim_annals-of-mathematics_1955-11_62_3/page/548), in Annals of Mathematics, vol. 62, n. 3, 1955, pp. 548–564, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.2307/1970079](https://dx.doi.org/10.2307%2F1970079).

[^4]: Freeman J. Dyson, [Statistical theory of the energy levels of complex systems. I–III](https://archive.org/details/sim_journal-of-mathematics-and-physics_january-february-1962_3_1/page/140), in Journal of Mathematical Physics, vol. 3, n. 1, 1962, pp. 140–175, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1063/1.1703773](https://dx.doi.org/10.1063%2F1.1703773).

[^5]: Madan Lal Mehta, Random Matrices, 1ª ed., New York, Academic Press, 1967, pp. 33-181.

[^6]: Bertrand Eynard, «L'universalité des matrices aléatoires», *Pour la science*, nº 487, maggio 2018, pp. 34-44.

[^7]: Bohr, Niels (1936). *The Compound Nucleus*. Disponibile online presso il Max Planck Institute for the History of Science: [https://www.mprl-series.mpg.de/proceedings/5/11/index.html](https://www.mprl-series.mpg.de/proceedings/5/11/index.html).

[^8]: Pennington, J., & Bahri, Y. (2017). “Geometry of neural network loss surfaces via random matrix theory”. In: *Proceedings of the 34th International Conference on Machine Learning (ICML)*, Vol. 70, pp. 2798–2806. PMLR. Disponibile online: [https://proceedings.mlr.press/v70/pennington17a.html](https://proceedings.mlr.press/v70/pennington17a.html).

[^9]: Martin, C. H., & Mahoney, M. W. (2021). “Implicit self-regularization in deep neural networks: Evidence from random matrix theory and implications for learning”. *Journal of Machine Learning Research*, 22(165): 1–73. Disponibile online: [https://www.jmlr.org/papers/v22/20-1250.html](https://www.jmlr.org/papers/v22/20-1250.html).

[^10]: John Wishart, [The generalised product moment distribution in samples from a normal multivariate population](https://oadoi.org/10.1093%2Fbiomet%2F20A.1-2.32), in Biometrika, 20A, 1–2, 1928, pp. 32–52, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1093/biomet/20A.1-2.32](https://dx.doi.org/10.1093%2Fbiomet%2F20A.1-2.32).

[^11]: Antonia M. Tulino e Sergio Verdú, Random Matrix Theory and Wireless Communications, Now Publishers, 2004, pp. 21-29.

[^12]: G.J. Rodgers e A.J. Bray, [Density of states of sparse random matrices](https://oadoi.org/10.1103%2FPhysRevB.37.3557), in Physical Review B, vol. 37, 1988, pp. 3557–3562, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1103/PhysRevB.37.3557](https://dx.doi.org/10.1103%2FPhysRevB.37.3557).

[^13]: A. Khorunzhy, Sparse random matrices: spectral edge and statistics of rooted trees, in Advances in Applied Probability, vol. 33, n. 1, 2001, pp. 124–140.

[^14]: Vladimir A. Marčenko e Leonid A. Pastur, [Distribution of eigenvalues for some sets of random matrices](https://oadoi.org/10.1070%2FSM1967v001n04ABEH001994), in Mathematics of the USSR–Sbornik, vol. 1, n. 4, 1967, pp. 457–483, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1070/SM1967v001n04ABEH001994](https://dx.doi.org/10.1070%2FSM1967v001n04ABEH001994).

[^15]: Craig A. Tracy e Harold Widom, [Level-spacing distributions and the Airy kernel](https://archive.org/details/sim_communications-in-mathematical-physics_1994-01_159_1/page/150), in Communications in Mathematical Physics, vol. 159, n. 1, 1994, pp. 151–174, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1007/BF02100489](https://dx.doi.org/10.1007%2FBF02100489).

[^16]: Fritz Evers e Alexander D. Mirlin, [Anderson transitions](https://oadoi.org/10.1103%2FRevModPhys.80.1355), in Reviews of Modern Physics, vol. 80, n. 4, 2008, pp. 1355–1417, [DOI](https://it.wikipedia.org/wiki/Digital_object_identifier "Digital object identifier"):[10.1103/RevModPhys.80.1355](https://dx.doi.org/10.1103%2FRevModPhys.80.1355).