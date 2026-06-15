# OpenAI-compatible YOLO11 COCO Detection API

CPU-only FastAPI scaffold for an OpenAI-compatible YOLO11 COCO detection service.

Status: early scaffold.

YOLO inference is not implemented yet.

Local test:

```bash
uv sync
uv run pytest
```

Local run:

```bash
uv run uvicorn yolo_openai_api.main:app --reload
```

