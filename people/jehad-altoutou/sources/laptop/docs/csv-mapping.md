---
type: source
source_type: laptop
title: csv_mapping
slug: csv-mapping
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/csv_mapping.html
original_size: 3285
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# csv_mapping

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/partials/csv_mapping.html` on 2026-05-14._

<div class="space-y-6">

<div class="bg-white rounded-xl border border-stone-200 p-6">

<div class="flex items-center gap-3 mb-4">

<div class="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold text-white"
style="background: var(--primary);">

2

</div>

## Map Columns

</div>

{% csrf_token %}

Match each CSV column to the corresponding post field. Leave unmapped
columns as "Skip".

<div class="overflow-x-auto mb-6 rounded-lg border border-stone-200">

{% for header in headers %}

{{ header }}

</div>

</div>

</div>

{% endfor %}

{% for row in preview_rows %}

{% for cell in row %}

{{ cell\|truncatechars:40 }}

{% endfor %}

{% endfor %}

<div class="grid grid-cols-2 sm:grid-cols-4 gap-3"
x-data="{ autoMapping: {{ auto_mapping_json|default:'{}' }} }"
x-init="$nextTick(() =&gt; {
                     Object.entries(autoMapping).forEach(([field, colIdx]) =&gt; {
                         const sel = $el.querySelector(`[name='map_${field}']`);
                         if (sel) sel.value = String(colIdx);
                     });
                 })">

{% for field in field_choices %}

<div>

{{ field }} - Skip - {% for header in headers %} {{ header }} {% endfor
%}

</div>

{% endfor %}

</div>

<div class="mt-5 flex justify-end">

Validate & Preview

</div>
