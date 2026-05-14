---
type: source
source_type: laptop
title: _shared_asset_grid
slug: shared-asset-grid
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_shared_asset_grid.html
original_size: 2917
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# _shared_asset_grid

_Extracted from `brightbean-studio/templates/media_library/_shared_asset_grid.html` on 2026-05-14._

{% comment %}Asset grid for shared org library. No workspace-scoped
URLs. Expects: page, query{% endcomment %} {% if page.object_list %}

<div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3"
hx-get="{% url 'media_library_org:shared_index' %}?page=1&amp;q={{ query|urlencode }}"
hx-trigger="uploadsComplete from:body" hx-target="#shared-grid"
hx-swap="innerHTML">

{% for asset in page.object_list %} {% include
"media_library/\_shared_asset_card.html" %} {% endfor %}

</div>

{% if page.has_other_pages %}

<div class="flex items-center justify-center gap-2 mt-6 pb-4">

{% if page.has_previous %} <a
href="?page=%7B%7B%20page.previous_page_number%20%7D%7D&amp;q=%7B%7B%20query%7Curlencode%20%7D%7D"
class="px-3 py-1.5 text-xs font-semibold rounded-full border transition-colors"
style="border-color: var(--border, #E7E5E4); color: var(--text-secondary, #57534E);"
data-hx-get="{% url &#39;media_library_org:shared_index&#39; %}?page={{ page.previous_page_number }}&amp;q={{ query|urlencode }}"
data-hx-target="#shared-grid" data-hx-swap="innerHTML">Previous</a> {%
endif %} <span class="text-xs px-3"
style="color: var(--text-tertiary, #78716C);"> Page {{ page.number }} of
{{ page.paginator.num_pages }} </span> {% if page.has_next %} <a
href="?page=%7B%7B%20page.next_page_number%20%7D%7D&amp;q=%7B%7B%20query%7Curlencode%20%7D%7D"
class="px-3 py-1.5 text-xs font-semibold rounded-full border transition-colors"
style="border-color: var(--border, #E7E5E4); color: var(--text-secondary, #57534E);"
data-hx-get="{% url &#39;media_library_org:shared_index&#39; %}?page={{ page.next_page_number }}&amp;q={{ query|urlencode }}"
data-hx-target="#shared-grid" data-hx-swap="innerHTML">Next</a> {% endif
%}

</div>

{% endif %} {% else %}

<div class="flex flex-col items-center justify-center py-20 text-center">

<div class="w-20 h-20 rounded-2xl flex items-center justify-center mb-5"
style="background: var(--primary-soft, #FFF7ED);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMCBoLTEwIiBzdHlsZT0iY29sb3I6IHZhcigtLXByaW1hcnksICNGOTczMTYpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+CiAgICAgIDxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik00IDE2bDQuNTg2LTQuNTg2YTIgMiAwIDAxMi44MjggMEwxNiAxNm0tMi0ybDEuNTg2LTEuNTg2YTIgMiAwIDAxMi44MjggMEwyMCAxNG0tNi02aC4wMU02IDIwaDEyYTIgMiAwIDAwMi0yVjZhMiAyIDAgMDAtMi0ySDZhMiAyIDAgMDAtMiAydjEyYTIgMiAwIDAwMiAyeiIgLz4KICAgIDwvc3ZnPg=="
class="w-10 h-10" />

</div>

{% if query %}

### No media matches your search

Try adjusting your search terms.

{% else %}

### No shared media yet

Organization admins can upload assets here for use across all
workspaces.

{% endif %}

</div>

{% endif %}
