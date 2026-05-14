---
type: source
source_type: laptop
title: _asset_grid
slug: asset-grid
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_asset_grid.html
original_size: 2779
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _asset_grid

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/_asset_grid.html` on 2026-05-14._

{% load static %} {% if page.object_list %}

<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3"
x-show="viewMode === 'grid'"
hx-get="{% url 'media_library:index' workspace_id=workspace.id %}?page=1&amp;q={{ query|urlencode }}&amp;sort={{ current_sort|urlencode }}"
hx-trigger="uploadsComplete from:body" hx-target="#asset-grid"
hx-swap="innerHTML">

{% for asset in page.object_list %} {% include
"media_library/\_asset_card.html" %} {% endfor %}

</div>

<div x-show="viewMode === 'list'" x-cloak="">

<div class="rounded-xl border overflow-hidden"
style="border-color: var(--border, #E7E5E4); background: var(--surface-0, #FFF);">

<div class="grid grid-cols-12 gap-3 px-4 py-2 text-xs font-bold uppercase tracking-wider border-b"
style="color: var(--text-tertiary, #78716C); border-color: var(--surface-2, #F5F5F4); background: var(--surface-1, #FAFAF9);">

<div class="col-span-5">

Name

</div>

<div class="col-span-2">

Type

</div>

<div class="col-span-2">

Size

</div>

<div class="col-span-2">

Uploaded

</div>

<div class="col-span-1">

</div>

</div>

{% for asset in page.object_list %} {% include
"media_library/\_asset_list_row.html" %} {% endfor %}

</div>

</div>

{% if page.has_other_pages %}

<div class="flex items-center justify-center gap-2 mt-6 pb-4">

{% if page.has_previous %} <a
href="?page=%7B%7B%20page.previous_page_number%20%7D%7D&amp;q=%7B%7B%20query%7Curlencode%20%7D%7D&amp;sort=%7B%7B%20current_sort%7Curlencode%20%7D%7D"
class="px-3 py-1.5 text-xs font-semibold rounded-full border transition-colors"
style="border-color: var(--border, #E7E5E4); color: var(--text-secondary, #57534E);"
data-hx-get="{% url &#39;media_library:index&#39; workspace_id=workspace.id %}?page={{ page.previous_page_number }}&amp;q={{ query|urlencode }}&amp;sort={{ current_sort|urlencode }}"
data-hx-target="#asset-grid" data-hx-swap="innerHTML">Previous</a> {%
endif %} <span class="text-xs px-3"
style="color: var(--text-tertiary, #78716C);"> Page {{ page.number }} of
{{ page.paginator.num_pages }} </span> {% if page.has_next %} <a
href="?page=%7B%7B%20page.next_page_number%20%7D%7D&amp;q=%7B%7B%20query%7Curlencode%20%7D%7D&amp;sort=%7B%7B%20current_sort%7Curlencode%20%7D%7D"
class="px-3 py-1.5 text-xs font-semibold rounded-full border transition-colors"
style="border-color: var(--border, #E7E5E4); color: var(--text-secondary, #57534E);"
data-hx-get="{% url &#39;media_library:index&#39; workspace_id=workspace.id %}?page={{ page.next_page_number }}&amp;q={{ query|urlencode }}&amp;sort={{ current_sort|urlencode }}"
data-hx-target="#asset-grid" data-hx-swap="innerHTML">Next</a> {% endif
%}

</div>

{% endif %} {% else %} {% include "media_library/\_empty_state.html" %}
{% endif %}
