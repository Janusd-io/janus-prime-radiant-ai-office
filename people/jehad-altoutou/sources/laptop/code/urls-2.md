---
type: source
source_type: laptop
title: urls
slug: urls-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/organizations/urls.py
original_size: 313
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# urls

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/organizations/urls.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "organizations"

urlpatterns = [
    path("settings/", views.settings_view, name="settings"),
    path("workspaces/", views.workspaces_view, name="workspaces"),
    path("calendar/", views.cross_workspace_calendar, name="cross_workspace_calendar"),
]

```