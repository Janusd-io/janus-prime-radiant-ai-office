---
type: source
source_type: laptop
title: urls_org
slug: urls-org
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/media_library/urls_org.py
original_size: 334
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# urls_org

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/media_library/urls_org.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "media_library_org"

urlpatterns = [
    path("shared/", views.shared_library_index, name="shared_index"),
    path("shared/upload/", views.shared_upload, name="shared_upload"),
    path("shared/<uuid:asset_id>/", views.shared_asset_detail, name="shared_asset_detail"),
]

```