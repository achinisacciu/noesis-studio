import os

import httpx
from fastapi import HTTPException
from fastapi.responses import JSONResponse


async def forward(
    method: str, base_url: str, path: str, payload: dict[str, object] | None = None
) -> JSONResponse:
    token = os.getenv("NOESIS_TOKEN")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.request(
                method, f"{base_url}{path}", json=payload, headers=headers
            )
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="servizio non risponde in tempo") from None
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="servizio non disponibile") from None
    return JSONResponse(status_code=response.status_code, content=response.json())


async def check(base_url: str, name: str) -> tuple[str, str]:
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.get(f"{base_url}/ready")
    except httpx.HTTPError:
        return name, "unavailable"
    return name, "healthy" if response.status_code == 200 else "degraded"
