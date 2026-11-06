import os
import shutil
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi import Path as PathParam
from noesis_contracts import (
    ApiResponse,
    DocumentChunks,
    DocumentSummary,
    HealthStatus,
)

from app.core.security import require_token
from app.parsing import PARSERS, chunk_blocks
from app.store import Store

MAX_BYTES = 50 * 1024 * 1024

DATA_DIR = Path(os.getenv("NOESIS_DATA") or Path(__file__).resolve().parents[3] / "data")
store = Store(DATA_DIR / "sqlite" / "documents.db", DATA_DIR / "files")

router = APIRouter()
api = APIRouter(dependencies=[Depends(require_token)])


@router.get("/health", response_model=ApiResponse[HealthStatus])
@router.get("/ready", response_model=ApiResponse[HealthStatus])
async def health() -> ApiResponse[HealthStatus]:
    return ApiResponse(data=HealthStatus(status="healthy", service="document-service"))


@api.post("/documents", response_model=ApiResponse[DocumentSummary])
async def import_document(
    file: Annotated[UploadFile, File()],
) -> ApiResponse[DocumentSummary]:
    filename = Path(file.filename or "").name
    parser = PARSERS.get(Path(filename).suffix.lower())
    if not filename or parser is None:
        raise HTTPException(
            status_code=422, detail="formato non supportato: usa PDF, DOCX, MD o TXT"
        )

    content = await file.read()
    if len(content) > MAX_BYTES:
        raise HTTPException(status_code=413, detail="file oltre i 50 MB")

    document_id = uuid.uuid4().hex
    target_dir = store.files_dir / document_id
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / filename
    target.write_bytes(content)

    try:
        chunks = chunk_blocks(document_id, parser(target))
    except Exception as error:
        shutil.rmtree(target_dir, ignore_errors=True)
        raise HTTPException(status_code=422, detail="file non leggibile") from error

    if not chunks:
        shutil.rmtree(target_dir, ignore_errors=True)
        raise HTTPException(status_code=422, detail="nessun testo estraibile dal file")

    created = store.create(
        document_id=document_id,
        title=Path(filename).stem,
        filename=filename,
        created_at=datetime.now(UTC),
        chunks=chunks,
    )
    return ApiResponse(data=created)


@api.get("/documents", response_model=ApiResponse[list[DocumentSummary]])
async def list_documents() -> ApiResponse[list[DocumentSummary]]:
    return ApiResponse(data=store.list_documents())


@api.get("/documents/{document_id}", response_model=ApiResponse[DocumentSummary])
async def get_document(
    document_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> ApiResponse[DocumentSummary]:
    document = store.get(document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="documento non trovato")
    return ApiResponse(data=document)


@api.get("/documents/{document_id}/chunks", response_model=ApiResponse[DocumentChunks])
async def get_chunks(
    document_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> ApiResponse[DocumentChunks]:
    if store.get(document_id) is None:
        raise HTTPException(status_code=404, detail="documento non trovato")
    return ApiResponse(
        data=DocumentChunks(document_id=document_id, chunks=store.chunks(document_id))
    )


@api.delete("/documents/{document_id}", response_model=ApiResponse[dict[str, str]])
async def delete_document(
    document_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> ApiResponse[dict[str, str]]:
    if not store.delete(document_id):
        raise HTTPException(status_code=404, detail="documento non trovato")
    return ApiResponse(data={"id": document_id})
