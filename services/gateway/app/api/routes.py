import asyncio
import os
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile
from fastapi import Path as PathParam
from fastapi.responses import JSONResponse, StreamingResponse
from noesis_contracts import (
    ApiResponse,
    FlashcardCreate,
    FlashcardUpdate,
    HealthStatus,
    SearchRequest,
    TutorRequest,
)

from app.core.security import require_token
from app.proxy import check, forward, forward_file, stream

DOCUMENT_URL = os.getenv("DOCUMENT_URL", "http://127.0.0.1:8002")
RAG_URL = os.getenv("RAG_URL", "http://127.0.0.1:8003")
AI_URL = os.getenv("AI_URL", "http://127.0.0.1:8004")
LEARNING_URL = os.getenv("LEARNING_URL", "http://127.0.0.1:8005")

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
async def import_document(file: Annotated[UploadFile, File()]) -> JSONResponse:
    filename = Path(file.filename or "").name
    if not filename:
        raise HTTPException(status_code=422, detail="nome file mancante")
    content = await file.read()
    return await forward_file(
        "POST",
        DOCUMENT_URL,
        "/documents",
        filename=filename,
        content=content,
        content_type=file.content_type or "application/octet-stream",
    )


@api.get("/api/documents")
async def list_documents() -> JSONResponse:
    return await forward("GET", DOCUMENT_URL, "/documents")


@api.get("/api/documents/{document_id}")
async def get_document(
    document_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> JSONResponse:
    return await forward("GET", DOCUMENT_URL, f"/documents/{document_id}")


@api.get("/api/documents/{document_id}/chunks")
async def get_document_chunks(
    document_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> JSONResponse:
    return await forward("GET", DOCUMENT_URL, f"/documents/{document_id}/chunks")


@api.delete("/api/documents/{document_id}")
async def delete_document(
    document_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> JSONResponse:
    # indice e schede sono derivati: vanno ripuliti prima, altrimenti restano riferimenti orfani
    indexed = await forward("DELETE", RAG_URL, f"/index/{document_id}")
    if indexed.status_code >= 500:
        raise HTTPException(status_code=502, detail="indice non ripulito, documento non eliminato")
    cards = await forward("DELETE", LEARNING_URL, f"/flashcards?document_id={document_id}")
    if cards.status_code >= 500:
        raise HTTPException(status_code=502, detail="schede non ripulite, documento non eliminato")
    return await forward("DELETE", DOCUMENT_URL, f"/documents/{document_id}")


@api.post("/api/index/rebuild")
async def rebuild_index() -> JSONResponse:
    return await forward("POST", RAG_URL, "/index/rebuild")


@api.post("/api/index/{document_id}")
async def index_document(
    document_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> JSONResponse:
    return await forward("POST", RAG_URL, "/index", {"document_id": document_id})


@api.post("/api/rag/search")
async def rag_search(payload: SearchRequest) -> JSONResponse:
    return await forward("POST", RAG_URL, "/search", payload.model_dump(mode="json"))


@api.get("/api/flashcards")
async def list_flashcards(
    document_id: str | None = Query(default=None, pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> JSONResponse:
    path = "/flashcards"
    if document_id:
        path += f"?document_id={document_id}"
    return await forward("GET", LEARNING_URL, path)


@api.post("/api/flashcards")
async def create_flashcard(payload: FlashcardCreate) -> JSONResponse:
    return await forward(
        "POST", LEARNING_URL, "/flashcards", payload.model_dump(mode="json", exclude_none=True)
    )


@api.patch("/api/flashcards/{card_id}")
async def update_flashcard(
    payload: FlashcardUpdate,
    card_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> JSONResponse:
    return await forward(
        "PATCH",
        LEARNING_URL,
        f"/flashcards/{card_id}",
        payload.model_dump(mode="json", exclude_none=True),
    )


@api.delete("/api/flashcards/{card_id}")
async def delete_flashcard(
    card_id: str = PathParam(pattern=r"^[A-Za-z0-9_-]{1,64}$"),
) -> JSONResponse:
    return await forward("DELETE", LEARNING_URL, f"/flashcards/{card_id}")


@api.get("/api/ai/models")
async def ai_models() -> JSONResponse:
    return await forward("GET", AI_URL, "/models")


@api.post("/api/ai/chat")
async def ai_chat(payload: TutorRequest) -> StreamingResponse:
    return StreamingResponse(
        stream(AI_URL, "/chat", payload.model_dump(mode="json")),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
