---
type: source
source_type: laptop
title: _reply_composer
slug: reply-composer
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_reply_composer.html
original_size: 5656
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _reply_composer

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_reply_composer.html` on 2026-05-14._

{% load humanize %}

<div class="border-t border-stone-200 px-5 py-3 flex-shrink-0"
style="background: var(--surface-1);"
x-data="{ mode: 'reply', noteText: '', replyText: '' }">

<div class="flex items-center gap-1 mb-2">

Reply

Internal Note

{% if saved_replies %}

<div class="relative ml-auto" x-data="{ srOpen: false }">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTkgMjFsLTctNS03IDVWNWEyIDIgMCAwMTItMmgxMGEyIDIgMCAwMTIgMnoiIC8+PC9zdmc+"
class="w-3.5 h-3.5" /> Saved Replies

<div class="absolute right-0 bottom-full mb-1 bg-white rounded-lg shadow-lg ring-1 ring-stone-200 py-1 z-50 min-w-[200px] max-h-[200px] overflow-y-auto"
x-show="srOpen" @click.away="srOpen = false" x-cloak="" x-transition="">

{% for sr in saved_replies %}

<span class="text-[12px] font-medium text-stone-800 block">{{ sr.title
}}</span> <span class="text-[11px] text-stone-400 block truncate">{{
sr.body\|truncatewords:10 }}</span>

{% endfor %}

</div>

</div>

{% endif %}

</div>

<div x-show="mode === 'reply'" x-transition="">

{% csrf_token %}

<div class="flex items-center justify-between mt-2">

Reply will be posted on {{
message.social_account.get_platform_display\|default:message.social_account.platform\|title
}}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48bGluZSB4MT0iMjIiIHkxPSIyIiB4Mj0iMTEiIHkyPSIxMyI+PC9saW5lPjxwb2x5Z29uIHBvaW50cz0iMjIgMiAxNSAyMiAxMSAxMyAyIDkgMjIgMiI+PC9wb2x5Z29uPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> Send Reply

</div>

</div>

<div x-show="mode === 'note'" x-transition="">

{% csrf_token %}

<div class="flex items-center justify-end mt-2">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTQgMkg2YTIgMiAwIDAwLTIgMnYxNmEyIDIgMCAwMDIgMmgxMmEyIDIgMCAwMDItMlY4eiIgLz48cG9seWxpbmUgcG9pbnRzPSIxNCAyIDE0IDggMjAgOCI+PC9wb2x5bGluZT48bGluZSB4MT0iMTYiIHkxPSIxMyIgeDI9IjgiIHkyPSIxMyI+PC9saW5lPjxsaW5lIHgxPSIxNiIgeTE9IjE3IiB4Mj0iOCIgeTI9IjE3Ij48L2xpbmU+PC9zdmc+"
class="w-3.5 h-3.5" /> Add Note

</div>

</div>

</div>
