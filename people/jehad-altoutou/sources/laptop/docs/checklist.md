---
type: source
source_type: laptop
title: _checklist
slug: checklist
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/brightbean-studio/templates/onboarding/partials/_checklist.html
original_size: 7984
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:41Z"
sensitivity: dept
sensitivity_confidence: 0.70
sensitivity_reason: "Brightbean Studio onboarding checklist HTML partial — boilerplate, no PII"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _checklist

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/onboarding/partials/_checklist.html` on 2026-05-14._

{% if not checklist_dismissed and checklist_items %}

<div id="onboarding-checklist"
class="fixed bottom-2 right-2 left-2 sm:left-auto sm:bottom-4 sm:right-4 z-[55] sm:w-[340px]"
x-data="{ open: true }" if="" request.workspace=""
hx-get="{% url 'onboarding:checklist_partial' workspace_id=request.workspace.id %}"
hx-trigger="ideaChanged from:body" hx-swap="outerHTML" {%="" endif=""
%}="">

<div class="w-8 h-8 rounded-lg flex items-center justify-center flex-shrink-0"
style="background: var(--primary-soft);">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUiIGhlaWdodD0iMTUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tcHJpbWFyeSkiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPgogICAgICAgICAgICAgICAgPHBhdGggZD0iTTEzIDJMMyAxNGg5bC0xIDggMTAtMTJoLTlsMS04eiIgLz4KICAgICAgICAgICAgPC9zdmc+)

</div>

<div class="flex-1 min-w-0">

<div class="text-sm font-semibold text-stone-800">

Get started

</div>

<div class="text-xs text-stone-400">

{{ checklist_completed_count }} of {{ checklist_total_count }} complete

</div>

</div>

<div class="relative w-8 h-8 flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCAtcm90YXRlLTkwIiB2aWV3Ym94PSIwIDAgMzIgMzIiPgogICAgICAgICAgICAgICAgPGNpcmNsZSBjeD0iMTYiIGN5PSIxNiIgcj0iMTMiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI0U3RTVFNCIgc3Ryb2tlLXdpZHRoPSIzIj48L2NpcmNsZT4KICAgICAgICAgICAgICAgIDxjaXJjbGUgY3g9IjE2IiBjeT0iMTYiIHI9IjEzIiBmaWxsPSJub25lIiBzdHJva2U9InZhcigtLXByaW1hcnkpIiBzdHJva2Utd2lkdGg9IjMiIHN0cm9rZS1kYXNoYXJyYXk9InslIHdpZHRocmF0aW8gY2hlY2tsaXN0X2NvbXBsZXRlZF9jb3VudCBjaGVja2xpc3RfdG90YWxfY291bnQgODIgJX0gODIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PC9jaXJjbGU+CiAgICAgICAgICAgIDwvc3ZnPg=="
class="w-8 h-8 -rotate-90" />
<span class="absolute inset-0 flex items-center justify-center text-[10px] font-bold text-stone-600">{{
checklist_completed_count }}/{{ checklist_total_count }}</span>

</div>

<div class="bg-white border border-stone-200 rounded-xl shadow-xl overflow-hidden"
x-show="open" x-cloak=""
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0 translate-y-2"
x-transition:enter-end="opacity-100 translate-y-0"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="opacity-100 translate-y-0"
x-transition:leave-end="opacity-0 translate-y-2">

<div class="flex items-center justify-between px-4 py-3 border-b border-stone-100">

<div class="flex items-center gap-2.5">

<div class="w-8 h-8 rounded-lg flex items-center justify-center"
style="background: var(--primary-soft);">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUiIGhlaWdodD0iMTUiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tcHJpbWFyeSkiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPgogICAgICAgICAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMTMgMkwzIDE0aDlsLTEgOCAxMC0xMmgtOWwxLTh6IiAvPgogICAgICAgICAgICAgICAgICAgIDwvc3ZnPg==)

</div>

<div>

<div class="text-sm font-semibold text-stone-800">

Get started

</div>

<div class="text-xs text-stone-400">

{{ checklist_completed_count }} of {{ checklist_total_count }} complete

</div>

</div>

</div>

<div class="flex items-center gap-1">

<div class="w-14 h-1 bg-stone-100 rounded-full overflow-hidden mr-1">

<div class="h-full rounded-full transition-all duration-300"
style="width: {% widthratio checklist_completed_count checklist_total_count 100 %}%; background: var(--primary);">

</div>

</div>

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBvbHlsaW5lIHBvaW50cz0iNiA5IDEyIDE1IDE4IDkiPjwvcG9seWxpbmU+CiAgICAgICAgICAgICAgICAgICAgPC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj4KICAgICAgICAgICAgICAgICAgICAgICAgPGxpbmUgeDE9IjE4IiB5MT0iNiIgeDI9IjYiIHkyPSIxOCI+PC9saW5lPjxsaW5lIHgxPSI2IiB5MT0iNiIgeDI9IjE4IiB5Mj0iMTgiPjwvbGluZT4KICAgICAgICAgICAgICAgICAgICA8L3N2Zz4=)

</div>

</div>

{% for item in checklist_items %} <a href="%7B%7B%20item.url%20%7D%7D"
class="flex items-center gap-3 px-4 py-2.5 {% if not forloop.last %}border-b border-stone-50{% endif %} hover:bg-stone-50 transition-colors no-underline group">{%
if item.completed %}</a>

<div class="w-7 h-7 rounded-lg flex items-center justify-center flex-shrink-0"
style="background: var(--success-50);">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tc3VjY2Vzcy01MDApIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPgogICAgICAgICAgICAgICAgICAgIDxwb2x5bGluZSBwb2ludHM9IjIwIDYgOSAxNyA0IDEyIj48L3BvbHlsaW5lPgogICAgICAgICAgICAgICAgPC9zdmc+)

</div>

{% else %}

<div class="w-7 h-7 rounded-lg flex items-center justify-center flex-shrink-0"
style="background: {% if item.icon_color == 'sky' %}var(--accent-sky-soft){% elif item.icon_color == 'emerald' %}var(--accent-emerald-soft){% elif item.icon_color == 'indigo' %}var(--accent-indigo-soft){% elif item.icon_color == 'brand' %}var(--primary-soft){% elif item.icon_color == 'amber' %}var(--accent-amber-soft){% else %}var(--surface-2){% endif %};">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0ieyUgaWYgaXRlbS5pY29uX2NvbG9yID09ICYjMzk7c2t5JiMzOTsgJX12YXIoLS1hY2NlbnQtc2t5KXslIGVsaWYgaXRlbS5pY29uX2NvbG9yID09ICYjMzk7ZW1lcmFsZCYjMzk7ICV9dmFyKC0tYWNjZW50LWVtZXJhbGQpeyUgZWxpZiBpdGVtLmljb25fY29sb3IgPT0gJiMzOTtpbmRpZ28mIzM5OyAlfXZhcigtLWFjY2VudC1pbmRpZ28peyUgZWxpZiBpdGVtLmljb25fY29sb3IgPT0gJiMzOTticmFuZCYjMzk7ICV9dmFyKC0tcHJpbWFyeSl7JSBlbGlmIGl0ZW0uaWNvbl9jb2xvciA9PSAmIzM5O2FtYmVyJiMzOTsgJX12YXIoLS1hY2NlbnQtYW1iZXIpeyUgZWxzZSAlfXZhcigtLXRleHQtdGVydGlhcnkpeyUgZW5kaWYgJX0iIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+CiAgICAgICAgICAgICAgICAgICAge3sgaXRlbS5pY29uX3N2Z3xzYWZlIH19CiAgICAgICAgICAgICAgICA8L3N2Zz4=)

</div>

{% endif %}

<div class="flex-1 min-w-0">

<div class="text-[13px] font-medium {% if item.completed %}text-stone-400 line-through{% else %}text-stone-700{% endif %}">

{{ item.title }}

</div>

<div class="text-[11px] text-stone-400 leading-tight">

{{ item.description }}

</div>

</div>

{% if not item.completed %} <img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0idGV4dC1zdG9uZS0zMDAgZ3JvdXAtaG92ZXI6dGV4dC1zdG9uZS01MDAgdHJhbnNpdGlvbi1jb2xvcnMgZmxleC1zaHJpbmstMCI+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNOSAxOGw2LTYtNi02IiAvPgogICAgICAgICAgICA8L3N2Zz4="
class="text-stone-300 group-hover:text-stone-500 transition-colors flex-shrink-0" />
{% endif %} {% endfor %}

</div>

</div>

{% endif %}
