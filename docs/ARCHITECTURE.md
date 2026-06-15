# Architecture

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Architecture summary

This service exposes YOLO11 COCO object detection through a selected OpenAI-compatible HTTP API surface.

The service is intentionally simple for MVP and RC1:

- stateless API service;
- one configured API key;
- one default model: `yolo11n.pt`;
- CPU-only inference;
- no database;
- no users;
- no billing;
- no persistent image storage.

---

## Intended high-level design

```text
OpenAI Python client / curl / browser
        |
        v
FastAPI app
        |
        +-- request ID middleware
        +-- single Bearer API key auth for /v1/*
        +-- OpenAI-compatible request parser
        +-- image decoder and validator
        +-- YOLO11 detection service
        +-- response formatter
        +-- OpenAI-shaped error handler
        |
        v
yolo11n.pt running on CPU
```

---

## Main components

| Component | Responsibility |
|---|---|
| `main.py` | Create FastAPI app and include routers. |
| `config.py` | Load settings from environment variables. |
| `auth.py` | Enforce one Bearer API key for `/v1/*`. |
| `errors.py` | Convert failures into OpenAI-shaped error responses. |
| `openai_schemas.py` | Pydantic schemas for selected OpenAI-compatible request/response shapes. |
| `detection_schemas.py` | Pydantic schemas for detection result JSON. |
| `image_io.py` | Parse and validate Base64 data URL image inputs. |
| `yolo_service.py` | Load YOLO11 model and produce detection results. |
| `routes/health.py` | Public health endpoint. |
| `routes/models.py` | OpenAI-style `/v1/models` endpoint. |
| `routes/chat_completions.py` | OpenAI-style `/v1/chat/completions` endpoint. |
| `routes/detections.py` | Later native CV endpoint. |

---

## Request flow for MVP

1. Client calls `POST /v1/chat/completions`.
2. API key is checked.
3. Request body is validated.
4. Service checks that `model` is `yolo11n-coco`.
5. Service extracts exactly one image from `messages[].content[]`.
6. Image is decoded and validated.
7. YOLO service runs inference with `yolo11n.pt` on CPU.
8. Detection result is converted into stable JSON.
9. JSON result is wrapped in an OpenAI-shaped chat completion response.

---

## Why two APIs later

The project should eventually expose two API styles:

| API | Purpose |
|---|---|
| `/v1/chat/completions` | Compatibility with OpenAI-style examples and SDK usage. |
| `/v1/detections` | Clean native computer-vision endpoint for direct clients and browser demo. |

The browser live-camera demo should use `/v1/detections` or a later WebSocket endpoint, not force continuous video through chat completions.

---

## MVP architecture exclusions

MVP excludes:

- database;
- user accounts;
- quota tracking;
- billing;
- persistent image storage;
- async job queues;
- GPU-specific deployment;
- complex frontend;
- Kubernetes/cloud deployment.

These exclusions are deliberate to keep the first release professional, testable, and CPU-compatible.

---

## Later architecture options

Possible post-RC1 extensions:

- WebSocket real-time detection endpoint;
- ONNX Runtime CPU optimization;
- optional model registry for `yolo11s-coco` and `yolo11m-coco`;
- Docker Compose deployment;
- reverse proxy with HTTPS;
- request metrics;
- batch image detection;
- optional storage of anonymized benchmark metadata only.

Each extension should be added only through a separate design decision and PR-sized work order.
