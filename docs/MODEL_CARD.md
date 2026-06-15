# Model Card

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Default model

Internal model file:

```text
yolo11n.pt
```

Public API model name:

```text
yolo11n-coco
```

Task:

```text
COCO object detection
```

Hardware target:

```text
CPU-only
```

---

## Optional later models

Optional future public names:

| Public name | Expected model file | Purpose |
|---|---|---|
| `yolo11s-coco` | `yolo11s.pt` | Better accuracy, slower CPU inference. |
| `yolo11m-coco` | `yolo11m.pt` | Higher accuracy, likely much slower CPU inference. |

Do not expose optional models until they are tested and documented.

---

## COCO classes

The model is expected to return COCO object classes.

The API should return both:

- `label`
- `class_id`

The exact class-name mapping should be taken from the loaded model metadata, not manually retyped unless necessary.

---

## Output fields

Each detection should include:

- class label;
- class ID;
- confidence score;
- pixel bounding box;
- image dimensions;
- model name;
- inference time.

---

## CPU performance posture

This project must work without GPU.

However, CPU speed depends on:

- machine CPU;
- image size;
- model size;
- confidence threshold;
- max detections;
- concurrent requests;
- PyTorch/Ultralytics runtime overhead.

Do not claim real-time camera performance until measured.

Benchmark results should be recorded in `docs/CPU_BENCHMARKS.md`.

---

## Known model limitations

The model detects only the classes it was trained for.

The service is not expected to:

- detect arbitrary custom classes;
- perform segmentation;
- perform tracking;
- perform pose estimation;
- perform OCR;
- explain image content as a language model;
- reason about scene meaning beyond object detections.

---

## Licensing note

Ultralytics model/software licensing must be verified before public or commercial release.

Until legal/licensing status is reviewed by the human owner, documentation should not claim unrestricted commercial/proprietary use.

This is a release risk and should remain tracked in `docs/LIMITATIONS.md` and `docs/REMEDIATION_MATRIX.md` if unresolved.
