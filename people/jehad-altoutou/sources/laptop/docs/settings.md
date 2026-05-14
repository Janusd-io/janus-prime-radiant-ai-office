---
type: source
source_type: laptop
title: settings
slug: settings
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/organizations/settings.html
original_size: 13923
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
---

# settings

_Extracted from `brightbean-studio/templates/organizations/settings.html` on 2026-05-14._

{% extends "layouts/settings.html" %} {% block title %}General -
Settings - Brightbean{% endblock %} {% block content %}

<div class="max-w-2xl">

## General

{% csrf_token %}

<div class="flex items-end gap-4">

<div class="flex-1">

Organization Name

</div>

Save Changes

</div>

{% csrf_token %}

<div class="flex items-end gap-4">

<div class="flex-1" @click.away="open = false; search = ''">

Default Timezone

Used as the fallback for workspaces that don't set their own.

<span x-text="selected || 'Select timezone'"></span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0cmFuc2l0aW9uLXRyYW5zZm9ybSBmbGV4LXNocmluay0wIiA6Y2xhc3M9Im9wZW4gJmFtcDsmYW1wOyAmIzM5O3JvdGF0ZS0xODAmIzM5OyIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LXRlcnRpYXJ5KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTkgOWwtNyA3LTctNyIgLz48L3N2Zz4="
class="w-4 h-4 transition-transform flex-shrink-0" />

<div class="bg-white rounded-xl shadow-lg ring-1 ring-stone-200 overflow-hidden"
x-show="open" x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
:style="'position:fixed; top:' + pos.top + '; left:' + pos.left + '; width:' + pos.width + '; z-index:9999;'"
x-cloak="">

<div class="p-2 border-b border-stone-100">

</div>

<div class="max-h-64 overflow-y-auto">

<div class="px-2 pt-2 pb-1">

Common

{% for tz in common_timezones %}

{{ tz }}

{% endfor %}

</div>

<div class="px-2 pb-2">

All Timezones

{% for tz in all_timezones %}

{{ tz }}

{% endfor %}

</div>

</div>

</div>

</div>

Save Changes

</div>

{% if is_owner %}

------------------------------------------------------------------------

{% if organization.is_deletion_pending %}

<div class="rounded-lg p-4 mb-4"
style="background: var(--error-soft, #FEE2E2); border: 1px solid var(--error-500, #EF4444);">

<div class="flex items-start justify-between gap-4">

<div>

### Deletion scheduled

This organization is scheduled for deletion on **{{
organization.deletion_scheduled_for\|date:"F j, Y" }}**. All workspaces,
posts, social accounts, media, and team data will be permanently removed
after this date.

</div>

{% csrf_token %}

Cancel Deletion

</div>

</div>

{% else %}

<div x-data="{ showDeleteModal: false }">

<div class="flex items-start justify-between gap-4">

<div>

### Delete this organization

Permanently delete this organization and all of its data. This includes
all workspaces, scheduled posts, social accounts, media assets, and team
memberships.

</div>

Delete Organization

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

### Delete this organization

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

<div class="px-6 py-5">

Are you sure you want to delete **{{ organization.name }}**? This will
schedule the organization for permanent deletion in 14 days.

All of the following will be permanently removed:

- All workspaces and their settings
- All scheduled and published posts
- Connected social accounts and credentials
- Media assets and files
- Team memberships and invitations

</div>

<div class="flex justify-end gap-3 px-6 py-4"
style="border-top: 1px solid var(--border);">

Cancel

{% csrf_token %}

Yes, delete this organization

</div>

</div>

</div>

</div>

{% endif %} {% endif %}

</div>

{% endblock %}
