from fastapi import FastAPI

from yolo_openai_api.auth import register_auth_middleware
from yolo_openai_api.config import get_settings
from yolo_openai_api.errors import register_error_handlers
from yolo_openai_api.routes.models import router as models_router


app = FastAPI(title="OpenAI-compatible YOLO11 COCO Detection API")
register_auth_middleware(app)
register_error_handlers(app)
app.include_router(models_router)


@app.get("/health")
def health() -> dict[str, str]:
    settings = get_settings()
    return {"status": "ok", "service": settings.service_name}
