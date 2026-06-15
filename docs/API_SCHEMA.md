# API Schema

Project: **OpenAI-compatible YOLO11 COCO Detection API**

This file defines the intended stable request and response schemas. It should be updated whenever API behavior changes.

---

## Detection result schema

The canonical internal detection result should be structured as:

```json
{
  "image_id": "img_...",
  "model": "yolo11n-coco",
  "detections": [
    {
      "label": "person",
      "class_id": 0,
      "confidence": 0.91,
      "box": {
        "x1": 120.4,
        "y1": 50.2,
        "x2": 310.8,
        "y2": 470.6
      }
    }
  ],
  "image_width": 640,
  "image_height": 480,
  "inference_ms": 83.2
}
```

---

## Bounding box convention

MVP box format:

- pixel coordinates;
- top-left origin;
- fields: `x1`, `y1`, `x2`, `y2`;
- floats allowed;
- image dimensions returned separately.

Optional later addition:

- normalized coordinates in a separate `box_normalized` field.

Do not silently change coordinate convention.

---

## OpenAI-shaped chat completion response

The outer response should look like:

```json
{
  "id": "chatcmpl_...",
  "object": "chat.completion",
  "created": 1710000000,
  "model": "yolo11n-coco",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "{... detection JSON string ...}"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": null
}
```

The `content` field should be a JSON string for SDK compatibility.

---

## OpenAI-shaped error response

Errors should use a stable shape:

```json
{
  "error": {
    "message": "Invalid API key.",
    "type": "authentication_error",
    "param": null,
    "code": "invalid_api_key"
  }
}
```

Implemented now:

- unknown routes return HTTP 404 with `type = "not_found_error"` and `code = "not_found"`;
- request validation errors return HTTP 422 with `type = "invalid_request_error"` and `code = "validation_error"`;
- authentication errors use the same envelope with `type = "authentication_error"`;
- reusable helper structure keeps `message`, `type`, `param`, and `code` in place for later endpoint-specific errors.

Recommended error types:

| Situation | HTTP | `type` | `code` |
|---|---:|---|---|
| Missing API key | 401 | `authentication_error` | `missing_api_key` |
| Invalid API key | 401 | `authentication_error` | `invalid_api_key` |
| Missing server config | 503 | `authentication_error` | `api_key_not_configured` |
| Unsupported model | 400 | `invalid_request_error` | `model_not_found` |
| Missing image | 400 | `invalid_request_error` | `missing_image` |
| Invalid image | 400 | `invalid_request_error` | `invalid_image` |
| Image too large | 413 | `invalid_request_error` | `image_too_large` |
| Unsupported request shape | 400 | `invalid_request_error` | `unsupported_request` |
| Internal inference error | 500 | `server_error` | `inference_error` |

---

## `/v1/models` response

MVP response should include `yolo11n-coco`:

```json
{
  "object": "list",
  "data": [
    {
      "id": "yolo11n-coco",
      "object": "model",
      "created": 0,
      "owned_by": "local"
    }
  ]
}
```

Implemented now:

- `GET /v1/models` returns an OpenAI-shaped list response;
- each model object includes `id`, `object`, `created`, `owned_by`, and `root`;
- only one model is listed for now: `yolo11n-coco` with `root = "yolo11n.pt"`.

---

## `/v1/detections` native response

Later native endpoint should return the canonical detection result directly, not wrapped in a chat completion.

```json
{
  "image_id": "img_...",
  "model": "yolo11n-coco",
  "detections": [],
  "image_width": 640,
  "image_height": 480,
  "inference_ms": 83.2
}
```

---

## Schema stability rule

Once an API shape is documented and tested, do not change it casually.

Breaking changes require:

- explicit decision in `docs/DECISIONS.md`;
- tests updated;
- compatibility docs updated;
- release notes updated.
