---
type: source
source_type: laptop
title: admin
slug: admin-4
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/client_portal/admin.py
original_size: 387
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# admin

_Extracted from `brightbean-studio/apps/client_portal/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import MagicLinkToken


@admin.register(MagicLinkToken)
class MagicLinkTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "workspace", "created_at", "expires_at", "is_consumed")
    list_filter = ("is_consumed", "created_at")
    search_fields = ("user__email", "workspace__name")
    readonly_fields = ("id", "token", "created_at")

```