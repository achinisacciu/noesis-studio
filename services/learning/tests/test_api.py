import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import routes
from app.main import app
from app.store import Store

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_state(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(routes, "store", Store(tmp_path / "learning.db"))
    os.environ.pop("NOESIS_TOKEN", None)


def create_card(document_id: str = "d1") -> dict[str, object]:
    response = client.post(
        "/flashcards",
        json={
            "document_id": document_id,
            "front": "Che cosa misura la varianza?",
            "back": "La dispersione dei valori rispetto alla media.",
            "page": None,
            "section": "Varianza",
        },
    )
    assert response.status_code == 200
    return response.json()["data"]


def test_create_list_update_and_delete() -> None:
    card = create_card()
    assert card["section"] == "Varianza"
    assert card["front"].startswith("Che cosa")

    listed = client.get("/flashcards")
    assert listed.status_code == 200
    assert [item["id"] for item in listed.json()["data"]["cards"]] == [card["id"]]

    updated = client.patch(
        f"/flashcards/{card['id']}",
        json={"back": "La media degli scarti al quadrato."},
    )
    assert updated.status_code == 200
    assert updated.json()["data"]["back"] == "La media degli scarti al quadrato."
    assert updated.json()["data"]["front"] == card["front"]

    deleted = client.delete(f"/flashcards/{card['id']}")
    assert deleted.status_code == 200
    assert client.get("/flashcards").json()["data"]["cards"] == []


def test_filter_and_delete_by_document() -> None:
    first = create_card("d1")
    create_card("d2")

    filtered = client.get("/flashcards", params={"document_id": "d1"})
    assert [item["id"] for item in filtered.json()["data"]["cards"]] == [first["id"]]

    removed = client.delete("/flashcards", params={"document_id": "d1"})
    assert removed.status_code == 200
    assert removed.json()["data"] == {"deleted": 1}
    assert client.get("/flashcards").json()["data"]["cards"][0]["document_id"] == "d2"


def test_missing_card_returns_404() -> None:
    assert client.patch("/flashcards/nope", json={"front": "x"}).status_code == 404
    assert client.delete("/flashcards/nope").status_code == 404


def test_rejects_invalid_payload() -> None:
    response = client.post(
        "/flashcards",
        json={"document_id": "d1", "front": "", "back": "testo"},
    )
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_rejects_missing_token() -> None:
    os.environ["NOESIS_TOKEN"] = "secret"
    response = client.post(
        "/flashcards",
        json={"document_id": "d1", "front": "domanda", "back": "risposta"},
    )
    assert response.status_code == 401


def test_health_and_ready() -> None:
    for path in ("/health", "/ready"):
        response = client.get(path)
        assert response.status_code == 200
        assert response.json()["data"]["status"] == "healthy"
