# Configuration

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Configuration principles

All runtime configuration should come from environment variables.

No secrets should be hardcoded.

A `.env.example` file should document required and optional settings using fake placeholder values.

---

## Required environment variables

| Variable | Required | Example | Purpose |
|---|---:|---|---|
| `YOLO_API_KEY` | Yes | `change-me-local-dev-key` | Single Bearer API key for `/v1/*` endpoints. |

---

## Recommended environment variables

| Variable | Required | Default | Purpose |
|---|---:|---|---|
| `YOLO_MODEL_NAME` | No | `yolo11n-coco` | Public API model name. |
| `YOLO_MODEL_PATH` | No | `yolo11n.pt` | Model file/path to load. |
| `YOLO_DEVICE` | No | `cpu` | Inference device. Must default to CPU. |
| `YOLO_CONFIDENCE` | No | `0.25` | Confidence threshold. |
| `YOLO_MAX_DETECTIONS` | No | `100` | Maximum detections per image. |
| `YOLO_MAX_IMAGE_MB` | No | `10` | Maximum decoded/uploaded image size. |
| `YOLO_MAX_IMAGE_PIXELS` | No | `4194304` | Maximum image pixel count, e.g. 2048x2048. |
| `YOLO_LOG_LEVEL` | No | `INFO` | Logging level. |
| `YOLO_ENABLE_REAL_MODEL_TESTS` | No | `false` | Allows slower integration tests using real YOLO model. |

---

## `.env.example` target content

When the repository scaffold is created, include something like:

```env
YOLO_API_KEY=change-me-local-dev-key
YOLO_MODEL_NAME=yolo11n-coco
YOLO_MODEL_PATH=yolo11n.pt
YOLO_DEVICE=cpu
YOLO_CONFIDENCE=0.25
YOLO_MAX_DETECTIONS=100
YOLO_MAX_IMAGE_MB=10
YOLO_MAX_IMAGE_PIXELS=4194304
YOLO_LOG_LEVEL=INFO
YOLO_ENABLE_REAL_MODEL_TESTS=false
```

---

## CPU-only configuration rule

`YOLO_DEVICE` must default to `cpu`.

Do not require CUDA or GPU-specific configuration for MVP or RC1.

---

## Configuration tests

Tests should verify:

- missing API key is handled clearly at startup or request time;
- default model name is `yolo11n-coco`;
- default model path is `yolo11n.pt`;
- default device is `cpu`;
- confidence and max detections parse correctly;
- invalid numeric config fails clearly.
