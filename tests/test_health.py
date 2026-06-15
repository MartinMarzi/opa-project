from fastapi.testclient import TestClient

from yolo_openai_api.main import app


def test_health_returns_ok_response() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "openai-compatible-yolo11-coco-detection-api",
    }

