from http import HTTPStatus
from typing import Any

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def error_body(
    message: str,
    *,
    error_type: str,
    param: str | None = None,
    code: str | None = None,
) -> dict[str, dict[str, Any]]:
    return {
        "error": {
            "message": message,
            "type": error_type,
            "param": param,
            "code": code,
        }
    }


def error_response(
    status_code: int,
    message: str,
    *,
    error_type: str,
    param: str | None = None,
    code: str | None = None,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content=error_body(
            message,
            error_type=error_type,
            param=param,
            code=code,
        ),
    )


def _status_code_name(status_code: int) -> str:
    try:
        return HTTPStatus(status_code).phrase.lower().replace(" ", "_")
    except ValueError:
        return "http_error"


async def http_exception_handler(
    request: Request,
    exc: HTTPException | StarletteHTTPException,
) -> JSONResponse:
    del request

    if exc.status_code == 404:
        return error_response(
            404,
            "Not Found",
            error_type="not_found_error",
            code="not_found",
        )

    message = exc.detail if isinstance(exc.detail, str) else "Request failed."
    return error_response(
        exc.status_code,
        message,
        error_type="invalid_request_error",
        code=_status_code_name(exc.status_code),
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    del request, exc

    return error_response(
        422,
        "Request validation failed.",
        error_type="invalid_request_error",
        code="validation_error",
    )


def register_error_handlers(app: Any) -> None:
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

