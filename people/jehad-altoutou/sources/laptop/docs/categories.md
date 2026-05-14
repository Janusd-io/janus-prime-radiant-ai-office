---
type: source
source_type: laptop
title: categories
slug: categories
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/categories.html
original_size: 6795
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# categories

_Extracted from `brightbean-studio/templates/composer/categories.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}Content Categories - {{
workspace.name }} - Brightbean{% endblock %} {% block page_header %}

<div class="flex items-center justify-between mb-6">

<div>

# Content Categories

Organize posts by category for calendar filtering and queue scheduling.

</div>

<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D"
class="text-sm text-stone-500 hover:text-stone-700 flex items-center gap-1"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xNSAxOGwtNi02IDYtNiIgLz48L3N2Zz4="
class="w-4 h-4" /> Back to Calendar</a>

</div>

{% endblock %} {% block content %}

<div class="max-w-2xl" x-data="{ showForm: false, editId: null }">

<div class="mb-6">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> Add Category

{% csrf_token %}

<div class="flex-1">

Name

</div>

<div>

Color

</div>

Save

Cancel

</div>

<div id="category-list"
hx-get="{% url 'composer:category_list' workspace_id=workspace.id %}"
hx-trigger="categoryChanged from:body" hx-select="#category-items"
hx-target="#category-items" hx-swap="outerHTML">

<div id="category-items" class="space-y-2">

{% for cat in categories %}

<div class="flex items-center gap-3 p-3 bg-white rounded-lg border border-stone-200 group hover:border-stone-300 transition-colors"
x-data="{ editing: false }">

<div class="flex items-center gap-3 w-full">

<span class="w-4 h-4 rounded-full flex-shrink-0"
style="background: {{ cat.color }};"></span>
<span class="flex-1 text-sm font-medium text-stone-800">{{ cat.name
}}</span> <span class="text-xs text-stone-400">{{ cat.posts.count }}
post{{ cat.posts.count\|pluralize }}</span>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMSA1SDZhMiAyIDAgMDAtMiAydjExYTIgMiAwIDAwMiAyaDExYTIgMiAwIDAwMi0ydi01bS0xLjQxNC05LjQxNGEyIDIgMCAxMTIuODI4IDIuODI4TDExLjgyOCAxNUg5di0yLjgyOGw4LjU4Ni04LjU4NnoiIC8+PC9zdmc+"
class="w-4 h-4" />

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA3bC0uODY3IDEyLjE0MkEyIDIgMCAwMTE2LjEzOCAyMUg3Ljg2MmEyIDIgMCAwMS0xLjk5NS0xLjg1OEw1IDdtNSA0djZtNC02djZtMS0xMFY0YTEgMSAwIDAwLTEtMWgtNGExIDEgMCAwMC0xIDF2M000IDdoMTYiIC8+PC9zdmc+"
class="w-4 h-4" />

</div>

{% csrf_token %}

Save

Cancel

</div>

{% empty %}

<div class="text-center py-12">

<div class="w-12 h-12 rounded-full bg-stone-100 flex items-center justify-center mx-auto mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTcgN2guMDFNNyAzaDVjLjUxMiAwIDEuMDI0LjE5NSAxLjQxNC41ODZsNyA3YTIgMiAwIDAxMCAyLjgyOGwtNyA3YTIgMiAwIDAxLTIuODI4IDBsLTctN0EyIDIgMCAwMTMgMTJWN2E0IDQgMCAwMTQtNHoiIC8+PC9zdmc+"
class="w-6 h-6 text-stone-400" />

</div>

No categories yet

Create categories to organize your posts.

</div>

{% endfor %}

</div>

</div>

</div>

{% endblock %}
