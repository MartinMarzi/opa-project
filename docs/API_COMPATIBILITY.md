# API Compatibility

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Compatibility claim

This project provides a **selected OpenAI-compatible API subset** for image-based YOLO11 object detection.

It is not a full OpenAI API replacement.

OpenAI-shaped error responses are implemented as part of the compatibility foundation, but full OpenAI error compatibility is not claimed.

Correct wording:

> This service is compatible with selected OpenAI Python client usage patterns for image detection calls.

Incorrect wording:

> This is a full OpenAI-compatible API server.

---

## Required OpenAI-style endpoints

| Endpoint | Status | Purpose |
|---|---|---|
| `GET /v1/models` | MVP | Return available model names such as `yolo11n-coco`. |
| `POST /v1/chat/completions` | MVP | Accept OpenAI-style chat completion requests containing one image and return detections. |

---

## Non-OpenAI native endpoints

| Endpoint | Status | Purpose |
|---|---|---|
| `POST /v1/detections` | Later | Direct computer-vision endpoint returning detection JSON without chat wrapper. |
| `WS /v1/detections/realtime` | Optional later | Browser/live-camera streaming endpoint. |

---

## Supported model names

MVP:

- `yolo11n-coco`

Optional later:

- `yolo11s-coco`
- `yolo11m-coco`

Unsupported model names must return a clear OpenAI-shaped error.

---

## Supported chat completion request subset

MVP should support requests shaped like:

```json
{
  "model": "yolo11n-coco",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Detect objects in this image."},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}
      ]
    }
  ]
}
```

The text instruction may be accepted but does not change the detector behavior in MVP.

---

## MVP input support

Required:

- Base64 data URL image input:
  - `data:image/jpeg;base64,...`
  - `data:image/png;base64,...`

Not required for MVP:

- remote image URLs;
- multiple images;
- video files;
- binary multipart upload through chat completions;
- prompts that alter detection behavior.

---

## Response compatibility

The response should be OpenAI-shaped at the outer layer and deterministic detection JSON inside the assistant message content.

MVP response shape should include:

- `id`
- `object`
- `created`
- `model`
- `choices`
- `choices[0].message.role`
- `choices[0].message.content`

The message `content` should contain a JSON string representing the detection result.

Error responses should also use the OpenAI-shaped `{"error": {...}}` envelope once API endpoints start failing in practice.

---

## Streaming compatibility

Streaming is not required for MVP.

For RC1, if implemented, `stream=true` should return server-sent event style chunks and a final done event.

Streaming in this project means streaming the API response. It does not mean true continuous video streaming from a browser camera.

---

## Unsupported OpenAI features

Unless explicitly added later, the service does not support:

- text-only language generation;
- tool/function calling;
- embeddings;
- assistants API;
- responses API;
- audio;
- image generation;
- fine-tuning;
- file upload API;
- arbitrary OpenAI model names;
- logprobs;
- temperature/top_p semantics;
- system prompts changing detection classes;
- conversation memory.

Unsupported features should fail clearly rather than being silently ignored when they could mislead users.

---

## Compatibility tests

At minimum, compatibility tests should include:

- OpenAI Python client can call `GET /v1/models` if supported by SDK path;
- OpenAI Python client can call `POST /v1/chat/completions` with `base_url` set to the local service;
- wrong model name returns OpenAI-shaped error;
- missing image returns OpenAI-shaped error;
- invalid image returns OpenAI-shaped error;
- invalid API key returns OpenAI-shaped error.
