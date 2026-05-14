---
type: source
source_type: laptop
title: kanban_column
slug: kanban-column
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/kanban_column.html
original_size: 3658
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---

# kanban_column

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/partials/kanban_column.html` on 2026-05-14._

<div class="kanban-column" group-id="{{ col.id }}" draggable="true"
@dragstart="startColumnDrag($event, '{{ col.id }}')"
@dragend="endColumnDrag($event)"
@dragover.prevent="columnDragOver($event)"
@dragleave="columnDragLeave($event)"
@drop="dropColumn($event, '{{ col.id }}')">

<div class="flex items-center justify-between px-3 py-2.5 column-header"
style="cursor: grab;" @mousedown="columnHeaderMouseDown()">

<div class="flex items-center gap-2">

<span class="group-label text-[13px] font-bold text-stone-800">{{
col.label }}</span>
<span class="column-count inline-flex items-center justify-center min-w-[20px] h-5 px-1.5 rounded-full text-[11px] font-semibold bg-stone-200/70 text-stone-500">{{
col.ideas\|length }}</span>

</div>

<div class="flex items-center gap-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48bGluZSB4MT0iMTIiIHkxPSI1IiB4Mj0iMTIiIHkyPSIxOSI+PC9saW5lPjxsaW5lIHgxPSI1IiB5MT0iMTIiIHgyPSIxOSIgeTI9IjEyIj48L2xpbmU+PC9zdmc+"
class="w-4 h-4" />

<div class="relative" x-data="{ menuOpen: false }">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxjaXJjbGUgY3g9IjEyIiBjeT0iNiIgcj0iMS41Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxLjUiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTgiIHI9IjEuNSI+PC9jaXJjbGU+PC9zdmc+"
class="w-4 h-4" />

<div class="absolute right-0 top-full mt-1 bg-white rounded-lg shadow-lg ring-1 ring-stone-200 py-1 z-50 min-w-[140px]"
x-show="menuOpen" @click.away="menuOpen = false" x-cloak=""
x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100">

{% if col.ideas\|length == 0 %}

Delete column

{% else %} <span class="block px-3 py-1.5 text-xs text-stone-400">
Remove all ideas first </span> {% endif %}

</div>

</div>

</div>

</div>

<div class="kanban-cards" @dragover.prevent="dragOver($event)"
@dragleave="dragLeave($event)"
@drop="dropOnColumn($event, '{{ col.id }}')">

{% for idea in col.ideas %} {% include
"composer/partials/idea_card.html" with idea=idea group_id=col.id %} {%
endfor %}

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48bGluZSB4MT0iMTIiIHkxPSI1IiB4Mj0iMTIiIHkyPSIxOSI+PC9saW5lPjxsaW5lIHgxPSI1IiB5MT0iMTIiIHgyPSIxOSIgeTI9IjEyIj48L2xpbmU+PC9zdmc+"
class="w-4 h-4" /> New Idea

</div>
