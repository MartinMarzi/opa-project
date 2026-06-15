from fastapi.testclient import TestClient

from yolo_openai_api.config import Settings, get_settings
from yolo_openai_api.main import app


def test_default_settings_use_expected_product_identity() -> None:
    settings = Settings()

    assert settings.service_name == "openai-compatible-yolo11-coco-detection-api"
    assert settings.public_model_name == "yolo11n-coco"
    assert settings.default_model_file == "yolo11n.pt"


def test_environment_override_applies_to_model_settings(monkeypatch) -> None:
    monkeypatch.setenv("YOLO_PUBLIC_MODEL_NAME", "custom-model")
    monkeypatch.setenv("YOLO_MODEL_FILE", "custom.pt")
    get_settings.cache_clear()

    settings = Settings()

    assert settings.public_model_name == "custom-model"
    assert settings.default_model_file == "custom.pt"


def test_health_uses_configured_service_name(monkeypatch) -> None:
    monkeypatch.setenv("YOLO_API_SERVICE_NAME", "openai-compatible-yolo11-coco-detection-api")
    get_settings.cache_clear()

    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "openai-compatible-yolo11-coco-detection-api",
    }
