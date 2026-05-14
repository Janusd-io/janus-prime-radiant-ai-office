---
type: source
source_type: laptop
title: admin
slug: admin-7
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/settings_manager/admin.py
original_size: 493
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

_Extracted from `brightbean-studio/apps/settings_manager/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import OrgSetting, WorkspaceSetting


@admin.register(OrgSetting)
class OrgSettingAdmin(admin.ModelAdmin):
    list_display = ("organization", "key", "value", "updated_at")
    list_filter = ("organization",)
    search_fields = ("key",)


@admin.register(WorkspaceSetting)
class WorkspaceSettingAdmin(admin.ModelAdmin):
    list_display = ("workspace", "key", "value", "updated_at")
    list_filter = ("workspace",)
    search_fields = ("key",)

```