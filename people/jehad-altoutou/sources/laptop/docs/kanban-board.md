---
type: source
source_type: laptop
title: kanban_board
slug: kanban-board
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/kanban_board.html
original_size: 1834
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# kanban_board

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/partials/kanban_board.html` on 2026-05-14._

<div class="flex gap-4 overflow-x-auto pb-4" style="min-height: 400px;">

{% for col in columns %} {% include
"composer/partials/kanban_column.html" with col=col %} {% endfor %}

<div class="flex-shrink-0 w-[260px]" new-group-tile=""
x-data="{ adding: false, newName: '' }">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48bGluZSB4MT0iMTIiIHkxPSI1IiB4Mj0iMTIiIHkyPSIxOSI+PC9saW5lPjxsaW5lIHgxPSI1IiB5MT0iMTIiIHgyPSIxOSIgeTI9IjEyIj48L2xpbmU+PC9zdmc+"
class="w-4 h-4" /> New Group

<div class="bg-stone-100 rounded-xl p-3" x-show="adding" x-cloak="">

<div class="flex items-center gap-2 mt-2">

Add

Cancel

</div>

</div>

</div>

</div>
