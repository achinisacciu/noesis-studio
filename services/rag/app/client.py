import os

import httpx
from fastapi import HTTPException
from noesis_contracts import ApiResponse, Document

DOCUMENT_URL = os.getenv("DOCUMENT_URL", "http://127.0.0.1:8002")


async def fetch_document(document_id: str) -> Document:
    token = os.getenv("NOESIS_TOKEN")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{DOCUMENT_URL}/documents/{document_id}", headers=headers)
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

    payload = ApiResponse[Document].model_validate(response.json())
    if payload.data is None:
        raise HTTPException(status_code=502, detail="document service non ha restituito dati")
    return payload.data
