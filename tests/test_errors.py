from fastapi.testclient import TestClient

from yolo_openai_api.errors import error_body
from yolo_openai_api.main import app


def test_unknown_route_returns_openai_shaped_error() -> None:
    client = TestClient(app)

    response = client.get("/does-not-exist")

    assert response.status_code == 404
    body = response.json()
    assert "error" in body
    assert set(body["error"]) == {"message", "type", "param", "code"}
    assert body["error"]["type"] == "not_found_error"
    assert body["error"]["code"] == "not_found"


def test_health_still_returns_expected_payload() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "openai-compatible-yolo11-coco-detection-api",
    }


def test_error_body_helper_returns_openai_shape() -> None:
    assert error_body(
        "Bad request.",
        error_type="invalid_request_error",
        code="bad_request",
    ) == {
        "error": {
            "message": "Bad request.",
            "type": "invalid_request_error",
            "param": None,
            "code": "bad_request",
        },
    }

