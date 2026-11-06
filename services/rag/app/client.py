import os

import httpx
from fastapi import HTTPException
from noesis_contracts import ApiResponse, Chunk, DocumentChunks, DocumentSummary

DOCUMENT_URL = os.getenv("DOCUMENT_URL", "http://127.0.0.1:8002")


def _headers() -> dict[str, str]:
    token = os.getenv("NOESIS_TOKEN")
    return {"Authorization": f"Bearer {token}"} if token else {}


async def _get(path: str) -> dict[str, object]:
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{DOCUMENT_URL}{path}", headers=_headers())
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504, detail="document service non risponde in tempo"
        ) from None
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="document service non disponibile") from None

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="documento non trovato")
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="document service ha risposto con errore")

    payload = response.json()
    if not isinstance(payload, dict):
        raise HTTPException(status_code=502, detail="risposta non valida dal document service")
    return payload


async def list_documents() -> list[DocumentSummary]:
    payload = ApiResponse[list[DocumentSummary]].model_validate(await _get("/documents"))
    return payload.data or []


async def fetch_chunks(document_id: str) -> list[Chunk]:
    payload = ApiResponse[DocumentChunks].model_validate(
        await _get(f"/documents/{document_id}/chunks")
    )
    if payload.data is None:
        raise HTTPException(status_code=502, detail="document service non ha restituito chunk")
    return payload.data.chunks
