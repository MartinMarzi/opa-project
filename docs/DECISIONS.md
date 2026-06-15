# Decisions Log

Project: **OpenAI-compatible YOLO11 COCO Detection API**

This file records durable architecture/product decisions. Add new decisions when the project direction changes.

---

## Decision 001 — Product name

Date: 2026-06-15

Decision:

Use the product name **OpenAI-compatible YOLO11 COCO Detection API**.

Reason:

The name states the product category, compatibility target, model family, dataset scope, and API nature.

Status: Accepted.

---

## Decision 002 — Default model

Date: 2026-06-15

Decision:

Use `yolo11n.pt` as the default model file and expose it publicly as `yolo11n-coco`.

Reason:

The project must work on CPU without GPU. The nano model is the appropriate first target for CPU feasibility.

Status: Accepted.

---

## Decision 003 — Optional later models

Date: 2026-06-15

Decision:

Reserve public model names `yolo11s-coco` and `yolo11m-coco` for later optional support.

Reason:

This preserves a clean model naming scheme while keeping MVP focused on one model.

Status: Accepted, deferred.

---

## Decision 004 — CPU-only first

Date: 2026-06-15

Decision:

MVP and RC1 must work on CPU without GPU, CUDA, or TensorRT.

Reason:

The target development environment has no GPU. Professional-grade means the documented path must work on available hardware.

Status: Accepted.

---

## Decision 005 — FastAPI backend

Date: 2026-06-15

Decision:

Use Python/FastAPI for the API service.

Reason:

The project is Python ML-centered, uses Ultralytics, and needs typed API schemas and good testability.

Status: Accepted.

---

## Decision 006 — Selected OpenAI compatibility only

Date: 2026-06-15

Decision:

Implement a selected OpenAI-compatible API subset, primarily `/v1/models` and `/v1/chat/completions` for image detection.

Reason:

Full OpenAI API replacement is unnecessary and would create false expectations. The useful product promise is SDK-style compatibility for image detection calls.

Status: Accepted.

---

## Decision 007 — One API key only

Date: 2026-06-15

Decision:

Use a single Bearer API key from environment configuration.

Reason:

The user requested a simplified access model. MVP does not require users, billing, database, or quotas.

Status: Accepted.

---

## Decision 008 — No database in v1

Date: 2026-06-15

Decision:

Do not use a database in MVP or initial RC1 path.

Reason:

The service is stateless: one API key, one model, no user accounts, no persistence.

Status: Accepted.

---

## Decision 009 — Add native CV endpoint later

Date: 2026-06-15

Decision:

Add `/v1/detections` after the OpenAI-style endpoint is stable.

Reason:

Chat completions compatibility is useful for SDK examples, but a native detection endpoint is cleaner for browser/live-camera use.

Status: Accepted, deferred.

---

## Decision 010 — GPT-5.4 mini work-order sizing

Date: 2026-06-15

Decision:

Split work into small PRs suitable for GPT-5.4 mini as execution agent.

Reason:

Smaller PRs reduce context drift, scope creep, and validation burden.

Status: Accepted.
