---
type: source
source_type: laptop
title: admin
slug: admin-3
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/social_accounts/admin.py
original_size: 774
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# admin

_Extracted from `brightbean-studio/apps/social_accounts/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import MastodonAppRegistration, SocialAccount


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = (
        "account_name",
        "platform",
        "workspace",
        "connection_status",
        "connected_at",
    )
    list_filter = ("platform", "connection_status")
    search_fields = ("account_name", "account_handle")
    readonly_fields = ("id", "created_at", "updated_at")
    exclude = ("oauth_access_token", "oauth_refresh_token")


@admin.register(MastodonAppRegistration)
class MastodonAppRegistrationAdmin(admin.ModelAdmin):
    list_display = ("instance_url", "created_at")
    readonly_fields = ("id", "created_at")
    exclude = ("client_id", "client_secret")

```