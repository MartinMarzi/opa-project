# AGENTS.md

Project: **OpenAI-compatible YOLO11 COCO Detection API**

This file is the repository constitution for AI coding agents. Read it before making any code, documentation, test, dependency, or workflow change.

The execution agent for this project is expected to be **GPT-5.4 mini** or another compact coding agent. Therefore, work must be split into small, mechanical, PR-sized changes with strict scope boundaries.

---

## 1. Mission

Build a professional-grade, CPU-only web API service that exposes **Ultralytics YOLO11 COCO object detection** through a selected **OpenAI-compatible API surface**.

The core user promise is:

> A developer can use the normal OpenAI client pattern, set `base_url` to this service, authenticate with one API key, send an image, and receive structured COCO object detections produced by `yolo11n.pt`.

Default model file:

- Internal model file: `yolo11n.pt`
- Public OpenAI-style model name: `yolo11n-coco`

Optional later public model names:

- `yolo11s-coco`
- `yolo11m-coco`

This project is not a full OpenAI API replacement and must never claim to be one.

---

## 2. Human / strategic / execution role separation

The human owner is the product and domain authority.

The strategic AI is the architecture, planning, review, risk, and work-order layer.

The execution agent implements narrow work orders only.

The execution agent must not:

- redefine the product goal;
- expand the OpenAI-compatible API scope without instruction;
- decide release readiness;
- silently add features outside the work order;
- ask the human to perform routine local dependency setup inside the approved execution environment.

The execution agent may:

- inspect the repository;
- edit files within the requested scope;
- install local development dependencies inside the approved VM/environment;
- run tests and lint checks;
- update directly relevant documentation;
- report blockers honestly.

---

## 3. Required context files

Before implementing any non-trivial task, read these files if present:

- `AGENTS.md`
- `docs/PROJECT_STATE.md`
- `docs/ARCHITECTURE.md`
- `docs/API_COMPATIBILITY.md`
- `docs/API_SCHEMA.md`
- `docs/SECURITY_MODEL.md`
- `docs/MODEL_CARD.md`
- `docs/RELEASE_CRITERIA.md`
- `docs/DECISIONS.md`

If your task affects testing, also read:

- `docs/TESTING.md`

If your task affects browser/live-camera work, also read:

- `docs/BROWSER_LIVE_DEMO.md`

If your task affects configuration, also read:

- `docs/CONFIGURATION.md`

If repository state conflicts with these docs, do not silently choose one. Report the conflict and make the minimum necessary update only if the work order asks you to do so.

---

## 4. Architecture principles

The intended first architecture is:

```text
OpenAI Python client / curl / browser
        |
        v
FastAPI API service
        |
        +-- single Bearer API key authentication
        +-- OpenAI-compatible request parser
        +-- image decoder and validator
        +-- YOLO11 inference service
        +-- detection response formatter
        +-- OpenAI-shaped error responses
        +-- optional later SSE streaming
        |
        v
yolo11n.pt on CPU
```

Required baseline stack:

- Python 3.11 or 3.12
- FastAPI
- Uvicorn
- Pydantic v2
- pydantic-settings
- Ultralytics
- Pillow
- NumPy
- httpx
- pytest
- ruff
- OpenAI Python SDK as a development/test/example dependency

Use `uv` for dependency management unless the human explicitly chooses another package manager.

---

## 5. API scope

Required API surface for MVP:

- `GET /health`
- `GET /v1/models`
- `POST /v1/chat/completions`

Recommended later API surface:

- `POST /v1/detections`
- OpenAI-style `stream=true` response streaming
- Browser demo using repeated frame requests or later WebSocket

The OpenAI-compatible layer must be described as a **selected compatibility subset**, not full compatibility.

The service should support OpenAI-style image input through Base64 data URLs inside chat message content.

Example public model name:

```text
yolo11n-coco
```

---

## 6. CPU-only rule

The project must work on CPU without GPU.

Do not add required CUDA, TensorRT, GPU-only Docker images, or GPU-only install steps.

Optional future acceleration work may be documented separately, but it must not be required for MVP or RC1.

All performance claims must be backed by benchmark output in `docs/CPU_BENCHMARKS.md`.

Never claim real-time 30 FPS performance unless measured on the target machine.

