from fastapi import APIRouter, Depends
from fastapi import Path as PathParam
from noesis_contracts import (
    ApiResponse,
    HealthStatus,
    IndexRequest,
    IndexResponse,
    RebuildResponse,
    SearchRequest,
    SearchResponse,
)

from app.client import fetch_chunks, list_documents
from app.core.security import require_token
from app.index import DATA_DIR, ChromaIndex, Index

index: Index = ChromaIndex(DATA_DIR / "chromadb")

router = APIRouter()
api = APIRouter(dependencies=[Depends(require_token)])


@router.get("/health", response_model=ApiResponse[HealthStatus])
@router.get("/ready", response_model=ApiResponse[HealthStatus])
async def health() -> ApiResponse[HealthStatus]:
    return ApiResponse(data=HealthStatus(status="healthy", service="rag-service"))


@api.post("/index", response_model=ApiResponse[IndexResponse])
async def index_document(payload: IndexRequest) -> ApiResponse[IndexResponse]:
    chunks = await fetch_chunks(payload.document_id)
    index.replace(chunks)
    return ApiResponse(data=IndexResponse(document_id=payload.document_id, chunks=len(chunks)))


@api.delete("/index/{document_id}", response_model=ApiResponse[dict[str, str]])
async def delete_index(
    document_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> ApiResponse[dict[str, str]]:
    index.delete(document_id)
    return ApiResponse(data={"id": document_id})


@api.post("/index/rebuild", response_model=ApiResponse[RebuildResponse])
async def rebuild() -> ApiResponse[RebuildResponse]:
    documents = await list_documents()
    index.reset()
    total = 0
    for document in documents:
        chunks = await fetch_chunks(document.id)
        index.replace(chunks)
        total += len(chunks)
    return ApiResponse(data=RebuildResponse(documents=len(documents), chunks=total))


@api.post("/search", response_model=ApiResponse[SearchResponse])
async def search(payload: SearchRequest) -> ApiResponse[SearchResponse]:
    hits = index.search(payload.query, payload.limit, payload.document_id)
    return ApiResponse(data=SearchResponse(query=payload.query, hits=hits))
