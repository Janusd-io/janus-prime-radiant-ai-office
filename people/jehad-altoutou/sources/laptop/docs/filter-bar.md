---
type: source
source_type: laptop
title: _filter_bar
slug: filter-bar
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_filter_bar.html
original_size: 11170
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _filter_bar

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_filter_bar.html` on 2026-05-14._

{% load humanize %}

<div class="px-4 py-2.5 border-b border-stone-100 flex items-center gap-2 flex-wrap flex-shrink-0"
style="background: var(--surface-1);">

<div class="relative flex-1 min-w-[160px]">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYWJzb2x1dGUgbGVmdC0yLjUgdG9wLTEvMiAtdHJhbnNsYXRlLXktMS8yIHctMy41IGgtMy41IHRleHQtc3RvbmUtNDAwIHBvaW50ZXItZXZlbnRzLW5vbmUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48Y2lyY2xlIGN4PSIxMSIgY3k9IjExIiByPSI4Ij48L2NpcmNsZT48bGluZSB4MT0iMjEiIHkxPSIyMSIgeDI9IjE2LjY1IiB5Mj0iMTYuNjUiPjwvbGluZT48L3N2Zz4="
class="absolute left-2.5 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-stone-400 pointer-events-none" />

</div>

<div x-data="{
            open: false,
            value: '{{ active_filters.platform|default:'' }}',
            pos: { top: 0, left: 0 },
            updatePos() { const r = this.$refs.btn.getBoundingClientRect(); this.pos = { top: r.bottom + 4 + 'px', left: r.left + 'px' }; },
            select(v) { this.value = v; this.open = false; htmx.trigger(document.querySelector('[name=q]'), 'change'); }
         }" @click.away="open = false">

<span x-text="value ? (document.querySelector('[data-plat=\'' + value + '\']')?.textContent || value) : 'All platforms'"></span>
<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0cmFuc2l0aW9uLXRyYW5zZm9ybSIgOmNsYXNzPSJvcGVuICZhbXA7JmFtcDsgJiMzOTtyb3RhdGUtMTgwJiMzOTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-3 h-3 transition-transform" />

<div class="w-48 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 overflow-hidden"
x-show="open" x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
:style="'position:fixed; top:' + pos.top + '; left:' + pos.left + '; z-index:9999;'"
x-cloak="">

<div class="p-1.5 max-h-48 overflow-y-auto">

All platforms

{% for account in social_accounts %}

{{ account.get_platform_display\|default:account.platform\|title }}

{% endfor %}

</div>

</div>

</div>

<div x-data="{
            open: false,
            value: '{{ active_filters.type|default:'' }}',
            pos: { top: 0, left: 0 },
            labels: { comment: 'Comments', mention: 'Mentions', dm: 'DMs', review: 'Reviews' },
            updatePos() { const r = this.$refs.btn.getBoundingClientRect(); this.pos = { top: r.bottom + 4 + 'px', left: r.left + 'px' }; },
            select(v) { this.value = v; this.open = false; htmx.trigger(document.querySelector('[name=q]'), 'change'); }
         }" @click.away="open = false">

<span x-text="value ? labels[value] : 'All types'"></span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0cmFuc2l0aW9uLXRyYW5zZm9ybSIgOmNsYXNzPSJvcGVuICZhbXA7JmFtcDsgJiMzOTtyb3RhdGUtMTgwJiMzOTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-3 h-3 transition-transform" />

<div class="w-40 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 overflow-hidden"
x-show="open" x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
:style="'position:fixed; top:' + pos.top + '; left:' + pos.left + '; z-index:9999;'"
x-cloak="">

<div class="p-1.5">

</div>

</div>

</div>

<div x-data="{
            open: false,
            value: '{{ active_filters.status|default:'' }}',
            pos: { top: 0, left: 0 },
            labels: { unread: 'Unread', open: 'Open', resolved: 'Resolved', archived: 'Archived' },
            updatePos() { const r = this.$refs.btn.getBoundingClientRect(); this.pos = { top: r.bottom + 4 + 'px', left: r.left + 'px' }; },
            select(v) { this.value = v; this.open = false; htmx.trigger(document.querySelector('[name=q]'), 'change'); }
         }" @click.away="open = false">

<span x-text="value ? labels[value] : 'All statuses'"></span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0cmFuc2l0aW9uLXRyYW5zZm9ybSIgOmNsYXNzPSJvcGVuICZhbXA7JmFtcDsgJiMzOTtyb3RhdGUtMTgwJiMzOTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-3 h-3 transition-transform" />

<div class="w-40 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 overflow-hidden"
x-show="open" x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
:style="'position:fixed; top:' + pos.top + '; left:' + pos.left + '; z-index:9999;'"
x-cloak="">

<div class="p-1.5">

</div>

</div>

</div>

<div x-data="{
            open: false,
            value: '{{ active_filters.sentiment|default:'' }}',
            pos: { top: 0, left: 0 },
            labels: { positive: 'Positive', neutral: 'Neutral', negative: 'Negative' },
            updatePos() { const r = this.$refs.btn.getBoundingClientRect(); this.pos = { top: r.bottom + 4 + 'px', left: r.left + 'px' }; },
            select(v) { this.value = v; this.open = false; htmx.trigger(document.querySelector('[name=q]'), 'change'); }
         }" @click.away="open = false">

<span x-text="value ? labels[value] : 'All sentiment'"></span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0cmFuc2l0aW9uLXRyYW5zZm9ybSIgOmNsYXNzPSJvcGVuICZhbXA7JmFtcDsgJiMzOTtyb3RhdGUtMTgwJiMzOTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-3 h-3 transition-transform" />

<div class="w-40 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 overflow-hidden"
x-show="open" x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
:style="'position:fixed; top:' + pos.top + '; left:' + pos.left + '; z-index:9999;'"
x-cloak="">

<div class="p-1.5">

</div>

</div>

</div>

</div>
