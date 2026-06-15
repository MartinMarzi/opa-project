# Browser Live Demo Plan

Project: **OpenAI-compatible YOLO11 COCO Detection API**

---

## Status

Browser live demo is not part of MVP.

It is a later Beta/RC1-path feature after the API foundation is stable.

---

## Goal

Create a local browser demo that:

1. asks for camera permission;
2. displays the live camera feed;
3. captures frames at controlled intervals;
4. sends frames to the API;
5. receives object detections;
6. draws bounding boxes over the image/video.

---

## Recommended first implementation

Use simple browser technology first:

- plain HTML;
- plain JavaScript;
- `navigator.mediaDevices.getUserMedia()`;
- `<video>` element;
- `<canvas>` for frame capture;
- second overlay `<canvas>` for boxes;
- repeated `fetch()` calls to `POST /v1/detections`;
- client-side throttling.

Do not start with React unless the UI becomes complex.

---

## Why not use chat completions for live video

`/v1/chat/completions` is useful for OpenAI-style SDK compatibility.

Live video is a different interaction pattern: the client sends many frames over time and receives many detection results.

For browser live detection, use:

- repeated calls to `/v1/detections` first;
- optional WebSocket later.

---

## Browser API-key warning

Do not commit a real API key in browser JavaScript.

For local demo only, the browser page may ask the user to paste a local API key at runtime.

For public hosted use, the single-key model is unsafe because the key would be visible to users.

A public browser deployment requires a separate design decision.

---

## Performance rules

Because the service is CPU-only:

- do not send every camera frame by default;
- start with 1-5 FPS target, depending on benchmark results;
- prevent overlapping requests;
- downscale frames before sending;
- display inference latency;
- allow the user to pause/resume detection.

---

## Planned browser PRs

| PR | Goal |
|---|---|
| Browser PR 1 | Static page with camera permission and video preview. |
| Browser PR 2 | Capture one frame to canvas. |
| Browser PR 3 | Send one captured frame to `/v1/detections` and display JSON. |
| Browser PR 4 | Draw boxes on canvas. |
| Browser PR 5 | Add throttling and no-overlap request loop. |
| Browser PR 6 | Document local-only security limitations. |

---

## Not in first browser demo

- user login;
- public hosted auth;
- WebRTC;
- video file upload;
- tracking across frames;
- GPU acceleration;
- React/Vite unless explicitly chosen later.
