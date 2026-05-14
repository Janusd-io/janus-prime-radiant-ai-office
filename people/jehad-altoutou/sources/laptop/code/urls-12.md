---
type: source
source_type: laptop
title: urls
slug: urls-12
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/media_library/urls.py
original_size: 1441
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# urls

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/media_library/urls.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "media_library"

urlpatterns = [
    path("", views.library_index, name="index"),
    path("upload/", views.upload, name="upload"),
    path("search/", views.search, name="search"),
    # Folders
    path("folders/create/", views.folder_create, name="folder_create"),
    path("folders/<uuid:folder_id>/rename/", views.folder_rename, name="folder_rename"),
    path("folders/<uuid:folder_id>/delete/", views.folder_delete, name="folder_delete"),
    # Tags
    path("tags/autocomplete/", views.tag_autocomplete, name="tag_autocomplete"),
    # Assets
    path("<uuid:asset_id>/", views.asset_detail, name="asset_detail"),
    path("<uuid:asset_id>/edit/", views.asset_edit, name="asset_edit"),
    path("<uuid:asset_id>/star/", views.asset_star_toggle, name="asset_star"),
    path("<uuid:asset_id>/tags/", views.asset_update_tags, name="asset_tags"),
    path("<uuid:asset_id>/move/", views.asset_move, name="asset_move"),
    path("<uuid:asset_id>/delete/", views.asset_delete, name="asset_delete"),
    path("<uuid:asset_id>/download/", views.asset_download, name="asset_download"),
    path("<uuid:asset_id>/versions/", views.version_list, name="version_list"),
    path("<uuid:asset_id>/versions/<uuid:version_id>/restore/", views.version_restore, name="version_restore"),
    path("<uuid:asset_id>/processing-status/", views.processing_status, name="processing_status"),
]

```