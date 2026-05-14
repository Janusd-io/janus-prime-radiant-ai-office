---
type: source
source_type: laptop
title: settings
slug: settings-4
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/accounts/settings.html
original_size: 15534
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---

# settings

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/accounts/settings.html` on 2026-05-14._

{% extends "layouts/settings.html" %} {% block title %}{% if
settings_active == 'preferences' %}Preferences{% else %}Profile{% endif
%} - Settings - Brightbean{% endblock %} {% block content %}

<div class="max-w-2xl">

{% if settings_active == 'preferences' %}

## Preferences

Manage how and when you receive notifications.

{% csrf_token %}

<div class="rounded-xl overflow-hidden"
style="border: 1px solid var(--border);">

<div class="grid gap-0 px-5 py-3"
style="background: var(--neutral-50); border-bottom: 1px solid var(--border); grid-template-columns: 1fr repeat({{ notification_channels|length }}, 80px);">

<span class="text-xs font-semibold uppercase tracking-wider"
style="color: var(--text-tertiary);">Event</span> {% for ch_value,
ch_label in notification_channels %}
<span class="text-xs font-semibold uppercase tracking-wider text-center"
style="color: var(--text-tertiary);">{{ ch_label }}</span> {% endfor %}

</div>

{% for pref in notification_prefs %}

<div class="grid gap-0 px-5 py-3 items-center"
style="{% if not forloop.last %}border-bottom: 1px solid var(--border);{% endif %} grid-template-columns: 1fr repeat({{ notification_channels|length }}, 80px);">

<span class="text-sm" style="color: var(--text-primary);">{{ pref.label
}}</span> {% for ch in pref.channel_list %}

{% endfor %}

</div>

{% endfor %}

</div>

<div class="mt-6">

Save Preferences

</div>

{% else %}

## Profile

{% csrf_token %}

<div class="flex items-center justify-between mb-10">

<div class="flex items-center gap-4">

<div class="relative">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

<div class="w-16 h-16 rounded-full flex items-center justify-center"
style="background: var(--neutral-200);">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0eWxlPSJjb2xvcjogdmFyKC0tbmV1dHJhbC00MDApOyI+PHBhdGggZD0iTTIwIDIxdi0yYTQgNCAwIDAwLTQtNEg4YTQgNCAwIDAwLTQgNHYyIiAvPjxjaXJjbGUgY3g9IjEyIiBjeT0iNyIgcj0iNCI+PC9jaXJjbGU+PC9zdmc+)

</div>

<div>

Photo

Please choose a photo that is at least 180×180 pixels in size.

</div>

</div>

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMjEgMTV2NGEyIDIgMCAwMS0yIDJINWEyIDIgMCAwMS0yLTJ2LTQiIC8+PHBvbHlsaW5lIHBvaW50cz0iMTcgOCAxMiAzIDcgOCI+PC9wb2x5bGluZT48bGluZSB4MT0iMTIiIHkxPSIzIiB4Mj0iMTIiIHkyPSIxNSI+PC9saW5lPjwvc3ZnPg==)
Upload Photo

</div>

{% csrf_token %}

<div class="flex items-end gap-4">

<div class="flex-1">

Name

</div>

Save Changes

</div>

<div class="mb-10">

Email

{{ user.email }}

</div>

{% csrf_token %}

<div class="space-y-4">

<div>

Current password

</div>

<div>

New password

</div>

<div>

Confirm new password

</div>

<div>

Change Password

</div>

</div>

{% if org_membership %}

<div class="mb-10">

Role

<div class="flex items-center gap-3">

<span class="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-full"
style="background: var(--neutral-100); color: var(--text-primary);"> {%
if org_membership.org_role == 'owner' %}
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTIgMmwzLjA5IDYuMjZMMjIgOS4yN2wtNSA0Ljg3IDEuMTggNi44OEwxMiAxNy43N2wtNi4xOCAzLjI1TDcgMTQuMTQgMiA5LjI3bDYuOTEtMS4wMUwxMiAyeiIgLz48L3N2Zz4=)
{% elif org_membership.org_role == 'admin' %}
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTIgMjJzOC00IDgtMTBWNWwtOC0zLTggM3Y3YzAgNiA4IDEwIDggMTB6IiAvPjwvc3ZnPg==)
{% else %}
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMjAgMjF2LTJhNCA0IDAgMDAtNC00SDhhNCA0IDAgMDAtNCA0djIiIC8+PGNpcmNsZSBjeD0iMTIiIGN5PSI3IiByPSI0Ij48L2NpcmNsZT48L3N2Zz4=)
{% endif %} {{ org_membership.get_org_role_display }} </span>
<span class="text-xs" style="color: var(--text-tertiary);"> in {{
org_membership.organization.name }} </span>

</div>

</div>

{% endif %}

------------------------------------------------------------------------

<div x-data="{ showDeleteModal: false }">

<div class="flex items-start justify-between gap-4">

<div>

### Delete your account

When you delete your account, you lose access to Brightbean account
services, and we permanently delete your personal data.

</div>

Delete Account

</div>

<div class="fixed inset-0 z-50 flex items-center justify-center"
x-show="showDeleteModal" x-transition.opacity=""
@keydown.escape.window="showDeleteModal = false"
style="background: rgba(0,0,0,0.4);">

<div class="w-full max-w-md rounded-xl shadow-xl"
@click.outside="showDeleteModal = false" x-show="showDeleteModal"
x-transition="" style="background: var(--surface-0);">

<div class="flex items-center justify-between px-6 py-4"
style="border-bottom: 1px solid var(--border);">

### Delete your account

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

<div class="px-6 py-5">

Are you sure you want to delete your account? This action is permanent
and cannot be undone. You will lose access to all Brightbean services,
and your personal data will be permanently deleted.

</div>

<div class="flex justify-end gap-3 px-6 py-4"
style="border-top: 1px solid var(--border);">

Cancel

{% csrf_token %}

Yes, delete my account

</div>

</div>

</div>

</div>

{% endif %}

</div>

{% endblock %}
