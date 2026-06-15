import pytest
from fastapi.testclient import TestClient

from yolo_openai_api.config import get_settings
from yolo_openai_api.main import app


@pytest.fixture(autouse=True)
def clear_settings_cache() -> None:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


def test_health_remains_public(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("YOLO_API_KEY", raising=False)
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "openai-compatible-yolo11-coco-detection-api",
    }


def test_v1_without_auth_returns_missing_key_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("YOLO_API_KEY", "local-test-key")
    client = TestClient(app)

    response = client.get("/v1/unknown")

    body = response.json()
    assert response.status_code == 401
    assert "error" in body
    assert body["error"]["type"] == "authentication_error"
    assert body["error"]["code"] == "missing_api_key"


def test_v1_with_malformed_auth_header_returns_invalid_header_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("YOLO_API_KEY", "local-test-key")
    client = TestClient(app)

    response = client.get("/v1/unknown", headers={"Authorization": "Token local-test-key"})

    assert response.status_code == 401
    assert response.json()["error"]["code"] == "invalid_authorization_header"


def test_v1_with_wrong_bearer_token_returns_invalid_key_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("YOLO_API_KEY", "local-test-key")
    client = TestClient(app)

    response = client.get(
        "/v1/unknown",
        headers={"Authorization": "Bearer wrong-key"},
    )

    assert response.status_code == 401
    assert response.json()["error"]["code"] == "invalid_api_key"


def test_v1_with_correct_bearer_token_reaches_not_found(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("YOLO_API_KEY", "local-test-key")
    client = TestClient(app)

    response = client.get(
        "/v1/unknown",
        headers={"Authorization": "Bearer local-test-key"},
    )

    assert response.status_code == 404
    assert response.json()["error"]["code"] == "not_found"


@pytest.mark.parametrize("configured_key", ["", None])
def test_missing_server_key_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
    configured_key: str | None,
) -> None:
    if configured_key is None:
        monkeypatch.delenv("YOLO_API_KEY", raising=False)
    else:
        monkeypatch.setenv("YOLO_API_KEY", configured_key)

    client = TestClient(app)

    response = client.get("/v1/unknown", headers={"Authorization": "Bearer whatever"})

    assert response.status_code == 503
    assert response.json()["error"]["code"] == "api_key_not_configured"

