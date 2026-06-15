from secrets import compare_digest

from fastapi import FastAPI, Request
from fastapi.responses import Response
from starlette.middleware.base import RequestResponseEndpoint

from yolo_openai_api.config import get_settings
from yolo_openai_api.errors import error_response


def is_v1_path(path: str) -> bool:
    return path == "/v1" or path.startswith("/v1/")


def extract_bearer_token(authorization_header: str | None) -> str | None:
    if authorization_header is None or not authorization_header.startswith("Bearer "):
        return None

    token = authorization_header.removeprefix("Bearer ")
    if not token or token != token.strip() or any(char.isspace() for char in token):
        return None

    return token


def register_auth_middleware(app: FastAPI) -> None:
    @app.middleware("http")
    async def auth_middleware(
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        if not is_v1_path(request.url.path):
            return await call_next(request)

        settings = get_settings()
        configured_key = settings.api_key
        if not configured_key or not configured_key.strip():
            return error_response(
                503,
                "API key authentication is not configured.",
                error_type="authentication_error",
                code="api_key_not_configured",
            )

        token = extract_bearer_token(request.headers.get("authorization"))
        if token is None:
            header_value = request.headers.get("authorization")
            if header_value is None:
                return error_response(
                    401,
                    "Missing Authorization header.",
                    error_type="authentication_error",
                    code="missing_api_key",
                )
            return error_response(
                401,
                "Authorization header must use Bearer authentication.",
                error_type="authentication_error",
                code="invalid_authorization_header",
            )

        if not compare_digest(token, configured_key):
            return error_response(
                401,
                "Invalid API key.",
                error_type="authentication_error",
                code="invalid_api_key",
            )

        return await call_next(request)
