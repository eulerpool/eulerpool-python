from __future__ import annotations

class EulerpoolError(Exception):
    """Base exception for Eulerpool API errors."""

    def __init__(self, message: str, status: int = 0, code: str = "api_error"):
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code


class AuthenticationError(EulerpoolError):
    """Raised when the API key is invalid or missing."""

    def __init__(self, message: str = "Invalid or missing API key."):
        super().__init__(message, status=401, code="authentication_error")


class NotFoundError(EulerpoolError):
    """Raised when the requested resource is not found."""

    def __init__(self, message: str = "The requested resource was not found."):
        super().__init__(message, status=404, code="not_found")


class RateLimitError(EulerpoolError):
    """Raised when rate limit is exceeded."""

    def __init__(self, message: str = "Rate limit exceeded.", retry_after=None):
        super().__init__(message, status=429, code="rate_limit_exceeded")
        self.retry_after = retry_after


class BadRequestError(EulerpoolError):
    """Raised on 400 bad request."""

    def __init__(self, message: str = "Bad request."):
        super().__init__(message, status=400, code="bad_request")


class ServerError(EulerpoolError):
    """Raised on 5xx server errors."""

    def __init__(self, message: str = "Internal server error."):
        super().__init__(message, status=500, code="server_error")
