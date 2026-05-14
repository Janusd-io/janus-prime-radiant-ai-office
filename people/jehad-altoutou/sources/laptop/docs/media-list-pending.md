---
type: source
source_type: laptop
title: media_list_pending
slug: media-list-pending
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/media_list_pending.html
original_size: 1820
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# media_list_pending

_Extracted from `brightbean-studio/templates/composer/partials/media_list_pending.html` on 2026-05-14._

{% comment %} Pending media thumbnails - shown before a post is saved.
Context: pending_assets, workspace. {% endcomment %} {% for asset in
pending_assets %}

<div class="media-thumb">

{% if asset.is_video %}

<div class="absolute inset-0 flex items-center justify-center pointer-events-none">

<div class="w-5 h-5 rounded-full bg-black/50 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUgdGV4dC13aGl0ZSBtbC1weCIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGQ9Ik02LjMgMi44NDFBMS41IDEuNSAwIDAwNCA0LjExVjE1Ljg5YTEuNSAxLjUgMCAwMDIuMyAxLjI2OWw5LjM0NC01Ljg5YTEuNSAxLjUgMCAwMDAtMi41MzhMNi4zIDIuODR6IiAvPjwvc3ZnPg=="
class="w-2.5 h-2.5 text-white ml-px" />

</div>

</div>

{% elif asset.file %} ![{{ asset.filename
}}](%7B%7B%20asset.file.url%20%7D%7D) {% else %}

<div class="w-full h-full bg-stone-100 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTQgMTZsNC41ODYtNC41ODZhMiAyIDAgMDEyLjgyOCAwTDE2IDE2bS0yLTJsMS41ODYtMS41ODZhMiAyIDAgMDEyLjgyOCAwTDIwIDE0bS02LTZoLjAxTTYgMjBoMTJhMiAyIDAgMDAyLTJWNmEyIDIgMCAwMC0yLTJINmEyIDIgMCAwMC0yIDJ2MTJhMiAyIDAgMDAyIDJ6IiAvPjwvc3ZnPg=="
class="w-5 h-5 text-stone-300" />

</div>

{% endif %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIzIiBkPSJNNiAxOEwxOCA2TTYgNmwxMiAxMiIgLz48L3N2Zz4="
class="w-2.5 h-2.5" />

</div>

{% endfor %}
