# Release Criteria

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Release language doctrine

Do not call the project complete, beta, RC1, or production-ready unless the evidence matches the claim.

Implemented behavior is not the same as release readiness.

---

## MVP criteria

MVP may be claimed when all of the following are true:

- local CPU service starts successfully;
- one API key auth works;
- `GET /health` works;
- `GET /v1/models` returns `yolo11n-coco`;
- `POST /v1/chat/completions` accepts one Base64 image;
- real `yolo11n.pt` inference works on CPU;
- response contains stable detection JSON;
- OpenAI Python client smoke example works;
- core unit/API tests pass;
- README includes quickstart and limitations;
- no GPU is required.

MVP does not require:

- browser UI;
- streaming;
- Docker;
- CI;
- native `/v1/detections`;
- multiple models.

---

## Alpha criteria

Alpha may be claimed when:

- MVP criteria are satisfied;
- bad inputs produce clear OpenAI-shaped errors;
- request/image limits are enforced;
- confidence/max detections are configurable;
- native `/v1/detections` exists or is deliberately deferred;
- CPU benchmark script exists;
- docs are updated for actual behavior.

---

## Beta criteria

Beta may be claimed when:

- Alpha criteria are satisfied;
- native `/v1/detections` is stable;
- streaming support exists or is explicitly deferred from RC1;
- minimal browser demo exists or is explicitly deferred from RC1;
- CPU benchmark has been run and documented;
- integration test with real model passes on CPU;
- OpenAI client smoke test passes;
- docs include security and browser limitations.

---

## RC1 criteria

RC1 may be claimed when:

- Beta criteria are satisfied;
- full relevant test suite passes;
- lint/format checks pass;
- no known current-scope blockers remain;
- `docs/API_COMPATIBILITY.md` matches behavior;
- `docs/API_SCHEMA.md` matches behavior;
- `docs/SECURITY_MODEL.md` matches behavior;
- `docs/CPU_BENCHMARKS.md` contains measured results;
- `docs/LIMITATIONS.md` is honest and current;
- release notes/checklist exist;
- human release authority accepts the evidence.

---

## Production-ready criteria

Production-ready is not an RC1 claim.

Before production-ready language, the project likely needs:

- HTTPS deployment guide;
- reverse proxy request limits;
- rate limiting;
- key rotation procedure;
- deployment secret management;
- dependency vulnerability review;
- license review;
- external security review;
- public-browser authentication design if browser UI is hosted;
- operational monitoring.

---

## Release decision brief template

Before any release, prepare:

```markdown
# Release Decision Brief

Recommendation: release / do not release / release with limitations

## Target release
- MVP / Alpha / Beta / RC1

## Evidence
- Tests:
- Lint:
- OpenAI client smoke:
- Real model integration:
- CPU benchmark:
- Docs:

## Known limitations
- ...

## Risks
- ...

## Human decision required
- ...
```
