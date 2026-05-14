---
type: source
source_type: laptop
title: _posting_slots_grid
slug: posting-slots-grid
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/social_accounts/partials/_posting_slots_grid.html
original_size: 9514
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# _posting_slots_grid

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/social_accounts/partials/_posting_slots_grid.html` on 2026-05-14._

{% comment %} Weekly posting slots grid for a single social account.
Shows 7 columns (Sun–Sat) with on/off toggle and time slots. Context:
account (with prefetched posting_slots), workspace_id. {% endcomment %}
{% load social_accounts_tags %} {% get_posting_slots_display account as
days %}

<div id="slots-grid-{{ account.id }}"
hx-get="{% url 'calendar:account_slots_partial' workspace_id=workspace_id %}?social_account_id={{ account.id }}"
hx-trigger="slotsUpdated[accountId=='{{ account.id }}'] from:body"
hx-swap="outerHTML">

<div class="overflow-x-auto">

{% for day in days %}

<div class="text-xs font-semibold text-stone-500 mb-2">

{{ day.short_name }}

</div>

{% if day.has_slots %}

{% csrf_token %}

<span class="inline-block h-3.5 w-3.5 rounded-full bg-white shadow-sm transform transition-transform duration-200 {% if day.is_active %}translate-x-[18px]{% else %}translate-x-[3px]{% endif %}"></span>

{% else %}

<div class="h-5">

</div>

{% endif %}

</div>

</div>

{% endfor %}

{% for day in days %}

<div class="space-y-1.5 min-h-[40px]">

{% for slot in day.slots %}

<div class="relative flex items-center justify-center"
x-data="{ editing: false, hovered: false }" @mouseenter="hovered = true"
@mouseleave="hovered = false">

<div class="flex items-center gap-0.5" x-show="!editing">

{{ slot.time\|time:"g:i A" }}

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-3 h-3" />

</div>

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNSAxM2w0IDRMMTkgNyIgLz48L3N2Zz4="
class="w-3.5 h-3.5" />

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNiAxOEwxOCA2TTYgNmwxMiAxMiIgLz48L3N2Zz4="
class="w-3.5 h-3.5" />

</div>

{% endfor %}

</div>

<div class="mt-2" x-data="{ adding: false, newTime: '09:00' }">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTIgNHYxNm04LThINCIgLz48L3N2Zz4="
class="w-3.5 h-3.5" />

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNSAxM2w0IDRMMTkgNyIgLz48L3N2Zz4="
class="w-3.5 h-3.5" />

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNiAxOEwxOCA2TTYgNmwxMiAxMiIgLz48L3N2Zz4="
class="w-3.5 h-3.5" />

</div>

{% endfor %}
