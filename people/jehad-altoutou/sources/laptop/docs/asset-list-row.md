---
type: source
source_type: laptop
title: _asset_list_row
slug: asset-list-row
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_asset_list_row.html
original_size: 4760
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# _asset_list_row

_Extracted from `brightbean-studio/templates/media_library/_asset_list_row.html` on 2026-05-14._

{% comment %}Single asset row for list view. Expects: asset, workspace{%
endcomment %}

<div class="grid grid-cols-12 gap-3 px-4 py-2.5 items-center border-b cursor-pointer transition-colors hover:bg-stone-50"
style="border-color: var(--surface-2, #F5F5F4);"
@click="openDetail('{{ asset.id }}')">

<div class="col-span-5 flex items-center gap-3 min-w-0">

<div class="w-9 h-9 rounded-lg overflow-hidden flex-shrink-0"
style="background: var(--surface-2, #F5F5F4);">

{% if asset.thumbnail %}
<img src="%7B%7B%20asset.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover" /> {% elif asset.file_type == 'image'
or asset.file_type == 'gif' %}
<img src="%7B%7B%20asset.file.url%20%7D%7D"
class="w-full h-full object-cover" /> {% else %}

<div class="w-full h-full flex items-center justify-center">

{% if asset.file_type == 'video' %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNC43NTIgMTEuMTY4bC0zLjE5Ny0yLjEzMkExIDEgMCAwMDEwIDkuODd2NC4yNjNhMSAxIDAgMDAxLjU1NS44MzJsMy4xOTctMi4xMzJhMSAxIDAgMDAwLTEuNjY0eiIgLz48L3N2Zz4="
class="w-4 h-4" /> {% elif asset.file_type == 'document' %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik03IDIxaDEwYTIgMiAwIDAwMi0yVjkuNDE0YTEgMSAwIDAwLS4yOTMtLjcwN2wtNS40MTQtNS40MTRBMSAxIDAgMDAxMi41ODYgM0g3YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-4 h-4" /> {% else %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik00IDE2bDQuNTg2LTQuNTg2YTIgMiAwIDAxMi44MjggMEwxNiAxNm0tMi0ybDEuNTg2LTEuNTg2YTIgMiAwIDAxMi44MjggMEwyMCAxNG0tNi02aC4wMU02IDIwaDEyYTIgMiAwIDAwMi0yVjZhMiAyIDAgMDAtMi0ySDZhMiAyIDAgMDAtMiAydjEyYTIgMiAwIDAwMiAyeiIgLz48L3N2Zz4="
class="w-4 h-4" /> {% endif %}

</div>

{% endif %}

</div>

<div class="min-w-0">

{{ asset.original_filename }}

{% if asset.tags %}

<div class="flex gap-1 mt-0.5">

{% for tag in asset.tags\|slice:":3" %}
<span class="text-xs px-1.5 py-0.5 rounded-full"
style="background: var(--surface-2); color: var(--text-tertiary);">{{
tag }}</span> {% endfor %}

</div>

{% endif %}

</div>

</div>

<div class="col-span-2">

<span class="ml-type-badge"
style="{% if asset.file_type == 'video' %}background: var(--error-50); color: var(--error-700);{% elif asset.file_type == 'gif' %}background: var(--accent-indigo-soft); color: #4338CA;{% elif asset.file_type == 'document' %}background: var(--info-50); color: var(--info-700);{% else %}background: var(--surface-2); color: var(--text-secondary);{% endif %}">
{{ asset.get_file_type_display }} </span>

</div>

<div class="col-span-2 text-xs" style="color: var(--text-secondary);">

{{ asset.human_file_size }} {% if asset.width and asset.height %}\
<span style="color: var(--text-ghost);">{{ asset.width }}×{{
asset.height }}</span> {% endif %}

</div>

<div class="col-span-2 text-xs" style="color: var(--text-secondary);">

{{ asset.created_at\|date:"M j, Y" }}

</div>

<div class="col-span-1 flex justify-end">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9InslIGlmIGFzc2V0LmlzX3N0YXJyZWQgJX12YXIoLS13YXJuaW5nLTUwMCl7JSBlbHNlICV9bm9uZXslIGVuZGlmICV9IiBzdHJva2U9InslIGlmIGFzc2V0LmlzX3N0YXJyZWQgJX12YXIoLS13YXJuaW5nLTUwMCl7JSBlbHNlICV9Y3VycmVudENvbG9yeyUgZW5kaWYgJX0iIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMS4wNDkgMi45MjdjLjMtLjkyMSAxLjYwMy0uOTIxIDEuOTAyIDBsMS41MTkgNC42NzRhMSAxIDAgMDAuOTUuNjloNC45MTVjLjk2OSAwIDEuMzcxIDEuMjQuNTg4IDEuODFsLTMuOTc2IDIuODg4YTEgMSAwIDAwLS4zNjMgMS4xMThsMS41MTggNC42NzRjLjMuOTIyLS43NTUgMS42ODgtMS41MzggMS4xMThsLTMuOTc2LTIuODg4YTEgMSAwIDAwLTEuMTc2IDBsLTMuOTc2IDIuODg4Yy0uNzgzLjU3LTEuODM4LS4xOTctMS41MzgtMS4xMThsMS41MTgtNC42NzRhMSAxIDAgMDAtLjM2My0xLjExOGwtMy45NzYtMi44ODhjLS43ODQtLjU3LS4zOC0xLjgxLjU4OC0xLjgxaDQuOTE0YTEgMSAwIDAwLjk1MS0uNjlsMS41MTktNC42NzR6IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" />

</div>

</div>
