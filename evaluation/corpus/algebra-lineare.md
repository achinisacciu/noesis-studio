# Algebra lineare

## Vettori e prodotto scalare

Un vettore è una freccia con una direzione, un verso e una lunghezza, oppure una lista ordinata di numeri. Il prodotto scalare tra due vettori si ottiene moltiplicando le componenti corrispondenti e sommando i risultati: restituisce un numero, non un vettore. Quando il prodotto scalare vale zero i due vettori sono ortogonali, cioè perpendicolari tra loro. La norma, o lunghezza, di un vettore è la radice quadrata del prodotto scalare del vettore con sé stesso.

## Matrici e operazioni

Una matrice è una tabella rettangolare di numeri disposti in righe e colonne. La somma tra matrici si fa elemento per elemento, purché abbiano le stesse dimensioni. Il prodotto tra matrici si può calcolare solo se il numero di colonne della prima è uguale al numero di righe della seconda: l'elemento in posizione riga i e colonna j è il prodotto scalare tra la riga i della prima e la colonna j della seconda. La matrice trasposta scambia righe e colonne, e la matrice identità lascia invariato qualunque vettore moltiplicato per essa.

## Determinante e rango

Il determinante è un numero associato a una matrice quadrata. Se è diverso da zero la matrice è invertibile e le sue colonne sono linearmente indipendenti; se vale zero la matrice è singolare e non ammette inversa. Il rango è il numero massimo di righe, o colonne, linearmente indipendenti: dice quante direzioni diverse genera la matrice e coincide con il numero di pivot dopo l'eliminazione di Gauss. Rango pieno significa che nessuna riga è combinazione lineare delle altre.

## Sistemi lineari

Un sistema di equazioni lineari si risolve con il metodo di eliminazione di Gauss, che combina le righe per annullare i coefficienti e ottenere una forma triangolare. Il sistema ha una sola soluzione se la matrice dei coefficienti ha determinante diverso da zero, nessuna soluzione se le equazioni sono contraddittorie, infinite soluzioni se una equazione è combinazione delle altre. Geometricamente, due rette nel piano si incontrano in un punto, sono parallele senza intersezioni oppure coincidono.

## Autovalori e autovettori

Un autovettore di una matrice è un vettore che, dopo la trasformazione, resta sulla stessa retta: cambia solo di lunghezza, e il fattore di scala è il suo autovalore. Si trovano risolvendo l'equazione che annulla il determinante della matrice meno l'autovalore per l'identità, cioè il polinomio caratteristico. Gli autovalori rivelano proprietà della trasformazione, come la stabilità di un sistema dinamico, e permettono la decomposizione spettrale usata in statistica, grafi e compressione delle immagini.
