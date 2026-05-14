---
type: source
source_type: laptop
title: urls_root
slug: urls-root
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/accounts/urls_root.py
original_size: 118
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# urls_root

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/accounts/urls_root.py` on 2026-05-14._

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]

```