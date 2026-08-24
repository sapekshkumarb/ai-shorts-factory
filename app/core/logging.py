"""Logging configuration."""

import logging
import logging.handlers
from pathlib import Path


def configure_logging(level: str = "INFO") -> None:
    """Configure structured logging."""
    log_level = getattr(logging, level.upper(), logging.INFO)

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler
    log_file = Path("./data/logs/app.log")
    log_file.parent.mkdir(parents=True, exist_ok=True)

    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10_000_000,  # 10MB
        backupCount=10,
    )
    file_handler.setLevel(log_level)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
