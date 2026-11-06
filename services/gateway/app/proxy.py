import os

import httpx
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def _headers() -> dict[str, str]:
    token = os.getenv("NOESIS_TOKEN")
    return {"Authorization": f"Bearer {token}"} if token else {}


async def forward(
    method: str, base_url: str, path: str, payload: dict[str, object] | None = None
) -> JSONResponse:
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.request(
                method, f"{base_url}{path}", json=payload, headers=_headers()
            )
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="servizio non risponde in tempo") from None
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="servizio non disponibile") from None
    return JSONResponse(status_code=response.status_code, content=response.json())


async def forward_file(
    method: str,
    base_url: str,
    path: str,
    filename: str,
    content: bytes,
    content_type: str,
) -> JSONResponse:
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.request(
                method,
                f"{base_url}{path}",
                files={"file": (filename, content, content_type)},
                headers=_headers(),
            )
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="import non completato in tempo") from None
    except httpx.HTTPError:
        raise HTTPException(status_code=502, detail="document service non disponibile") from None
    return JSONResponse(status_code=response.status_code, content=response.json())


async def check(base_url: str, name: str) -> tuple[str, str]:
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.get(f"{base_url}/ready")
    except httpx.HTTPError:
        return name, "unavailable"
    return name, "healthy" if response.status_code == 200 else "degraded"
