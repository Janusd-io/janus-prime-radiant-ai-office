---
type: source
source_type: laptop
title: admin
slug: admin-11
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/notifications/admin.py
original_size: 1165
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

_Extracted from `brightbean-studio/apps/notifications/admin.py` on 2026-05-14._

```python
from django.contrib import admin

from .models import Notification, NotificationDelivery, NotificationPreference, QuietHours


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "event_type", "is_read", "created_at")
    list_filter = ("event_type", "is_read", "created_at")
    search_fields = ("title", "body", "user__email")
    readonly_fields = ("id", "created_at")
    raw_id_fields = ("user",)


@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ("user", "event_type", "channel", "is_enabled")
    list_filter = ("event_type", "channel", "is_enabled")
    raw_id_fields = ("user",)


@admin.register(NotificationDelivery)
class NotificationDeliveryAdmin(admin.ModelAdmin):
    list_display = ("notification", "channel", "status", "attempts", "delivered_at")
    list_filter = ("channel", "status")
    readonly_fields = ("id", "created_at")


@admin.register(QuietHours)
class QuietHoursAdmin(admin.ModelAdmin):
    list_display = ("user", "is_enabled", "start_time", "end_time", "timezone", "digest_mode")
    raw_id_fields = ("user",)

```