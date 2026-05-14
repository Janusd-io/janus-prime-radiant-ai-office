---
type: source
source_type: laptop
title: preview_panel
slug: preview-panel
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/preview_panel.html
original_size: 51429
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# preview_panel

_Extracted from `brightbean-studio/templates/composer/partials/preview_panel.html` on 2026-05-14._

{% comment %} Preview Panel - platform-specific post previews. Context:
previews (list of dicts with account, title, caption, first_comment,
char_count, char_limit, is_over_limit, truncated_caption, needs_title),
media_items, workspace. {% endcomment %} {% if previews %} {% for p in
previews %}

<div class="preview-card"
style="animation: slideUp 200ms {{ forloop.counter0|add:0 }}50ms cubic-bezier(0.16,1,0.3,1) both">

<div class="px-3.5 py-2 border-b flex items-center gap-2"
style="border-color: #E7E5E4;">

{% include "partials/\_platform_icon.html" with
platform=p.account.platform size="sm" %}
<span class="text-[11px] font-semibold text-stone-500 flex-1">{{
p.account.platform\|title }} Preview</span>
<span class="text-[10px] font-semibold tabular-nums px-2 py-0.5 rounded-full {% if p.is_over_limit %}bg-red-50 text-red-600{% else %}bg-stone-100 text-stone-500{% endif %}">
{{ p.char_count }}/{{ p.char_limit }} </span>

</div>

{% if p.account.platform == "youtube" %} {# ─── YouTube ─── video-first
layout like a YouTube upload preview \#}

<div class="bg-white">

{% if media_items %} {% with m=media_items.0 %}

<div class="relative bg-black" style="aspect-ratio: 16/9;">

{% if m.is_video %}

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-12 h-12 rounded-full bg-red-600/90 flex items-center justify-center shadow-lg">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LXdoaXRlIG1sLTAuNSIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGQ9Ik02LjMgMi44NDFBMS41IDEuNSAwIDAwNCA0LjExVjE1Ljg5YTEuNSAxLjUgMCAwMDIuMyAxLjI2OWw5LjM0NC01Ljg5YTEuNSAxLjUgMCAwMDAtMi41MzhMNi4zIDIuODR6IiAvPjwvc3ZnPg=="
class="w-5 h-5 text-white ml-0.5" />

</div>

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full h-full object-cover" />
{% endif %}

</div>

{% endwith %} {% else %}

<div class="bg-stone-900 flex items-center justify-center"
style="aspect-ratio: 16/9;">

<div class="text-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCBteC1hdXRvIHRleHQtc3RvbmUtNjAwIG1iLTEiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNSAxMGw0LjU1My0yLjI3NkExIDEgMCAwMTIxIDguNjE4djYuNzY0YTEgMSAwIDAxLTEuNDQ3Ljg5NEwxNSAxNE01IDE4aDhhMiAyIDAgMDAyLTJWOGEyIDIgMCAwMC0yLTJINWEyIDIgMCAwMC0yIDJ2OGEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-8 h-8 mx-auto text-stone-600 mb-1" />
<span class="text-[11px] text-stone-500">Video thumbnail</span>

</div>

</div>

{% endif %}

<div class="p-3">

<div class="text-[13px] font-semibold text-stone-900 leading-snug mb-1.5 line-clamp-2">

{% if p.title %}{{ p.title\|truncatechars:100 }}{% elif p.caption %}{{
p.caption\|truncatechars:100 }}{% else
%}<span class="text-stone-300 italic font-normal">Video title…</span>{%
endif %}

</div>

<div class="flex items-center gap-2 mb-2">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-6 h-6 rounded-full object-cover" /> {% else %}

<div class="w-6 h-6 rounded-full bg-red-600 flex items-center justify-center text-[9px] font-bold text-white">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %}

<div>

<div class="text-[11px] font-medium text-stone-600">

{{ p.account.account_name\|default:p.account.account_handle }}

</div>

<div class="text-[10px] text-stone-400">

0 views · Just now

</div>

</div>

</div>

{% if p.caption %}

<div class="text-[11px] text-stone-500 leading-relaxed line-clamp-3 whitespace-pre-wrap break-words">

{{ p.truncated_caption\|truncatechars:200 }}

</div>

{% endif %}

</div>

</div>

{% elif p.account.platform == "instagram" or p.account.platform ==
"instagram_personal" %} {# ─── Instagram ─── square media, account
header, action icons \#}

<div class="bg-white">

<div class="flex items-center gap-2.5 px-3 py-2.5">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-8 h-8 rounded-full object-cover"
style="border: 2px solid #E7E5E4;" /> {% else %}

<div class="w-8 h-8 rounded-full flex items-center justify-center text-[10px] font-bold text-white"
style="background: linear-gradient(135deg, #F58529, #DD2A7B, #8134AF);">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %} <span class="text-[13px] font-semibold text-stone-900">{{
p.account.account_name\|default:p.account.account_handle }}</span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTQwMCBtbC1hdXRvIiBmaWxsPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjeD0iMTIiIGN5PSI2IiByPSIyIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMiIgY3k9IjE4IiByPSIyIj48L2NpcmNsZT48L3N2Zz4="
class="w-4 h-4 text-stone-400 ml-auto" />

</div>

