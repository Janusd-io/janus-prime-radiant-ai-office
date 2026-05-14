---
type: source
source_type: laptop
title: Brightbean Studio — admin
slug: admin-8
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/members/admin.py
original_size: 978
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# admin

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/members/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import CustomRole, Invitation, OrgMembership, WorkspaceMembership


@admin.register(OrgMembership)
class OrgMembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "org_role", "invited_at", "accepted_at")
    list_filter = ("org_role",)
    search_fields = ("user__email",)


@admin.register(WorkspaceMembership)
class WorkspaceMembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "workspace", "workspace_role", "custom_role", "added_at")
    list_filter = ("workspace_role",)
    search_fields = ("user__email",)


@admin.register(CustomRole)
class CustomRoleAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "created_at")
    search_fields = ("name",)


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ("email", "organization", "invited_by", "expires_at", "accepted_at")
    list_filter = ("accepted_at",)
    search_fields = ("email",)

```