# Risorse di studio

Materiale di studio versionato che alimenta il RAG e l'aiuto allo studio. Non è stato di runtime: gli originali restano qui, l'app ne importa una copia in `data/files/` quando li carichi.

| Cartella | Cosa contiene | Trattamento |
| --- | --- | --- |
| `wikipedia/` | Articoli di it.wikipedia.org su probabilità, statistica e processi stocastici | Sorgente canonica, versionata |
| `../evaluation/corpus/` | Corpus etichettato per misurare la qualità delle citazioni | Non mescolarlo con le risorse: serve solo alla valutazione |
| `../data/` | Copie importate, SQLite, ChromaDB, log | Runtime, gitignored |

## Provenienza e licenza

- Ogni file ha il front matter del clipper: `source` con l'URL originale, `published`, `created`.
- I testi sono di Wikipedia in italiano, licenza **CC BY-SA 4.0**. L'attribuzione è l'URL in `source`; se pubblichi estratti, mantieni la licenza e il link.
- Il codice del progetto non è coperto da questa licenza: vale solo per il testo delle risorse.

## Come si usano

1. Avvia lo stack (`python scripts/stack.py --dev`) e la UI.
2. "Importa" un file da questa cartella: il Document Service lo copia in `data/files/<document_id>/` e lo indicizza.
3. "Ricostruisci indice" dopo un import massiccio o un cambio di modello di embedding.

Oggi l'import è un file alla volta: non c'è un import di cartella. L'originale qui resta la sorgente; la copia in `data/` è quella che il RAG legge.

## Aggiungere materiale

- Un file Markdown per articolo, nome = titolo (le parentesi sono ammesse).
- Tieni il front matter con `title` e `source`: senza URL l'attribuzione si perde.
- Preferisci testo già pulito: link e immagini wiki restano nel Markdown e finiscono nei chunk.
- Dopo l'aggiunta, importa i nuovi file dalla UI e ricostruisci l'indice.
