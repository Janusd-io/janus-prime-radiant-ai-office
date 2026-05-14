---
type: source
source_type: laptop
title: queue_detail
slug: queue-detail
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/queue_detail.html
original_size: 6109
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# queue_detail

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/calendar/queue_detail.html` on 2026-05-14._

{% extends "base.html" %} {% block title %}{{ queue.name }} - {{
workspace.name }} - Brightbean{% endblock %} {% block page_header %}

<div class="flex items-center justify-between mb-6">

<div class="flex items-center gap-3">

<a
href="%7B%%20url%20&#39;calendar:queue_list&#39;%20workspace_id=workspace.id%20%%7D"
class="text-stone-400 hover:text-stone-600 transition-colors"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xNSAxOGwtNi02IDYtNiIgLz48L3N2Zz4="
class="w-5 h-5" /></a>

<div>

# {{ queue.name }}

<div class="flex items-center gap-2 mt-0.5">

<span class="text-xs text-stone-500">{{
queue.social_account.account_name\|default:queue.social_account.account_handle
}} · {{ queue.social_account.get_platform_display }}</span> {% if
queue.category %}
<span class="inline-flex items-center gap-1 text-[10px] font-semibold px-1.5 py-0.5 rounded-full border border-stone-200">
<span class="w-2 h-2 rounded-full"
style="background: {{ queue.category.color }};"></span> {{
queue.category.name }} </span> {% endif %}

</div>

</div>

</div>

</div>

{% endblock %} {% block content %}

<div id="queue-entries" class="max-w-2xl" x-data="{
         draggedId: null,
         onDragStart(e, id) { this.draggedId = id; e.dataTransfer.effectAllowed = 'move'; },
         onDragOver(e) { e.preventDefault(); e.dataTransfer.dropEffect = 'move'; },
         onDrop(e, targetId) {
             e.preventDefault();
             if (this.draggedId === targetId) return;
             // Collect new order from DOM
             const items = [...document.querySelectorAll('[data-entry-id]')];
             const ids = items.map(el =&gt; el.dataset.entryId).join(',');
             htmx.ajax('POST', '{% url 'calendar:queue_reorder' workspace_id=workspace.id queue_id=queue.id %}', {
                 values: { entry_ids: ids },
                 headers: { 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value }
             });
             this.draggedId = null;
         }
     }"
hx-get="{% url 'calendar:queue_detail' workspace_id=workspace.id queue_id=queue.id %}"
hx-trigger="queueReordered from:body" hx-select="#entries-list"
hx-target="#entries-list" hx-swap="outerHTML">

<div id="entries-list" class="space-y-2">

{% for entry in entries %}

<div class="flex items-center gap-3 p-3 bg-white rounded-lg border border-stone-200 hover:border-stone-300 transition-colors cursor-grab active:cursor-grabbing"
draggable="true" entry-id="{{ entry.id }}"
@dragstart="onDragStart($event, '{{ entry.id }}')"
@dragover="onDragOver($event)" @drop="onDrop($event, '{{ entry.id }}')">

<div class="text-stone-300 flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxjaXJjbGUgY3g9IjkiIGN5PSI2IiByPSIxLjUiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjE1IiBjeT0iNiIgcj0iMS41Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSI5IiBjeT0iMTIiIHI9IjEuNSI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTUiIGN5PSIxMiIgcj0iMS41Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSI5IiBjeT0iMTgiIHI9IjEuNSI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTUiIGN5PSIxOCIgcj0iMS41Ij48L2NpcmNsZT48L3N2Zz4="
class="w-4 h-4" />

</div>

<div class="w-6 h-6 rounded-full bg-stone-100 flex items-center justify-center text-[10px] font-bold text-stone-500 flex-shrink-0">

{{ entry.position\|add:1 }}

</div>

<div class="flex-1 min-w-0">

<a
href="%7B%%20url%20&#39;composer:compose_edit&#39;%20workspace_id=workspace.id%20post_id=entry.post.id%20%%7D"
class="text-sm font-medium text-stone-800 hover:text-stone-900 line-clamp-1">{{
entry.post.caption_snippet|default:"(no caption)" }}</a>

<div class="flex items-center gap-2 mt-0.5">

<span class="inline-flex items-center gap-1 text-[10px] font-semibold px-1.5 py-0.5 rounded-full {% if entry.post.status == 'draft' %}bg-stone-100 text-stone-600 {% elif entry.post.status == 'scheduled' %}bg-blue-50 text-blue-700 {% elif entry.post.status == 'published' %}bg-green-50 text-green-700 {% else %}bg-stone-100 text-stone-600{% endif %}">
{{ entry.post.get_status_display }} </span> {% if entry.post.author %}
<span class="text-[10px] text-stone-400">{{
entry.post.author.name\|default:entry.post.author.email }}</span> {%
endif %}

</div>

</div>

<div class="text-right flex-shrink-0">

{% if entry.assigned_slot_datetime %}
<span class="text-xs font-medium text-stone-700">{{
entry.assigned_slot_datetime\|date:"M d" }}</span>
<span class="text-[10px] text-stone-400 block">{{
entry.assigned_slot_datetime\|time:"H:i" }}</span> {% else %}
<span class="text-xs text-stone-400">No slot</span> {% endif %}

</div>

</div>

{% empty %}

<div class="text-center py-16">

<div class="w-12 h-12 rounded-full bg-stone-100 flex items-center justify-center mx-auto mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDR2MTZtOC04SDQiIC8+PC9zdmc+"
class="w-6 h-6 text-stone-400" />

</div>

Queue is empty

Add posts to this queue from the composer using "Add to Queue".

</div>

{% endfor %}

</div>

</div>

{% endblock %}
