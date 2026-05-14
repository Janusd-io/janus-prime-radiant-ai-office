---
type: source
source_type: laptop
title: test
slug: test
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/config/settings/test.py
original_size: 1197
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---

# test

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/config/settings/test.py` on 2026-05-14._

```python
import os

os.environ.setdefault("SECRET_KEY", "test-secret-key-not-for-production")
os.environ.setdefault("ENCRYPTION_KEY_SALT", "test-salt-not-for-production")

from .base import *  # noqa: F401, F403

DEBUG = False
ALLOWED_HOSTS = ["*"]

# Use faster password hasher in tests
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# Use in-memory email backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Disable CSP in tests
CSP_REPORT_ONLY = True

# Use local storage in tests
STORAGE_BACKEND = "local"
MEDIA_ROOT = BASE_DIR / "test_media"  # noqa: F405

# Use simple static files storage in tests (no manifest/collectstatic needed)
STORAGES["staticfiles"] = {  # noqa: F405
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "brightbean_test",
        "USER": env("DB_USER", default="postgres"),  # noqa: F405
        "PASSWORD": env("DB_PASSWORD", default="postgres"),  # noqa: F405
        "HOST": env("DB_HOST", default="localhost"),  # noqa: F405
        "PORT": env.int("DB_PORT", default=5432),  # noqa: F405
    },
}

```