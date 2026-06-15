from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    service_name: str = Field(
        default="openai-compatible-yolo11-coco-detection-api",
        validation_alias="YOLO_API_SERVICE_NAME",
    )
    public_model_name: str = Field(
        default="yolo11n-coco",
        validation_alias="YOLO_PUBLIC_MODEL_NAME",
    )
    default_model_file: str = Field(
        default="yolo11n.pt",
        validation_alias="YOLO_MODEL_FILE",
    )
    api_key: str = Field(default="", validation_alias="YOLO_API_KEY")
    max_image_bytes: int = Field(default=5_000_000, validation_alias="YOLO_MAX_IMAGE_BYTES")
    default_confidence_threshold: float = Field(
        default=0.25,
        validation_alias="YOLO_DEFAULT_CONFIDENCE_THRESHOLD",
    )
    max_detections: int = Field(default=100, validation_alias="YOLO_MAX_DETECTIONS")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
