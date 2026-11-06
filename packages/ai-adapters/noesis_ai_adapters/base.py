from collections.abc import AsyncIterator
from typing import Literal, Protocol

from noesis_contracts import ErrorCode, HealthStatus
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    model: str
    messages: list[ChatMessage]
    stream: bool = True
    temperature: float = Field(default=0.7, ge=0, le=2)
    request_id: str | None = None


class ChatChunk(BaseModel):
    delta: str
    finish_reason: str | None = None


class ModelInfo(BaseModel):
    id: str
    capabilities: set[str] = Field(default_factory=set)


class AdapterError(Exception):
    """Errore del runtime, già tradotto in una categoria del contratto."""

    def __init__(self, message: str, code: ErrorCode = "DEPENDENCY_ERROR") -> None:
        super().__init__(message)
        self.code = code


class RuntimeAdapter(Protocol):
    async def list_models(self) -> list[ModelInfo]: ...

    def chat(self, req: ChatRequest) -> AsyncIterator[ChatChunk]: ...

    async def abort(self, request_id: str) -> None: ...

    async def health(self) -> HealthStatus: ...
