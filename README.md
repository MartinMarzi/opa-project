# OpenAI-compatible YOLO11 COCO Detection API

CPU-only FastAPI scaffold for an OpenAI-compatible YOLO11 COCO detection service.

Status: early scaffold.

YOLO inference is not implemented yet.

Configuration is environment-variable based.
Copy `.env.example` to `.env` for local development.
Authentication is enforced on `/v1/*` with `Authorization: Bearer <YOLO_API_KEY>`.
OpenAI-shaped error responses are now part of the API foundation.
`GET /health` is public; future `/v1/*` endpoints require `Authorization: Bearer <YOLO_API_KEY>`.

Local test:

```bash
uv sync
uv run pytest
```

Local run:

```bash
uv run uvicorn yolo_openai_api.main:app --reload
```
