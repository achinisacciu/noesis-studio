import os

import pytest
from fastapi.testclient import TestClient
from noesis_contracts import Chunk, DocumentSummary, SearchHit

from app.api import routes
from app.main import app

client = TestClient(app)

CHUNK = Chunk(
    id="doc1:0",
    document_id="doc1",
    position=0,
    text="La varianza misura la dispersione dei dati.",
    page=3,
    section="Varianza",
)
DOCUMENT = DocumentSummary(
    id="doc1",
    title="Statistica",
    filename="statistica.md",
    created_at="2026-01-01T00:00:00Z",
    chunk_count=1,
)


class FakeIndex:
    def __init__(self) -> None:
        self.chunks: list[Chunk] = []
        self.deleted: list[str] = []
        self.resets = 0

    def replace(self, chunks: list[Chunk]) -> None:
        self.chunks = chunks

    def delete(self, document_id: str) -> None:
        self.deleted.append(document_id)
        self.chunks = [chunk for chunk in self.chunks if chunk.document_id != document_id]

    def reset(self) -> None:
        self.resets += 1
        self.chunks = []

    def search(self, query: str, limit: int, document_id: str | None = None) -> list[SearchHit]:
        return [
            SearchHit(
                document_id=CHUNK.document_id,
                text=CHUNK.text,
                page=CHUNK.page,
                section=CHUNK.section,
                score=0.87,
            )
        ][:limit]


@pytest.fixture(autouse=True)
def clean_state(monkeypatch: pytest.MonkeyPatch) -> None:
    fake = FakeIndex()
    monkeypatch.setattr(routes, "index", fake)
    os.environ.pop("NOESIS_TOKEN", None)


def test_health_and_ready() -> None:
    for path in ("/health", "/ready"):
        response = client.get(path)
        assert response.status_code == 200
        assert response.json()["data"]["status"] == "healthy"


def test_index_fetches_chunks_and_replaces(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_fetch(document_id: str) -> list[Chunk]:
        assert document_id == "doc1"
        return [CHUNK]

    monkeypatch.setattr(routes, "fetch_chunks", fake_fetch)
    response = client.post("/index", json={"document_id": "doc1"})

    assert response.status_code == 200
    assert response.json()["data"] == {"document_id": "doc1", "chunks": 1}
    assert routes.index.chunks == [CHUNK]


def test_search_returns_citations(monkeypatch: pytest.MonkeyPatch) -> None:
    response = client.post("/search", json={"query": "dispersione", "limit": 3})

    assert response.status_code == 200
    hit = response.json()["data"]["hits"][0]
    assert hit["document_id"] == "doc1"
    assert hit["page"] == 3
    assert hit["section"] == "Varianza"
    assert hit["score"] == 0.87


def test_delete_removes_document_from_index() -> None:
    response = client.delete("/index/doc1")

    assert response.status_code == 200
    assert response.json()["data"] == {"id": "doc1"}
    assert routes.index.deleted == ["doc1"]


def test_rebuild_resets_and_reindexes_all_documents(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_list() -> list[DocumentSummary]:
        return [DOCUMENT]

    async def fake_fetch(document_id: str) -> list[Chunk]:
        assert document_id == "doc1"
        return [CHUNK]

    monkeypatch.setattr(routes, "list_documents", fake_list)
    monkeypatch.setattr(routes, "fetch_chunks", fake_fetch)
    response = client.post("/index/rebuild")

    assert response.status_code == 200
    assert response.json()["data"] == {"documents": 1, "chunks": 1}
    assert routes.index.resets == 1
    assert routes.index.chunks == [CHUNK]


def test_search_requires_token() -> None:
    os.environ["NOESIS_TOKEN"] = "secret"
    response = client.post("/search", json={"query": "dispersione"})
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_search_validates_empty_query() -> None:
    response = client.post("/search", json={"query": ""})
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"
