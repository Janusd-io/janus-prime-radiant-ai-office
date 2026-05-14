---
type: source
source_type: laptop
title: urls
slug: urls-15
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/onboarding/urls.py
original_size: 1692
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# urls

_Extracted from `brightbean-studio/apps/onboarding/urls.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "onboarding"

urlpatterns = [
    # Management (authenticated, workspace-scoped)
    path(
        "<uuid:workspace_id>/links/create/",
        views.create_link,
        name="create_link",
    ),
    path(
        "<uuid:workspace_id>/links/<uuid:link_id>/revoke/",
        views.revoke_link,
        name="revoke_link",
    ),
    path(
        "<uuid:workspace_id>/links/<uuid:link_id>/send-email/",
        views.send_link_email,
        name="send_link_email",
    ),
    path(
        "<uuid:workspace_id>/checklist/",
        views.checklist_partial,
        name="checklist_partial",
    ),
    path(
        "<uuid:workspace_id>/checklist/dismiss/",
        views.dismiss_checklist,
        name="dismiss_checklist",
    ),
    # Public connection link page (NO auth required)
    path(
        "connect/<str:token>/",
        views.connection_page,
        name="connection_page",
    ),
    path(
        "connect/<str:token>/oauth/start/",
        views.connection_oauth_start,
        name="connection_oauth_start",
    ),
    path(
        "connect/<str:token>/done/",
        views.connection_done,
        name="connection_done",
    ),
    path(
        "connect/<str:token>/bluesky/",
        views.connection_bluesky_connect,
        name="connection_bluesky",
    ),
    path(
        "connect/<str:token>/mastodon/",
        views.connection_mastodon_start,
        name="connection_mastodon",
    ),
    # OAuth callback for connection link flow (NO auth, token in state)
    path(
        "connect/callback/<str:platform>/",
        views.connection_oauth_callback,
        name="oauth_callback",
    ),
]

```