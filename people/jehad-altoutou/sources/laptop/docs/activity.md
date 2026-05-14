---
type: source
source_type: laptop
title: activity
slug: activity
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/activity.html
original_size: 3999
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# activity

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/client_portal/activity.html` on 2026-05-14._

{% extends "client_portal/portal_base.html" %} {% load humanize %} {%
block title %}Activity - {{ workspace.name }}{% endblock %} {% block
content %}

<div>

<div class="mb-6">

# Your Activity

Your review history and actions

</div>

<div class="rounded-xl border overflow-hidden"
style="background: var(--surface-0); border-color: var(--border);">

{% for action in actions %}

<div class="flex items-center gap-3 px-5 py-3.5 {% if not forloop.last %}border-b{% endif %}"
style="border-color: var(--surface-2);">

{% if action.action == 'approved' %}

<div class="w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0"
style="background: var(--success-50);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgc3R5bGU9ImNvbG9yOiB2YXIoLS1zdWNjZXNzLTUwMCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNSAxM2w0IDRMMTkgNyIgLz48L3N2Zz4="
class="w-4 h-4" />

</div>

{% elif action.action == 'changes_requested' %}

<div class="w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0"
style="background: var(--warning-50);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgc3R5bGU9ImNvbG9yOiB2YXIoLS13YXJuaW5nLTUwMCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTYuODYyIDQuNDg3bDEuNjg3LTEuNjg4YTEuODc1IDEuODc1IDAgMTEyLjY1MiAyLjY1MkwxMC41ODIgMTYuMDdhNC41IDQuNSAwIDAxLTEuODk3IDEuMTNMNiAxOGwuOC0yLjY4NWE0LjUgNC41IDAgMDExLjEzLTEuODk3bDguOTMyLTguOTMxeiIgLz48L3N2Zz4="
class="w-4 h-4" />

</div>

{% elif action.action == 'rejected' %}

<div class="w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0"
style="background: var(--error-50);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgc3R5bGU9ImNvbG9yOiB2YXIoLS1lcnJvci01MDApOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTYgMThMMTggNk02IDZsMTIgMTIiIC8+PC9zdmc+"
class="w-4 h-4" />

</div>

{% else %}

<div class="w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0"
style="background: var(--surface-2);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LXRlcnRpYXJ5KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTAiPjwvY2lyY2xlPjwvc3ZnPg=="
class="w-4 h-4" />

</div>

{% endif %}

<div class="flex-1 min-w-0">

{{ action.get_action_display }}

{% if action.comment %}

"{{ action.comment\|truncatechars:80 }}"

{% endif %}

{{ action.post.caption_snippet\|truncatechars:60 }}

</div>

<span class="text-[0.6875rem] flex-shrink-0"
style="color: var(--text-ghost);">{{ action.created_at\|timesince }}
ago</span>

</div>

{% empty %}

<div class="text-center py-16">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibXgtYXV0byB3LTE0IGgtMTQgbWItMyIgc3R5bGU9ImNvbG9yOiB2YXIoLS1uZXV0cmFsLTMwMCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjEuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMy43NSAxMmgxNi41bS0xNi41IDMuNzVoMTYuNU0zLjc1IDE5LjVoMTYuNU01LjYyNSA0LjVoMTIuNzVhMS44NzUgMS44NzUgMCAwMTAgMy43NUg1LjYyNWExLjg3NSAxLjg3NSAwIDAxMC0zLjc1eiIgLz48L3N2Zz4="
class="mx-auto w-14 h-14 mb-3" />

No activity yet

Your review actions will be logged here

</div>

{% endfor %}

</div>

</div>

{% endblock %}
