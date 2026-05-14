---
type: source
source_type: laptop
title: posting_slots
slug: posting-slots
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/posting_slots.html
original_size: 2725
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# posting_slots

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/calendar/posting_slots.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}Posting Slots - {{
workspace.name }} - Brightbean{% endblock %} {% block page_title
%}Posting Schedule{% endblock %} {% block content %}

<div class="max-w-3xl">

<div class="mb-6">

## Posting Schedule

Define recurring time slots for automatic queue scheduling

</div>

{% for account in accounts %}

<div class="bg-white border border-stone-200 rounded-xl mb-4 overflow-hidden">

<div class="px-5 py-3 border-b border-stone-100 flex items-center gap-3">

<span class="platform-icon pi-{{ account.platform }} w-7 h-7 text-[10px] rounded-lg">
{{ account.platform_icon\|upper }} </span>

<div>

<div class="text-sm font-semibold text-stone-800">

{{ account.account_name\|default:account.account_handle }}

</div>

<div class="text-xs text-stone-400">

{{ account.get_platform_display }}

</div>

</div>

</div>

<div class="p-5">

{% with account_slots=slots_by_account\|default_if_none:"" %} {% endwith
%}

{% for value, label in day_choices %} {{ label }} {% endfor %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-3 h-3" /> Add Slot

</div>

</div>

{% empty %}

<div class="text-center py-12">

No connected accounts to configure posting slots for.

</div>

{% endfor %}

</div>

{% endblock %}
