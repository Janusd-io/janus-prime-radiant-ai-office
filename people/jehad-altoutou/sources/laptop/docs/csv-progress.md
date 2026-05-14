---
type: source
source_type: laptop
title: csv_progress
slug: csv-progress
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/csv_progress.html
original_size: 2153
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# csv_progress

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/partials/csv_progress.html` on 2026-05-14._

<div class="bg-white rounded-xl border border-stone-200 p-8 text-center">

<div class="w-14 h-14 rounded-full flex items-center justify-center mx-auto mb-4"
style="background: var(--primary); opacity: 0.1;">

</div>

<div class="w-14 h-14 rounded-full flex items-center justify-center mx-auto -mt-[72px] mb-4"
style="color: var(--primary);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik01IDEzbDQgNEwxOSA3IiAvPjwvc3ZnPg=="
class="w-8 h-8" />

</div>

## Import Complete

<div class="flex items-center justify-center gap-4 mt-4 mb-6">

<div class="px-4 py-2 rounded-lg bg-green-50 border border-green-200">

<span class="text-2xl font-bold text-green-700">{{ created_count
}}</span> <span class="text-xs text-green-600 block">post{{
created_count\|pluralize }} created</span>

</div>

{% if error_count \> 0 %}

<div class="px-4 py-2 rounded-lg bg-red-50 border border-red-200">

<span class="text-2xl font-bold text-red-700">{{ error_count }}</span>
<span class="text-xs text-red-600 block">row{{ error_count\|pluralize }}
skipped</span>

</div>

{% endif %}

</div>

{% if created_count \> 0 %} Your imported posts are now on the calendar.
{% else %} No posts were imported. Check your CSV and try again. {%
endif %}

<div class="flex items-center justify-center gap-3">

<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D"
class="btn-brand text-sm py-2 px-5">View Calendar</a> <a
href="%7B%%20url%20&#39;composer:csv_upload&#39;%20workspace_id=workspace.id%20%%7D"
class="text-sm font-semibold py-2 px-5 rounded-full border border-stone-200 hover:border-stone-300 text-stone-700 hover:text-stone-900 transition-colors">Import
More</a>

</div>

</div>
