---
type: source
source_type: laptop
title: Brightbean Studio — admin
slug: admin-10
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/approvals/admin.py
original_size: 923
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

_Extracted from `brightbean-studio/apps/approvals/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import ApprovalAction, ApprovalReminder, PostComment


@admin.register(ApprovalAction)
class ApprovalActionAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "action", "created_at")
    list_filter = ("action", "created_at")
    search_fields = ("post__caption", "user__email")
    readonly_fields = ("id", "created_at")


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "visibility", "created_at", "deleted_at")
    list_filter = ("visibility", "created_at")
    search_fields = ("body", "author__email")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(ApprovalReminder)
class ApprovalReminderAdmin(admin.ModelAdmin):
    list_display = ("post", "stage", "reminder_count", "last_reminder_at", "escalated")
    list_filter = ("stage", "escalated")
    readonly_fields = ("id",)

```