import os

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.store import store

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_state() -> None:
    store.clear()
    os.environ.pop("NOESIS_TOKEN", None)


def test_create_and_get_document() -> None:
    created = client.post(
        "/documents",
        json={"title": "Statistica", "text": "La varianza misura la dispersione."},
    )
    assert created.status_code == 200
    body = created.json()
    assert body["status"] == "success"
    document = body["data"]

    fetched = client.get(f"/documents/{document['id']}")
    assert fetched.status_code == 200
    assert fetched.json()["data"]["title"] == "Statistica"


def test_rejects_missing_token() -> None:
    os.environ["NOESIS_TOKEN"] = "secret"
    response = client.post("/documents", json={"title": "x", "text": "y"})
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_missing_document_returns_envelope() -> None:
    response = client.get("/documents/nope")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_validation_error_returns_envelope() -> None:
    response = client.post("/documents", json={"title": "", "text": ""})
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_health_and_ready() -> None:
    for path in ("/health", "/ready"):
        response = client.get(path)
        assert response.status_code == 200
        assert response.json()["data"]["status"] == "healthy"
