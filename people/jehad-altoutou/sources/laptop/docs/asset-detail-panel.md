---
type: source
source_type: laptop
title: _asset_detail_panel
slug: asset-detail-panel
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_asset_detail_panel.html
original_size: 10339
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---

# _asset_detail_panel

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/_asset_detail_panel.html` on 2026-05-14._

{% comment %}Slide-over detail panel content. Expects: asset, workspace,
versions{% endcomment %}

<div class="flex flex-col h-full" x-data="{ showDeleteConfirm: false }">

<div class="flex items-center justify-between px-5 py-4 border-b"
style="border-color: var(--border, #E7E5E4);">

## {{ asset.original_filename }}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-4 h-4" />

</div>

<div class="px-5 py-4">

<div class="rounded-xl overflow-hidden border"
style="border-color: var(--border, #E7E5E4); background: var(--surface-1, #FAFAF9);">

{% if asset.file_type == 'image' or asset.file_type == 'gif' %}
<img src="%7B%7B%20asset.file.url%20%7D%7D"
class="w-full max-h-80 object-contain"
alt="{{ asset.original_filename }}" /> {% elif asset.file_type ==
'video' %}

{% elif asset.file_type == 'document' %}

<div class="flex items-center justify-center py-16">

<div class="text-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMiBoLTEyIG14LWF1dG8gbWItMiIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0LCAjQThBMjlFKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik03IDIxaDEwYTIgMiAwIDAwMi0yVjkuNDE0YTEgMSAwIDAwLS4yOTMtLjcwN2wtNS40MTQtNS40MTRBMSAxIDAgMDAxMi41ODYgM0g3YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-12 h-12 mx-auto mb-2" />

{{ asset.original_filename }}

</div>

</div>

{% endif %}

</div>

</div>

<div class="px-5 pb-3 flex items-center gap-2">

{% if not asset.is_shared %} <a
href="%7B%%20url%20&#39;media_library:asset_edit&#39;%20workspace_id=workspace.id%20asset_id=asset.id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-2 text-xs font-semibold text-white rounded-full transition-all"
style="background: var(--primary, #F97316); box-shadow: var(--shadow-primary);"
onmouseenter="this.style.background=&#39;var(--primary-hover)&#39;"
onmouseleave="this.style.background=&#39;var(--primary)&#39;"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTEgNUg2YTIgMiAwIDAwLTIgMnYxMWEyIDIgMCAwMDIgMmgxMWEyIDIgMCAwMDItMnYtNW0tMS40MTQtOS40MTRhMiAyIDAgMTEyLjgyOCAyLjgyOEwxMS44MjggMTVIOXYtMi44MjhsOC41ODYtOC41ODZ6IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> Edit</a> {% endif %} <a
href="%7B%%20url%20&#39;media_library:asset_download&#39;%20workspace_id=workspace.id%20asset_id=asset.id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-2 text-xs font-semibold rounded-full border transition-all"
style="border-color: var(--border, #E7E5E4); color: var(--text-secondary, #57534E);"
onmouseenter="this.style.background=&#39;var(--surface-1)&#39;"
onmouseleave="this.style.background=&#39;transparent&#39;"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNNCAxNnYxYTMgMyAwIDAwMyAzaDEwYTMgMyAwIDAwMy0zdi0xbS00LTRsLTQgNG0wIDBsLTQtNG00IDRWNCIgLz48L3N2Zz4="
class="w-3.5 h-3.5" /> Download</a> {% if not asset.is_shared %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTkgN2wtLjg2NyAxMi4xNDJBMiAyIDAgMDExNi4xMzggMjFINy44NjJhMiAyIDAgMDEtMS45OTUtMS44NThMNSA3bTUgNHY2bTQtNnY2bTEtMTBWNGExIDEgMCAwMC0xLTFoLTRhMSAxIDAgMDAtMSAxdjNNNCA3aDE2IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> Delete

<div class="fixed inset-0 z-[60] flex items-center justify-center"
x-show="showDeleteConfirm" x-cloak=""
@keydown.escape.window="showDeleteConfirm = false">

<div class="absolute inset-0 bg-black/30 backdrop-blur-sm"
@click="showDeleteConfirm = false">

</div>

<div class="relative bg-white rounded-2xl shadow-xl w-full max-w-sm mx-4 p-6"
@click.stop="">

<div class="w-10 h-10 rounded-full flex items-center justify-center mx-auto mb-3"
style="background: var(--error-50, #FEF2F2);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgc3R5bGU9ImNvbG9yOiB2YXIoLS1lcnJvci01MDAsICNFRjQ0NDQpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xOSA3bC0uODY3IDEyLjE0MkEyIDIgMCAwMTE2LjEzOCAyMUg3Ljg2MmEyIDIgMCAwMS0xLjk5NS0xLjg1OEw1IDdtNSA0djZtNC02djZtMS0xMFY0YTEgMSAwIDAwLTEtMWgtNGExIDEgMCAwMC0xIDF2M000IDdoMTYiIC8+PC9zdmc+"
class="w-5 h-5" />

</div>

### Delete asset?

This cannot be undone. The file will be permanently removed.

<div class="flex gap-2">

Cancel

Delete

</div>

</div>

</div>

{% endif %}

</div>

<div class="flex-1 overflow-y-auto border-t"
style="border-color: var(--border, #E7E5E4);">

<div class="px-5 py-4">

### Details

File size  
{{ asset.human_file_size }}

Format  
{{ asset.mime_type }}

Dimensions  
{{ asset.width }} × {{ asset.height }}px

Duration  
{{ asset.duration_seconds }}s

Uploaded  
{{ asset.created_at\|date:"M j, Y g:i A" }}

Uploaded by  
{{ asset.uploaded_by.display_name }}

</div>

<div class="px-5 py-4 border-t"
style="border-color: var(--surface-2, #F5F5F4);">

### Tags

<div id="tag-editor-{{ asset.id }}">

{% include "media_library/\_tag_input.html" %}

</div>

</div>

<div class="px-5 py-4 border-t"
style="border-color: var(--surface-2, #F5F5F4);">

<div class="flex items-center justify-between mb-3">

### Version History

{% if versions %}
<span class="text-xs px-2 py-0.5 rounded-full font-semibold"
style="background: var(--surface-2); color: var(--text-tertiary);">{{
versions\|length }}</span> {% endif %}

</div>

<div id="version-list-{{ asset.id }}"
hx-get="{% url 'media_library:version_list' workspace_id=workspace.id asset_id=asset.id %}"
hx-trigger="load" hx-target="#version-list-{{ asset.id }}">

{% include "media_library/\_version_list.html" %}

</div>

</div>

</div>

</div>
