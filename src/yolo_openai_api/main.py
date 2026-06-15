from fastapi import FastAPI

SERVICE_NAME = "openai-compatible-yolo11-coco-detection-api"

app = FastAPI(title="OpenAI-compatible YOLO11 COCO Detection API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": SERVICE_NAME}

