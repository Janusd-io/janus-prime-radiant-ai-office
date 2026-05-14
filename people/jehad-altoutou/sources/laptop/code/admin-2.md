---
type: source
source_type: laptop
title: admin
slug: admin-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/inbox/admin.py
original_size: 1314
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# admin

_Extracted from `brightbean-studio/apps/inbox/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import InboxMessage, InboxReply, InboxSLAConfig, InternalNote, SavedReply


@admin.register(InboxMessage)
class InboxMessageAdmin(admin.ModelAdmin):
    list_display = [
        "sender_name",
        "message_type",
        "status",
        "sentiment",
        "social_account",
        "received_at",
    ]
    list_filter = ["message_type", "status", "sentiment"]
    search_fields = ["sender_name", "sender_handle", "body"]
    raw_id_fields = ["workspace", "social_account", "assigned_to", "parent_message", "related_post"]


@admin.register(InboxReply)
class InboxReplyAdmin(admin.ModelAdmin):
    list_display = ["inbox_message", "author", "sent_at"]
    raw_id_fields = ["inbox_message", "author"]


@admin.register(InternalNote)
class InternalNoteAdmin(admin.ModelAdmin):
    list_display = ["inbox_message", "author", "created_at"]
    raw_id_fields = ["inbox_message", "author"]


@admin.register(SavedReply)
class SavedReplyAdmin(admin.ModelAdmin):
    list_display = ["title", "workspace", "created_by", "updated_at"]
    raw_id_fields = ["workspace", "created_by"]


@admin.register(InboxSLAConfig)
class InboxSLAConfigAdmin(admin.ModelAdmin):
    list_display = ["workspace", "target_response_minutes", "is_active"]
    raw_id_fields = ["workspace"]

```