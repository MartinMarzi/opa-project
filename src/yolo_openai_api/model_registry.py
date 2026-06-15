from collections.abc import Mapping


def list_models(settings: Mapping[str, str]) -> list[dict[str, object]]:
    return [
        {
            "id": settings["public_model_name"],
            "object": "model",
            "created": 0,
            "owned_by": "local",
            "root": settings["default_model_file"],
        }
    ]

