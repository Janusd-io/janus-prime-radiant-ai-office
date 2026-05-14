---
type: source
source_type: laptop
title: urls
slug: urls-9
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/accounts/urls.py
original_size: 279
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# urls

_Extracted from `brightbean-studio/apps/accounts/urls.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("accept-terms/", views.accept_terms, name="accept_terms"),
    path("settings/", views.account_settings, name="settings"),
    path("logout/", views.logout_view, name="logout"),
]

```