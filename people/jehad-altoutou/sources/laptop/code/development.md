---
type: source
source_type: laptop
title: development
slug: development
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/config/settings/development.py
original_size: 752
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---

# development

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/config/settings/development.py` on 2026-05-14._

```python
from .base import *  # noqa: F401, F403

DEBUG = True
ALLOWED_HOSTS = ["*"]

# Plain storage in dev — no manifest needed, runserver uses finders directly.
STORAGES["staticfiles"] = {  # noqa: F405
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
}

# Use console email backend in development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Disable CSP in development
CSP_REPORT_ONLY = True

# Django debug toolbar (optional)
try:
    import debug_toolbar  # noqa: F401

    INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa: F405
    INTERNAL_IPS = ["127.0.0.1"]
except ImportError:
    pass

SESSION_COOKIE_SECURE = False

```