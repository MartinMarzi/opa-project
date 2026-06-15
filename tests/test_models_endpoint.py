import pytest
from fastapi.testclient import TestClient

from yolo_openai_api.config import get_settings
from yolo_openai_api.main import app


@pytest.fixture(autouse=True)
def clear_settings_cache() -> None:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


def test_models_endpoint_requires_auth(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("YOLO_API_KEY", "local-test-key")
    client = TestClient(app)

    response = client.get("/v1/models")

    assert response.status_code == 401
    assert "error" in response.json()


def test_models_endpoint_rejects_wrong_token(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("YOLO_API_KEY", "local-test-key")
    client = TestClient(app)

    response = client.get(
        "/v1/models",
        headers={"Authorization": "Bearer wrong-key"},
    )

    assert response.status_code == 401
    assert response.json()["error"]["code"] == "invalid_api_key"


def test_models_endpoint_returns_single_model(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("YOLO_API_KEY", "local-test-key")
    client = TestClient(app)

    response = client.get(
        "/v1/models",
        headers={"Authorization": "Bearer local-test-key"},
    )

    body = response.json()
    assert response.status_code == 200
    assert body["object"] == "list"
    assert isinstance(body["data"], list)
    assert len(body["data"]) == 1

    model = body["data"][0]
    assert model["id"] == "yolo11n-coco"
    assert model["object"] == "model"
    assert model["owned_by"] == "local"
    assert model["root"] == "yolo11n.pt"


def test_health_still_public(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("YOLO_API_KEY", raising=False)
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "openai-compatible-yolo11-coco-detection-api",
    }

