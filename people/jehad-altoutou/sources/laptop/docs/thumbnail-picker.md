---
type: source
source_type: laptop
title: thumbnail_picker
slug: thumbnail-picker
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/thumbnail_picker.html
original_size: 3112
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# thumbnail_picker

_Extracted from `brightbean-studio/templates/composer/partials/thumbnail_picker.html` on 2026-05-14._

{% comment %} YouTube thumbnail picker modal content - loaded via HTMX.
Context: assets (image-only), workspace. Clicking an asset dispatches a
'thumbnail-selected' event with the asset id and URL. The composer's
Alpine root listens and writes the value to the per-account thumbnails
map. {% endcomment %} {% if assets %}

<div class="grid grid-cols-4 gap-3">

{% for asset in assets %}

<div class="group relative rounded-xl overflow-hidden border border-stone-200 aspect-video cursor-pointer hover:border-orange-400 hover:shadow-md transition-all duration-150"
@click="$dispatch('thumbnail-selected', { assetId: '{{ asset.id }}', url: '{% if asset.thumbnail %}{{ asset.thumbnail.url }}{% elif asset.file %}{{ asset.file.url }}{% endif %}', filename: '{{ asset.filename|escapejs }}' })">

{% if asset.thumbnail %}
<img src="%7B%7B%20asset.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover" alt="{{ asset.filename }}" /> {% elif
asset.file %} <img src="%7B%7B%20asset.file.url%20%7D%7D"
class="w-full h-full object-cover" alt="{{ asset.filename }}" /> {% else
%}

<div class="w-full h-full bg-stone-100 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTQgMTZsNC41ODYtNC41ODZhMiAyIDAgMDEyLjgyOCAwTDE2IDE2bS0yLTJsMS41ODYtMS41ODZhMiAyIDAgMDEyLjgyOCAwTDIwIDE0bS02LTZoLjAxTTYgMjBoMTJhMiAyIDAgMDAyLTJWNmEyIDIgMCAwMC0yLTJINmEyIDIgMCAwMC0yIDJ2MTJhMiAyIDAgMDAyIDJ6IiAvPjwvc3ZnPg=="
class="w-8 h-8 text-stone-300" />

</div>

{% endif %}

<div class="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-all duration-150 flex items-center justify-center">

<div class="w-8 h-8 rounded-full bg-white/90 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-150 shadow-sm">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTcwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik01IDEzbDQgNEwxOSA3IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-stone-700" />

</div>

</div>

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

No images available

Upload images to your media library to use them as thumbnails

</div>

{% endif %}
