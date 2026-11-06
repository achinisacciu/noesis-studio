import os

import httpx
from fastapi import HTTPException
from noesis_contracts import ApiResponse, SearchHit, SearchRequest, SearchResponse

RAG_URL = os.getenv("RAG_URL", "http://127.0.0.1:8003")


def _headers() -> dict[str, str]:
    token = os.getenv("NOESIS_TOKEN")
    return {"Authorization": f"Bearer {token}"} if token else {}


async def search(query: str, document_id: str | None, limit: int) -> list[SearchHit]:
    payload = SearchRequest(query=query, document_id=document_id, limit=limit)
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                f"{RAG_URL}/search",
                json=payload.model_dump(mode="json"),
                headers=_headers(),
            )
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="ricerca non completata in tempo") from None
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="rag service non disponibile") from None

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="ricerca non disponibile")

    body = ApiResponse[SearchResponse].model_validate(response.json())
    if body.data is None:
        raise HTTPException(status_code=502, detail="risposta di ricerca non valida")
    return body.data.hits
