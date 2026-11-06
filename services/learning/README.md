# Learning Service

Possiede le schede di studio e la posizione di lettura: creazione, modifica, eliminazione e recupero delle flashcard, ripresa del documento dall'ultimo punto letto.

## Dati

- SQLite: `data/sqlite/learning.db` (tabelle `flashcards` e `reading_positions`).
- Nessuna dipendenza dagli altri servizi: il documento citato è solo un riferimento (`document_id`, pagina, sezione).

## Endpoint

| Metodo | Percorso | Uso |
| --- | --- | --- |
| `GET` | `/flashcards` | Elenco, filtrabile con `?document_id=` |
| `POST` | `/flashcards` | Crea una scheda |
| `PATCH` | `/flashcards/{id}` | Aggiorna fronte e retro |
| `DELETE` | `/flashcards/{id}` | Elimina una scheda |
| `DELETE` | `/flashcards?document_id=` | Elimina le schede di un documento |
| `GET` | `/reading-positions/{document_id}` | Ultima posizione di lettura, o `null` |
| `PUT` | `/reading-positions/{document_id}` | Salva chunk e posizione corrente |
| `DELETE` | `/reading-positions/{document_id}` | Elimina la posizione di un documento |
| `GET` | `/health`, `/ready` | Stato del servizio |

Le API sono protette da `Authorization: Bearer <token>` come gli altri servizi; il gateway è l'unico client.
