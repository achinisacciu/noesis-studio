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
    store = Store(tmp_path / "documents.db", tmp_path / "files")
    monkeypatch.setattr(routes, "store", store)
    os.environ.pop("NOESIS_TOKEN", None)


def import_markdown() -> dict[str, object]:
    response = client.post(
        "/documents",
        files={
            "file": (
                "statistica.md",
                b"# Varianza\n\nLa varianza misura la dispersione dei dati.",
                "text/markdown",
            )
        },
    )
    assert response.status_code == 200
    return response.json()["data"]


def test_import_list_get_chunks_and_delete() -> None:
    document = import_markdown()
    assert document["title"] == "statistica"
    assert document["chunk_count"] == 1

    listed = client.get("/documents")
    assert listed.status_code == 200
    assert [item["id"] for item in listed.json()["data"]] == [document["id"]]

    fetched = client.get(f"/documents/{document['id']}")
    assert fetched.status_code == 200
    assert fetched.json()["data"]["filename"] == "statistica.md"

    chunks = client.get(f"/documents/{document['id']}/chunks")
    assert chunks.status_code == 200
    chunk = chunks.json()["data"]["chunks"][0]
    assert chunk["section"] == "Varianza"
    assert chunk["document_id"] == document["id"]

    deleted = client.delete(f"/documents/{document['id']}")
    assert deleted.status_code == 200
    assert client.get(f"/documents/{document['id']}").status_code == 404


def test_pdf_page_and_section_are_preserved(tmp_path: Path) -> None:
    """Il parser PDF deve produrre citazioni con il numero di pagina."""
    import pymupdf

    path = tmp_path / "dispense.pdf"
    pdf = pymupdf.open()
    page = pdf.new_page()
    page.insert_text((72, 72), "La media e il valore centrale dei dati.")
    pdf.save(path)
    pdf.close()

    response = client.post(
        "/documents",
        files={"file": ("dispense.pdf", path.read_bytes(), "application/pdf")},
    )
    assert response.status_code == 200
    document = response.json()["data"]
    chunks = client.get(f"/documents/{document['id']}/chunks").json()["data"]["chunks"]
    assert chunks[0]["page"] == 1


def test_rejects_unsupported_format() -> None:
    response = client.post("/documents", files={"file": ("dati.csv", b"a,b\n1,2", "text/csv")})
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_rejects_file_without_text() -> None:
    response = client.post("/documents", files={"file": ("vuoto.md", b"   \n\n", "text/markdown")})
    assert response.status_code == 422


def test_rejects_oversized_file(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(routes, "MAX_BYTES", 10)
    response = client.post("/documents", files={"file": ("lungo.md", b"x" * 11, "text/markdown")})
    assert response.status_code == 413
    assert response.json()["error"]["code"] == "RESOURCE_LIMIT"


def test_rejects_missing_token() -> None:
    os.environ["NOESIS_TOKEN"] = "secret"
    response = client.post("/documents", files={"file": ("x.md", b"testo", "text/markdown")})
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_missing_document_returns_envelope() -> None:
    response = client.get("/documents/nope")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_health_and_ready() -> None:
    for path in ("/health", "/ready"):
        response = client.get(path)
        assert response.status_code == 200
        assert response.json()["data"]["status"] == "healthy"
