---
type: source
source_type: laptop
title: csv_validation
slug: csv-validation
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/csv_validation.html
original_size: 3726
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---

# csv_validation

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/partials/csv_validation.html` on 2026-05-14._

<div class="space-y-6">

<div class="bg-white rounded-xl border border-stone-200 p-6">

<div class="flex items-center gap-3 mb-4">

<div class="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold text-white"
style="background: var(--primary);">

3

</div>

## Validation Results

</div>

<div class="flex items-center gap-4 mb-5">

<div class="flex items-center gap-2 px-3 py-2 rounded-lg bg-green-50 border border-green-200">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LWdyZWVuLTYwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik01IDEzbDQgNEwxOSA3IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-green-600" />
<span class="text-sm font-semibold text-green-800">{{ valid_count }}
valid</span>

</div>

{% if errors %}

<div class="flex items-center gap-2 px-3 py-2 rounded-lg bg-red-50 border border-red-200">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXJlZC02MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNiAxOEwxOCA2TTYgNmwxMiAxMiIgLz48L3N2Zz4="
class="w-4 h-4 text-red-600" />
<span class="text-sm font-semibold text-red-800">{{ errors\|length }}{%
if has_more_errors %}+{% endif %} error{{ errors\|length\|pluralize
}}</span>

</div>

{% endif %} <span class="text-xs text-stone-400">{{ total_rows }} total
rows</span>

</div>

{% if errors %}

<div class="mb-5 max-h-64 overflow-y-auto rounded-lg border border-red-100">

{% for err in errors %}

<div class="flex items-start gap-2 px-3 py-2 text-xs {% if not forloop.last %}border-b border-red-50{% endif %} bg-red-50/50">

<span class="font-mono font-semibold text-red-600 flex-shrink-0">Row {{
err.row }}</span>

<div class="text-red-700">

{% for e in err.errors %} {{ e }}{% if not forloop.last %}; {% endif %}
{% endfor %}

</div>

</div>

{% endfor %}

</div>

{% if has_more_errors %}

Showing first 50 errors. Fix and re-upload for the full list.

{% endif %} {% endif %} {% if valid_count \> 0 %}

{% csrf_token %}

<div class="flex items-center justify-between p-4 bg-stone-50 rounded-lg">

<div>

Ready to import {{ valid_count }} post{{ valid_count\|pluralize }}

{% if errors %}

{{ errors\|length }} invalid row{{ errors\|length\|pluralize }} will be
skipped.

{% endif %}

</div>

Confirm Import

</div>

{% else %}

<div class="p-4 bg-red-50 rounded-lg text-center">

No valid rows to import.

Fix the errors in your CSV and re-upload.

</div>

{% endif %}

</div>

</div>
