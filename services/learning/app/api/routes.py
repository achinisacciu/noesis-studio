import os
import uuid
from datetime import UTC, datetime
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi import Path as PathParam
from noesis_contracts import (
    ApiResponse,
    Flashcard,
    FlashcardCreate,
    FlashcardList,
    FlashcardUpdate,
    HealthStatus,
    ReadingPosition,
    ReadingPositionState,
    ReadingPositionUpdate,
)

from app.core.security import require_token
from app.store import Store

DATA_DIR = Path(os.getenv("NOESIS_DATA") or Path(__file__).resolve().parents[3] / "data")
store = Store(DATA_DIR / "sqlite" / "learning.db")

router = APIRouter()
api = APIRouter(dependencies=[Depends(require_token)])

DOCUMENT_PATTERN = r"^[A-Za-z0-9_-]{1,64}$"
CARD_PATTERN = r"^[A-Za-z0-9_-]{1,64}$"


@router.get("/health", response_model=ApiResponse[HealthStatus])
@router.get("/ready", response_model=ApiResponse[HealthStatus])
async def health() -> ApiResponse[HealthStatus]:
    return ApiResponse(data=HealthStatus(status="healthy", service="learning-service"))


@api.get("/flashcards", response_model=ApiResponse[FlashcardList])
async def list_flashcards(
    document_id: str | None = Query(default=None, pattern=DOCUMENT_PATTERN),
) -> ApiResponse[FlashcardList]:
    return ApiResponse(data=FlashcardList(cards=store.list(document_id)))


@api.post("/flashcards", response_model=ApiResponse[Flashcard])
async def create_flashcard(payload: FlashcardCreate) -> ApiResponse[Flashcard]:
    return ApiResponse(data=store.create(uuid.uuid4().hex, payload, datetime.now(UTC)))


@api.patch("/flashcards/{card_id}", response_model=ApiResponse[Flashcard])
async def update_flashcard(
    payload: FlashcardUpdate,
    card_id: str = PathParam(pattern=CARD_PATTERN),
) -> ApiResponse[Flashcard]:
    card = store.update(card_id, payload)
    if card is None:
        raise HTTPException(status_code=404, detail="scheda non trovata")
    return ApiResponse(data=card)


@api.delete("/flashcards/{card_id}", response_model=ApiResponse[dict[str, str]])
async def delete_flashcard(
    card_id: str = PathParam(pattern=CARD_PATTERN),
) -> ApiResponse[dict[str, str]]:
    if not store.delete(card_id):
        raise HTTPException(status_code=404, detail="scheda non trovata")
    return ApiResponse(data={"id": card_id})


@api.delete("/flashcards", response_model=ApiResponse[dict[str, int]])
async def delete_document_flashcards(
    document_id: str = Query(pattern=DOCUMENT_PATTERN),
) -> ApiResponse[dict[str, int]]:
    return ApiResponse(data={"deleted": store.delete_for_document(document_id)})


@api.get("/reading-positions/{document_id}", response_model=ApiResponse[ReadingPositionState])
async def get_reading_position(
    document_id: str = PathParam(pattern=DOCUMENT_PATTERN),
) -> ApiResponse[ReadingPositionState]:
    return ApiResponse(data=ReadingPositionState(position=store.reading_position(document_id)))


@api.put("/reading-positions/{document_id}", response_model=ApiResponse[ReadingPosition])
async def save_reading_position(
    payload: ReadingPositionUpdate,
    document_id: str = PathParam(pattern=DOCUMENT_PATTERN),
) -> ApiResponse[ReadingPosition]:
    return ApiResponse(data=store.save_reading_position(document_id, payload, datetime.now(UTC)))


@api.delete("/reading-positions/{document_id}", response_model=ApiResponse[dict[str, int]])
async def delete_reading_position(
    document_id: str = PathParam(pattern=DOCUMENT_PATTERN),
) -> ApiResponse[dict[str, int]]:
    return ApiResponse(data={"deleted": store.delete_reading_position(document_id)})
