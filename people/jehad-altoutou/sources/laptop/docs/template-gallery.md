---
type: source
source_type: laptop
title: template_gallery
slug: template-gallery
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/partials/template_gallery.html
original_size: 6727
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---

# template_gallery

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/partials/template_gallery.html` on 2026-05-14._

{% comment %} Template gallery - featured templates banner + category
filter + card grid. Uses Alpine.js for client-side category filtering.
{% endcomment %}

<div x-data="{ activeCategory: 'all' }">

<div class="rounded-2xl bg-gradient-to-br from-green-50 via-green-50/60 to-white border border-green-100 p-6 mb-8">

<div class="flex flex-col lg:flex-row gap-6">

<div class="flex-shrink-0 lg:w-48 flex flex-col justify-center">

<span class="text-xs font-semibold text-green-700 tracking-wide">Featured
templates</span>

## Our top picks

Helpful starting points to plan your next post.

</div>

<div class="flex-1 grid grid-cols-1 sm:grid-cols-3 gap-3">

{% for tpl in featured_templates %}

<div class="text-2xl mb-2">

{{ tpl.emoji }}

</div>

### {{ tpl.title }}

{{ tpl.description }}

{% endfor %}

</div>

</div>

</div>

<div class="flex items-center gap-2 mb-6 overflow-x-auto pb-1 -mx-1 px-1">

{% for cat in template_categories %}

{% if cat.slug == "all" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cmVjdCB4PSIzIiB5PSIzIiB3aWR0aD0iNyIgaGVpZ2h0PSI3IiByeD0iMSIgLz48cmVjdCB4PSIxNCIgeT0iMyIgd2lkdGg9IjciIGhlaWdodD0iNyIgcng9IjEiIC8+PHJlY3QgeD0iMyIgeT0iMTQiIHdpZHRoPSI3IiBoZWlnaHQ9IjciIHJ4PSIxIiAvPjxyZWN0IHg9IjE0IiB5PSIxNCIgd2lkdGg9IjciIGhlaWdodD0iNyIgcng9IjEiIC8+PC9zdmc+"
class="w-3.5 h-3.5" /> {% elif cat.slug == "tip" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTUgMTRjLjItMSAuNy0xLjcgMS41LTIuNSAxLS45IDEuNS0yLjIgMS41LTMuNUE2IDYgMCAwMDYgOGMwIDEgLjIgMi4yIDEuNSAzLjUuNy43IDEuMiAxLjUgMS41IDIuNSIgLz48cGF0aCBkPSJNOSAxOGg2IiAvPjxwYXRoIGQ9Ik0xMCAyMmg0IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> {% elif cat.slug == "case-study" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTUgMTJIMTBNMTUgOEgxME0xOSAxN1Y1YTIgMiAwIDAwLTItMkg0TTQgM2EyIDIgMCAwMC0yIDJ2MmExIDEgMCAwMDEgMWgzbTIgMTNhMiAyIDAgMDEtMi0ydi0xYTEgMSAwIDAxMS0xaDEwYTEgMSAwIDAxMSAxdjFhMiAyIDAgMDEtMiAySDh6IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> {% elif cat.slug == "story" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTIgN1YyMU0xMiA3QzEyIDUuOSAxMS42IDQuOSAxMC44IDQuMiAxMC4xIDMuNCA5LjEgMyA4IDNIM2ExIDEgMCAwMC0xIDF2MTNhMSAxIDAgMDAxIDFoNmMxLjYgMCAzIDEuMyAzIDNNMTIgN2MwLTEuMS40LTIuMSAxLjItMi44QzEzLjkgMy40IDE0LjkgMyAxNiAzaDVhMSAxIDAgMDExIDF2MTNhMSAxIDAgMDEtMSAxaC02Yy0xLjYgMC0zIDEuMy0zIDMiIC8+PC9zdmc+"
class="w-3.5 h-3.5" /> {% elif cat.slug == "how-to" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTQuNSAxMi41TDYuNiAyMC40YTIgMiAwIDAxLTIuOCAwIDIgMiAwIDAxMC0yLjhsNy45LTcuOU0xNS43IDQuM2ExLjQgMS40IDAgMDEyIDBsMiAyYTEuNCAxLjQgMCAwMTAgMmwtNC42IDQuNi00LTQgNC42LTQuNnoiIC8+PC9zdmc+"
class="w-3.5 h-3.5" /> {% elif cat.slug == "question" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCI+PC9jaXJjbGU+PHBhdGggZD0iTTkuMSA5YTMgMyAwIDAxNS44IDFjMCAyLTMgMy0zIDMiIC8+PHBhdGggZD0iTTEyIDE3aC4wMSIgLz48L3N2Zz4="
class="w-3.5 h-3.5" /> {% elif cat.slug == "opinion" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMjEgMTVhMiAyIDAgMDEtMiAySDdsLTQgNFY1YTIgMiAwIDAxMi0yaDE0YTIgMiAwIDAxMiAyeiIgLz48cGF0aCBkPSJNOCAxMmgydi0ySDh6TTE0IDEyaDJ2LTJoLTJ6IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> {% elif cat.slug == "list" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cmVjdCB4PSI0IiB5PSIyIiB3aWR0aD0iMTYiIGhlaWdodD0iMjAiIHJ4PSIyIiAvPjxwYXRoIGQ9Ik0xMiAxMWg0TTEyIDE2aDRNOCAxMWguMDFNOCAxNmguMDEiIC8+PHBhdGggZD0iTTkgNmg2IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> {% elif cat.slug == "behind-the-scenes" %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMyAxMWw3LTUgNCA0IDctNU0zIDExdjhhMiAyIDAgMDAyIDJoMTRhMiAyIDAgMDAyLTJ2LTgiIC8+PC9zdmc+"
class="w-3.5 h-3.5" /> {% endif %} {{ cat.label }}

{% endfor %}

</div>

<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4">

{% for tpl in builtin_templates %}

<div class="text-2xl mb-2">

{{ tpl.emoji }}

</div>

### {{ tpl.title }}

{{ tpl.description }}

{% endfor %}

</div>

</div>
