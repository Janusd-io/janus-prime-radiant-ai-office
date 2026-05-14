---
type: source
source_type: laptop
title: drafts_list
slug: drafts-list
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/drafts_list.html
original_size: 3953
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# drafts_list

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/drafts_list.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}Drafts - {{ workspace.name
}} - Brightbean{% endblock %} {% block page_title %}Drafts{% endblock %}
{% block content %}

<div class="max-w-4xl">

<div class="flex items-center justify-between mb-6">

<div>

## Drafts

{{ drafts\|length }} draft{{ drafts\|length\|pluralize }}

</div>

<a
href="%7B%%20url%20&#39;composer:compose&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-5 py-2 text-sm font-semibold text-white bg-orange-500 rounded-full shadow-[0_4px_14px_rgba(249,115,22,0.28)] hover:bg-orange-600 hover:shadow-[0_6px_20px_rgba(249,115,22,0.35)] hover:-translate-y-px transition-all duration-150"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> New Post</a>

</div>

{% if drafts %}

<div class="space-y-3">

{% for draft in drafts %} <a
href="%7B%%20url%20&#39;composer:compose_edit&#39;%20workspace_id=workspace.id%20post_id=draft.id%20%%7D"
class="block bg-white border border-stone-200 rounded-xl p-4 hover:shadow-lg hover:border-transparent hover:-translate-y-px transition-all duration-200 group"></a>

<div class="flex items-start gap-4">

<div class="flex-1 min-w-0">

{{ draft.caption_snippet\|default:"(No caption)" }}

<div class="flex items-center gap-3 mt-2">

<span class="inline-flex items-center gap-1 text-xs text-stone-400">
<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA4djRsMyAzbTYtM2E5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="w-3 h-3" /> {{ draft.updated_at\|timesince }} ago </span> {% if
draft.author %} <span class="text-xs text-stone-400">by {{
draft.author.display_name }}</span> {% endif %}

</div>

</div>

<div class="flex items-center gap-1 flex-shrink-0">

{% for platform in draft.platform_posts_summary %}
<span class="w-5 h-5 rounded-[5px] flex items-center justify-center text-[8px] font-bold text-white pi-{{ platform }}">
{{ platform\|truncatechars:2\|upper }} </span> {% endfor %}

</div>

</div>

{% endfor %}

</div>

{% else %}

<div class="text-center py-16">

<div class="w-16 h-16 mx-auto rounded-2xl bg-stone-100 flex items-center justify-center mb-4">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy03IGgtNyB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTExIDVINmEyIDIgMCAwMC0yIDJ2MTFhMiAyIDAgMDAyIDJoMTFhMiAyIDAgMDAyLTJ2LTVtLTEuNDE0LTkuNDE0YTIgMiAwIDExMi44MjggMi44MjhMMTEuODI4IDE1SDl2LTIuODI4bDguNTg2LTguNTg2eiIgLz48L3N2Zz4="
class="w-7 h-7 text-stone-300" />

</div>

No drafts

Start composing to create your first draft

<a
href="%7B%%20url%20&#39;composer:compose&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-5 py-1.5 text-sm font-semibold text-orange-600 bg-orange-50 border border-orange-200 rounded-full hover:bg-orange-100 hover:border-orange-300 active:bg-orange-100 transition-all duration-150">Create
Post</a>

</div>

{% endif %}

</div>

{% endblock %}
