import os

import pytest
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

from app.api import routes
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_env() -> None:
    os.environ.pop("NOESIS_TOKEN", None)


def test_create_document_forwards(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str, str, dict[str, object] | None]] = []

    async def fake_forward(
        method: str, base_url: str, path: str, payload: dict[str, object] | None = None
    ) -> JSONResponse:
        calls.append((method, base_url, path, payload))
        return JSONResponse(status_code=200, content={"status": "success", "data": {"id": "x"}})

    monkeypatch.setattr(routes, "forward", fake_forward)
    response = client.post("/api/documents", json={"title": "t", "text": "contenuto"})

    assert response.status_code == 200
    assert calls == [
        ("POST", routes.DOCUMENT_URL, "/documents", {"title": "t", "text": "contenuto"})
    ]


def test_rag_search_forwards(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str, str]] = []

    async def fake_forward(
        method: str, base_url: str, path: str, payload: dict[str, object] | None = None
    ) -> JSONResponse:
        calls.append((method, base_url, path))
        return JSONResponse(status_code=200, content={"status": "success", "data": {"hits": []}})

    monkeypatch.setattr(routes, "forward", fake_forward)
    response = client.post("/api/rag/search", json={"query": "varianza", "document_id": "d1"})

    assert response.status_code == 200
    assert calls == [("POST", routes.RAG_URL, "/search")]


def test_api_requires_token() -> None:
    os.environ["NOESIS_TOKEN"] = "secret"
    response = client.post("/api/rag/search", json={"query": "varianza", "document_id": "d1"})
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_ready_reports_degraded(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_check(base_url: str, name: str) -> tuple[str, str]:
        return name, "unavailable" if name == "rag" else "healthy"

    monkeypatch.setattr(routes, "check", fake_check)
    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json()["data"] == {"document": "healthy", "rag": "unavailable"}


def test_health() -> None:
    assert client.get("/health").json()["data"]["status"] == "healthy"
