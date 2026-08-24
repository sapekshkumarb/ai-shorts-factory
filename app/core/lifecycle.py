"""Application lifecycle handlers."""

import logging

logger = logging.getLogger(__name__)


async def startup_handler() -> None:
    """Handle application startup."""
    logger.info("Initializing AI Shorts Factory")
    # Future: Initialize database, connect to providers, etc.


async def shutdown_handler() -> None:
    """Handle application shutdown."""
    logger.info("Shutting down AI Shorts Factory")
    # Future: Close database connections, cleanup resources, etc.
