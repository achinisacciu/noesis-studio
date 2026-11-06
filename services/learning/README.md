# Learning Service

Possiede le schede di studio: creazione, modifica, eliminazione e recupero delle flashcard.

## Dati

- SQLite: `data/sqlite/learning.db` (tabelle `flashcards`).
- Nessuna dipendenza dagli altri servizi: il documento citato è solo un riferimento (`document_id`, pagina, sezione).

## Endpoint

| Metodo | Percorso | Uso |
| --- | --- | --- |
| `GET` | `/flashcards` | Elenco, filtrabile con `?document_id=` |
| `POST` | `/flashcards` | Crea una scheda |
| `PATCH` | `/flashcards/{id}` | Aggiorna fronte e retro |
| `DELETE` | `/flashcards/{id}` | Elimina una scheda |
| `DELETE` | `/flashcards?document_id=` | Elimina le schede di un documento |
| `GET` | `/health`, `/ready` | Stato del servizio |

Le API sono protette da `Authorization: Bearer <token>` come gli altri servizi; il gateway è l'unico client.
