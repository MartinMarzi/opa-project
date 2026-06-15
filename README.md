# OpenAI-compatible YOLO11 COCO Detection API

CPU-only FastAPI scaffold for an OpenAI-compatible YOLO11 COCO detection service.

Status: early scaffold.

YOLO inference is not implemented yet.

Configuration is environment-variable based.
Copy `.env.example` to `.env` for local development.
Authentication is not implemented yet; `YOLO_API_KEY` is currently configuration-only and will be enforced in a later work order.

Local test:

```bash
uv sync
uv run pytest
```

Local run:

```bash
uv run uvicorn yolo_openai_api.main:app --reload
```
