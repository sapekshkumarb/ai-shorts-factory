"""Application configuration."""

import os
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # Application
    app_name: str = "AI Shorts Factory"
    environment: str = os.getenv("ENVIRONMENT", "development")
    debug: bool = environment == "development"

    # API
    api_host: str = os.getenv("API_HOST", "127.0.0.1")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    cors_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]

    # Database
    database_url: str = os.getenv(
        "DATABASE_URL", "sqlite:///./data/app.db"
    )

    # Storage
    storage_dir: Path = Path(os.getenv("STORAGE_DIR", "./data/projects"))
    temp_dir: Path = Path(os.getenv("TEMP_DIR", "./data/temp"))

    # Logging
    logging_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_file: Path = Path(os.getenv("LOG_FILE", "./data/logs/app.log"))

    # LLM Provider
    llm_provider: str = os.getenv("LLM_PROVIDER", "mock")
    llm_model: str = os.getenv("LLM_MODEL", "mock-model")
    llm_api_key: str | None = os.getenv("LLM_API_KEY")
    llm_base_url: str | None = os.getenv("LLM_BASE_URL")
    llm_temperature: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    llm_max_tokens: int = int(os.getenv("LLM_MAX_TOKENS", "4096"))
    llm_timeout: int = int(os.getenv("LLM_TIMEOUT", "60"))
    llm_retry_count: int = int(os.getenv("LLM_RETRY_COUNT", "3"))

    # TTS Provider
    tts_provider: str = os.getenv("TTS_PROVIDER", "mock")
    tts_api_key: str | None = os.getenv("TTS_API_KEY")
    tts_base_url: str | None = os.getenv("TTS_BASE_URL")

    # Video Provider
    video_provider: str = os.getenv("VIDEO_PROVIDER", "mock")
    video_api_key: str | None = os.getenv("VIDEO_API_KEY")
    video_base_url: str | None = os.getenv("VIDEO_BASE_URL")

    # Research Provider
    research_provider: str = os.getenv("RESEARCH_PROVIDER", "mock")
    research_api_key: str | None = os.getenv("RESEARCH_API_KEY")

    # FFmpeg
    ffmpeg_path: str = os.getenv("FFMPEG_PATH", "ffmpeg")

    # Content defaults
    default_language: str = os.getenv("DEFAULT_LANGUAGE", "en")
    default_duration_seconds: int = int(
        os.getenv("DEFAULT_DURATION_SECONDS", "45")
    )
    default_resolution: str = os.getenv("DEFAULT_RESOLUTION", "1080x1920")
    default_fps: int = int(os.getenv("DEFAULT_FPS", "30"))
    default_aspect_ratio: str = os.getenv("DEFAULT_ASPECT_RATIO", "9:16")

    # Job system
    max_concurrent_jobs: int = int(
        os.getenv("MAX_CONCURRENT_JOBS", "2")
    )
    job_timeout_seconds: int = int(os.getenv("JOB_TIMEOUT_SECONDS", "3600"))
    job_retry_max_attempts: int = int(
        os.getenv("JOB_RETRY_MAX_ATTEMPTS", "3")
    )

    # Offline mode
    offline_mode: bool = os.getenv("OFFLINE_MODE", "false").lower() == "true"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Create necessary directories
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)


settings = Settings()
