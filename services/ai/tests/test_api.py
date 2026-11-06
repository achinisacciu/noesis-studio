import asyncio
import json
import os
from collections.abc import AsyncIterator

import pytest
from fastapi.testclient import TestClient
from noesis_ai_adapters import AdapterError, ChatChunk, ChatRequest, ModelInfo
from noesis_contracts import HealthStatus, SearchHit, TutorRequest

from app.api import routes
from app.main import app

client = TestClient(app)

HIT = SearchHit(
    document_id="doc1",
    text="La varianza misura la dispersione dei dati.",
    page=2,
    section="Varianza",
    score=0.81,
)


class FakeAdapter:
    def __init__(self, error: AdapterError | None = None) -> None:
        self.error = error
        self.calls = 0
        self.aborted: list[str] = []

    async def list_models(self) -> list[ModelInfo]:
        return [ModelInfo(id="fake:1", capabilities={"chat"})]

    async def chat(self, req: ChatRequest) -> AsyncIterator[ChatChunk]:
        self.calls += 1
        if self.error is not None:
            raise self.error
        yield ChatChunk(delta="La varianza ")
        yield ChatChunk(delta="misura la dispersione.")
        yield ChatChunk(delta="", finish_reason="stop")

    async def abort(self, request_id: str) -> None:
        self.aborted.append(request_id)

    async def health(self) -> HealthStatus:
        return HealthStatus(status="healthy", service="fake")


def parse_events(text: str) -> list[tuple[str, dict[str, object]]]:
    events: list[tuple[str, dict[str, object]]] = []
    for block in text.strip().split("\n\n"):
        lines = block.splitlines()
        event = next(line[7:] for line in lines if line.startswith("event: "))
        data = json.loads(next(line[6:] for line in lines if line.startswith("data: ")))
        events.append((event, data))
    return events


@pytest.fixture(autouse=True)
def clean_state(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(routes, "adapter", FakeAdapter())
    os.environ.pop("NOESIS_TOKEN", None)


def test_chat_streams_citations_and_tokens(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_search(query: str, document_id: str | None, limit: int) -> list[SearchHit]:
        assert query == "cos'è la varianza?"
        return [HIT]

    monkeypatch.setattr(routes, "search", fake_search)
    response = client.post("/chat", json={"question": "cos'è la varianza?"})

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")
    events = parse_events(response.text)
    assert [name for name, _ in events] == ["citation", "token", "token", "done"]
    assert events[0][1]["citation"]["section"] == "Varianza"
    assert events[0][1]["citation"]["page"] == 2
    assert events[1][1]["delta"] + events[2][1]["delta"] == "La varianza misura la dispersione."
    assert events[3][1]["citations"] == 1


def test_chat_without_sources_does_not_call_model(monkeypatch: pytest.MonkeyPatch) -> None:
    async def fake_search(query: str, document_id: str | None, limit: int) -> list[SearchHit]:
        return []

    monkeypatch.setattr(routes, "search", fake_search)
    response = client.post("/chat", json={"question": "domanda senza fonti"})

    events = parse_events(response.text)
    assert [name for name, _ in events] == ["token", "done"]
    assert "Nessuna fonte" in events[0][1]["delta"]
    assert events[1][1]["citations"] == 0
    assert isinstance(routes.adapter, FakeAdapter)
    assert routes.adapter.calls == 0


def test_chat_reports_adapter_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        routes,
        "adapter",
        FakeAdapter(error=AdapterError("modello non disponibile", "SERVICE_UNAVAILABLE")),
    )

    async def fake_search(query: str, document_id: str | None, limit: int) -> list[SearchHit]:
        return [HIT]

    monkeypatch.setattr(routes, "search", fake_search)
    response = client.post("/chat", json={"question": "varianza"})

    events = parse_events(response.text)
    assert events[-1][0] == "error"
    assert events[-1][1]["code"] == "SERVICE_UNAVAILABLE"


def test_client_disconnect_aborts_generation(monkeypatch: pytest.MonkeyPatch) -> None:
    adapter = FakeAdapter()
    monkeypatch.setattr(routes, "adapter", adapter)

    async def fake_search(query: str, document_id: str | None, limit: int) -> list[SearchHit]:
        return [HIT]

    monkeypatch.setattr(routes, "search", fake_search)

    async def scenario() -> None:
        generator = routes.events(TutorRequest(question="varianza"), "req-1")
        await generator.__anext__()  # citation
        await generator.__anext__()  # primo token, poi il client si disconnette
        await generator.aclose()

    asyncio.run(scenario())
    assert adapter.aborted == ["req-1"]


def test_models_returns_adapter_models() -> None:
    response = client.get("/models")
    assert response.status_code == 200
    assert response.json()["data"] == [{"id": "fake:1", "capabilities": ["chat"]}]


def test_health_and_ready() -> None:
    for path in ("/health", "/ready"):
        response = client.get(path)
        assert response.status_code == 200
        assert response.json()["data"]["status"] == "healthy"


def test_chat_requires_token() -> None:
    os.environ["NOESIS_TOKEN"] = "secret"
    response = client.post("/chat", json={"question": "varianza"})
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_chat_validates_empty_question() -> None:
    response = client.post("/chat", json={"question": ""})
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"
