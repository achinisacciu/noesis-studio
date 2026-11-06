import os
import uuid
from collections.abc import AsyncIterator

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from noesis_ai_adapters import AdapterError, ChatRequest, ModelInfo, OllamaAdapter, RuntimeAdapter
from noesis_contracts import (
    ApiResponse,
    CitationEvent,
    DoneEvent,
    ErrorEvent,
    HealthStatus,
    TokenEvent,
    TutorRequest,
)

from app.client import search
from app.core.security import require_token
from app.prompt import build_messages, citations_from_hits
from app.sse import format_event

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
MODEL = os.getenv("NOESIS_MODEL", "qwen3.5:0.8b")

adapter: RuntimeAdapter = OllamaAdapter(OLLAMA_URL)

router = APIRouter()
api = APIRouter(dependencies=[Depends(require_token)])


@router.get("/health", response_model=ApiResponse[HealthStatus])
async def health() -> ApiResponse[HealthStatus]:
    return ApiResponse(data=HealthStatus(status="healthy", service="ai-service"))


@router.get("/ready")
async def ready() -> ApiResponse[HealthStatus]:
    return ApiResponse(data=await adapter.health())


@api.get("/models", response_model=ApiResponse[list[ModelInfo]])
async def list_models() -> ApiResponse[list[ModelInfo]]:
    return ApiResponse(data=await adapter.list_models())


async def events(payload: TutorRequest, request_id: str) -> AsyncIterator[str]:
    hits = await search(payload.question, payload.document_id, payload.limit)
    if not hits:
        yield format_event(
            "token",
            TokenEvent(
                delta="Nessuna fonte nei documenti: non posso rispondere senza citare una fonte."
            ),
        )
        yield format_event("done", DoneEvent(model=None, citations=0))
        return

    for citation in citations_from_hits(hits):
        yield format_event("citation", CitationEvent(citation=citation))

    request = ChatRequest(
        model=MODEL,
        messages=build_messages(payload.question, hits),
        request_id=request_id,
    )
    try:
        async for chunk in adapter.chat(request):
            if chunk.delta:
                yield format_event("token", TokenEvent(delta=chunk.delta))
    except AdapterError as error:
        yield format_event("error", ErrorEvent(code=error.code, message=str(error)))
        return
    finally:
        await adapter.abort(request_id)

    yield format_event("done", DoneEvent(model=MODEL, citations=len(hits)))


@api.post("/chat")
async def chat(payload: TutorRequest) -> StreamingResponse:
    request_id = uuid.uuid4().hex
    return StreamingResponse(
        events(payload, request_id),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
