---
type: source
source_type: laptop
title: day_grid
slug: day-grid-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/day_grid.html
original_size: 3487
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
---

# day_grid

_Extracted from `brightbean-studio/templates/calendar/partials/day_grid.html` on 2026-05-14._

{% comment %} Day view - single-day timeline with hourly divisions.
Context: day_slots, target_date, workspace. {% endcomment %}

<div class="bg-white mx-auto"
style="animation: slideUp 200ms cubic-bezier(0.16,1,0.3,1) both; max-height: calc(100vh - 200px); overflow-y: auto;">

{% for hour, hour_posts in day_slots %}

<div class="flex border-b border-stone-100 min-h-[64px] cal-add-cell {% if hour_posts %}has-posts{% endif %} {% if is_today and hour == current_hour %}bg-orange-50/50{% endif %}"
@dragover.prevent="allowDrop($event)"
@drop="dropOnSlot($event, '{{ target_date|date:'Y-m-d' }}', {{ hour }})">

<div class="w-20 flex-shrink-0 border-r border-stone-200 px-3 py-2 text-right">

<span class="text-xs font-medium tabular-nums {% if is_today and hour == current_hour %}text-orange-600 font-semibold{% else %}text-stone-400{% endif %}">
{% if hour \< 10 %}0{% endif %}{{ hour }}:00 </span>

</div>

<div class="flex-1 p-2 flex flex-col justify-center gap-1">

{% if not is_past_day and not is_today or not is_past_day and hour \>=
current_hour %} <a
href="%7B%%20url%20&#39;composer:compose&#39;%20workspace_id=workspace.id%20%%7D?scheduled_date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D&amp;scheduled_time=%7B%7B%20hour%20%7D%7D:00"
class="cal-add-btn cal-add-btn--inline"
style="position:static; margin:0 auto;" title="Create post"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIzIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-3 h-3" /></a> {% endif %} {% for pp in hour_posts %}

<span class="w-4 h-4 rounded flex items-center justify-center pi-{{ pp.social_account.platform }} flex-shrink-0 text-white">
{% include "social_accounts/partials/\_platform_icon.html" with
platform=pp.social_account.platform size="3" %} </span> {% with
first_media=pp.post.media_attachments.all.0 %} {% if first_media and
first_media.media_asset.thumbnail %}
<img src="%7B%7B%20first_media.media_asset.thumbnail.url%20%7D%7D"
class="w-5 h-5 rounded object-cover flex-shrink-0" /> {% elif
first_media and not first_media.media_asset.is_video %}
<img src="%7B%7B%20first_media.media_asset.file.url%20%7D%7D"
class="w-5 h-5 rounded object-cover flex-shrink-0" /> {% elif
first_media and first_media.media_asset.is_video %}

{% endif %} {% endwith %} <span class="truncate">{{
pp.post.title\|default:pp.post.caption_snippet\|truncatechars:28
}}</span> {% endfor %}

</div>

</div>

{% endfor %}

</div>
