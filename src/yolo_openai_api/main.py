from fastapi import FastAPI

from yolo_openai_api.auth import register_auth_middleware
from yolo_openai_api.config import get_settings
from yolo_openai_api.errors import register_error_handlers


app = FastAPI(title="OpenAI-compatible YOLO11 COCO Detection API")
register_auth_middleware(app)
register_error_handlers(app)


@app.get("/health")
def health() -> dict[str, str]:
    settings = get_settings()
    return {"status": "ok", "service": settings.service_name}
