---
type: source
source_type: laptop
title: urls
slug: urls-14
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/notifications/urls.py
original_size: 499
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# urls

_Extracted from `brightbean-studio/apps/notifications/urls.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "notifications"

urlpatterns = [
    path("", views.notification_list, name="list"),
    path("drawer/", views.notification_drawer, name="drawer"),
    path("unread-count/", views.unread_count, name="unread_count"),
    path("mark-all-read/", views.mark_all_read, name="mark_all_read"),
    path("<uuid:notification_id>/read/", views.mark_as_read, name="mark_as_read"),
    path("preferences/", views.preferences, name="preferences"),
]

```