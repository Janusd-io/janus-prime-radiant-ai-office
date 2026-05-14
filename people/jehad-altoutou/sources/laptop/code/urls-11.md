---
type: source
source_type: laptop
title: urls
slug: urls-11
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/members/urls.py
original_size: 722
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

_Extracted from `brightbean-studio/apps/members/urls.py` on 2026-05-14._

```python
from django.urls import path

from . import views

app_name = "members"

urlpatterns = [
    path("", views.member_list, name="list"),
    path("invite/", views.invite_member, name="invite"),
    path("invite/<uuid:invitation_id>/resend/", views.resend_invite, name="resend_invite"),
    path("invite/<uuid:invitation_id>/revoke/", views.revoke_invite, name="revoke_invite"),
    path("invite/<str:token>/accept/", views.accept_invite, name="accept_invite"),
    path("<uuid:membership_id>/role/", views.update_member_role, name="update_role"),
    path("<uuid:membership_id>/remove/", views.remove_member, name="remove"),
    path("<uuid:membership_id>/workspaces/", views.manage_workspaces, name="manage_workspaces"),
]

```