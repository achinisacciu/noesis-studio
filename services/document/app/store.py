import shutil
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

from noesis_contracts import Annotation, AnnotationCreate, Chunk, DocumentSummary

SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    filename TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS chunks (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    position INTEGER NOT NULL,
    text TEXT NOT NULL,
    page INTEGER,
    section TEXT
);
CREATE INDEX IF NOT EXISTS idx_chunks_document ON chunks(document_id);
CREATE TABLE IF NOT EXISTS annotations (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    chunk_id TEXT NOT NULL REFERENCES chunks(id) ON DELETE CASCADE,
    kind TEXT NOT NULL,
    start INTEGER NOT NULL DEFAULT 0,
    end INTEGER NOT NULL DEFAULT 0,
    note TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_annotations_document ON annotations(document_id);
"""


class Store:
    def __init__(self, db_path: Path, files_dir: Path) -> None:
        self.db_path = db_path
        self.files_dir = files_dir
        db_path.parent.mkdir(parents=True, exist_ok=True)
        files_dir.mkdir(parents=True, exist_ok=True)
        with self._db() as conn:
            conn.execute("PRAGMA journal_mode=WAL")
            conn.executescript(SCHEMA)

    @contextmanager
    def _db(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.db_path, timeout=5)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def _summary(row: sqlite3.Row) -> DocumentSummary:
        return DocumentSummary(
            id=row["id"],
            title=row["title"],
            filename=row["filename"],
            created_at=datetime.fromisoformat(row["created_at"]),
            chunk_count=int(row["chunk_count"]),
        )

    def create(
        self,
        document_id: str,
        title: str,
        filename: str,
        created_at: datetime,
        chunks: list[Chunk],
    ) -> DocumentSummary:
        with self._db() as conn:
            conn.execute(
                "INSERT INTO documents (id, title, filename, created_at) VALUES (?, ?, ?, ?)",
                (document_id, title, filename, created_at.isoformat()),
            )
            conn.executemany(
                "INSERT INTO chunks (id, document_id, position, text, page, section)"
                " VALUES (?, ?, ?, ?, ?, ?)",
                [
                    (
                        chunk.id,
                        chunk.document_id,
                        chunk.position,
                        chunk.text,
                        chunk.page,
                        chunk.section,
                    )
                    for chunk in chunks
                ],
            )
        return DocumentSummary(
            id=document_id,
            title=title,
            filename=filename,
            created_at=created_at,
            chunk_count=len(chunks),
        )

    def list_documents(self) -> list[DocumentSummary]:
        with self._db() as conn:
            rows = conn.execute(
                "SELECT d.*, COUNT(c.id) AS chunk_count FROM documents d"
                " LEFT JOIN chunks c ON c.document_id = d.id"
                " GROUP BY d.id ORDER BY d.created_at"
            ).fetchall()
        return [self._summary(row) for row in rows]

    def get(self, document_id: str) -> DocumentSummary | None:
        with self._db() as conn:
            row = conn.execute(
                "SELECT d.*, COUNT(c.id) AS chunk_count FROM documents d"
                " LEFT JOIN chunks c ON c.document_id = d.id"
                " WHERE d.id = ? GROUP BY d.id",
                (document_id,),
            ).fetchone()
        return self._summary(row) if row else None

    def chunks(self, document_id: str) -> list[Chunk]:
        with self._db() as conn:
            rows = conn.execute(
                "SELECT * FROM chunks WHERE document_id = ? ORDER BY position",
                (document_id,),
            ).fetchall()
        return [
            Chunk(
                id=row["id"],
                document_id=row["document_id"],
                position=row["position"],
                text=row["text"],
                page=row["page"],
                section=row["section"],
            )
            for row in rows
        ]

    def chunk_text(self, document_id: str, chunk_id: str) -> str | None:
        with self._db() as conn:
            row = conn.execute(
                "SELECT text FROM chunks WHERE id = ? AND document_id = ?",
                (chunk_id, document_id),
            ).fetchone()
        return row["text"] if row else None

    @staticmethod
    def _annotation(row: sqlite3.Row) -> Annotation:
        return Annotation(
            id=row["id"],
            document_id=row["document_id"],
            chunk_id=row["chunk_id"],
            kind=row["kind"],
            start=row["start"],
            end=row["end"],
            note=row["note"],
            created_at=datetime.fromisoformat(row["created_at"]),
        )

    def annotations(self, document_id: str) -> list[Annotation]:
        with self._db() as conn:
            rows = conn.execute(
                "SELECT * FROM annotations WHERE document_id = ? ORDER BY created_at, id",
                (document_id,),
            ).fetchall()
        return [self._annotation(row) for row in rows]

    def add_annotation(
        self,
        annotation_id: str,
        document_id: str,
        payload: AnnotationCreate,
        created_at: datetime,
    ) -> Annotation:
        with self._db() as conn:
            conn.execute(
                "INSERT INTO annotations"
                " (id, document_id, chunk_id, kind, start, end, note, created_at)"
                " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    annotation_id,
                    document_id,
                    payload.chunk_id,
                    payload.kind,
                    payload.start,
                    payload.end,
                    payload.note,
                    created_at.isoformat(),
                ),
            )
        return Annotation(
            id=annotation_id,
            document_id=document_id,
            chunk_id=payload.chunk_id,
            kind=payload.kind,
            start=payload.start,
            end=payload.end,
            note=payload.note,
            created_at=created_at,
        )

    def delete_annotation(self, annotation_id: str) -> bool:
        with self._db() as conn:
            cursor = conn.execute("DELETE FROM annotations WHERE id = ?", (annotation_id,))
            return cursor.rowcount > 0

    def delete(self, document_id: str) -> bool:
        with self._db() as conn:
            row = conn.execute("SELECT id FROM documents WHERE id = ?", (document_id,)).fetchone()
            if row is None:
                return False
            conn.execute("DELETE FROM documents WHERE id = ?", (document_id,))
        shutil.rmtree(self.files_dir / document_id, ignore_errors=True)
        return True
