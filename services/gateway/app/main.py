import json
import logging
import os
import time
import uuid
from collections.abc import Awaitable, Callable

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api, router
from app.core.errors import install_error_handlers

SERVICE = "gateway"
log = logging.getLogger(SERVICE)

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.getLogger("httpx").setLevel(logging.WARNING)


def create_app() -> FastAPI:
    app = FastAPI(title=SERVICE, version="0.1.0")
    origins = os.getenv(
        "NOESIS_FRONTEND_ORIGIN",
        # Vite in sviluppo e webview Tauri nel bundle
        "http://localhost:5173,http://127.0.0.1:5173,tauri://localhost,http://tauri.localhost",
    ).split(",")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origin.strip() for origin in origins],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    install_error_handlers(app)
    app.include_router(router)
    app.include_router(api)

    @app.middleware("http")
    async def request_context(
        request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        request.state.request_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex
        started = time.perf_counter()
        response = await call_next(request)
        response.headers["X-Request-ID"] = request.state.request_id
        log.info(
            json.dumps(
                {
                    "service": SERVICE,
                    "request_id": request.state.request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "status": response.status_code,
                    "duration_ms": round((time.perf_counter() - started) * 1000, 1),
                }
            )
        )
        return response

    return app


app = create_app()
