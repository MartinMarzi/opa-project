# Work Orders

Project: **OpenAI-compatible YOLO11 COCO Detection API**

This file indexes planned and completed GPT-5.4-mini-sized work orders.

---

## Work-order rules

Each work order should:

- have one goal;
- specify scope and non-goals;
- name tests required;
- name docs to update;
- prohibit unrelated changes;
- require a final report.

---

## Planned work orders

| ID | Status | Title | Summary |
|---|---|---|---|
| WO-001 | Completed | Repo scaffold | Create package layout, minimal FastAPI app, `/health`, pytest, ruff, README skeleton. |
| WO-002 | Completed | Config system | Add environment-based settings and `.env.example`. |
| WO-003 | Completed | OpenAI-shaped errors | Add error helper/handlers and tests. |
| WO-004 | Completed | API key auth | Add Bearer API key auth and tests. |
| WO-005 | Planned | Model registry | Add `yolo11n-coco` registry and `/v1/models`. |
| WO-006 | Planned | Detection schema | Add detection result Pydantic models. |
| WO-007 | Planned | Image parser | Add Base64 data URL parser and validation. |
| WO-008 | Planned | Mock YOLO service | Add mockable detection service interface and fake implementation for tests. |
| WO-009 | Planned | Chat request parser | Extract one image from OpenAI-style messages. |
| WO-010 | Planned | Chat completion wrapper | Return OpenAI-shaped response with mocked detections. |
| WO-011 | Planned | Real YOLO integration | Load `yolo11n.pt` and run CPU inference. |
| WO-012 | Planned | MVP smoke | Add OpenAI Python client example and smoke script. |

---

## Work-order template

```markdown
# Work Order: WO-XXX — Title

## Goal
Implement only ...

## Scope
Touch only:
- ...

## Non-goals
- Do not ...

## Required behavior
- ...

## Required tests
- ...

## Documentation updates
- ...

## Commands to run
- ...

## Final report required
Use the `AGENTS.md` final report format.
```

---

## Completed work orders

- WO-001 — Repo scaffold
- WO-002 — Config system
- WO-003 — OpenAI-shaped errors
- WO-004 — API key auth
