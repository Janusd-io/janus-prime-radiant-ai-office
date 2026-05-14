---
type: source
source_type: laptop
title: month_grid
slug: month-grid
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/month_grid.html
original_size: 5245
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
---

# month_grid

_Extracted from `brightbean-studio/templates/calendar/partials/month_grid.html` on 2026-05-14._

{% comment %} Month view grid - 7 columns, N rows of weeks. Context:
calendar_weeks, month_name, prev_month, next_month, day_names,
unscheduled_drafts, workspace. Enhanced with: holidays, custom events,
category colors, recurring badges. {% endcomment %}

<div class="bg-white overflow-x-auto"
style="animation: slideUp 200ms cubic-bezier(0.16,1,0.3,1) both">

<div class="min-w-[640px]">

<div class="grid grid-cols-7 border-b border-stone-200 bg-stone-50">

{% for day_name in day_names %}

<div class="px-3 py-2.5 text-xs font-semibold text-stone-500 text-center border-r border-stone-200 last:border-r-0 tracking-wide">

{{ day_name }}

</div>

{% endfor %}

</div>

{% for week in calendar_weeks %}

<div class="grid grid-cols-7">

{% for day in week %}

<div class="cal-day cal-add-cell {% if day.posts %}has-posts{% endif %} {% if day.is_today %}today{% elif day.is_past %}past{% endif %} {% if not day.is_current_month %}other-month{% endif %}"
@dragover.prevent="allowDrop($event)"
@drop="dropOnSlot($event, '{{ day.date|date:'Y-m-d' }}', 9)">

{% if not day.is_past %} <a
href="%7B%%20url%20&#39;composer:compose&#39;%20workspace_id=workspace.id%20%%7D?scheduled_date=%7B%7B%20day.date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D"
class="cal-add-btn" title="Create post"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIzIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-3 h-3" /></a> {% endif %}

<div class="flex items-center justify-between mb-1">

<div class="day-num">

{{ day.date.day }}

</div>

{% if day.holidays %}

<div class="flex items-center gap-0.5">

{% for h in day.holidays %} <span class="text-[10px]"
title="{{ h.name }}">{{ h.emoji }}</span> {% endfor %}

</div>

{% endif %}

</div>

{% if day.holidays %}

<div class="mb-1">

{% for h in day.holidays %}

<div class="text-[9px] text-amber-600 font-medium leading-tight truncate"
title="{{ h.name }}">

{{ h.name }}

</div>

{% endfor %}

</div>

{% endif %} {% for event in day.events %}

<div class="text-[9px] font-semibold text-white px-1.5 py-0.5 rounded mb-0.5 truncate"
style="background: {{ event.color }};"
title="{{ event.title }}{% if event.description %} - {{ event.description }}{% endif %}">

{{ event.title }}

</div>

{% endfor %} {% for pp in day.posts %}

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
}}</span> {% if pp.post.recurrence_rule %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0ZXh0LWN1cnJlbnQgb3BhY2l0eS01MCBmbGV4LXNocmluay0wIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTQgNHY1aC41ODJtMTUuMzU2IDJBOC4wMDEgOC4wMDEgMCAwMDQuNTgyIDltMCAwSDltMTEgMTF2LTVoLS41ODFtMCAwYTguMDAzIDguMDAzIDAgMDEtMTUuMzU3LTJtMTUuMzU3IDJIMTUiIC8+PC9zdmc+"
class="w-3 h-3 text-current opacity-50 flex-shrink-0" /> {% endif %} {%
endfor %} {% if day.overflow \> 0 %}

<div class="text-[10px] font-semibold text-stone-400 pl-1 mt-0.5">

+{{ day.overflow }} more

</div>

{% endif %}

</div>

{% endfor %}

</div>

{% endfor %}

</div>

</div>
