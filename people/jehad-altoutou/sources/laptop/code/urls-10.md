---
type: source
source_type: laptop
title: urls
slug: urls-10
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/settings_manager/urls.py
original_size: 150
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# urls

_Extracted from `brightbean-studio/apps/settings_manager/urls.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "settings_manager"

urlpatterns = [
    path("", views.settings_index, name="index"),
]

```