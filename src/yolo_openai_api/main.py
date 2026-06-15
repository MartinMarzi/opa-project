from fastapi import FastAPI

from yolo_openai_api.config import get_settings


app = FastAPI(title="OpenAI-compatible YOLO11 COCO Detection API")


@app.get("/health")
def health() -> dict[str, str]:
    settings = get_settings()
    return {"status": "ok", "service": settings.service_name}
