---
type: source
source_type: laptop
title: urls_admin
slug: urls-admin
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/client_portal/urls_admin.py
original_size: 427
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# urls_admin

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/client_portal/urls_admin.py` on 2026-05-14._

```python
from django.urls import path

from . import views_admin

app_name = "client_portal_admin"

urlpatterns = [
    path("", views_admin.client_list, name="client_list"),
    path("invite/", views_admin.invite_client, name="invite_client"),
    path("<uuid:membership_id>/send-link/", views_admin.send_magic_link, name="send_magic_link"),
    path("<uuid:membership_id>/remove/", views_admin.remove_client, name="remove_client"),
]

```