"""Health and diagnostics endpoints."""

import logging
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.config import settings

logger = logging.getLogger(__name__)
router = APIRouter(prefix="", tags=["health"])


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    version: str
    environment: str
    debug: bool


class ProviderStatus(BaseModel):
    """Status of a single provider."""

    status: str  # OK, WARNING, ERROR, NOT_CONFIGURED
    provider: str | None = None
    message: str | None = None


class ProvidersHealthResponse(BaseModel):
    """Health check response for all providers."""

    overall_status: str  # OK, WARNING, ERROR
    providers: dict[str, ProviderStatus]


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Basic health check."""
    return HealthResponse(
        status="OK",
        version="0.1.0",
        environment=settings.environment,
        debug=settings.debug,
    )


@router.get("/health/providers", response_model=ProvidersHealthResponse)
async def health_providers() -> ProvidersHealthResponse:
    """Check health of all configured providers."""
    providers: dict[str, ProviderStatus] = {}
    overall_status = "OK"

    # LLM Provider
    if settings.offline_mode or settings.llm_provider == "mock":
        providers["llm"] = ProviderStatus(
            status="OK",
            provider=settings.llm_provider,
            message="Using mock provider",
        )
    else:
        providers["llm"] = ProviderStatus(
            status="NOT_CONFIGURED",
            provider=settings.llm_provider,
            message=f"Provider {settings.llm_provider} not yet implemented",
        )
        overall_status = "WARNING"

    # TTS Provider
    if settings.offline_mode or settings.tts_provider == "mock":
        providers["tts"] = ProviderStatus(
            status="OK",
            provider=settings.tts_provider,
            message="Using mock provider",
        )
    else:
        providers["tts"] = ProviderStatus(
            status="NOT_CONFIGURED",
            provider=settings.tts_provider,
            message=f"Provider {settings.tts_provider} not yet implemented",
        )
        overall_status = "WARNING"

    # Video Provider
    if settings.offline_mode or settings.video_provider == "mock":
        providers["video"] = ProviderStatus(
            status="OK",
            provider=settings.video_provider,
            message="Using mock provider",
        )
    else:
        providers["video"] = ProviderStatus(
            status="NOT_CONFIGURED",
            provider=settings.video_provider,
            message=f"Provider {settings.video_provider} not yet implemented",
        )
        overall_status = "WARNING"

    # Research Provider
    if settings.offline_mode or settings.research_provider == "mock":
        providers["research"] = ProviderStatus(
            status="OK",
            provider=settings.research_provider,
            message="Using mock provider",
        )
    else:
        providers["research"] = ProviderStatus(
            status="NOT_CONFIGURED",
            provider=settings.research_provider,
            message=f"Provider {settings.research_provider} not yet implemented",
        )
        overall_status = "WARNING"

    # Publishing Providers
    providers["youtube"] = ProviderStatus(
        status="NOT_CONFIGURED",
        message="Not yet implemented",
    )
    providers["facebook"] = ProviderStatus(
        status="NOT_CONFIGURED",
        message="Not yet implemented",
    )
    providers["instagram"] = ProviderStatus(
        status="NOT_CONFIGURED",
        message="Not yet implemented",
    )

    return ProvidersHealthResponse(
        overall_status=overall_status,
        providers=providers,
    )
