# Testing

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Testing doctrine

A skipped test is not a passing test.

A test that was not run is not evidence.

Test reports must distinguish:

- passed;
- failed;
- skipped;
- not run;
- blocked.

---

## Test layers

| Layer | Purpose | Should run by default? |
|---|---|---:|
| Unit tests | Test pure helpers, schemas, parsing, config. | Yes |
| API tests | Test FastAPI endpoints with mocked model service. | Yes |
| Auth tests | Verify API key behavior. | Yes |
| Error-shape tests | Verify OpenAI-shaped errors. | Yes |
| Mocked inference tests | Verify endpoint behavior without loading real YOLO. | Yes |
| Real-model integration test | Verify `yolo11n.pt` inference path. | No, mark separately |
| OpenAI client smoke test | Verify actual SDK usage. | Manual or optional CI |
| CPU benchmark | Measure latency/performance. | Manual/release |

---

## Required MVP tests

MVP should include tests for:

- `GET /health` returns OK;
- `/v1/*` rejects missing API key;
- `/v1/*` rejects invalid API key;
- `/v1/models` returns `yolo11n-coco`;
- unsupported model returns OpenAI-shaped error;
- Base64 data URL image parser accepts valid JPEG/PNG;
- invalid Base64 image is rejected;
- missing image is rejected;
- chat completions endpoint returns OpenAI-shaped response with mocked detections;
- detection JSON schema contains label, class ID, confidence, box, image size, inference time.

---

## Real-model test policy

Real YOLO tests may download or load model weights and may be slower.

They should be:

- marked as integration tests;
- disabled by default unless `YOLO_ENABLE_REAL_MODEL_TESTS=true` or a pytest marker is passed;
- CPU-only;
- limited to one or a few small test images.

---

## Suggested commands

After scaffold exists, preferred commands should be documented here.

Expected shape:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

Optional later:

```bash
YOLO_ENABLE_REAL_MODEL_TESTS=true uv run pytest tests/integration
uv run python scripts/smoke_openai_client.py
uv run python scripts/benchmark_cpu.py
```

---

## Test design rules for coding agents

Do not make tests pass by weakening assertions.

Do not skip hard tests without reporting why.

Do not mock away the behavior being tested.

For endpoint tests, prefer dependency injection or monkeypatching to replace the real YOLO service with a deterministic fake.

For schema tests, assert the stable public fields, not fragile internal implementation details.

---

## Release evidence

Before RC1, the project should have evidence for:

- unit tests passing;
- API tests passing;
- lint passing;
- real-model integration test passing on CPU;
- OpenAI Python client smoke test passing;
- CPU benchmark run recorded;
- docs updated to match implemented behavior.
