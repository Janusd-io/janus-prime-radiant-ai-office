---
type: source
source_type: laptop
title: _asset_card
slug: asset-card
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_asset_card.html
original_size: 5826
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _asset_card

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/_asset_card.html` on 2026-05-14._

{% comment %}Single asset card for grid view. Expects: asset,
workspace{% endcomment %}

<div class="ml-asset-card group cursor-pointer overflow-hidden"
@click="openDetail('{{ asset.id }}')" if="" 'pending'="" or=""
asset.processing_status="=" 'processing'=""
hx-get="{% url 'media_library:processing_status' workspace_id=workspace.id asset_id=asset.id %}"
hx-trigger="every 3s" hx-swap="outerHTML" {%="" endif="" %}="">

<div class="relative aspect-square overflow-hidden rounded-t-xl">

{% if asset.thumbnail %}
<img src="%7B%7B%20asset.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
loading="lazy" alt="{{ asset.original_filename }}" /> {% elif
asset.file_type == 'image' or asset.file_type == 'gif' %}
<img src="%7B%7B%20asset.file.url%20%7D%7D"
class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
loading="lazy" alt="{{ asset.original_filename }}" /> {% elif
asset.processing_status == 'pending' or asset.processing_status ==
'processing' %}

<div class="w-full h-full ml-shimmer flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiBhbmltYXRlLXNwaW4iIHN0eWxlPSJjb2xvcjogdmFyKC0tdGV4dC1naG9zdCwgI0E4QTI5RSk7IiBmaWxsPSJub25lIiB2aWV3Ym94PSIwIDAgMjQgMjQiPgogICAgICAgICAgPGNpcmNsZSBjbGFzcz0ib3BhY2l0eS0yNSIgY3g9IjEyIiBjeT0iMTIiIHI9IjEwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyLjUiPjwvY2lyY2xlPgogICAgICAgICAgPHBhdGggY2xhc3M9Im9wYWNpdHktNzUiIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTQgMTJhOCA4IDAgMDE4LThWMEM1LjM3MyAwIDAgNS4zNzMgMCAxMmg0eiIgLz4KICAgICAgICA8L3N2Zz4="
class="w-6 h-6 animate-spin" />

</div>

{% else %}

<div class="w-full h-full ml-thumb-placeholder flex items-center justify-center">

{% if asset.file_type == 'video' %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0LCAjQThBMjlFKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNC43NTIgMTEuMTY4bC0zLjE5Ny0yLjEzMkExIDEgMCAwMDEwIDkuODd2NC4yNjNhMSAxIDAgMDAxLjU1NS44MzJsMy4xOTctMi4xMzJhMSAxIDAgMDAwLTEuNjY0eiIgLz48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMS41IiBkPSJNMjEgMTJhOSA5IDAgMTEtMTggMCA5IDkgMCAwMTE4IDB6IiAvPjwvc3ZnPg=="
class="w-8 h-8" /> {% elif asset.file_type == 'document' %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0LCAjQThBMjlFKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik03IDIxaDEwYTIgMiAwIDAwMi0yVjkuNDE0YTEgMSAwIDAwLS4yOTMtLjcwN2wtNS40MTQtNS40MTRBMSAxIDAgMDAxMi41ODYgM0g3YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-8 h-8" /> {% else %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0LCAjQThBMjlFKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik00IDE2bDQuNTg2LTQuNTg2YTIgMiAwIDAxMi44MjggMEwxNiAxNm0tMi0ybDEuNTg2LTEuNTg2YTIgMiAwIDAxMi44MjggMEwyMCAxNG0tNi02aC4wMU02IDIwaDEyYTIgMiAwIDAwMi0yVjZhMiAyIDAgMDAtMi0ySDZhMiAyIDAgMDAtMiAydjEyYTIgMiAwIDAwMiAyeiIgLz48L3N2Zz4="
class="w-8 h-8" /> {% endif %}

</div>

{% endif %}
<span class="ml-type-badge absolute top-2 left-2 {% if asset.file_type == 'image' %}{% elif asset.file_type == 'video' %}{% elif asset.file_type == 'gif' %}{% else %}{% endif %}"
style="{% if asset.file_type == 'video' %}background: rgba(239,68,68,0.9); color: white;{% elif asset.file_type == 'gif' %}background: rgba(99,102,241,0.9); color: white;{% elif asset.file_type == 'document' %}background: rgba(59,130,246,0.9); color: white;{% else %}background: rgba(255,255,255,0.9); color: var(--text-secondary, #57534E);{% endif %}">
{{ asset.file_type\|upper }} </span> {% if asset.is_shared %}
<span class="ml-type-badge absolute top-2 right-2"
style="background: rgba(20,184,166,0.9); color: white;"> SHARED </span>
{% endif %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9InslIGlmIGFzc2V0LmlzX3N0YXJyZWQgJX12YXIoLS13YXJuaW5nLTUwMCwgI0VBQjMwOCl7JSBlbHNlICV9bm9uZXslIGVuZGlmICV9IiBzdHJva2U9InslIGlmIGFzc2V0LmlzX3N0YXJyZWQgJX12YXIoLS13YXJuaW5nLTUwMCwgI0VBQjMwOCl7JSBlbHNlICV9dmFyKC0tdGV4dC10ZXJ0aWFyeSwgIzc4NzE2Qyl7JSBlbmRpZiAlfSIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgZD0iTTExLjA0OSAyLjkyN2MuMy0uOTIxIDEuNjAzLS45MjEgMS45MDIgMGwxLjUxOSA0LjY3NGExIDEgMCAwMC45NS42OWg0LjkxNWMuOTY5IDAgMS4zNzEgMS4yNC41ODggMS44MWwtMy45NzYgMi44ODhhMSAxIDAgMDAtLjM2MyAxLjExOGwxLjUxOCA0LjY3NGMuMy45MjItLjc1NSAxLjY4OC0xLjUzOCAxLjExOGwtMy45NzYtMi44ODhhMSAxIDAgMDAtMS4xNzYgMGwtMy45NzYgMi44ODhjLS43ODMuNTctMS44MzgtLjE5Ny0xLjUzOC0xLjExOGwxLjUxOC00LjY3NGExIDEgMCAwMC0uMzYzLTEuMTE4bC0zLjk3Ni0yLjg4OGMtLjc4NC0uNTctLjM4LTEuODEuNTg4LTEuODFoNC45MTRhMSAxIDAgMDAuOTUxLS42OWwxLjUxOS00LjY3NHoiIC8+PC9zdmc+"
class="w-3.5 h-3.5" />

{% if asset.file_type == 'video' and asset.duration_seconds %}
<span class="absolute bottom-2 left-2 text-xs font-semibold px-1.5 py-0.5 rounded"
style="background: rgba(0,0,0,0.7); color: white; font-variant-numeric: tabular-nums;">
{% widthratio asset.duration_seconds 60 1 as mins %} {% widthratio
asset.duration_seconds 1 1 as secs %} {{ mins }}:{{
secs\|stringformat:"02d" }} </span> {% endif %}

</div>

<div class="px-3 py-2.5">

{{ asset.original_filename }}

{{ asset.human_file_size }}{% if asset.width and asset.height %} · {{
asset.width }}×{{ asset.height }}{% endif %}

</div>

</div>
