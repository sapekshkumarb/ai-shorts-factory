"""Application-wide exceptions."""


class AIShortFactoryException(Exception):
    """Base exception for all application errors."""

    def __init__(self, code: str, message: str, stage: str | None = None):
        self.code = code
        self.message = message
        self.stage = stage
        super().__init__(message)


class ConfigurationError(AIShortFactoryException):
    """Configuration is invalid or missing."""

    pass


class ProviderError(AIShortFactoryException):
    """Provider operation failed."""

    pass


class ProviderUnavailableError(ProviderError):
    """Provider is unavailable."""

    pass


class ProviderTimeoutError(ProviderError):
    """Provider request timed out."""

    pass


class ProjectNotFoundError(AIShortFactoryException):
    """Project does not exist."""

    pass


class AssetNotFoundError(AIShortFactoryException):
    """Asset does not exist."""

    pass


class JobError(AIShortFactoryException):
    """Job operation failed."""

    pass


class ValidationError(AIShortFactoryException):
    """Validation of input failed."""

    pass
