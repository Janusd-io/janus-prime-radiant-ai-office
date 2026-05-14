---
type: source
source_type: laptop
title: asset_edit
slug: asset-edit
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/asset_edit.html
original_size: 13209
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# asset_edit

_Extracted from `brightbean-studio/templates/media_library/asset_edit.html` on 2026-05-14._

{% extends "base.html" %} {% load static %} {% block title %}Edit - {{
asset.original_filename }}{% endblock %} {% block extra_head %} {% if
asset.file_type == 'image' or asset.file_type == 'gif' %} {% endif %}
<style>
  .ml-edit-canvas {
    background: var(--surface-1, #FAFAF9);
    border: 1px solid var(--border, #E7E5E4);
    border-radius: var(--radius-xl, 0.75rem);
    overflow: hidden;
  }
  .ml-edit-toolbar {
    background: var(--surface-0, #FFF);
    border: 1px solid var(--border, #E7E5E4);
    border-radius: var(--radius-xl, 0.75rem);
    box-shadow: var(--shadow-sm);
  }
  .ml-tool-btn {
    display: flex; flex-direction: column; align-items: center; gap: 4px;
    padding: 10px 14px;
    border-radius: var(--radius-lg, 0.5rem);
    font-size: 10px; font-weight: 600;
    color: var(--text-secondary, #57534E);
    cursor: pointer;
    transition: all var(--dur-fast, 150ms) ease;
  }
  .ml-tool-btn:hover { background: var(--surface-1, #FAFAF9); color: var(--text-primary, #1C1917); }
  .ml-tool-btn.active { background: var(--primary-soft, #FFF7ED); color: var(--brand-700, #C2410C); }
  .ml-trim-track {
    height: 48px;
    background: var(--surface-2, #F5F5F4);
    border-radius: var(--radius-lg, 0.5rem);
    position: relative;
    overflow: hidden;
  }
  .ml-trim-selection {
    position: absolute; top: 0; bottom: 0;
    background: rgba(249, 115, 22, 0.15);
    border-left: 3px solid var(--primary, #F97316);
    border-right: 3px solid var(--primary, #F97316);
  }
</style> {% endblock %} {% block page_header %}

<div class="flex items-center gap-3">

<a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D"
class="w-8 h-8 rounded-lg flex items-center justify-center transition-colors"
style="color: var(--text-tertiary, #78716C);"
onmouseenter="this.style.background=&#39;var(--surface-2)&#39;"
onmouseleave="this.style.background=&#39;transparent&#39;"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4" /></a>

# Edit - {{ asset.original_filename }}

</div>

{% endblock %} {% block content %} {% if asset.file_type == 'image' or
asset.file_type == 'gif' %}

<div class="space-y-4" x-data="imageCropper()">

<div class="ml-edit-canvas">

<div class="max-h-[500px] overflow-hidden">

<img src="%7B%7B%20asset.file.url%20%7D%7D" class="max-w-full"
style="display: block;" data-x-ref="image"
alt="{{ asset.original_filename }}" />

</div>

</div>

<div class="ml-edit-toolbar p-2">

<div class="flex items-center gap-1">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTMgN2g0bTAgMFYzbTAgNHYxNGgxNG0tNC00aDRtMCAwdjRtMC00SDciIC8+PC9zdmc+"
class="w-5 h-5" /> Crop

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTMgMTBoMWwxLTIgMi0yaDRWMmw1IDUtNSA1VjhIN2wtMSAxLTEgMkgzdi0xeiIgLz48L3N2Zz4="
class="w-5 h-5" /> Rotate Left

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InRyYW5zZm9ybTogc2NhbGVYKC0xKSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTMgMTBoMWwxLTIgMi0yaDRWMmw1IDUtNSA1VjhIN2wtMSAxLTEgMkgzdi0xeiIgLz48L3N2Zz4="
class="w-5 h-5" /> Rotate Right

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTcgMTZWNG0wIDBMMyA4bTQtNGw0IDRtNiAwdjEybTAgMGw0LTRtLTQgNGwtNC00IiAvPjwvc3ZnPg=="
class="w-5 h-5" /> Flip H

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InRyYW5zZm9ybTogcm90YXRlKDkwZGVnKSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTcgMTZWNG0wIDBMMyA4bTQtNGw0IDRtNiAwdjEybTAgMGw0LTRtLTQgNGwtNC00IiAvPjwvc3ZnPg=="
class="w-5 h-5" /> Flip V

<div class="flex-1">

</div>

<a
href="%7B%%20url%20&#39;media_library:asset_detail&#39;%20workspace_id=workspace.id%20asset_id=asset.id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-2 text-xs font-semibold rounded-full border transition-colors"
style="border-color: var(--border); color: var(--text-secondary);"
onmouseenter="this.style.background=&#39;var(--surface-1)&#39;"
onmouseleave="this.style.background=&#39;transparent&#39;">Cancel</a>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjUiIGQ9Ik01IDEzbDQgNEwxOSA3IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> Save as new version

</div>

</div>

{% csrf_token %}

</div>

{% elif asset.file_type == 'video' %}

<div class="space-y-4" x-data="videoTrimmer()">

<div class="ml-edit-canvas">

</div>

<div class="ml-edit-toolbar p-4">

<div class="flex items-center gap-6 mb-3">

<div class="flex items-center gap-2">

Start <span class="text-xs" style="color: var(--text-ghost);">sec</span>

</div>

<div class="flex items-center gap-2">

End <span class="text-xs" style="color: var(--text-ghost);">sec</span>

</div>

<span class="text-xs font-semibold px-2.5 py-1 rounded-full"
style="background: var(--primary-soft); color: var(--brand-700);"
x-text="'Duration: ' + (trimEnd - trimStart).toFixed(1) + 's'"></span>

</div>

<div class="ml-trim-track">

<div class="ml-trim-selection"
:style="'left: ' + (trimStart / duration * 100) + '%; right: ' + (100 - trimEnd / duration * 100) + '%'">

</div>

<div class="absolute top-0 bottom-0 w-0.5"
style="background: var(--error-500);"
:style="'left: ' + (currentTime / duration * 100) + '%'">

</div>

</div>

<div class="flex items-center justify-between mt-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNC43NTIgMTEuMTY4bC0zLjE5Ny0yLjEzMkExIDEgMCAwMDEwIDkuODd2NC4yNjNhMSAxIDAgMDAxLjU1NS44MzJsMy4xOTctMi4xMzJhMSAxIDAgMDAwLTEuNjY0eiIgLz48L3N2Zz4="
class="w-4 h-4" /> Preview trim

<div class="flex items-center gap-2">

<a
href="%7B%%20url%20&#39;media_library:asset_detail&#39;%20workspace_id=workspace.id%20asset_id=asset.id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-2 text-xs font-semibold rounded-full border transition-colors"
style="border-color: var(--border); color: var(--text-secondary);">Cancel</a>

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyLjUiIGQ9Ik01IDEzbDQgNEwxOSA3IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> Trim & save

</div>

</div>

</div>

</div>

{% else %}

<div class="text-center py-20">

Editing is not available for this file type.

<a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 mt-4 px-4 py-2 text-sm font-semibold rounded-full border"
style="border-color: var(--border); color: var(--text-secondary);">Back
to library</a>

</div>

{% endif %} {% endblock %} {% block extra_js %} {% if asset.file_type ==
'image' or asset.file_type == 'gif' %}

{% elif asset.file_type == 'video' %}

{% endif %} {% endblock %}
