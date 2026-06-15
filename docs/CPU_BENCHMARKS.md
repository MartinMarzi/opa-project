# CPU Benchmarks

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Benchmark status

No benchmark has been run yet.

This file must be updated before RC1.

---

## Benchmark purpose

The project is CPU-only. Performance claims must be based on measured evidence.

Benchmarks should measure:

- model load time;
- single-image inference latency;
- end-to-end API latency;
- image size used;
- confidence threshold;
- max detections;
- machine CPU;
- RAM;
- OS/environment.

---

## Required benchmark table

| Date | Machine | CPU | RAM | OS/VM | Model | Image size | Endpoint/path | Mean ms | p50 ms | p95 ms | Notes |
|---|---|---|---|---|---|---|---|---:|---:|---:|---|
| TBD | TBD | TBD | TBD | TBD | `yolo11n.pt` | TBD | TBD | TBD | TBD | TBD | Not measured yet. |

---

## Performance honesty rules

Do not claim:

- real-time 30 FPS;
- production throughput;
- stable latency under concurrency;
- performance of `yolo11s` or `yolo11m`;

unless measured and documented.

---

## Initial expectation

`yolo11n.pt` is chosen because it is the smallest intended model for CPU-first MVP.

Even with a small model, live camera detection may need:

- lower resolution;
- frame skipping;
- request throttling;
- no overlapping requests;
- optional future model export/optimization.

---

## Benchmark script target

A later `scripts/benchmark_cpu.py` should:

- load configured model;
- warm up inference;
- run N iterations on one or more sample images;
- report mean, p50, p95;
- optionally test API path separately;
- write results in a copy-pasteable Markdown row.
