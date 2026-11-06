import uuid
from datetime import UTC, datetime

from noesis_contracts import Document, DocumentCreate


class Store:
    def __init__(self) -> None:
        self._documents: dict[str, Document] = {}

    def save(self, payload: DocumentCreate) -> Document:
        document = Document(
            id=uuid.uuid4().hex,
            created_at=datetime.now(UTC),
            **payload.model_dump(),
        )
        self._documents[document.id] = document
        return document

    def get(self, document_id: str) -> Document | None:
        return self._documents.get(document_id)

    def clear(self) -> None:
        self._documents.clear()


store = Store()