{% if media_items %} {% if media_items\|length \> 1 %} {# ─── Carousel
─── \#}

<div class="relative bg-stone-100" style="aspect-ratio: 1/1;"
x-data="{ slide: 0, count: {{ media_items|length }} }">

{% for m in media_items %}

<div class="absolute inset-0" x-show="slide === {{ forloop.counter0 }}">

{% if m.is_video %}

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full h-full object-cover" />
{% endif %}

</div>

{% endfor %}

<div class="absolute top-3 right-3 bg-black/60 text-white text-[11px] font-medium px-2 py-0.5 rounded-full"
x-text="(slide + 1) + '/' + count">

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1zdG9uZS03MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS43NSAxOS41TDguMjUgMTJsNy41LTcuNSIgLz48L3N2Zz4="
class="w-3.5 h-3.5 text-stone-700" />

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1zdG9uZS03MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik04LjI1IDQuNWw3LjUgNy41LTcuNSA3LjUiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-stone-700" />

<div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-1.5">

{% for m in media_items %}

{% endfor %}

</div>

</div>

{% else %} {# ─── Single media ─── \#} {% with m=media_items.0 %}

<div class="relative bg-stone-100" style="aspect-ratio: 1/1;">

{% if m.is_video %}

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full h-full object-cover" />
{% endif %}

</div>

{% endwith %} {% endif %} {% else %}

<div class="bg-stone-50 flex items-center justify-center"
style="aspect-ratio: 1/1;">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMCBoLTEwIHRleHQtc3RvbmUtMjAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMS41IiBkPSJNNCAxNmw0LjU4Ni00LjU4NmEyIDIgMCAwMTIuODI4IDBMMTYgMTZtLTItMmwxLjU4Ni0xLjU4NmEyIDIgMCAwMTIuODI4IDBMMjAgMTRtLTYtNmguMDFNNiAyMGgxMmEyIDIgMCAwMDItMlY2YTIgMiAwIDAwLTItMkg2YTIgMiAwIDAwLTIgMnYxMmEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-10 h-10 text-stone-200" />

</div>

{% endif %}

<div class="flex items-center gap-4 px-3 py-2.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTgwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTIxIDguMjVjMC0yLjQ4NS0yLjA5OS00LjUtNC42ODgtNC41LTEuOTM1IDAtMy41OTcgMS4xMjYtNC4zMTIgMi43MzMtLjcxNS0xLjYwNy0yLjM3Ny0yLjczMy00LjMxMy0yLjczM0M1LjEgMy43NSAzIDUuNzY1IDMgOC4yNWMwIDcuMjIgOSAxMiA5IDEyczktNC43OCA5LTEyeiIgLz48L3N2Zz4="
class="w-6 h-6 text-stone-800" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTgwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDIwLjI1YzQuOTcgMCA5LTMuNjk0IDktOC4yNXMtNC4wMy04LjI1LTktOC4yNVMzIDcuNDQ0IDMgMTJjMCAyLjEwNC44NTkgNC4wMjMgMi4yNzMgNS40OC40MzIuNDQ3Ljc0IDEuMDQuNTg2IDEuNjQxYTQuNDgzIDQuNDgzIDAgMDEtLjkyMyAxLjc4NUE1Ljk2OSA1Ljk2OSAwIDAwNiAyMWMxLjI4MiAwIDIuNDctLjQwMiAzLjQ0NS0xLjA4Ny44MS4yMiAxLjY2OC4zMzcgMi41NTUuMzM3eiIgLz48L3N2Zz4="
class="w-6 h-6 text-stone-800" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTgwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTYgMTJMMy4yNjkgMy4xMjZBNTkuNzY4IDU5Ljc2OCAwIDAxMjEuNDg1IDEyIDU5Ljc3IDU5Ljc3IDAgMDEzLjI3IDIwLjg3Nkw1Ljk5OSAxMnptMCAwaDcuNSIgLz48L3N2Zz4="
class="w-6 h-6 text-stone-800" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LXN0b25lLTgwMCBtbC1hdXRvIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjEuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTcuNTkzIDMuMzIyYzEuMS4xMjggMS45MDcgMS4wNzcgMS45MDcgMi4xODVWMjFMMTIgMTcuMjUgNC41IDIxVjUuNTA3YzAtMS4xMDguODA2LTIuMDU3IDEuOTA3LTIuMTg1YTQ4LjUwNyA0OC41MDcgMCAwMTExLjE4NiAweiIgLz48L3N2Zz4="
class="w-5 h-5 text-stone-800 ml-auto" />

</div>

<div class="px-3 pb-3">

{% if p.caption %}

<div class="text-[13px] text-stone-900 leading-relaxed">

<span class="font-semibold">{{
p.account.account_name\|default:p.account.account_handle }}</span>
<span class="whitespace-pre-wrap break-words">{{
p.truncated_caption\|truncatechars:150 }}</span>

</div>

{% else %}

<div class="text-[13px] text-stone-300 italic">

Write a caption…

</div>

{% endif %} {% if p.first_comment %}

<div class="text-[12px] text-stone-400 mt-1.5">

View all comments

</div>

{% endif %}

<div class="text-[10px] text-stone-400 uppercase tracking-wider mt-1.5">

Just now

</div>

</div>

</div>

{% elif p.account.platform == "facebook" %} {# ─── Facebook ─── classic
FB post card \#}

<div class="bg-white">

<div class="flex items-center gap-2.5 px-3 py-3">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-10 h-10 rounded-full object-cover" /> {% else %}

<div class="w-10 h-10 rounded-full bg-[#1877F2] flex items-center justify-center text-xs font-bold text-white">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %}

<div class="flex-1">

<div class="text-[13px] font-semibold text-stone-900">

{{ p.account.account_name\|default:p.account.account_handle }}

</div>

<div class="text-[11px] text-stone-400 flex items-center gap-1">

Just now · <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGQ9Ik04IDE2QTggOCAwIDEwOCAwYTggOCAwIDAwMCAxNnpNNC41IDcuNWEuNS41IDAgMDEuNS0uNWg2YS41LjUgMCAwMTAgMUg1YS41LjUgMCAwMS0uNS0uNXoiIC8+PC9zdmc+"
class="w-3 h-3" />

</div>

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LXN0b25lLTQwMCIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxjaXJjbGUgY3g9IjEyIiBjeT0iNiIgcj0iMiI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMiI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTIiIGN5PSIxOCIgcj0iMiI+PC9jaXJjbGU+PC9zdmc+"
class="w-5 h-5 text-stone-400" />

</div>

{% if p.caption %}

<div class="px-3 pb-3 text-[14px] text-stone-800 leading-relaxed whitespace-pre-wrap break-words">

{{ p.truncated_caption\|truncatechars:250 }}

</div>

{% endif %} {% if media_items %} {% if media_items\|length \> 1 %} {#
─── Carousel ─── \#}

<div class="relative bg-stone-100 overflow-hidden"
style="aspect-ratio: 16/9;"
x-data="{ slide: 0, count: {{ media_items|length }} }">

{% for m in media_items %}

<div class="absolute inset-0" x-show="slide === {{ forloop.counter0 }}">

{% if m.is_video %}

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-14 h-14 rounded-full bg-black/40 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXdoaXRlIG1sLTAuNSIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGQ9Ik02LjMgMi44NDFBMS41IDEuNSAwIDAwNCA0LjExVjE1Ljg5YTEuNSAxLjUgMCAwMDIuMyAxLjI2OWw5LjM0NC01Ljg5YTEuNSAxLjUgMCAwMDAtMi41MzhMNi4zIDIuODR6IiAvPjwvc3ZnPg=="
class="w-6 h-6 text-white ml-0.5" />

</div>

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full h-full object-cover" />
{% endif %}

</div>

{% endfor %}

<div class="absolute top-3 right-3 bg-black/60 text-white text-[11px] font-medium px-2 py-0.5 rounded-full z-10"
x-text="(slide + 1) + '/' + count">

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1zdG9uZS03MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS43NSAxOS41TDguMjUgMTJsNy41LTcuNSIgLz48L3N2Zz4="
class="w-3.5 h-3.5 text-stone-700" />

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1zdG9uZS03MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik04LjI1IDQuNWw3LjUgNy41LTcuNSA3LjUiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-stone-700" />

<div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-1.5 z-10">

{% for m in media_items %}

{% endfor %}

</div>

</div>

{% else %} {# ─── Single media ─── \#} {% with m=media_items.0 %}

<div class="relative bg-stone-100">

{% if m.is_video %}

<div style="aspect-ratio: 16/9;">

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-14 h-14 rounded-full bg-black/40 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXdoaXRlIG1sLTAuNSIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGQ9Ik02LjMgMi44NDFBMS41IDEuNSAwIDAwNCA0LjExVjE1Ljg5YTEuNSAxLjUgMCAwMDIuMyAxLjI2OWw5LjM0NC01Ljg5YTEuNSAxLjUgMCAwMDAtMi41MzhMNi4zIDIuODR6IiAvPjwvc3ZnPg=="
class="w-6 h-6 text-white ml-0.5" />

</div>

</div>

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full object-cover"
style="max-height: 220px;" /> {% endif %}

</div>

{% endwith %} {% endif %} {% endif %}

<div class="px-3 py-2 border-t border-stone-100 flex items-center justify-around text-stone-500 text-[12px] font-medium">

<span class="flex items-center gap-1.5 hover:bg-stone-50 px-3 py-1.5 rounded-md">
<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTYuNjMzIDEwLjVjLjgwNiAwIDEuNTMzLS40NDYgMi4wMzEtMS4wOGE5LjA0MSA5LjA0MSAwIDAxMi44NjEtMi40Yy43MjMtLjM4NCAxLjM1LS45NTYgMS42NTMtMS43MTVhNC40OTggNC40OTggMCAwMC4zMjItMS42NzJWM2EuNzUuNzUgMCAwMS43NS0uNzVBMi4yNSAyLjI1IDAgMDExNi41IDQuNWMwIDEuMTUyLS4yNiAyLjI0My0uNzIzIDMuMjE4LS4yNjYuNTU4LjEwNyAxLjI4Mi43MjUgMS4yODJoMy4xMjZjMS4wMjYgMCAxLjk0NS42OTQgMi4wNTQgMS43MTUuMDQ1LjQyMi4wNjguODUuMDY4IDEuMjg1YTExLjk1IDExLjk1IDAgMDEtMi42NDkgNy41MjFjLS4zODguNDgyLS45ODcuNzI5LTEuNjA1LjcyOUgxMy40OGMtLjQ4MyAwLS45NjQtLjA3OC0xLjQyMy0uMjNsLTMuMTE0LTEuMDRhNC41MDEgNC41MDEgMCAwMC0xLjQyMy0uMjNINS45MDRNMTQuMjUgOWgyLjI1TTUuOTA0IDE4Ljc1Yy4wODMuMjA1LjE3My40MDUuMjcuNjAyLjE5Ny40LS4wNzguODk4LS41MjMuODk4aC0uOTA4Yy0uODg5IDAtMS43MTMtLjUxOC0xLjk3Mi0xLjM2OGExMiAxMiAwIDAxLS41MjEtMy41MDdjMC0xLjU1My4yOTUtMy4wMzYuODMxLTQuMzk4QzMuMzg3IDkuOTUzIDQuMTY3IDkuNSA1IDkuNWguMDk2Yy41IDAgLjkwNS40MDUuOTA1LjkwNSAwIC43MTQtLjIxMSAxLjQxMi0uNjA4IDIuMDA2TDQgMTQuMjVsMS45MDQgNC41eiIgLz48L3N2Zz4="
class="w-4 h-4" /> Like </span>
<span class="flex items-center gap-1.5 hover:bg-stone-50 px-3 py-1.5 rounded-md">
<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDIwLjI1YzQuOTcgMCA5LTMuNjk0IDktOC4yNXMtNC4wMy04LjI1LTktOC4yNVMzIDcuNDQ0IDMgMTJjMCAyLjEwNC44NTkgNC4wMjMgMi4yNzMgNS40OC40MzIuNDQ3Ljc0IDEuMDQuNTg2IDEuNjQxYTQuNDgzIDQuNDgzIDAgMDEtLjkyMyAxLjc4NUE1Ljk2OSA1Ljk2OSAwIDAwNiAyMWMxLjI4MiAwIDIuNDctLjQwMiAzLjQ0NS0xLjA4Ny44MS4yMiAxLjY2OC4zMzcgMi41NTUuMzM3eiIgLz48L3N2Zz4="
class="w-4 h-4" /> Comment </span>
<span class="flex items-center gap-1.5 hover:bg-stone-50 px-3 py-1.5 rounded-md">
<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTcuMjE3IDEwLjkwN2EyLjI1IDIuMjUgMCAxMDAgMi4xODZtMC0yLjE4NmMuMTguMzI0LjI4My42OTYuMjgzIDEuMDkzcy0uMTAzLjc3LS4yODMgMS4wOTNtMC0yLjE4Nmw5LjU2Ni01LjMxNG0tOS41NjYgNy41bDkuNTY2IDUuMzE0bTAgMGEyLjI1IDIuMjUgMCAxMDMuOTM1IDIuMTg2IDIuMjUgMi4yNSAwIDAwLTMuOTM1LTIuMTg2em0wLTEyLjgxNGEyLjI1IDIuMjUgMCAxMDMuOTMzLTIuMTg1IDIuMjUgMi4yNSAwIDAwLTMuOTMzIDIuMTg1eiIgLz48L3N2Zz4="
class="w-4 h-4" /> Share </span>

</div>

</div>

{% elif p.account.platform == "linkedin_personal" or p.account.platform
== "linkedin_company" %} {# ─── LinkedIn ─── professional feed card \#}

<div class="bg-white">

<div class="flex items-start gap-2.5 px-3 py-3">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-12 h-12 rounded-full object-cover" /> {% else %}

<div class="w-12 h-12 rounded-full bg-[#0A66C2] flex items-center justify-center text-sm font-bold text-white">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %}

<div class="flex-1 min-w-0">

<div class="text-[13px] font-semibold text-stone-900">

{{ p.account.account_name\|default:p.account.account_handle }}

</div>

<div class="text-[11px] text-stone-400 leading-tight truncate">

{{ p.account.account_handle\|default:"Company page" }}

</div>

<div class="text-[11px] text-stone-400 flex items-center gap-1 mt-0.5">

Just now · <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGQ9Ik0wIDhhOCA4IDAgMTExNiAwQTggOCAwIDAxMCA4em01LjQ5Ni0zLjM5N0EuNzUuNzUgMCAwMDQuNSA1LjI1djUuNWEuNzUuNzUgMCAwMDEuMDUyLjY4N2w0Ljk3LTIuNTIyLjA2My0uMDM1YS43NS43NSAwIDAwMC0xLjM0bC0uMDYzLS4wMzYtNC45Ny0yLjUyMS0uMDU2LS4wMnoiIC8+PC9zdmc+"
class="w-3 h-3" />

</div>

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LXN0b25lLTQwMCBmbGV4LXNocmluay0wIiBmaWxsPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjeD0iMTIiIGN5PSI2IiByPSIyIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIj48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMiIgY3k9IjE4IiByPSIyIj48L2NpcmNsZT48L3N2Zz4="
class="w-5 h-5 text-stone-400 flex-shrink-0" />

</div>

{% if p.caption %}

<div class="px-3 pb-3 text-[13px] text-stone-700 leading-relaxed whitespace-pre-wrap break-words">

{{ p.truncated_caption\|truncatechars:200 }}

</div>

{% endif %} {% if media_items %} {% if media_items\|length \> 1 %} {#
─── Carousel ─── \#}

<div class="relative bg-stone-100 overflow-hidden"
style="aspect-ratio: 16/9;"
x-data="{ slide: 0, count: {{ media_items|length }} }">

{% for m in media_items %}

<div class="absolute inset-0" x-show="slide === {{ forloop.counter0 }}">

{% if m.is_video %}

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-14 h-14 rounded-full bg-[#0A66C2]/80 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXdoaXRlIG1sLTAuNSIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGQ9Ik02LjMgMi44NDFBMS41IDEuNSAwIDAwNCA0LjExVjE1Ljg5YTEuNSAxLjUgMCAwMDIuMyAxLjI2OWw5LjM0NC01Ljg5YTEuNSAxLjUgMCAwMDAtMi41MzhMNi4zIDIuODR6IiAvPjwvc3ZnPg=="
class="w-6 h-6 text-white ml-0.5" />

</div>

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full h-full object-cover" />
{% endif %}

</div>

{% endfor %}

<div class="absolute top-3 right-3 bg-black/60 text-white text-[11px] font-medium px-2 py-0.5 rounded-full z-10"
x-text="(slide + 1) + '/' + count">

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1zdG9uZS03MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS43NSAxOS41TDguMjUgMTJsNy41LTcuNSIgLz48L3N2Zz4="
class="w-3.5 h-3.5 text-stone-700" />

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1zdG9uZS03MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik04LjI1IDQuNWw3LjUgNy41LTcuNSA3LjUiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-stone-700" />

<div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-1.5 z-10">

{% for m in media_items %}

{% endfor %}

</div>

</div>

{% else %} {# ─── Single media ─── \#} {% with m=media_items.0 %}

<div class="relative bg-stone-100">

{% if m.is_video %}

<div style="aspect-ratio: 16/9;">

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-14 h-14 rounded-full bg-[#0A66C2]/80 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXdoaXRlIG1sLTAuNSIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGQ9Ik02LjMgMi44NDFBMS41IDEuNSAwIDAwNCA0LjExVjE1Ljg5YTEuNSAxLjUgMCAwMDIuMyAxLjI2OWw5LjM0NC01Ljg5YTEuNSAxLjUgMCAwMDAtMi41MzhMNi4zIDIuODR6IiAvPjwvc3ZnPg=="
class="w-6 h-6 text-white ml-0.5" />

</div>

</div>

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full object-cover"
style="max-height: 220px;" /> {% endif %}

</div>

{% endwith %} {% endif %} {% endif %}

<div class="px-3 py-2 border-t border-stone-100 flex items-center justify-around text-stone-500 text-[11px] font-medium">

<span class="flex items-center gap-1"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTYuNjMzIDEwLjVjLjgwNiAwIDEuNTMzLS40NDYgMi4wMzEtMS4wOGE5LjA0MSA5LjA0MSAwIDAxMi44NjEtMi40Yy43MjMtLjM4NCAxLjM1LS45NTYgMS42NTMtMS43MTVhNC40OTggNC40OTggMCAwMC4zMjItMS42NzJWM2EuNzUuNzUgMCAwMS43NS0uNzVBMi4yNSAyLjI1IDAgMDExNi41IDQuNWMwIDEuMTUyLS4yNiAyLjI0My0uNzIzIDMuMjE4LS4yNjYuNTU4LjEwNyAxLjI4Mi43MjUgMS4yODJoMy4xMjZjMS4wMjYgMCAxLjk0NS42OTQgMi4wNTQgMS43MTUuMDQ1LjQyMi4wNjguODUuMDY4IDEuMjg1YTExLjk1IDExLjk1IDAgMDEtMi42NDkgNy41MjFjLS4zODguNDgyLS45ODcuNzI5LTEuNjA1LjcyOUgxMy40OGMtLjQ4MyAwLS45NjQtLjA3OC0xLjQyMy0uMjNsLTMuMTE0LTEuMDRhNC41MDEgNC41MDEgMCAwMC0xLjQyMy0uMjNINS45MDRNMTQuMjUgOWgyLjI1TTUuOTA0IDE4Ljc1Yy4wODMuMjA1LjE3My40MDUuMjcuNjAyLjE5Ny40LS4wNzguODk4LS41MjMuODk4aC0uOTA4Yy0uODg5IDAtMS43MTMtLjUxOC0xLjk3Mi0xLjM2OGExMiAxMiAwIDAxLS41MjEtMy41MDdjMC0xLjU1My4yOTUtMy4wMzYuODMxLTQuMzk4QzMuMzg3IDkuOTUzIDQuMTY3IDkuNSA1IDkuNWguMDk2Yy41IDAgLjkwNS40MDUuOTA1LjkwNSAwIC43MTQtLjIxMSAxLjQxMi0uNjA4IDIuMDA2TDQgMTQuMjVsMS45MDQgNC41eiIgLz48L3N2Zz4="
class="w-4 h-4" /> Like</span>
<span class="flex items-center gap-1"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDIwLjI1YzQuOTcgMCA5LTMuNjk0IDktOC4yNXMtNC4wMy04LjI1LTktOC4yNVMzIDcuNDQ0IDMgMTJjMCAyLjEwNC44NTkgNC4wMjMgMi4yNzMgNS40OC40MzIuNDQ3Ljc0IDEuMDQuNTg2IDEuNjQxYTQuNDgzIDQuNDgzIDAgMDEtLjkyMyAxLjc4NUE1Ljk2OSA1Ljk2OSAwIDAwNiAyMWMxLjI4MiAwIDIuNDctLjQwMiAzLjQ0NS0xLjA4Ny44MS4yMiAxLjY2OC4zMzcgMi41NTUuMzM3eiIgLz48L3N2Zz4="
class="w-4 h-4" /> Comment</span>
<span class="flex items-center gap-1"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE5LjUgMTJjMC0xLjIzMi0uMDQ2LTIuNDUzLS4xMzgtMy42NjJhNC4wMDYgNC4wMDYgMCAwMC0zLjctMy43IDQ4LjY3OCA0OC42NzggMCAwMC03LjMyNCAwIDQuMDA2IDQuMDA2IDAgMDAtMy43IDMuN2MtLjAxNy4yMi0uMDMyLjQ0MS0uMDQ2LjY2Mk0xOS41IDEybDMtM20tMyAzbC0zLTNtLTEyIDNjMCAxLjIzMi4wNDYgMi40NTMuMTM4IDMuNjYyYTQuMDA2IDQuMDA2IDAgMDAzLjcgMy43IDQ4LjY1NiA0OC42NTYgMCAwMDcuMzI0IDAgNC4wMDYgNC4wMDYgMCAwMDMuNy0zLjdjLjAxNy0uMjIuMDMyLS40NDEuMDQ2LS42NjJNNC41IDEybDMgM20tMy0zbC0zIDMiIC8+PC9zdmc+"
class="w-4 h-4" /> Repost</span>
<span class="flex items-center gap-1"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTYgMTJMMy4yNjkgMy4xMjZBNTkuNzY4IDU5Ljc2OCAwIDAxMjEuNDg1IDEyIDU5Ljc3IDU5Ljc3IDAgMDEzLjI3IDIwLjg3Nkw1Ljk5OSAxMnptMCAwaDcuNSIgLz48L3N2Zz4="
class="w-4 h-4" /> Send</span>

</div>

</div>

{% elif p.account.platform == "tiktok" %} {# ─── TikTok ─── vertical
phone-style preview \#}

<div class="bg-black">

<div class="bg-black text-white relative overflow-hidden mx-auto"
style="aspect-ratio: 9/16; max-height: 480px;">

{% if media_items %} {% with m=media_items.0 %} {% if m.is_video %}

{% else %} <img src="%7B%7B%20m.url%20%7D%7D"
class="absolute inset-0 w-full h-full object-cover" /> {% endif %} {%
endwith %} {% else %}

<div class="absolute inset-0 flex flex-col items-center justify-center bg-stone-900">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMCBoLTEwIHRleHQtc3RvbmUtNjAwIG1iLTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNS43NSAxMC41bDQuNzItNC43MmEuNzUuNzUgMCAwMTEuMjguNTN2MTEuMzhhLjc1Ljc1IDAgMDEtMS4yOC41M2wtNC43Mi00LjcyTTQuNSAxOC43NWg5YTIuMjUgMi4yNSAwIDAwMi4yNS0yLjI1di05YTIuMjUgMi4yNSAwIDAwLTIuMjUtMi4yNWgtOUEyLjI1IDIuMjUgMCAwMDIuMjUgNy41djlhMi4yNSAyLjI1IDAgMDAyLjI1IDIuMjV6IiAvPjwvc3ZnPg=="
class="w-10 h-10 text-stone-600 mb-2" />
<span class="text-[11px] text-stone-500">Upload a video</span>

</div>

{% endif %}

<div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent">

</div>

<div class="absolute right-2.5 bottom-16 flex flex-col items-center gap-3.5">

<div class="relative mb-1">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-10 h-10 rounded-full object-cover border-2 border-white" /> {%
else %}

<div class="w-10 h-10 rounded-full bg-stone-700 flex items-center justify-center text-[11px] font-bold text-white border-2 border-white">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %}

<div class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-4.5 h-4.5 bg-[#FE2C55] rounded-full flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUgdGV4dC13aGl0ZSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIzIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIGQ9Ik0xMiA2djEybS02LTZoMTIiIC8+PC9zdmc+"
class="w-2.5 h-2.5 text-white" />

</div>

</div>

<div class="flex flex-col items-center gap-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy03IGgtNyBkcm9wLXNoYWRvdy1zbSIgZmlsbD0id2hpdGUiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDIxLjM1bC0xLjQ1LTEuMzJDNS40IDE1LjM2IDIgMTIuMjggMiA4LjUgMiA1LjQyIDQuNDIgMyA3LjUgM2MxLjc0IDAgMy40MS44MSA0LjUgMi4wOUMxMy4wOSAzLjgxIDE0Ljc2IDMgMTYuNSAzIDE5LjU4IDMgMjIgNS40MiAyMiA4LjVjMCAzLjc4LTMuNCA2Ljg2LTguNTUgMTEuNTRMMTIgMjEuMzV6IiAvPjwvc3ZnPg=="
class="w-7 h-7 drop-shadow-sm" />
<span class="text-[10px] font-medium drop-shadow-sm">0</span>

</div>

<div class="flex flex-col items-center gap-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy03IGgtNyBkcm9wLXNoYWRvdy1zbSIgZmlsbD0id2hpdGUiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJDNi40NzcgMiAyIDUuODEzIDIgMTAuNWMwIDIuNjE0IDEuMzk0IDQuOTYgMy41ODYgNi41My0uMTYgMS40MDQtLjg2MiAyLjY3Mi0xLjU4NiAzLjQ3YS41LjUgMCAwMC4zNjIuODRjMi4wMjYtLjA2NCAzLjc2Mi0uNzYgNS4wMjgtMS41OS44NTMuMTY0IDEuNzQuMjUgMi42MS4yNSA1LjUyMyAwIDEwLTMuODEzIDEwLTguNVMxNy41MjMgMiAxMiAyeiIgLz48L3N2Zz4="
class="w-7 h-7 drop-shadow-sm" />
<span class="text-[10px] font-medium drop-shadow-sm">0</span>

</div>

<div class="flex flex-col items-center gap-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiBkcm9wLXNoYWRvdy1zbSIgZmlsbD0id2hpdGUiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTUgNWEyIDIgMCAwMTItMmgxMGEyIDIgMCAwMTIgMnYxNmwtNy0zLjVMNSAyMVY1eiIgLz48L3N2Zz4="
class="w-6 h-6 drop-shadow-sm" />
<span class="text-[10px] font-medium drop-shadow-sm">0</span>

</div>

<div class="flex flex-col items-center gap-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiBkcm9wLXNoYWRvdy1zbSIgZmlsbD0id2hpdGUiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE1IDVsLTEuNDEgMS40MUwxNS4xNyA4SDExYy0zLjg3IDAtNyAzLjEzLTcgN3YyaDJ2LTJjMC0yLjc2IDIuMjQtNSA1LTVoNC4xN2wtMS41OCAxLjU5TDE1IDEzbDQtNC00LTR6IiAvPjwvc3ZnPg=="
class="w-6 h-6 drop-shadow-sm" />

</div>

<div class="w-8 h-8 rounded-full border-2 border-stone-500 bg-stone-800 flex items-center justify-center mt-0.5">

<div class="w-3 h-3 rounded-full bg-stone-400">

</div>

</div>

</div>

<div class="absolute bottom-3 left-3 right-16">

<div class="text-[13px] font-bold mb-1 drop-shadow-sm">

@{{ p.account.account_name\|default:p.account.account_handle }}

</div>

{% if p.caption %}

<div class="text-[12px] leading-relaxed line-clamp-2 whitespace-pre-wrap drop-shadow-sm">

{{ p.truncated_caption\|truncatechars:100 }}

</div>

{% endif %}

<div class="flex items-center gap-1.5 mt-2">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyBmbGV4LXNocmluay0wIiBmaWxsPSJ3aGl0ZSIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMTIgM3YxMC41NWMtLjU5LS4zNC0xLjI3LS41NS0yLS41NS0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRWN2g0VjNoLTZ6IiAvPjwvc3ZnPg=="
class="w-3 h-3 flex-shrink-0" />
<span class="text-[11px] truncate drop-shadow-sm">Original sound - {{
p.account.account_name\|default:p.account.account_handle }}</span>

</div>

</div>

</div>

</div>

{% elif p.account.platform == "threads" %} {# ─── Threads ─── minimal
text-first layout \#}

<div class="bg-white p-3">

<div class="flex gap-3">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-9 h-9 rounded-full object-cover flex-shrink-0" /> {% else %}

<div class="w-9 h-9 rounded-full bg-black flex items-center justify-center text-[10px] font-bold text-white flex-shrink-0">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %}

<div class="flex-1 min-w-0">

<div class="flex items-center gap-1.5 mb-0.5">

<span class="text-[13px] font-semibold text-stone-900">{{
p.account.account_name\|default:p.account.account_handle }}</span>
<span class="text-[11px] text-stone-400">just now</span>

</div>

{% if p.caption %}

<div class="text-[13px] text-stone-800 leading-relaxed whitespace-pre-wrap break-words mb-2">

{{ p.truncated_caption\|truncatechars:200 }}

</div>

{% else %}

<div class="text-[13px] text-stone-300 italic mb-2">

Start a thread…

</div>

{% endif %} {% if media_items %} {% if media_items\|length \> 1 %} {#
─── Carousel ─── \#}

<div class="relative rounded-lg overflow-hidden mb-2"
style="aspect-ratio: 4/3;"
x-data="{ slide: 0, count: {{ media_items|length }} }">

{% for m in media_items %}

<div class="absolute inset-0" x-show="slide === {{ forloop.counter0 }}">

{% if m.is_video %}

<div class="relative bg-stone-900 w-full h-full">

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full h-full object-cover" />
{% endif %}

</div>

{% endfor %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0ZXh0LXN0b25lLTcwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE1Ljc1IDE5LjVMOC4yNSAxMmw3LjUtNy41IiAvPjwvc3ZnPg=="
class="w-3 h-3 text-stone-700" />

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0ZXh0LXN0b25lLTcwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTguMjUgNC41bDcuNSA3LjUtNy41IDcuNSIgLz48L3N2Zz4="
class="w-3 h-3 text-stone-700" />

<div class="absolute bottom-2 left-1/2 -translate-x-1/2 flex gap-1.5 z-10">

{% for m in media_items %}

{% endfor %}

</div>

</div>

{% else %} {# ─── Single media ─── \#} {% with m=media_items.0 %}

<div class="rounded-lg overflow-hidden mb-2">

{% if m.is_video %}

<div class="relative bg-stone-900" style="aspect-ratio: 16/9;">

</div>

{% else %} <img src="%7B%7B%20m.url%20%7D%7D"
class="w-full rounded-lg object-cover" style="max-height: 180px;" /> {%
endif %}

</div>

{% endwith %} {% endif %} {% endif %}

<div class="flex items-center gap-4 text-stone-400">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00LjUgaC00LjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0yMSA4LjI1YzAtMi40ODUtMi4wOTktNC41LTQuNjg4LTQuNS0xLjkzNSAwLTMuNTk3IDEuMTI2LTQuMzEyIDIuNzMzLS43MTUtMS42MDctMi4zNzctMi43MzMtNC4zMTMtMi43MzNDNS4xIDMuNzUgMyA1Ljc2NSAzIDguMjVjMCA3LjIyIDkgMTIgOSAxMnM5LTQuNzggOS0xMnoiIC8+PC9zdmc+"
class="w-4.5 h-4.5" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00LjUgaC00LjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiAyMC4yNWM0Ljk3IDAgOS0zLjY5NCA5LTguMjVzLTQuMDMtOC4yNS05LTguMjVTMyA3LjQ0NCAzIDEyYzAgMi4xMDQuODU5IDQuMDIzIDIuMjczIDUuNDguNDMyLjQ0Ny43NCAxLjA0LjU4NiAxLjY0MWE0LjQ4MyA0LjQ4MyAwIDAxLS45MjMgMS43ODVBNS45NjkgNS45NjkgMCAwMDYgMjFjMS4yODIgMCAyLjQ3LS40MDIgMy40NDUtMS4wODcuODEuMjIgMS42NjguMzM3IDIuNTU1LjMzN3oiIC8+PC9zdmc+"
class="w-4.5 h-4.5" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00LjUgaC00LjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOS41IDEyYzAtMS4yMzItLjA0Ni0yLjQ1My0uMTM4LTMuNjYyYTQuMDA2IDQuMDA2IDAgMDAtMy43LTMuNyA0OC42NzggNDguNjc4IDAgMDAtNy4zMjQgMCA0LjAwNiA0LjAwNiAwIDAwLTMuNyAzLjdjLS4wMTcuMjItLjAzMi40NDEtLjA0Ni42NjJNMTkuNSAxMmwzLTNtLTMgM2wtMy0zbS0xMiAzYzAgMS4yMzIuMDQ2IDIuNDUzLjEzOCAzLjY2MmE0LjAwNiA0LjAwNiAwIDAwMy43IDMuNyA0OC42NTYgNDguNjU2IDAgMDA3LjMyNCAwIDQuMDA2IDQuMDA2IDAgMDAzLjctMy43Yy4wMTctLjIyLjAzMi0uNDQxLjA0Ni0uNjYyTTQuNSAxMmwzIDNtLTMtM2wtMyAzIiAvPjwvc3ZnPg=="
class="w-4.5 h-4.5" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00LjUgaC00LjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik02IDEyTDMuMjY5IDMuMTI2QTU5Ljc2OCA1OS43NjggMCAwMTIxLjQ4NSAxMiA1OS43NyA1OS43NyAwIDAxMy4yNyAyMC44NzZMNS45OTkgMTJ6bTAgMGg3LjUiIC8+PC9zdmc+"
class="w-4.5 h-4.5" />

</div>

</div>

</div>

</div>

{% elif p.account.platform == "bluesky" %} {# ─── Bluesky ─── tweet-like
minimal card \#}

<div class="bg-white p-3">

<div class="flex gap-2.5">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-10 h-10 rounded-full object-cover flex-shrink-0" /> {% else %}

<div class="w-10 h-10 rounded-full bg-[#0085FF] flex items-center justify-center text-xs font-bold text-white flex-shrink-0">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %}

<div class="flex-1 min-w-0">

<div class="flex items-center gap-1.5 mb-0.5">

<span class="text-[13px] font-semibold text-stone-900">{{
p.account.account_name\|default:p.account.account_handle }}</span>
<span class="text-[12px] text-stone-400">{{
p.account.account_handle\|default:"@handle" }}</span>
<span class="text-[11px] text-stone-400 ml-auto">now</span>

</div>

{% if p.caption %}

<div class="text-[13px] text-stone-800 leading-relaxed whitespace-pre-wrap break-words mb-2">

{{ p.truncated_caption\|truncatechars:200 }}

</div>

{% else %}

<div class="text-[13px] text-stone-300 italic mb-2">

What's up?

</div>

{% endif %} {% if media_items %} {% with m=media_items.0 %}

<div class="rounded-xl overflow-hidden border border-stone-200 mb-2">

{% if m.is_video %}

<div class="relative bg-stone-900" style="aspect-ratio: 16/9;">

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full object-cover"
style="max-height: 180px;" /> {% endif %}

</div>

{% endwith %} {% endif %}

<div class="flex items-center justify-between text-stone-400 pr-4">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDIwLjI1YzQuOTcgMCA5LTMuNjk0IDktOC4yNXMtNC4wMy04LjI1LTktOC4yNVMzIDcuNDQ0IDMgMTJjMCAyLjEwNC44NTkgNC4wMjMgMi4yNzMgNS40OC40MzIuNDQ3Ljc0IDEuMDQuNTg2IDEuNjQxYTQuNDgzIDQuNDgzIDAgMDEtLjkyMyAxLjc4NUE1Ljk2OSA1Ljk2OSAwIDAwNiAyMWMxLjI4MiAwIDIuNDctLjQwMiAzLjQ0NS0xLjA4Ny44MS4yMiAxLjY2OC4zMzcgMi41NTUuMzM3eiIgLz48L3N2Zz4="
class="w-4 h-4" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE5LjUgMTJjMC0xLjIzMi0uMDQ2LTIuNDUzLS4xMzgtMy42NjJhNC4wMDYgNC4wMDYgMCAwMC0zLjctMy43IDQ4LjY3OCA0OC42NzggMCAwMC03LjMyNCAwIDQuMDA2IDQuMDA2IDAgMDAtMy43IDMuN2MtLjAxNy4yMi0uMDMyLjQ0MS0uMDQ2LjY2Mk0xOS41IDEybDMtM20tMyAzbC0zLTNtLTEyIDNjMCAxLjIzMi4wNDYgMi40NTMuMTM4IDMuNjYyYTQuMDA2IDQuMDA2IDAgMDAzLjcgMy43IDQ4LjY1NiA0OC42NTYgMCAwMDcuMzI0IDAgNC4wMDYgNC4wMDYgMCAwMDMuNy0zLjdjLjAxNy0uMjIuMDMyLS40NDEuMDQ2LS42NjJNNC41IDEybDMgM20tMy0zbC0zIDMiIC8+PC9zdmc+"
class="w-4 h-4" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTIxIDguMjVjMC0yLjQ4NS0yLjA5OS00LjUtNC42ODgtNC41LTEuOTM1IDAtMy41OTcgMS4xMjYtNC4zMTIgMi43MzMtLjcxNS0xLjYwNy0yLjM3Ny0yLjczMy00LjMxMy0yLjczM0M1LjEgMy43NSAzIDUuNzY1IDMgOC4yNWMwIDcuMjIgOSAxMiA5IDEyczktNC43OCA5LTEyeiIgLz48L3N2Zz4="
class="w-4 h-4" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDYuNzVhLjc1Ljc1IDAgMTEwLTEuNS43NS43NSAwIDAxMCAxLjV6TTEyIDEyLjc1YS43NS43NSAwIDExMC0xLjUuNzUuNzUgMCAwMTAgMS41ek0xMiAxOC43NWEuNzUuNzUgMCAxMTAtMS41Ljc1Ljc1IDAgMDEwIDEuNXoiIC8+PC9zdmc+"
class="w-4 h-4" />

</div>

</div>

</div>

</div>

{% elif p.account.platform == "pinterest" %} {# ─── Pinterest ─── pin
card with rounded corners \#}

<div class="bg-white">

{% if media_items %} {% with m=media_items.0 %}

<div class="rounded-t-xl overflow-hidden bg-stone-100">

{% if m.is_video %}

<div class="relative" style="aspect-ratio: 2/3; max-height: 260px;">

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full object-cover"
style="aspect-ratio: 2/3; max-height: 260px;" /> {% endif %}

</div>

{% endwith %} {% else %}

<div class="bg-stone-50 flex items-center justify-center rounded-t-xl w-full"
style="aspect-ratio: 2/3; max-height: 200px;">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMCBoLTEwIHRleHQtWyNFNjAwMjNdLzMwIiBmaWxsPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyLjAxNyAwQzUuMzk2IDAgLjAyOSA1LjM2Ny4wMjkgMTEuOTg3YzAgNS4wNzkgMy4xNTggOS40MTcgNy42MTggMTEuMTYyLS4xMDUtLjk0OS0uMTk5LTIuNDAzLjA0MS0zLjQzOS4yMTktLjkzNyAxLjQwNi01Ljk1NyAxLjQwNi01Ljk1N3MtLjM1OS0uNzItLjM1OS0xLjc4MWMwLTEuNjYzLjk2Ny0yLjkxMSAyLjE2OC0yLjkxMSAxLjAyNCAwIDEuNTE4Ljc2OSAxLjUxOCAxLjY4OCAwIDEuMDI5LS42NTMgMi41NjctLjk5MiAzLjk5Mi0uMjg1IDEuMTkzLjYgMi4xNjUgMS43NzUgMi4xNjUgMi4xMjggMCAzLjc2OC0yLjI0NSAzLjc2OC01LjQ4NyAwLTIuODYxLTIuMDYzLTQuODY5LTUuMDA4LTQuODY5LTMuNDEgMC01LjQwOSAyLjU2Mi01LjQwOSA1LjE5OSAwIDEuMDMzLjM5NCAyLjE0My44ODkgMi43NDEuMDk5LjEyLjExMi4yMjUuMDg1LjM0NS0uMDkuMzc1LS4yOTMgMS4xOTktLjMzNCAxLjM2My0uMDUzLjIyNS0uMTc0LjI3MS0uNDAxLjE2NS0xLjQ5NS0uNjktMi40MzMtMi44NzgtMi40MzMtNC42NDYgMC0zLjc3NiAyLjc0OC03LjI1MiA3LjkyLTcuMjUyIDQuMTU4IDAgNy4zOTIgMi45NjcgNy4zOTIgNi45MjMgMCA0LjEzNS0yLjYwNyA3LjQ2Mi02LjIzMyA3LjQ2Mi0xLjIxNCAwLTIuMzU0LS42MjktMi43NTgtMS4zNzlsLS43NDkgMi44NDhjLS4yNjkgMS4wNDUtMS4wMDQgMi4zNTItMS40OTggMy4xNDYgMS4xMjMuMzQ1IDIuMzA2LjUzNSAzLjU1LjUzNSA2LjYwNyAwIDExLjk4NS01LjM2NSAxMS45ODUtMTEuOTg3QzIzLjk3IDUuMzkgMTguNTkyLjAyNiAxMS45ODUuMDI2TDEyLjAxNyAweiIgLz48L3N2Zz4="
class="w-10 h-10 text-[#E60023]/30" />

</div>

{% endif %}

<div class="p-3">

{% if p.title %}

<div class="text-[13px] font-semibold text-stone-900 leading-snug mb-1 line-clamp-2">

{{ p.title\|truncatechars:100 }}

</div>

{% endif %} {% if p.caption %}

<div class="text-[11px] text-stone-500 leading-relaxed mb-2 line-clamp-2 whitespace-pre-wrap break-words">

{{ p.truncated_caption\|truncatechars:150 }}

</div>

{% endif %}

<div class="flex items-center gap-2">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-6 h-6 rounded-full object-cover" /> {% else %}

<div class="w-6 h-6 rounded-full bg-[#E60023] flex items-center justify-center text-[9px] font-bold text-white">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %} <span class="text-[11px] font-medium text-stone-600">{{
p.account.account_name\|default:p.account.account_handle }}</span>

</div>

</div>

</div>

{% else %} {# ─── Generic fallback (mastodon, google_business, etc.) \#}

<div class="bg-white p-4">

<div class="flex items-center gap-2.5 mb-3">

{% if p.account.avatar_url %}
<img src="%7B%7B%20p.account.avatar_url%20%7D%7D"
class="w-10 h-10 rounded-full object-cover border border-stone-100" />
{% else %}

<div class="w-10 h-10 rounded-full bg-stone-500 flex items-center justify-center text-xs font-bold text-white">

{{
p.account.account_name\|default:p.account.account_handle\|make_list\|first\|upper
}}

</div>

{% endif %}

<div>

<div class="text-[13px] font-semibold text-stone-800 leading-tight">

{{ p.account.account_name\|default:p.account.account_handle }}

</div>

{% if p.account.account_handle %}

<div class="text-[11px] text-stone-400 leading-tight">

{{ p.account.account_handle }}

</div>

{% endif %}

<div class="text-[10px] text-stone-400">

Just now

</div>

</div>

</div>

{% if p.caption %}

<div class="text-[13px] leading-relaxed text-stone-700 mb-3 whitespace-pre-wrap break-words">

{{ p.truncated_caption\|truncatechars:200 }}

</div>

{% else %}

<div class="text-[13px] text-stone-300 italic mb-3">

No caption yet…

</div>

{% endif %} {% if media_items %} {% with m=media_items.0 %}

<div class="rounded-lg overflow-hidden mb-3">

{% if m.is_video %}

<div class="relative bg-stone-900" style="aspect-ratio: 16/9;">

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-12 h-12 rounded-full bg-black/40 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LXdoaXRlIG1sLTAuNSIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGQ9Ik02LjMgMi44NDFBMS41IDEuNSAwIDAwNCA0LjExVjE1Ljg5YTEuNSAxLjUgMCAwMDIuMyAxLjI2OWw5LjM0NC01Ljg5YTEuNSAxLjUgMCAwMDAtMi41MzhMNi4zIDIuODR6IiAvPjwvc3ZnPg=="
class="w-5 h-5 text-white ml-0.5" />

</div>

</div>

</div>

{% else %}
<img src="%7B%7B%20m.url%20%7D%7D" class="w-full object-cover"
style="max-height: 200px;" /> {% endif %}

</div>

{% endwith %} {% endif %}

<div class="flex items-center gap-5 text-stone-300">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTIxIDguMjVjMC0yLjQ4NS0yLjA5OS00LjUtNC42ODgtNC41LTEuOTM1IDAtMy41OTcgMS4xMjYtNC4zMTIgMi43MzMtLjcxNS0xLjYwNy0yLjM3Ny0yLjczMy00LjMxMy0yLjczM0M1LjEgMy43NSAzIDUuNzY1IDMgOC4yNWMwIDcuMjIgOSAxMiA5IDEyczktNC43OCA5LTEyeiIgLz48L3N2Zz4="
class="w-4 h-4" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDIwLjI1YzQuOTcgMCA5LTMuNjk0IDktOC4yNXMtNC4wMy04LjI1LTktOC4yNVMzIDcuNDQ0IDMgMTJjMCAyLjEwNC44NTkgNC4wMjMgMi4yNzMgNS40OC40MzIuNDQ3Ljc0IDEuMDQuNTg2IDEuNjQxYTQuNDgzIDQuNDgzIDAgMDEtLjkyMyAxLjc4NUE1Ljk2OSA1Ljk2OSAwIDAwNiAyMWMxLjI4MiAwIDIuNDctLjQwMiAzLjQ0NS0xLjA4Ny44MS4yMiAxLjY2OC4zMzcgMi41NTUuMzM3eiIgLz48L3N2Zz4="
class="w-4 h-4" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTcuMjE3IDEwLjkwN2EyLjI1IDIuMjUgMCAxMDAgMi4xODZtMC0yLjE4NmMuMTguMzI0LjI4My42OTYuMjgzIDEuMDkzcy0uMTAzLjc3LS4yODMgMS4wOTNtMC0yLjE4Nmw5LjU2Ni01LjMxNG0tOS41NjYgNy41bDkuNTY2IDUuMzE0bTAgMGEyLjI1IDIuMjUgMCAxMDMuOTM1IDIuMTg2IDIuMjUgMi4yNSAwIDAwLTMuOTM1LTIuMTg2em0wLTEyLjgxNGEyLjI1IDIuMjUgMCAxMDMuOTMzLTIuMTg1IDIuMjUgMi4yNSAwIDAwLTMuOTMzIDIuMTg1eiIgLz48L3N2Zz4="
class="w-4 h-4" />

</div>

</div>

{% endif %} {% if p.is_over_limit %}

<div class="px-3 py-2 border-t border-red-100 bg-red-50/50 flex items-center gap-1.5 text-[11px] font-medium text-red-500">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgZmxleC1zaHJpbmstMCIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguMjU3IDMuMDk5Yy43NjUtMS4zNiAyLjcyMi0xLjM2IDMuNDg2IDBsNS41OCA5LjkyYy43NSAxLjMzNC0uMjEzIDIuOTgtMS43NDIgMi45OEg0LjQyYy0xLjUzIDAtMi40OTMtMS42NDYtMS43NDMtMi45OGw1LjU4LTkuOTJ6TTExIDEzYTEgMSAwIDExLTIgMCAxIDEgMCAwMTIgMHptLTEtOGExIDEgMCAwMC0xIDF2M2ExIDEgMCAwMDIgMFY2YTEgMSAwIDAwLTEtMXoiIGNsaXAtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4="
class="w-3.5 h-3.5 flex-shrink-0" /> Caption exceeds {{ p.char_limit }}
character limit

</div>

{% endif %}

</div>

{% endfor %} {% else %}

<div class="flex flex-col items-center justify-center h-full text-center px-6 py-12">

<div class="w-16 h-16 rounded-2xl bg-stone-100 flex items-center justify-center mb-4"
style="animation: slideUp 400ms cubic-bezier(0.16,1,0.3,1) both">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy03IGgtNyB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTE1IDEyYTMgMyAwIDExLTYgMCAzIDMgMCAwMTYgMHoiIC8+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTIuNDU4IDEyQzMuNzMyIDcuOTQzIDcuNTIzIDUgMTIgNWM0LjQ3OCAwIDguMjY4IDIuOTQzIDkuNTQyIDctMS4yNzQgNC4wNTctNS4wNjQgNy05LjU0MiA3LTQuNDc3IDAtOC4yNjgtMi45NDMtOS41NDItN3oiIC8+PC9zdmc+"
class="w-7 h-7 text-stone-300" />

</div>

No preview yet

Select a platform and start writing to see how your post will look

</div>

{% endif %}
