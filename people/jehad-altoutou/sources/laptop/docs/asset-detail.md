---
type: source
source_type: laptop
title: asset_detail
slug: asset-detail
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/asset_detail.html
original_size: 2236
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---

# asset_detail

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/asset_detail.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}{{ asset.original_filename
}} - Media Library{% endblock %} {% block page_header %}

<div class="flex items-center gap-3">

<a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D"
class="w-8 h-8 rounded-lg flex items-center justify-center transition-colors"
style="color: var(--text-tertiary, #78716C);"
onmouseenter="this.style.background=&#39;var(--surface-2)&#39;"
onmouseleave="this.style.background=&#39;transparent&#39;"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4" /></a>

# {{ asset.original_filename }}

{% if asset.is_shared %}
<span class="text-xs font-bold px-2.5 py-1 rounded-full uppercase tracking-wider"
style="background: var(--accent-teal-soft); color: #0F766E;">Shared</span>
{% endif %}

</div>

{% endblock %} {% block content %}

<div class="grid grid-cols-3 gap-6">

<div class="col-span-2">

<div class="rounded-xl overflow-hidden border"
style="border-color: var(--border); background: var(--surface-1);">

{% if asset.file_type == 'image' or asset.file_type == 'gif' %}
<img src="%7B%7B%20asset.file.url%20%7D%7D"
class="w-full max-h-[600px] object-contain"
alt="{{ asset.original_filename }}" /> {% elif asset.file_type ==
'video' %}

{% else %}

<div class="flex items-center justify-center py-24">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xNiBoLTE2IiBzdHlsZT0iY29sb3I6IHZhcigtLXRleHQtZ2hvc3QpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEiIGQ9Ik03IDIxaDEwYTIgMiAwIDAwMi0yVjkuNDE0YTEgMSAwIDAwLS4yOTMtLjcwN2wtNS40MTQtNS40MTRBMSAxIDAgMDAxMi41ODYgM0g3YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-16 h-16" />

</div>

{% endif %}

</div>

</div>

<div class="space-y-5">

{% include "media_library/\_asset_detail_panel.html" %}

</div>

</div>

{% endblock %}
