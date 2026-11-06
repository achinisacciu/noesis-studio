import os
from collections.abc import AsyncIterator

import pytest
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

from app.api import routes
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_env() -> None:
    os.environ.pop("NOESIS_TOKEN", None)


def test_import_forwards_file(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str, str, str, bytes]] = []

    async def fake_forward_file(
        method: str,
        base_url: str,
        path: str,
        filename: str,
        content: bytes,
        content_type: str,
    ) -> JSONResponse:
        calls.append((method, base_url, path, filename, content))
        return JSONResponse(status_code=200, content={"status": "success", "data": {"id": "x"}})

    monkeypatch.setattr(routes, "forward_file", fake_forward_file)
    response = client.post(
        "/api/documents", files={"file": ("note.md", b"# Titolo\ntesto", "text/markdown")}
    )

    assert response.status_code == 200
    assert calls == [("POST", routes.DOCUMENT_URL, "/documents", "note.md", b"# Titolo\ntesto")]


def test_delete_cleans_index_before_document(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str, str]] = []

    async def fake_forward(
        method: str, base_url: str, path: str, payload: dict[str, object] | None = None
    ) -> JSONResponse:
        calls.append((method, base_url, path))
        return JSONResponse(status_code=200, content={"status": "success", "data": {"id": "d1"}})

    monkeypatch.setattr(routes, "forward", fake_forward)
    response = client.delete("/api/documents/d1")

    assert response.status_code == 200
    assert calls == [
        ("DELETE", routes.RAG_URL, "/index/d1"),
        ("DELETE", routes.DOCUMENT_URL, "/documents/d1"),
    ]


def test_delete_aborts_when_index_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    async def fake_forward(
        method: str, base_url: str, path: str, payload: dict[str, object] | None = None
    ) -> JSONResponse:
        calls.append(path)
        return JSONResponse(status_code=502, content={"status": "error"})

    monkeypatch.setattr(routes, "forward", fake_forward)
    response = client.delete("/api/documents/d1")

    assert response.status_code == 502
    assert calls == ["/index/d1"]


def test_index_and_rebuild_forward(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str, dict[str, object] | None]] = []

    async def fake_forward(
        method: str, base_url: str, path: str, payload: dict[str, object] | None = None
    ) -> JSONResponse:
        calls.append((method, path, payload))
        return JSONResponse(status_code=200, content={"status": "success", "data": {}})

    monkeypatch.setattr(routes, "forward", fake_forward)
    client.post("/api/index/d1")
    client.post("/api/index/rebuild")

    assert calls == [
        ("POST", "/index", {"document_id": "d1"}),
        ("POST", "/index/rebuild", None),
    ]


def test_rag_search_forwards(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str, str]] = []

    async def fake_forward(
        method: str, base_url: str, path: str, payload: dict[str, object] | None = None
    ) -> JSONResponse:
        calls.append((method, base_url, path))
        return JSONResponse(status_code=200, content={"status": "success", "data": {"hits": []}})

    monkeypatch.setattr(routes, "forward", fake_forward)
    response = client.post("/api/rag/search", json={"query": "varianza"})

    assert response.status_code == 200
    assert calls == [("POST", routes.RAG_URL, "/search")]


def test_ai_chat_streams_raw_events(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str, dict[str, object]]] = []

    async def fake_stream(
        base_url: str, path: str, payload: dict[str, object]
    ) -> AsyncIterator[bytes]:
        calls.append((base_url, path, payload))
        yield b'event: token\ndata: {"delta": "La varianza"}\n\n'
        yield b'event: done\ndata: {"model": null, "citations": 0}\n\n'

    monkeypatch.setattr(routes, "stream", fake_stream)
    response = client.post("/api/ai/chat", json={"question": "cos'è la varianza?"})

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")
    assert "La varianza" in response.text
    assert calls == [
        (
            routes.AI_URL,
            "/chat",
            {"question": "cos'è la varianza?", "document_id": None, "limit": 5},
        )
    ]


def test_ai_models_forwards(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str]] = []

    async def fake_forward(
        method: str, base_url: str, path: str, payload: dict[str, object] | None = None
    ) -> JSONResponse:
        calls.append((method, path))
        return JSONResponse(status_code=200, content={"status": "success", "data": []})

    monkeypatch.setattr(routes, "forward", fake_forward)
    response = client.get("/api/ai/models")

    assert response.status_code == 200
    assert calls == [("GET", "/models")]


def test_chunks_forward_to_document(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, str, str]] = []

    async def fake_forward(
        method: str, base_url: str, path: str, payload: dict[str, object] | None = None
    ) -> JSONResponse:
        calls.append((method, base_url, path))
        return JSONResponse(
            status_code=200,
            content={"status": "success", "data": {"document_id": "d1", "chunks": []}},
        )

    monkeypatch.setattr(routes, "forward", fake_forward)
    response = client.get("/api/documents/d1/chunks")

    assert response.status_code == 200
    assert calls == [("GET", routes.DOCUMENT_URL, "/documents/d1/chunks")]


def test_api_requires_token() -> None:
    os.environ["NOESIS_TOKEN"] = "secret"
    response = client.post("/api/rag/search", json={"query": "varianza"})
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_ready_reports_degraded(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_check(base_url: str, name: str) -> tuple[str, str]:
        return name, "unavailable" if name == "rag" else "healthy"

    monkeypatch.setattr(routes, "check", fake_check)
    response = client.get("/ready")

    assert response.status_code == 503
    assert response.json()["data"] == {"document": "healthy", "rag": "unavailable"}


def test_cors_allows_frontend_origin() -> None:
    response = client.options(
        "/api/documents",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:5173"


def test_health() -> None:
    assert client.get("/health").json()["data"]["status"] == "healthy"
