---
type: source
source_type: laptop
title: Brightbean Studio — models
slug: models-6
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/client_portal/models.py
original_size: 1708
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# models

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/client_portal/models.py` on 2026-05-14._

```python
"""Client Portal models (F-1.4).

Models:
    MagicLinkToken - Time-limited token for passwordless client access.
"""

import secrets
import uuid
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone


def _generate_magic_token():
    return secrets.token_urlsafe(48)


def _default_expiry():
    return timezone.now() + timedelta(days=30)


class MagicLinkToken(models.Model):
    """A magic link token for passwordless client portal access."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="magic_link_tokens",
    )
    workspace = models.ForeignKey(
        "workspaces.Workspace",
        on_delete=models.CASCADE,
        related_name="magic_link_tokens",
    )
    token = models.CharField(
        max_length=128,
        unique=True,
        db_index=True,
        default=_generate_magic_token,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=_default_expiry)
    last_used_at = models.DateTimeField(null=True, blank=True)
    is_consumed = models.BooleanField(default=False)

    class Meta:
        db_table = "client_portal_magic_link_token"
        indexes = [
            models.Index(fields=["user", "workspace"], name="idx_magic_user_ws"),
        ]

    def __str__(self):
        return f"MagicLink for {self.user} → {self.workspace}"

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

    @property
    def is_valid(self):
        return not self.is_expired

```