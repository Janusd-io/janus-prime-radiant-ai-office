---
type: source
source_type: laptop
title: _assignment_dropdown
slug: assignment-dropdown
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_assignment_dropdown.html
original_size: 3127
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _assignment_dropdown

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_assignment_dropdown.html` on 2026-05-14._

<div class="relative" x-data="{ assignOpen: false }">

{% if message.assigned_to %}

<div class="w-5 h-5 rounded-full flex items-center justify-center text-[9px] font-bold text-white flex-shrink-0"
style="background: var(--accent-indigo);">

{{ message.assigned_to.email\|make_list\|first\|upper }}

</div>

<span class="text-stone-700">{{
message.assigned_to.get_short_name\|default:message.assigned_to.email\|truncatechars:12
}}</span> {% else %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xNiAyMXYtMmE0IDQgMCAwMC00LTRINWE0IDQgMCAwMC00IDR2MiIgLz48Y2lyY2xlIGN4PSI4LjUiIGN5PSI3IiByPSI0Ij48L2NpcmNsZT48bGluZSB4MT0iMjAiIHkxPSI4IiB4Mj0iMjAiIHkyPSIxNCI+PC9saW5lPjxsaW5lIHgxPSIyMyIgeTE9IjExIiB4Mj0iMTciIHkyPSIxMSI+PC9saW5lPjwvc3ZnPg=="
class="w-4 h-4" /> Assign {% endif %}

<div class="absolute right-0 top-full mt-1 bg-white rounded-lg shadow-lg ring-1 ring-stone-200 py-1 z-50 min-w-[180px] max-h-[220px] overflow-y-auto"
x-show="assignOpen" @click.away="assignOpen = false" x-cloak=""
x-transition="">

{% if message.assigned_to %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNiAxOEwxOCA2TTYgNmwxMiAxMiIgLz48L3N2Zz4="
class="w-3.5 h-3.5" /> Unassign

<div class="border-t border-stone-100 my-0.5">

</div>

{% endif %} {% for membership in team_members %}

<div class="w-5 h-5 rounded-full flex items-center justify-center text-[9px] font-bold text-white flex-shrink-0"
style="background: var(--accent-indigo);">

{{ membership.user.email\|make_list\|first\|upper }}

</div>

{{ membership.user.get_short_name\|default:membership.user.email }}

{% endfor %}

</div>

</div>
