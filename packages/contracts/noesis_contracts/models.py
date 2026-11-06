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


class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    text: str = Field(min_length=1)


class Document(BaseModel):
    id: str
    title: str
    text: str
    created_at: datetime


class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=500)
    document_id: str


class SearchHit(BaseModel):
    text: str
    position: int


class SearchResponse(BaseModel):
    document_id: str
    hits: list[SearchHit]
