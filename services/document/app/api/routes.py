from fastapi import APIRouter, Depends, HTTPException
from noesis_contracts import ApiResponse, Document, DocumentCreate, HealthStatus

from app.core.security import require_token
from app.store import store

router = APIRouter()


@router.get("/health", response_model=ApiResponse[HealthStatus])
@router.get("/ready", response_model=ApiResponse[HealthStatus])
async def health() -> ApiResponse[HealthStatus]:
    return ApiResponse(data=HealthStatus(status="healthy", service="document-service"))


@router.post(
    "/documents", response_model=ApiResponse[Document], dependencies=[Depends(require_token)]
)
async def create_document(payload: DocumentCreate) -> ApiResponse[Document]:
    return ApiResponse(data=store.save(payload))


@router.get(
    "/documents/{document_id}",
    response_model=ApiResponse[Document],
    dependencies=[Depends(require_token)],
)
async def get_document(document_id: str) -> ApiResponse[Document]:
    document = store.get(document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="documento non trovato")
    return ApiResponse(data=document)
