---
type: source
source_type: laptop
title: error_messages
slug: error-messages
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/social_accounts/error_messages.py
original_size: 1377
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# error_messages

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/social_accounts/error_messages.py` on 2026-05-14._

```python
"""User-facing error messages for social account health checks."""

from providers.exceptions import (
    APIError,
    OAuthError,
    RateLimitError,
    TokenExpiredError,
)

RECONNECT_MESSAGE = "Account connection expired. Please reconnect."
RATE_LIMIT_MESSAGE = "Rate limit reached. We'll retry this check shortly."
PLATFORM_UNAVAILABLE_MESSAGE = "The platform is temporarily unavailable. We'll retry shortly."
GENERIC_MESSAGE = "Connection check failed. Please try reconnecting."

_EXPIRED_TOKEN_ERRORS = {
    "ExpiredToken",
    "invalid_token",
    "InvalidToken",
    "invalid_grant",
}


def friendly_health_check_error(exc: Exception) -> str:
    """Map a provider exception to a short, user-facing message."""
    if isinstance(exc, TokenExpiredError):
        return RECONNECT_MESSAGE

    if isinstance(exc, RateLimitError):
        return RATE_LIMIT_MESSAGE

    if isinstance(exc, APIError):
        if exc.status_code in (401, 403):
            return RECONNECT_MESSAGE
        error_code = (exc.raw_response or {}).get("error")
        if error_code in _EXPIRED_TOKEN_ERRORS:
            return RECONNECT_MESSAGE
        if exc.status_code is not None and exc.status_code >= 500:
            return PLATFORM_UNAVAILABLE_MESSAGE
        return GENERIC_MESSAGE

    if isinstance(exc, OAuthError):
        return RECONNECT_MESSAGE

    return GENERIC_MESSAGE

```