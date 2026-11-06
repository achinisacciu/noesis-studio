import os

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from noesis_contracts import Document

from app.api import routes
from app.main import app
from app.search import extract_hits

client = TestClient(app)

DOCUMENT = Document(
    id="doc1",
    title="Statistica",
    text="La media è 3. La varianza misura la dispersione dei dati.",
    created_at="2026-01-01T00:00:00Z",
)


@pytest.fixture(autouse=True)
def clean_env() -> None:
    os.environ.pop("NOESIS_TOKEN", None)


def test_extract_hits_matches_sentence() -> None:
    hits = extract_hits("varianza", DOCUMENT.text)
    assert len(hits) == 1
    assert hits[0].position == 1


def test_extract_hits_ignores_short_terms() -> None:
    assert extract_hits("di", DOCUMENT.text) == []


def test_search_returns_hits(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_fetch(document_id: str) -> Document:
        assert document_id == DOCUMENT.id
        return DOCUMENT

    monkeypatch.setattr(routes, "fetch_document", fake_fetch)
    response = client.post("/search", json={"query": "varianza", "document_id": DOCUMENT.id})
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["document_id"] == DOCUMENT.id
    assert body["data"]["hits"][0]["position"] == 1


def test_search_missing_document_returns_envelope(monkeypatch: pytest.MonkeyPatch) -> None:
    async def missing(document_id: str) -> Document:
        raise HTTPException(status_code=404, detail="documento non trovato")

    monkeypatch.setattr(routes, "fetch_document", missing)
    response = client.post("/search", json={"query": "varianza", "document_id": "nope"})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_search_requires_token() -> None:
    os.environ["NOESIS_TOKEN"] = "secret"
    response = client.post("/search", json={"query": "varianza", "document_id": DOCUMENT.id})
    assert response.status_code == 401
