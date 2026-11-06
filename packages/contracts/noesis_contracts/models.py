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
