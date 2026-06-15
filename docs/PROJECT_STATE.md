# Project State

Project: **OpenAI-compatible YOLO11 COCO Detection API**

Last updated: 2026-06-15

---

## Current truth

This repository is being initialized.

The initial scaffold exists, exposes a minimal health endpoint, and enforces API key auth on `/v1/*`.

The initial strategic decisions are:

- Product name: `OpenAI-compatible YOLO11 COCO Detection API`
- Default model file: `yolo11n.pt`
- Public OpenAI-style model name: `yolo11n-coco`
- Optional later model names: `yolo11s-coco`, `yolo11m-coco`
- Hardware target: CPU-only, no GPU required
- Main compatibility goal: selected OpenAI-style API behavior, not full OpenAI API replacement
- Authentication model: one Bearer API key from environment configuration
- First API goal: single-image COCO object detection through `/v1/chat/completions`

---

## Current milestone

Current milestone: **M1 — Skeleton**

M1 is complete when the repository contains:

- `AGENTS.md`
- initial `docs/` long-term state files
- initial project skeleton
- a minimal unauthenticated health endpoint

---

## Implemented

- Python package scaffold
- FastAPI application scaffold
- `GET /health`
- configuration system
- OpenAI-shaped error responses
- single API key authentication for `/v1/*`

---

## Not implemented yet

- `/v1/models`
- image parser
- detection schema
- mocked YOLO service
- `/v1/chat/completions`
- real `yolo11n.pt` CPU inference
- OpenAI Python client smoke example
- CPU benchmark script
- `/v1/detections`
- streaming response support
- browser live-camera demo
- Dockerfile
- CI

---

## Current risks

| Risk | Status | Mitigation |
|---|---|---|
| Overclaiming OpenAI compatibility | Open | Document selected subset in `API_COMPATIBILITY.md`. |
| CPU performance may be too slow for live detection | Open | Benchmark before making FPS claims. |
| YOLO/Ultralytics dependency may be heavy | Open | Isolate real-model integration in a separate PR and keep mocked tests fast. |
| Coding agent scope creep | Open | Use small PRs and strict non-goals in `AGENTS.md`. |
| License/commercial-use implications | Open | Document licensing risk in `MODEL_CARD.md` and `LIMITATIONS.md`; human to verify before commercial release. |

---

## Next recommended work order

Implement `WO-005` Model registry and `/v1/models`.

---

## Do not do next

Do not implement:

- real YOLO inference;
- browser UI;
- streaming;
- Docker;
- database;
- user accounts;
- multiple models.

Those come later after the API foundation is stable.
