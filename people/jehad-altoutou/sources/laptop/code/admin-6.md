---
type: source
source_type: laptop
title: admin
slug: admin-6
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/accounts/admin.py
original_size: 1148
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# admin

_Extracted from `brightbean-studio/apps/accounts/admin.py` on 2026-05-14._

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import OAuthConnection, Session, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("email", "name", "is_active", "is_staff", "created_at")
    list_filter = ("is_active", "is_staff", "totp_enabled")
    search_fields = ("email", "name")
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("name", "avatar")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("2FA", {"fields": ("totp_enabled",)}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)


@admin.register(OAuthConnection)
class OAuthConnectionAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "provider_email", "created_at")
    list_filter = ("provider",)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("user", "device_info", "ip_address", "last_active_at", "expires_at")
    list_filter = ("created_at",)

```