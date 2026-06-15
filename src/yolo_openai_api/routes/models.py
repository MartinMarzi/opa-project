from fastapi import APIRouter

from yolo_openai_api.config import get_settings
from yolo_openai_api.model_registry import list_models

router = APIRouter()


@router.get("/v1/models")
def get_models() -> dict[str, object]:
    settings = get_settings()
    return {
        "object": "list",
        "data": list_models(
            {
                "public_model_name": settings.public_model_name,
                "default_model_file": settings.default_model_file,
            }
        ),
    }

