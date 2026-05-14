---
type: source
source_type: laptop
title: settings
slug: settings-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/workspaces/settings.html
original_size: 16299
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# settings

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/workspaces/settings.html` on 2026-05-14._

{% extends "layouts/workspace_settings.html" %} {% block title
%}Settings - {{ workspace.name }} - Brightbean{% endblock %} {% block
content %}

<div class="max-w-2xl">

## General

{% csrf_token %}

<div class="flex items-end gap-4">

<div class="flex-1">

Workspace Name

</div>

Save Changes

</div>

{% csrf_token %}

<div class="flex items-center justify-between mb-10">

<div class="flex items-center gap-4">

<div class="relative">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAiIGhlaWdodD0iMTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMyIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

<div class="w-16 h-16 rounded-lg flex items-center justify-center"
style="background: var(--neutral-200);">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0eWxlPSJjb2xvcjogdmFyKC0tbmV1dHJhbC00MDApOyI+PHJlY3QgeD0iMyIgeT0iMyIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiByeD0iMiIgcnk9IjIiIC8+PGNpcmNsZSBjeD0iOC41IiBjeT0iOC41IiByPSIxLjUiPjwvY2lyY2xlPjxwb2x5bGluZSBwb2ludHM9IjIxIDE1IDE2IDEwIDUgMjEiPjwvcG9seWxpbmU+PC9zdmc+)

</div>

<div>

Logo

JPEG, PNG, WebP, or GIF. Max 2 MB.

</div>

</div>

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMjEgMTV2NGEyIDIgMCAwMS0yIDJINWEyIDIgMCAwMS0yLTJ2LTQiIC8+PHBvbHlsaW5lIHBvaW50cz0iMTcgOCAxMiAzIDcgOCI+PC9wb2x5bGluZT48bGluZSB4MT0iMTIiIHkxPSIzIiB4Mj0iMTIiIHkyPSIxNSI+PC9saW5lPjwvc3ZnPg==)
Upload Logo

</div>

{% if is_owner_or_manager %}

------------------------------------------------------------------------

<div x-data="{ showArchiveModal: false }">

<div class="flex items-start justify-between gap-4 mb-10">

<div>

### {% if workspace.is_archived %}Restore this workspace{% else %}Archive this workspace{% endif %}

{% if workspace.is_archived %} This workspace is currently archived.
Restoring it will make it visible in the sidebar and accessible to all
members again. {% elif can_archive %} Archiving hides this workspace
from the sidebar and prevents new posts. All existing data is preserved
and the workspace can be restored at any time. {% else %} You cannot
archive the last active workspace in the organization. Create another
workspace first. {% endif %}

</div>

{% if workspace.is_archived %}

{% csrf_token %}

Restore Workspace

{% elif can_archive %}

Archive Workspace

<div class="fixed inset-0 z-50 flex items-center justify-center"
x-show="showArchiveModal" x-transition.opacity=""
@keydown.escape.window="showArchiveModal = false"
style="background: rgba(0,0,0,0.4);">

<div class="w-full max-w-md rounded-xl shadow-xl"
@click.outside="showArchiveModal = false" x-show="showArchiveModal"
x-transition="" style="background: var(--surface-0);">

<div class="flex items-center justify-between px-6 py-4"
style="border-bottom: 1px solid var(--border);">

### Archive this workspace

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

<div class="px-6 py-5">

Are you sure you want to archive **{{ workspace.name }}**? The workspace
will be hidden from the sidebar and no new posts can be created. All
existing data will be preserved.

</div>

<div class="flex justify-end gap-3 px-6 py-4"
style="border-top: 1px solid var(--border);">

Cancel

{% csrf_token %}

Yes, archive this workspace

</div>

</div>

</div>

{% endif %}

</div>

</div>

<div x-data="{ showDeleteModal: false }">

<div class="flex items-start justify-between gap-4">

<div>

### Delete this workspace

{% if can_delete %} Permanently delete this workspace and all of its
data. This includes all posts, connected social accounts, media assets,
and workspace memberships. This action cannot be undone. {% else %} You
cannot delete the last active workspace in the organization. Create
another workspace first. {% endif %}

</div>

{% if can_delete %}

Delete Workspace

{% endif %}

</div>

{% if can_delete %}

<div class="fixed inset-0 z-50 flex items-center justify-center"
x-show="showDeleteModal" x-transition.opacity=""
@keydown.escape.window="showDeleteModal = false"
style="background: rgba(0,0,0,0.4);">

<div class="w-full max-w-md rounded-xl shadow-xl"
@click.outside="showDeleteModal = false" x-show="showDeleteModal"
x-transition="" style="background: var(--surface-0);">

<div class="flex items-center justify-between px-6 py-4"
style="border-bottom: 1px solid var(--border);">

### Delete this workspace

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIj48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

</div>

<div class="px-6 py-5">

Are you sure you want to permanently delete **{{ workspace.name }}**?
This action cannot be undone.

All of the following will be permanently removed:

- All scheduled and published posts
- Connected social accounts
- Media assets and files
- Workspace memberships

</div>

<div class="flex justify-end gap-3 px-6 py-4"
style="border-top: 1px solid var(--border);">

Cancel

{% csrf_token %}

Yes, delete this workspace

</div>

</div>

</div>

{% endif %}

</div>

{% endif %}

</div>

{% endblock %}
