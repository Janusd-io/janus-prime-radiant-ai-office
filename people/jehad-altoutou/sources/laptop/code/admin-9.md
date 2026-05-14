---
type: source
source_type: laptop
title: admin
slug: admin-9
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/media_library/admin.py
original_size: 921
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# admin

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/media_library/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import MediaAsset, MediaAssetVersion, MediaFolder


@admin.register(MediaFolder)
class MediaFolderAdmin(admin.ModelAdmin):
    list_display = ("name", "workspace", "parent_folder", "created_at")
    list_filter = ("workspace",)
    search_fields = ("name",)


@admin.register(MediaAsset)
class MediaAssetAdmin(admin.ModelAdmin):
    list_display = (
        "filename",
        "media_type",
        "workspace",
        "uploaded_by",
        "processing_status",
        "created_at",
    )
    list_filter = ("media_type", "processing_status", "is_starred")
    search_fields = ("filename",)
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(MediaAssetVersion)
class MediaAssetVersionAdmin(admin.ModelAdmin):
    list_display = ("media_asset", "version_number", "change_description", "created_by", "created_at")
    list_filter = ("created_at",)

```