---
type: source
source_type: laptop
title: _shared_asset_card
slug: shared-asset-card
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_shared_asset_card.html
original_size: 3327
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# _shared_asset_card

_Extracted from `brightbean-studio/templates/media_library/_shared_asset_card.html` on 2026-05-14._

{% comment %}Asset card for shared org library. Uses org-scoped URLs
only. Expects: asset{% endcomment %}

<div class="ml-asset-card group cursor-pointer overflow-hidden"
@click="window.location.href='{% url 'media_library_org:shared_asset_detail' asset_id=asset.id %}'">

<div class="relative aspect-square overflow-hidden rounded-t-xl">

{% if asset.thumbnail %}
<img src="%7B%7B%20asset.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
loading="lazy" alt="{{ asset.filename }}" /> {% else %}

<div class="w-full h-full flex items-center justify-center"
style="background: linear-gradient(135deg, var(--surface-2, #F5F5F4) 0%, var(--surface-1, #FAFAF9) 100%);">

{% if asset.media_type == 'video' %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0LCAjQThBMjlFKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNC43NTIgMTEuMTY4bC0zLjE5Ny0yLjEzMkExIDEgMCAwMDEwIDkuODd2NC4yNjNhMSAxIDAgMDAxLjU1NS44MzJsMy4xOTctMi4xMzJhMSAxIDAgMDAwLTEuNjY0eiIgLz48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMS41IiBkPSJNMjEgMTJhOSA5IDAgMTEtMTggMCA5IDkgMCAwMTE4IDB6IiAvPjwvc3ZnPg=="
class="w-8 h-8" /> {% elif asset.media_type == 'document' %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0LCAjQThBMjlFKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik03IDIxaDEwYTIgMiAwIDAwMi0yVjkuNDE0YTEgMSAwIDAwLS4yOTMtLjcwN2wtNS40MTQtNS40MTRBMSAxIDAgMDAxMi41ODYgM0g3YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-8 h-8" /> {% else %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0LCAjQThBMjlFKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik00IDE2bDQuNTg2LTQuNTg2YTIgMiAwIDAxMi44MjggMEwxNiAxNm0tMi0ybDEuNTg2LTEuNTg2YTIgMiAwIDAxMi44MjggMEwyMCAxNG0tNi02aC4wMU02IDIwaDEyYTIgMiAwIDAwMi0yVjZhMiAyIDAgMDAtMi0ySDZhMiAyIDAgMDAtMiAydjEyYTIgMiAwIDAwMiAyeiIgLz48L3N2Zz4="
class="w-8 h-8" /> {% endif %}

</div>

{% endif %} <span class="absolute top-2 left-2"
style="font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 2px 6px; border-radius: var(--radius-sm, 0.25rem); {% if asset.media_type == 'video' %}background: rgba(239,68,68,0.9); color: white;{% elif asset.media_type == 'gif' %}background: rgba(99,102,241,0.9); color: white;{% elif asset.media_type == 'document' %}background: rgba(59,130,246,0.9); color: white;{% else %}background: rgba(255,255,255,0.9); color: var(--text-secondary, #57534E);{% endif %}">
{{ asset.media_type\|upper }} </span>
<span class="absolute top-2 right-2"
style="font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 2px 6px; border-radius: var(--radius-sm, 0.25rem); background: rgba(20,184,166,0.9); color: white;">
SHARED </span>

</div>

<div class="px-3 py-2.5">

{{ asset.filename }}

{{ asset.file_size_display }}{% if asset.width and asset.height %} · {{
asset.width }}×{{ asset.height }}{% endif %}

</div>

</div>
