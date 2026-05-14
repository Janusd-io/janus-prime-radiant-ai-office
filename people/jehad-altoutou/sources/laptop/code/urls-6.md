---
type: source
source_type: laptop
title: urls
slug: urls-6
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/client_portal/urls.py
original_size: 907
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# urls

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/client_portal/urls.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "client_portal"

urlpatterns = [
    path("expired/", views.magic_link_expired, name="magic_link_expired"),
    path("", views.portal_dashboard, name="dashboard"),
    path("approvals/", views.portal_approval_queue, name="approval_queue"),
    path("approvals/<uuid:post_id>/approve/", views.portal_approve, name="approve"),
    path("approvals/<uuid:post_id>/request-changes/", views.portal_request_changes, name="request_changes"),
    path("approvals/<uuid:post_id>/reject/", views.portal_reject, name="reject"),
    path("published/", views.portal_published, name="published"),
    path("activity/", views.portal_activity, name="activity"),
    path("reports/", views.portal_reports, name="reports"),
    # Magic link entry must be last (catches any token string)
    path("<str:token>/", views.magic_link_entry, name="magic_link_entry"),
]

```