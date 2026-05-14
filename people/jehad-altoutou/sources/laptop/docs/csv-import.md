---
type: source
source_type: laptop
title: csv_import
slug: csv-import
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/csv_import.html
original_size: 3813
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# csv_import

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/csv_import.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}Import from CSV - {{
workspace.name }} - Brightbean{% endblock %} {% block page_header %}

<div class="flex items-center justify-between mb-6">

<div>

# Import from CSV

Bulk import posts from a CSV or TSV file.

</div>

<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D"
class="text-sm text-stone-500 hover:text-stone-700 flex items-center gap-1"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xNSAxOGwtNi02IDYtNiIgLz48L3N2Zz4="
class="w-4 h-4" /> Back to Calendar</a>

</div>

{% endblock %} {% block content %}

<div id="csv-import-container" class="max-w-3xl">

{% if error %}

<div class="rounded-lg p-4 bg-red-50 text-red-800 text-sm mb-4">

{{ error }}

</div>

{% endif %}

<div class="bg-white rounded-xl border border-stone-200 p-6">

<div class="flex items-center gap-3 mb-4">

<div class="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold text-white"
style="background: var(--primary);">

1

</div>

## Upload CSV File

</div>

{% csrf_token %}

<div class="border-2 border-dashed border-stone-200 rounded-xl p-8 text-center cursor-pointer hover:border-stone-300 transition-colors"
x-data="{ dragging: false, filename: '' }" role="button" tabindex="0"
@click="$refs.fileInput.click()"
@keydown.enter.prevent="$refs.fileInput.click()"
@keydown.space.prevent="$refs.fileInput.click()"
@dragover.prevent="dragging = true" @dragleave="dragging = false"
@drop.prevent="dragging = false; $refs.fileInput.files = $event.dataTransfer.files; filename = $event.dataTransfer.files[0]?.name"
:class="dragging &amp;&amp; 'border-orange-300 bg-orange-50/30'">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMCBoLTEwIHRleHQtc3RvbmUtMzAwIG14LWF1dG8gbWItMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTMgMTYuNXYyLjI1QTIuMjUgMi4yNSAwIDAwNS4yNSAyMWgxMy41QTIuMjUgMi4yNSAwIDAwMjEgMTguNzVWMTYuNW0tMTMuNS05TDEyIDNtMCAwbDQuNSA0LjVNMTIgM3YxMy41IiAvPjwvc3ZnPg=="
class="w-10 h-10 text-stone-300 mx-auto mb-3" />

Drop your CSV file here, or browse

Supports .csv and .tsv files

</div>

<div class="mt-4 flex items-center justify-between">

<div class="text-xs text-stone-400">

Expected columns: date, time, platforms, caption, media_url, category,
tags, first_comment

</div>

Upload & Map Columns

</div>

</div>

</div>

{% endblock %}
