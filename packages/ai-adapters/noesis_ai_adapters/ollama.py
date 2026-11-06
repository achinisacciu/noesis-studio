import asyncio
import json
from collections.abc import AsyncIterator

import httpx
from noesis_contracts import HealthStatus

from noesis_ai_adapters.base import (
    AdapterError,
    ChatChunk,
    ChatRequest,
    ModelInfo,
)


class OllamaAdapter:
    def __init__(self, base_url: str = "http://127.0.0.1:11434", timeout: float = 120.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._active: dict[str, httpx.Response] = {}
        self._lock = asyncio.Lock()

    async def list_models(self) -> list[ModelInfo]:
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
        except httpx.HTTPError as error:
            raise AdapterError("runtime Ollama non raggiungibile", "SERVICE_UNAVAILABLE") from error
        if response.status_code != 200:
            raise AdapterError("runtime Ollama non disponibile", "SERVICE_UNAVAILABLE")
        payload = response.json()
        models = payload.get("models", []) if isinstance(payload, dict) else []
        return [
            ModelInfo(id=str(model["name"]), capabilities={"chat"})
            for model in models
            if isinstance(model, dict) and "name" in model
        ]

    async def chat(self, req: ChatRequest) -> AsyncIterator[ChatChunk]:
        payload = {
            "model": req.model,
            "messages": [message.model_dump() for message in req.messages],
            "stream": True,
            "think": False,
            "options": {"temperature": req.temperature},
        }
        request_id = req.request_id or ""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                async with client.stream(
                    "POST", f"{self.base_url}/api/chat", json=payload
                ) as response:
                    if response.status_code != 200:
                        body = await response.aread()
                        raise AdapterError(
                            f"Ollama ha risposto {response.status_code}: {body.decode(errors='replace')[:200]}",
                            "SERVICE_UNAVAILABLE",
                        )
                    if request_id:
                        async with self._lock:
                            self._active[request_id] = response
                    async for line in response.aiter_lines():
                        if not line.strip():
                            continue
                        data = json.loads(line)
                        text = data.get("message", {}).get("content", "")
                        if text:
                            yield ChatChunk(delta=str(text))
                        if data.get("done"):
                            yield ChatChunk(delta="", finish_reason="stop")
                            return
        except httpx.TimeoutException as error:
            raise AdapterError("runtime AI non ha risposto in tempo", "TIMEOUT") from error
        except httpx.HTTPError as error:
            raise AdapterError("runtime AI non raggiungibile", "SERVICE_UNAVAILABLE") from error
        finally:
            if request_id:
                async with self._lock:
                    self._active.pop(request_id, None)

    async def abort(self, request_id: str) -> None:
        async with self._lock:
            response = self._active.pop(request_id, None)
        if response is not None:
            await response.aclose()

    async def health(self) -> HealthStatus:
        try:
            async with httpx.AsyncClient(timeout=2.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
        except httpx.HTTPError:
            return HealthStatus(status="unavailable", service="ollama")
        if response.status_code == 200:
            return HealthStatus(status="healthy", service="ollama")
        return HealthStatus(status="degraded", service="ollama")

