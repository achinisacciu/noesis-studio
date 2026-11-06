from fastapi import APIRouter, Depends
from noesis_contracts import ApiResponse, HealthStatus, SearchRequest, SearchResponse

from app.client import fetch_document
from app.core.security import require_token
from app.search import extract_hits

router = APIRouter()


@router.get("/health", response_model=ApiResponse[HealthStatus])
@router.get("/ready", response_model=ApiResponse[HealthStatus])
async def health() -> ApiResponse[HealthStatus]:
    return ApiResponse(data=HealthStatus(status="healthy", service="rag-service"))


@router.post(
    "/search", response_model=ApiResponse[SearchResponse], dependencies=[Depends(require_token)]
)
async def search(payload: SearchRequest) -> ApiResponse[SearchResponse]:
    document = await fetch_document(payload.document_id)
    return ApiResponse(
        data=SearchResponse(
            document_id=document.id, hits=extract_hits(payload.query, document.text)
        )
    )
