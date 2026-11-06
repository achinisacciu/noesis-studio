from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from noesis_contracts import ApiError, ApiResponse, ErrorCode


def error_body(request: Request, code: ErrorCode, message: str) -> dict[str, Any]:
    request_id = getattr(request.state, "request_id", None)
    response = ApiResponse[None](
        status="error",
        error=ApiError(code=code, message=message, request_id=request_id),
    )
    return response.model_dump(mode="json")


def error_code(status: int) -> ErrorCode:
    if status == 413:
        return "RESOURCE_LIMIT"
    if status == 502:
        return "DEPENDENCY_ERROR"
    if status == 503:
        return "SERVICE_UNAVAILABLE"
    if status == 504:
        return "TIMEOUT"
    return "VALIDATION_ERROR" if status < 500 else "INTERNAL_ERROR"


def install_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(HTTPException)
    async def http_error(request: Request, exc: HTTPException) -> JSONResponse:
        code = error_code(exc.status_code)
        return JSONResponse(
            status_code=exc.status_code, content=error_body(request, code, str(exc.detail))
        )

    @app.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=422,
            content=error_body(request, "VALIDATION_ERROR", "payload non valido"),
        )
