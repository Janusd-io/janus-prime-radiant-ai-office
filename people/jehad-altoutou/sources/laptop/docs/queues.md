---
type: source
source_type: laptop
title: queues
slug: queues
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/queues.html
original_size: 7924
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# queues

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/calendar/queues.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}Queues - {{ workspace.name
}} - Brightbean{% endblock %} {% block page_header %}

<div class="flex items-center justify-between mb-6">

<div>

# Publishing Queues

Auto-schedule posts into time slots by category and channel.

</div>

<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D"
class="text-sm text-stone-500 hover:text-stone-700 flex items-center gap-1"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xNSAxOGwtNi02IDYtNiIgLz48L3N2Zz4="
class="w-4 h-4" /> Back to Calendar</a>

</div>

{% endblock %} {% block content %}

<div class="max-w-3xl" x-data="{ showForm: false }">

<div class="mb-6">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> Create Queue

{% csrf_token %}

<div>

Queue Name

</div>

<div class="grid grid-cols-2 gap-3">

<div>

Channel Select channel... {% for acc in accounts %} {{
acc.account_name\|default:acc.account_handle }} ({{
acc.get_platform_display }}) {% endfor %}

</div>

<div>

Category (optional) Any category {% for cat in categories %} {{ cat.name
}} {% endfor %}

</div>

</div>

<div class="flex items-center gap-2 pt-1">

Create

Cancel

</div>

</div>

<div id="queue-list"
hx-get="{% url 'calendar:queue_list' workspace_id=workspace.id %}"
hx-trigger="queueChanged from:body" hx-select="#queue-items"
hx-target="#queue-items" hx-swap="outerHTML">

<div id="queue-items" class="space-y-3">

{% for queue in queues %}

<div class="bg-white rounded-xl border border-stone-200 p-4 hover:border-stone-300 transition-colors group">

<div class="flex items-center justify-between">

<div class="flex items-center gap-3">

<div class="w-9 h-9 rounded-lg flex items-center justify-center text-white text-sm font-bold"
style="background: {% if queue.category %}{{ queue.category.color }}{% else %}var(--primary){% endif %};">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSAxMUg1bTE0IDBhMiAyIDAgMDEyIDJ2NmEyIDIgMCAwMS0yIDJINWEyIDIgMCAwMS0yLTJ2LTZhMiAyIDAgMDEyLTJtMTQgMFY5YTIgMiAwIDAwLTItMk01IDExVjlhMiAyIDAgMDEyLTJtMCAwVjVhMiAyIDAgMDEyLTJoNmEyIDIgMCAwMTIgMnYyTTcgN2gxMCIgLz48L3N2Zz4="
class="w-4 h-4" />

</div>

<div>

<a
href="%7B%%20url%20&#39;calendar:queue_detail&#39;%20workspace_id=workspace.id%20queue_id=queue.id%20%%7D"
class="text-sm font-semibold text-stone-800 hover:text-stone-900">{{
queue.name }}</a>

<div class="flex items-center gap-2 mt-0.5">

<span class="text-xs text-stone-500">{{
queue.social_account.account_name\|default:queue.social_account.account_handle
}}</span> {% if queue.category %}
<span class="inline-flex items-center gap-1 text-[10px] font-semibold px-1.5 py-0.5 rounded-full border border-stone-200">
<span class="w-2 h-2 rounded-full"
style="background: {{ queue.category.color }};"></span> {{
queue.category.name }} </span> {% endif %}

</div>

</div>

</div>

<div class="flex items-center gap-2">

<span class="text-xs text-stone-400">{{ queue.entries.count }} post{{
queue.entries.count\|pluralize }}</span> <a
href="%7B%%20url%20&#39;calendar:queue_detail&#39;%20workspace_id=workspace.id%20queue_id=queue.id%20%%7D"
class="text-xs font-semibold py-1.5 px-3 rounded-full border border-stone-200 hover:border-stone-300 text-stone-600 hover:text-stone-800 transition-colors">View</a>

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA3bC0uODY3IDEyLjE0MkEyIDIgMCAwMTE2LjEzOCAyMUg3Ljg2MmEyIDIgMCAwMS0xLjk5NS0xLjg1OEw1IDdtNSA0djZtNC02djZtMS0xMFY0YTEgMSAwIDAwLTEtMWgtNGExIDEgMCAwMC0xIDF2M000IDdoMTYiIC8+PC9zdmc+"
class="w-4 h-4" />

</div>

</div>

</div>

{% empty %}

<div class="text-center py-16">

<div class="w-12 h-12 rounded-full bg-stone-100 flex items-center justify-center mx-auto mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE5IDExSDVtMTQgMGEyIDIgMCAwMTIgMnY2YTIgMiAwIDAxLTIgMkg1YTIgMiAwIDAxLTItMnYtNmEyIDIgMCAwMTItMm0xNCAwVjlhMiAyIDAgMDAtMi0yTTUgMTFWOWEyIDIgMCAwMTItMm0wIDBWNWEyIDIgMCAwMTItMmg2YTIgMiAwIDAxMiAydjJNNyA3aDEwIiAvPjwvc3ZnPg=="
class="w-6 h-6 text-stone-400" />

</div>

No queues yet

Create a queue to auto-schedule posts into time slots.

</div>

{% endfor %}

</div>

</div>

</div>

{% endblock %}
