# Remediation Matrix

Project: **OpenAI-compatible YOLO11 COCO Detection API**

This file tracks issues found during review, audit, testing, or release preparation.

---

## Status values

- `Open`
- `Accepted risk`
- `Deferred`
- `In progress`
- `Fixed, awaiting verification`
- `Closed`
- `Rejected`

---

## Matrix

| ID | Status | Severity | Area | Finding | Required remediation | Evidence to close | Linked PR |
|---|---|---|---|---|---|---|---|
| R-001 | Open | Medium | Licensing | Ultralytics/model licensing must be reviewed before commercial/proprietary release. | Human verifies license obligations and updates docs. | Updated `MODEL_CARD.md`, `LIMITATIONS.md`, and release notes. | TBD |
| R-002 | Open | Medium | Performance | CPU FPS/latency unknown. | Add benchmark script and record results. | `docs/CPU_BENCHMARKS.md` contains measured data. | TBD |
| R-003 | Open | Medium | Compatibility | OpenAI compatibility scope not yet implemented. | Implement selected `/v1/models` and `/v1/chat/completions` behavior with tests. | API tests and OpenAI client smoke pass. | TBD |
| R-004 | Open | Medium | Security | Browser demo auth model may expose single API key if hosted publicly. | Keep browser demo local-only or design separate browser auth before public deployment. | `BROWSER_LIVE_DEMO.md` and `SECURITY_MODEL.md` updated. | TBD |

---

## Closing rule

Do not close a remediation item with “done” alone.

Closure requires evidence:

- test result;
- code link/PR;
- documentation update;
- benchmark result;
- explicit human acceptance of risk.
