---
type: source
source_type: laptop
title: media_picker
slug: media-picker
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/media_picker.html
original_size: 3495
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# media_picker

_Extracted from `brightbean-studio/templates/composer/partials/media_picker.html` on 2026-05-14._

{% comment %} Media Library picker modal content - loaded via HTMX.
Context: assets, workspace, post (optional). {% endcomment %} {% if
assets %}

<div class="grid grid-cols-4 gap-3">

{% for asset in assets %}

<div class="group relative rounded-xl overflow-hidden border border-stone-200 aspect-square cursor-pointer hover:border-orange-400 hover:shadow-md transition-all duration-150"
if="" post="" else=""
hx-post="{% url 'composer:attach_pending_media' workspace_id=workspace.id %}"
{%="" endif="" %}=""
hx-vals="{&quot;media_asset_id&quot;: &quot;{{ asset.id }}&quot;}"
hx-target="#media-list" hx-swap="beforeend"
@click="showMediaPicker = false">

{% if asset.thumbnail %}
<img src="%7B%7B%20asset.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover" alt="{{ asset.filename }}" /> {% elif
asset.is_video and asset.file %}

{% elif asset.file %} <img src="%7B%7B%20asset.file.url%20%7D%7D"
class="w-full h-full object-cover" alt="{{ asset.filename }}" /> {% else
%}

<div class="w-full h-full bg-stone-100 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTcgMjFoMTBhMiAyIDAgMDAyLTJWOS40MTRhMSAxIDAgMDAtLjI5My0uNzA3bC01LjQxNC01LjQxNEExIDEgMCAwMDEyLjU4NiAzSDdhMiAyIDAgMDAtMiAydjE0YTIgMiAwIDAwMiAyeiIgLz48L3N2Zz4="
class="w-8 h-8 text-stone-300" />

</div>

{% endif %}

<div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-all duration-150 flex items-center justify-center">

<div class="w-8 h-8 rounded-full bg-white/90 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-150 shadow-sm">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTcwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-stone-700" />

</div>

</div>

{% if asset.is_video %}

<div class="absolute bottom-1.5 left-1.5 px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-black/60 backdrop-blur-sm">

{{ asset.duration\|floatformat:0 }}s

</div>

{% endif %}

<div class="absolute bottom-0 left-0 right-0 p-1.5 bg-gradient-to-t from-black/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-150">

<span class="text-[10px] text-white font-medium truncate block">{{
asset.filename }}</span>

</div>

</div>

{% endfor %}

</div>

{% else %}

<div class="text-center py-12">

<div class="w-14 h-14 mx-auto rounded-2xl bg-stone-100 flex items-center justify-center mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTQgMTZsNC41ODYtNC41ODZhMiAyIDAgMDEyLjgyOCAwTDE2IDE2bS0yLTJsMS41ODYtMS41ODZhMiAyIDAgMDEyLjgyOCAwTDIwIDE0bS02LTZoLjAxTTYgMjBoMTJhMiAyIDAgMDAyLTJWNmEyIDIgMCAwMC0yLTJINmEyIDIgMCAwMC0yIDJ2MTJhMiAyIDAgMDAyIDJ6IiAvPjwvc3ZnPg=="
class="w-6 h-6 text-stone-300" />

</div>

No media yet

Upload files to your media library to use them here

</div>

{% endif %}
