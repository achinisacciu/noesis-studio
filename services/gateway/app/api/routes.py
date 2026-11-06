import asyncio
import os

from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from noesis_contracts import ApiResponse, DocumentCreate, HealthStatus, SearchRequest

from app.core.security import require_token
from app.proxy import check, forward

DOCUMENT_URL = os.getenv("DOCUMENT_URL", "http://127.0.0.1:8002")
RAG_URL = os.getenv("RAG_URL", "http://127.0.0.1:8003")

router = APIRouter()
api = APIRouter(dependencies=[Depends(require_token)])


@router.get("/health", response_model=ApiResponse[HealthStatus])
async def health() -> ApiResponse[HealthStatus]:
    return ApiResponse(data=HealthStatus(status="healthy", service="gateway"))


@router.get("/ready")
async def ready() -> JSONResponse:
    services = dict(await asyncio.gather(check(DOCUMENT_URL, "document"), check(RAG_URL, "rag")))
    healthy = all(status == "healthy" for status in services.values())
    body = ApiResponse[dict[str, str]](data=services)
    return JSONResponse(
        status_code=200 if healthy else 503,
        content=body.model_dump(mode="json"),
    )


@api.post("/api/documents")
async def create_document(payload: DocumentCreate) -> JSONResponse:
    return await forward("POST", DOCUMENT_URL, "/documents", payload.model_dump(mode="json"))


@api.get("/api/documents/{document_id}")
async def get_document(
    document_id: str = Path(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> JSONResponse:
    return await forward("GET", DOCUMENT_URL, f"/documents/{document_id}")


@api.post("/api/rag/search")
async def rag_search(payload: SearchRequest) -> JSONResponse:
    return await forward("POST", RAG_URL, "/search", payload.model_dump(mode="json"))
