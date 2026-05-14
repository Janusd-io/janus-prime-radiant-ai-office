---
type: source
source_type: laptop
title: saved_replies
slug: saved-replies
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/saved_replies.html
original_size: 5053
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# saved_replies

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/saved_replies.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}Saved Replies - {{
workspace.name }} - Brightbean{% endblock %} {% block content %}

<div class="max-w-2xl">

<div class="flex items-center justify-between mb-6">

<div>

<div class="flex items-center gap-3 mb-1">

<a
href="%7B%%20url%20&#39;inbox:feed&#39;%20workspace_id=workspace.id%20%%7D"
class="text-stone-400 hover:text-stone-600 transition-colors"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwb2x5bGluZSBwb2ludHM9IjE1IDE4IDkgMTIgMTUgNiI+PC9wb2x5bGluZT48L3N2Zz4="
class="w-5 h-5" /></a>

## Saved Replies

</div>

Pre-written responses for common questions. Use variables:
`{sender_name}` `{account_name}` `{post_url}`

</div>

<a
href="%7B%%20url%20&#39;inbox:saved_reply_create&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-2 text-[13px] font-semibold text-white rounded-full transition-all duration-150"
style="background: var(--primary); box-shadow: var(--shadow-primary);"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> New Reply</a>

</div>

{% if saved_replies %}

<div class="bg-white border border-stone-200 rounded-xl overflow-hidden"
style="box-shadow: var(--shadow-xs);">

{% for reply in saved_replies %}

<div class="flex items-start gap-4 px-5 py-4 {% if not forloop.last %}border-b border-stone-100{% endif %} hover:bg-stone-50 transition-colors group">

<div class="flex-shrink-0 w-8 h-8 rounded-lg flex items-center justify-center"
style="background: var(--primary-soft);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgc3R5bGU9ImNvbG9yOiB2YXIoLS1wcmltYXJ5KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTkgMjFsLTctNS03IDVWNWEyIDIgMCAwMTItMmgxMGEyIDIgMCAwMTIgMnoiIC8+PC9zdmc+"
class="w-4 h-4" />

</div>

<div class="flex-1 min-w-0">

### {{ reply.title }}

{{ reply.body\|truncatewords:30 }}

</div>

<div class="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity flex-shrink-0">

<a
href="%7B%%20url%20&#39;inbox:saved_reply_edit&#39;%20workspace_id=workspace.id%20reply_id=reply.id%20%%7D"
class="w-7 h-7 flex items-center justify-center rounded-md text-stone-400 hover:text-stone-600 hover:bg-stone-100 transition-all"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTEgNEg0YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGEyIDIgMCAwMDItMnYtNyIgLz48cGF0aCBkPSJNMTguNSAyLjVhMi4xMjEgMi4xMjEgMCAwMTMgM0wxMiAxNWwtNCAxIDEtNCA5LjUtOS41eiIgLz48L3N2Zz4="
class="w-3.5 h-3.5" /></a>

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cG9seWxpbmUgcG9pbnRzPSIzIDYgNSA2IDIxIDYiPjwvcG9seWxpbmU+PHBhdGggZD0iTTE5IDZ2MTRhMiAyIDAgMDEtMiAySDdhMiAyIDAgMDEtMi0yVjZtMyAwVjRhMiAyIDAgMDEyLTJoNGEyIDIgMCAwMTIgMnYyIiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" />

</div>

</div>

{% endfor %}

</div>

{% else %}

<div class="bg-white border border-stone-200 rounded-xl p-12 text-center"
style="box-shadow: var(--shadow-xs);">

<div class="w-12 h-12 rounded-xl flex items-center justify-center mx-auto mb-3"
style="background: var(--surface-2);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xOSAyMWwtNy01LTcgNVY1YTIgMiAwIDAxMi0yaDEwYTIgMiAwIDAxMiAyeiIgLz48L3N2Zz4="
class="w-6 h-6" />

</div>

### No saved replies yet

Create reusable response templates for common questions.

</div>

{% endif %}

</div>

{% endblock %}
