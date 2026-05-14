---
type: source
source_type: laptop
title: admin
slug: admin
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/organizations/admin.py
original_size: 314
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# admin

_Extracted from `brightbean-studio/apps/organizations/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "default_timezone", "created_at", "is_deletion_pending")
    search_fields = ("name",)
    readonly_fields = ("id", "created_at", "updated_at")

```