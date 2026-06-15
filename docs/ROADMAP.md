# Roadmap

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Roadmap doctrine

Build the project in small PRs suitable for GPT-5.4 mini as execution agent.

Do not mix API compatibility, real model inference, streaming, browser UI, Docker, and CI in one large task.

---

## Milestones

| Milestone | Name | Goal |
|---|---|---|
| M0 | Constitution and docs | Establish project law and long-term state. |
| M1 | Skeleton | Minimal package, app, health endpoint, config, auth, model registry. |
| M2 | Mocked API MVP | OpenAI-shaped detection API works with mocked detections. |
| M3 | Real YOLO MVP | `yolo11n.pt` CPU inference works through OpenAI-style call. |
| M4 | Hardened API Alpha | Input limits, stable schema, native `/v1/detections`, CPU benchmark. |
| M5 | Streaming/browser Beta | SSE response streaming and minimal HTML5 camera demo. |
| M6 | RC1 readiness | Docker/CI/docs/release checklist/verification. |

---

## PR-sized path

| PR | Work package | Goal |
|---:|---|---|
| 1 | Repo scaffold | Package layout, minimal FastAPI app, `/health`, basic tests. |
| 2 | Config system | Settings, `.env.example`, config tests. |
| 3 | OpenAI error format | Error helper/handlers and tests. |
| 4 | API key auth | Bearer auth dependency and tests. |
| 5 | Model registry | `yolo11n-coco` registry and `/v1/models`. |
| 6 | Detection schema | Pydantic detection result models and tests. |
| 7 | Image parser | Base64 data URL parser and validation tests. |
| 8 | Mock YOLO service | Interface/fake service for deterministic tests. |
| 9 | Chat request parser | Extract one image from OpenAI-style messages. |
| 10 | Chat completion wrapper | Return OpenAI-shaped response with mocked detections. |
| 11 | Real YOLO integration | Load `yolo11n.pt` and run CPU inference behind service interface. |
| 12 | MVP smoke | OpenAI Python client example and smoke script. |
| 13 | Request limits | Max payload/image limits and errors. |
| 14 | Configurable thresholds | Confidence and max detection settings. |
| 15 | Output hardening | Optional normalized boxes or schema refinements. |
| 16 | Native detections endpoint | `POST /v1/detections`. |
| 17 | Native endpoint examples | curl/Python examples. |
| 18 | CPU benchmark | `scripts/benchmark_cpu.py` and benchmark docs. |
| 19 | Streaming skeleton | `stream=true` SSE with mocked data. |
| 20 | Streaming real detections | Connect streaming to real detection result. |
| 21 | Browser page scaffold | Static HTML camera permission page. |
| 22 | Browser frame capture | Video to canvas capture. |
| 23 | Browser API call | Send frame to `/v1/detections`, show JSON. |
| 24 | Browser overlay | Draw detection boxes. |
| 25 | Browser throttling | FPS limit and no overlapping requests. |
| 26 | Dockerfile | CPU-only Docker image. |
| 27 | CI | Lint/tests in GitHub Actions. |
| 28 | Docs hardening | Update architecture, compatibility, testing, limitations. |
| 29 | Release checklist | RC1 release notes and checklist. |
| 30 | Verification-only RC1 | No code edits; run verification and report. |

---

## MVP definition

MVP is reached after PR 12 when:

- service runs locally on CPU;
- single API key auth works;
- `GET /v1/models` returns `yolo11n-coco`;
- `POST /v1/chat/completions` accepts one Base64 image;
- endpoint returns detections from real `yolo11n.pt`;
- OpenAI Python client smoke example works;
- core tests pass.

---

## RC1 definition

RC1 is reached after M6 when:

- selected OpenAI-compatible API is stable;
- native detections endpoint exists;
- streaming response support exists if included in RC1 scope;
- minimal browser demo works locally if included in RC1 scope;
- CPU benchmark is documented;
- tests and lint pass;
- docs match behavior;
- release limitations are honest;
- human release authority accepts evidence.
