from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.

    Loads settings from environment variables or .env file.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    # Project configuration
    PROJECT_NAME: str = "FastAPI Todo API"
    PROJECT_DESCRIPTION: str = "A template backend web service using FastAPI"
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"

    # Environment configuration
    ENV: str = "development"
    DEBUG: bool = True

    @field_validator("ENV")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Validate that the environment is one of the expected values."""
        allowed_environments = ["development", "test", "production"]
        if v not in allowed_environments:
            raise ValueError(f"Environment must be one of {allowed_environments}")
        return v


settings = Settings()