---

## 7. Security rules

Authentication:

- All `/v1/*` endpoints require `Authorization: Bearer <API_KEY>`.
- The API key comes from environment configuration.
- `GET /health` may remain unauthenticated.

Secrets:

- Never commit real API keys.
- Never put secrets in tests, examples, docs, logs, or screenshots.
- Use `.env.example` with fake placeholders only.
- Never print the configured API key.

Input safety:

- Enforce image size and payload limits.
- Reject invalid image data clearly.
- Reject unsupported models clearly.
- Fail closed on ambiguous or unsupported request shapes.

Output safety:

- Do not include raw image data in API responses.
- Do not store images by default.
- Do not add persistence unless explicitly requested.

---

## 8. Non-goals unless explicitly requested

Do not implement these unless a work order explicitly requests them:

- user accounts;
- database persistence;
- billing;
- quota tracking;
- multi-tenant API keys;
- GPU/CUDA deployment;
- custom training;
- full OpenAI API replacement;
- full video streaming through `/v1/chat/completions`;
- production Kubernetes deployment;
- cloud storage;
- telemetry that stores images;
- complex React frontend.

---

## 9. GPT-5.4 mini PR-size discipline

Each implementation task should be small.

Preferred PR limits:

- one main goal;
- 3 to 8 changed files when possible;
- 0 or 1 new endpoint;
- 0 to 2 new dependencies;
- focused tests required;
- no mixed backend + frontend + model + streaming work in one PR.

If the work order is too broad, stop and report that it should be split.

Good task examples:

- add `/health` endpoint and tests;
- add settings object and `.env.example`;
- add OpenAI-shaped error response helper;
- add model registry and `/v1/models`;
- add Base64 data URL image parser;
- add mocked chat completions detection response;
- connect real YOLO11 inference behind existing service interface.

Bad task examples:

- build the whole MVP;
- implement all OpenAI compatibility;
- add live browser UI and streaming;
- make it production-ready;
- refactor everything.

---

## 10. Testing rules

A skipped test is not a passing test.

A test that was not run is not evidence.

Required test categories over time:

- health endpoint tests;
- auth success/failure tests;
- model registry tests;
- image parser tests;
- OpenAI-compatible request parser tests;
- detection schema tests;
- mocked inference API tests;
- optional marked integration test using real `yolo11n.pt`;
- OpenAI Python client smoke test;
- CPU benchmark script.

Tests should not require GPU.

Real-model tests may be slower and should be clearly marked so normal unit tests can run quickly.

Run relevant tests after each change. If a test cannot be run, report it as `not run` or `blocked`, not as passed.

---

## 11. Documentation rules

If behavior changes, update the directly relevant docs.

Do not update unrelated docs just to appear thorough.

Do not overclaim:

- Say “selected OpenAI-compatible detection API.”
- Do not say “full OpenAI-compatible API.”
- Say “CPU-only supported; performance depends on hardware.”
- Do not promise real-time video until benchmarked.

Documentation should preserve long-term project state and help future strategic sessions continue safely.

---

## 12. Workflow rules

Default workflow:

1. Start from current `main`.
2. Create a feature branch.
3. Make one scoped change.
4. Add or update focused tests.
5. Run relevant tests and lint checks.
6. Commit only related files.
7. Open a pull request if working with a remote repository.
8. Do not merge your own PR.

Never commit directly to protected `main` unless the human explicitly instructs this for a local-only initial repository.

---

## 13. Final report format

Every coding-agent run must end with:

```markdown
## Agent Report

Branch:
Commit:
Pull request:

## Summary
- ...

## Files changed
- ...

## Tests run
- command: result

## Documentation updated
- ...

## Safety confirmations
- No real API keys committed.
- No GPU-only dependency introduced.
- No database/user/billing scope added.
- No skipped tests reported as passed.

## Known limitations / blockers
- ...

## Recommended next step
- ...
```

If no branch/commit/PR exists, write `not created` and explain why.

---

## 14. Release honesty

MVP, Alpha, Beta, and RC1 are different claims.

Do not mark the project RC1-ready unless `docs/RELEASE_CRITERIA.md` is satisfied and the human release authority accepts the evidence.

The execution agent may recommend readiness but may not decide readiness.
