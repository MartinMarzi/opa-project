# Configuration

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Configuration principles

All runtime configuration comes from environment variables.

`pydantic-settings` loads values from the process environment and an optional local `.env` file.

No secrets should be hardcoded.

---

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `YOLO_API_SERVICE_NAME` | `openai-compatible-yolo11-coco-detection-api` | Service name returned by `GET /health`. |
| `YOLO_PUBLIC_MODEL_NAME` | `yolo11n-coco` | Public OpenAI-style model name. |
| `YOLO_MODEL_FILE` | `yolo11n.pt` | Internal YOLO model file name. |
| `YOLO_API_KEY` | `` | API key placeholder for later `/v1/*` authentication. |
| `YOLO_MAX_IMAGE_BYTES` | `5000000` | Maximum decoded image size in bytes. |
| `YOLO_DEFAULT_CONFIDENCE_THRESHOLD` | `0.25` | Default confidence threshold for later detection requests. |
| `YOLO_MAX_DETECTIONS` | `100` | Maximum detections per image. |

---

## `.env.example`

The repository includes safe placeholder values in `.env.example`.
Copy that file to `.env` for local development.

---

## Authentication note

`YOLO_API_KEY` is present in configuration now, but authentication is not implemented yet.
It will be enforced in a later work order.

