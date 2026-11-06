from datetime import datetime
from typing import Generic, Literal, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")

ErrorCode = Literal[
    "VALIDATION_ERROR",
    "SERVICE_UNAVAILABLE",
    "TIMEOUT",
    "RESOURCE_LIMIT",
    "INTERNAL_ERROR",
    "DEPENDENCY_ERROR",
]


class ApiError(BaseModel):
    code: ErrorCode
    message: str
    request_id: str | None = None


class ApiResponse(BaseModel, Generic[T]):
    status: Literal["success", "error"] = "success"
    data: T | None = None
    error: ApiError | None = None


class HealthStatus(BaseModel):
    status: Literal["healthy", "degraded", "unavailable"]
    service: str


class DocumentSummary(BaseModel):
    id: str
    title: str
    filename: str
    created_at: datetime
    chunk_count: int


class Chunk(BaseModel):
    id: str
    document_id: str
    position: int
    text: str
    page: int | None = None
    section: str | None = None


class DocumentChunks(BaseModel):
    document_id: str
    chunks: list[Chunk]


AnnotationKind = Literal["highlight", "note", "bookmark"]


class Annotation(BaseModel):
    id: str
    document_id: str
    chunk_id: str
    kind: AnnotationKind
    start: int
    end: int
    note: str
    created_at: datetime


class AnnotationCreate(BaseModel):
    chunk_id: str = Field(min_length=1, max_length=128)
    kind: AnnotationKind = "highlight"
    start: int = Field(default=0, ge=0)
    end: int = Field(default=0, ge=0)
    note: str = Field(default="", max_length=2000)


class AnnotationList(BaseModel):
    annotations: list[Annotation]


class IndexRequest(BaseModel):
    document_id: str


class IndexResponse(BaseModel):
    document_id: str
    chunks: int


class RebuildResponse(BaseModel):
    documents: int
    chunks: int


class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=500)
    document_id: str | None = None
    limit: int = Field(default=5, ge=1, le=20)


class SearchHit(BaseModel):
    document_id: str
    text: str
    page: int | None = None
    section: str | None = None
    score: float


class SearchResponse(BaseModel):
    query: str
    hits: list[SearchHit]


class Citation(BaseModel):
    document_id: str
    page: int | None = None
    section: str | None = None
    snippet: str


class TutorRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    document_id: str | None = None
    limit: int = Field(default=5, ge=1, le=20)


class TokenEvent(BaseModel):
    delta: str


class CitationEvent(BaseModel):
    citation: Citation


class DoneEvent(BaseModel):
    model: str | None = None
    citations: int = 0


class ErrorEvent(BaseModel):
    code: ErrorCode
    message: str


class Flashcard(BaseModel):
    id: str
    document_id: str
    front: str
    back: str
    page: int | None = None
    section: str | None = None
    created_at: datetime


class FlashcardCreate(BaseModel):
    document_id: str = Field(min_length=1, max_length=64)
    front: str = Field(min_length=1, max_length=2000)
    back: str = Field(min_length=1, max_length=8000)
    page: int | None = Field(default=None, ge=1)
    section: str | None = Field(default=None, max_length=200)


class FlashcardUpdate(BaseModel):
    front: str | None = Field(default=None, min_length=1, max_length=2000)
    back: str | None = Field(default=None, min_length=1, max_length=8000)


class FlashcardList(BaseModel):
    cards: list[Flashcard]


class ReadingPosition(BaseModel):
    document_id: str
    chunk_id: str
    position: int
    updated_at: datetime


class ReadingPositionUpdate(BaseModel):
    chunk_id: str = Field(min_length=1, max_length=64)
    position: int = Field(ge=0)


class ReadingPositionState(BaseModel):
    position: ReadingPosition | None = None
