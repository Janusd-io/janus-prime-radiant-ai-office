---
type: source
source_type: laptop
title: admin
slug: admin-12
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/onboarding/admin.py
original_size: 860
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# admin

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/onboarding/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import ConnectionLink, ConnectionLinkUsage, OnboardingChecklist


@admin.register(ConnectionLink)
class ConnectionLinkAdmin(admin.ModelAdmin):
    list_display = ("workspace", "created_by", "expires_at", "revoked_at", "created_at")
    list_filter = ("workspace",)
    readonly_fields = ("id", "token", "created_at")
    search_fields = ("workspace__name", "created_by__email")


@admin.register(ConnectionLinkUsage)
class ConnectionLinkUsageAdmin(admin.ModelAdmin):
    list_display = ("connection_link", "social_account", "connected_at")
    readonly_fields = ("id", "connected_at")


@admin.register(OnboardingChecklist)
class OnboardingChecklistAdmin(admin.ModelAdmin):
    list_display = ("user", "workspace", "is_dismissed", "dismissed_at")
    list_filter = ("is_dismissed",)
    readonly_fields = ("id",)

```