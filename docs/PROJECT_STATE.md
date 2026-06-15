# Project State

Project: **OpenAI-compatible YOLO11 COCO Detection API**

Last updated: 2026-06-15

---

## Current truth

This repository is being initialized.

No application code has been implemented yet.

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

Current milestone: **M0 — Constitution and repository setup**

M0 is complete when the repository contains:

- `AGENTS.md`
- initial `docs/` long-term state files
- initial project skeleton in a later PR

---

## Implemented

Nothing implemented yet.

---

## Not implemented yet

- Python package scaffold
- FastAPI application
- `/health`
- configuration system
- single API key authentication
- OpenAI-shaped error responses
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

Create the initial repository scaffold:

- `pyproject.toml`
- `src/yolo_openai_api/`
- minimal FastAPI app
- `/health` endpoint
- basic pytest setup
- README skeleton

Do not add YOLO inference in the first implementation PR.

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
