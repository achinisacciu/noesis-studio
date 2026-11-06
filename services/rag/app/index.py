import os
from pathlib import Path
from typing import Protocol

import chromadb
from chromadb.config import Settings
from noesis_contracts import Chunk, SearchHit

DATA_DIR = Path(os.getenv("NOESIS_DATA") or Path(__file__).resolve().parents[3] / "data")
COLLECTION = "chunks"


class Index(Protocol):
    def replace(self, chunks: list[Chunk]) -> None: ...

    def delete(self, document_id: str) -> None: ...

    def reset(self) -> None: ...

    def search(self, query: str, limit: int, document_id: str | None = None) -> list[SearchHit]: ...


class ChromaIndex:
    def __init__(self, path: Path) -> None:
        self._client = chromadb.PersistentClient(
            path=str(path), settings=Settings(anonymized_telemetry=False)
        )
        self._collection = self._client.get_or_create_collection(COLLECTION)

    def replace(self, chunks: list[Chunk]) -> None:
        if not chunks:
            return
        self.delete(chunks[0].document_id)
        for start in range(0, len(chunks), 100):
            batch = chunks[start : start + 100]
            self._collection.add(
                ids=[chunk.id for chunk in batch],
                documents=[chunk.text for chunk in batch],
                # shortcut: Chroma non accetta None nei metadati, -1 e "" indicano assente
                metadatas=[
                    {
                        "document_id": chunk.document_id,
                        "page": chunk.page if chunk.page is not None else -1,
                        "section": chunk.section or "",
                    }
                    for chunk in batch
                ],
            )

    def delete(self, document_id: str) -> None:
        self._collection.delete(where={"document_id": document_id})

    def reset(self) -> None:
        self._client.delete_collection(COLLECTION)
        self._collection = self._client.get_or_create_collection(COLLECTION)

    def search(self, query: str, limit: int, document_id: str | None = None) -> list[SearchHit]:
        total = self._collection.count()
        if total == 0:
            return []
        result = self._collection.query(
            query_texts=[query],
            n_results=min(limit, total),
            where={"document_id": document_id} if document_id else None,
        )
        metadatas = (result["metadatas"] or [[]])[0]
        documents = (result["documents"] or [[]])[0]
        distances = (result["distances"] or [[]])[0]
        return [
            SearchHit(
                document_id=str(metadata["document_id"]),
                text=text or "",
                page=(
                    int(metadata["page"])
                    if isinstance(metadata["page"], int | float) and metadata["page"] >= 0
                    else None
                ),
                section=str(metadata["section"]) or None,
                score=round(1 - float(distance), 4),
            )
            for metadata, text, distance in zip(metadatas, documents, distances, strict=True)
        ]
