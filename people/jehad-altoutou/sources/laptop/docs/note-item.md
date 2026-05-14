---
type: source
source_type: laptop
title: _note_item
slug: note-item
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_note_item.html
original_size: 1254
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
---

# _note_item

_Extracted from `brightbean-studio/templates/inbox/partials/_note_item.html` on 2026-05-14._

{% load humanize %}

<div class="flex gap-2.5 items-start">

<div class="w-7 h-7 rounded-full flex items-center justify-center text-[10px] font-bold flex-shrink-0"
style="background: var(--warning-50); color: var(--warning-700);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xNCAySDZhMiAyIDAgMDAtMiAydjE2YTIgMiAwIDAwMiAyaDEyYTIgMiAwIDAwMi0yVjh6IiAvPjxwb2x5bGluZSBwb2ludHM9IjE0IDIgMTQgOCAyMCA4Ij48L3BvbHlsaW5lPjwvc3ZnPg=="
class="w-3.5 h-3.5" />

</div>

<div class="flex-1 min-w-0">

<div class="bg-amber-50 border border-amber-200 rounded-xl rounded-tl-sm px-3.5 py-2.5">

<div class="flex items-center gap-2 mb-1">

<span class="text-[12px] font-semibold text-amber-900">{{
note.author.get_short_name\|default:note.author.email }}</span>
<span class="badge-pill"
style="background: var(--warning-50); color: var(--warning-700); border: 1px solid rgba(234,179,8,0.2);">Internal</span>
<span class="text-[11px] text-stone-400 ml-auto">{{
note.created_at\|timesince }} ago</span>

</div>

{{ note.body }}

</div>

</div>

</div>
