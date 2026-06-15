# Limitations

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Current limitation status

This project is being initialized. Limitations listed here are design constraints until implementation proves otherwise.

---

## OpenAI compatibility limitations

This service is not a full OpenAI API replacement.

It only aims to support selected OpenAI-style calls for image detection, primarily:

- `GET /v1/models`
- `POST /v1/chat/completions`

Unsupported unless explicitly implemented:

- text generation;
- embeddings;
- assistants;
- responses API;
- tool calling;
- audio;
- image generation;
- fine-tuning;
- file API;
- arbitrary OpenAI models.

---

## Model limitations

The default model is `yolo11n.pt` exposed as `yolo11n-coco`.

Expected limitations:

- COCO classes only;
- no custom classes;
- no segmentation;
- no tracking;
- no OCR;
- no scene reasoning;
- no language explanation beyond deterministic detection JSON.

---

## CPU limitations

The service must run on CPU.

CPU-only operation means:

- inference latency may be significant;
- high FPS live camera detection is not guaranteed;
- larger models may be impractical;
- request concurrency may need to be limited;
- benchmark evidence is required before performance claims.

---

## Browser/live-camera limitations

The browser demo is not part of MVP.

For RC1, a minimal browser demo may be included, but it should be described as a demo unless hardened.

Important limitation:

- exposing a single API key in browser JavaScript is unsafe for public deployments.

For local demo, the user may paste a key at runtime. For public deployment, a different auth/session design is needed.

---

## Security limitations

MVP/RC1 should not be described as production-secure for public internet exposure unless hardening is completed.

Known production gaps before public deployment may include:

- no rate limiting;
- no key rotation UI;
- no audit logs;
- no reverse-proxy HTTPS documentation;
- no public browser auth design;
- no dependency security review;
- no external security audit.

---

## Licensing limitations

Ultralytics software/model licensing must be reviewed before commercial or closed-source release.

Until reviewed, do not claim unrestricted commercial use.

---

## Data limitations

MVP/RC1 should not persist images by default.

The service should not create datasets, logs with image contents, or telemetry containing raw image data unless deliberately designed later.
