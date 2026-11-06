import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

from noesis_contracts import Flashcard, FlashcardCreate, FlashcardUpdate

SCHEMA = """
CREATE TABLE IF NOT EXISTS flashcards (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    front TEXT NOT NULL,
    back TEXT NOT NULL,
    page INTEGER,
    section TEXT,
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_flashcards_document ON flashcards(document_id);
"""


class Store:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._db() as conn:
            conn.execute("PRAGMA journal_mode=WAL")
            conn.executescript(SCHEMA)

    @contextmanager
    def _db(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.db_path, timeout=5)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def _card(row: sqlite3.Row) -> Flashcard:
        return Flashcard(
            id=row["id"],
            document_id=row["document_id"],
            front=row["front"],
            back=row["back"],
            page=row["page"],
            section=row["section"],
            created_at=datetime.fromisoformat(row["created_at"]),
        )

    def create(self, card_id: str, payload: FlashcardCreate, created_at: datetime) -> Flashcard:
        with self._db() as conn:
            conn.execute(
                "INSERT INTO flashcards (id, document_id, front, back, page, section, created_at)"
                " VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    card_id,
                    payload.document_id,
                    payload.front,
                    payload.back,
                    payload.page,
                    payload.section,
                    created_at.isoformat(),
                ),
            )
        return Flashcard(
            id=card_id,
            document_id=payload.document_id,
            front=payload.front,
            back=payload.back,
            page=payload.page,
            section=payload.section,
            created_at=created_at,
        )

    def list(self, document_id: str | None = None) -> list[Flashcard]:
        query = "SELECT * FROM flashcards"
        params: tuple[str, ...] = ()
        if document_id is not None:
            query += " WHERE document_id = ?"
            params = (document_id,)
        query += " ORDER BY created_at DESC, id"
        with self._db() as conn:
            rows = conn.execute(query, params).fetchall()
        return [self._card(row) for row in rows]

    def get(self, card_id: str) -> Flashcard | None:
        with self._db() as conn:
            row = conn.execute("SELECT * FROM flashcards WHERE id = ?", (card_id,)).fetchone()
        return self._card(row) if row else None

    def update(self, card_id: str, payload: FlashcardUpdate) -> Flashcard | None:
        fields: list[str] = []
        values: list[str] = []
        if payload.front is not None:
            fields.append("front = ?")
            values.append(payload.front)
        if payload.back is not None:
            fields.append("back = ?")
            values.append(payload.back)
        if not fields:
            return self.get(card_id)
        with self._db() as conn:
            row = conn.execute("SELECT id FROM flashcards WHERE id = ?", (card_id,)).fetchone()
            if row is None:
                return None
            conn.execute(
                f"UPDATE flashcards SET {', '.join(fields)} WHERE id = ?",
                (*values, card_id),
            )
        return self.get(card_id)

    def delete(self, card_id: str) -> bool:
        with self._db() as conn:
            row = conn.execute("SELECT id FROM flashcards WHERE id = ?", (card_id,)).fetchone()
            if row is None:
                return False
            conn.execute("DELETE FROM flashcards WHERE id = ?", (card_id,))
        return True

    def delete_for_document(self, document_id: str) -> int:
        with self._db() as conn:
            cursor = conn.execute("DELETE FROM flashcards WHERE document_id = ?", (document_id,))
            return cursor.rowcount
