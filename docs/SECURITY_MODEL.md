# Security Model

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Security posture for MVP and RC1

This is a local/self-hosted API service with one configured API key and no user database.

The MVP security goal is not enterprise identity management. The goal is a simple, predictable, fail-closed API boundary.

---

## Authentication

All `/v1/*` endpoints require:

```http
Authorization: Bearer <YOLO_API_KEY>
```

Rules:

- API key is loaded from environment configuration.
- API key must never be hardcoded.
- API key must never be committed.
- Missing or invalid key returns an OpenAI-shaped authentication error.
- `GET /health` may be unauthenticated.

---

## Secrets

Forbidden:

- real API keys in repository;
- real secrets in tests;
- real secrets in docs;
- printing API keys in logs;
- exposing API key in browser demo code;
- storing API key in committed frontend files.

Required:

- provide `.env.example` with fake placeholder values;
- mention local `.env` usage in docs;
- add `.env` to `.gitignore` when repository scaffold is created.

---

## Input validation

The service must validate image inputs before inference.

MVP should enforce:

- supported image MIME types;
- valid Base64 data URL format;
- maximum request body size;
- maximum decoded image size;
- maximum image pixel count or dimensions;
- clear rejection of invalid images.

Unsupported or ambiguous input must fail closed.

---

## Image handling

MVP/RC1 should not store images by default.

Rules:

- decode image in memory;
- run inference;
- return detections;
- do not persist raw image;
- do not log Base64 image content;
- do not include raw image content in response.

Optional future logging must be explicitly designed to avoid storing sensitive image content.

---

## Network behavior

MVP should not fetch remote image URLs unless explicitly implemented later.

Reason:

- remote URL fetching creates SSRF and network policy risks;
- Base64 data URLs are enough for MVP compatibility.

If remote URLs are added later, document and test:

- allowed protocols;
- timeouts;
- max download size;
- redirect policy;
- private network blocking;
- error behavior.

---

## Denial-of-service considerations

CPU-only inference is expensive relative to normal API parsing.

Mitigations for MVP/RC1:

- request size limit;
- image dimension/pixel limit;
- max detections limit;
- configurable confidence threshold;
- reject unsupported models before inference;
- reject unauthenticated requests before image decoding;
- document that this is not yet a high-scale production service.

---

## Browser demo security

The later browser demo must not commit a real API key into JavaScript.

For local demo only, it may ask the user to paste a local key into the browser at runtime.

For hosted deployments, a browser-facing version needs a different design, because exposing the single API key to the browser exposes it to users.

This must be documented before any public browser deployment.

---

## Production readiness warning

MVP and RC1 do not automatically mean production security certification.

Before public production exposure, the project needs at minimum:

- HTTPS reverse proxy;
- stricter rate limiting;
- request body limits at proxy and app level;
- key rotation procedure;
- deployment secret management;
- logging review;
- dependency vulnerability review;
- license review;
- possibly a different browser-auth design.
