---
type: source
source_type: laptop
title: publish_calendar_shell
slug: publish-calendar-shell
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/publish_calendar_shell.html
original_size: 10937
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---

# publish_calendar_shell

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/calendar/partials/publish_calendar_shell.html` on 2026-05-14._

{% comment %} Calendar mode shell for the Publish page. Toolbar: nav
arrows + period + Today + view dropdown \| right: filter dropdowns. {%
endcomment %}

<div class="flex-1 flex flex-col min-h-0 -mx-3 sm:-mx-4 lg:-mx-6"
x-data="{ ...calendarApp(), showEventForm: false, viewOpen: false }"
@calendar-refresh.window="htmx.trigger('#calendar-content', 'refresh')"
hx-trigger="calendarRefresh from:body"
hx-get="{% url 'calendar:calendar' workspace_id=workspace.id %}?mode=calendar&amp;view={{ view_type }}&amp;date={{ target_date|date:'Y-m-d' }}{% if show_holidays %}&amp;holidays=1{% endif %}"
hx-target="#calendar-content" hx-swap="innerHTML">

<div class="bg-white border-b border-stone-200 px-3 sm:px-4 lg:px-6 pb-2 flex flex-wrap items-center gap-2 sm:gap-3">

<div class="flex items-center gap-2">

<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D?mode=calendar&amp;view=%7B%7B%20view_type%20%7D%7D&amp;date=%7B%7B%20prev_date%20%7D%7D"
class="w-7 h-7 rounded-md text-stone-400 hover:text-stone-700 hover:bg-stone-100 flex items-center justify-center transition-all duration-150"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4" /></a> <a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D?mode=calendar&amp;view=%7B%7B%20view_type%20%7D%7D&amp;date=%7B%7B%20next_date%20%7D%7D"
class="w-7 h-7 rounded-md text-stone-400 hover:text-stone-700 hover:bg-stone-100 flex items-center justify-center transition-all duration-150"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik05IDVsNyA3LTcgNyIgLz48L3N2Zz4="
class="w-4 h-4" /></a>

</div>

## {{ period_label }}

<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D?mode=calendar&amp;view=%7B%7B%20view_type%20%7D%7D"
class="px-3 py-1 text-xs font-semibold text-stone-600 border border-stone-200 rounded-md hover:bg-stone-50 transition-all duration-150 no-underline">Today</a>

<div class="relative" @click.away="viewOpen = false">

<span x-text="activeView.charAt(0).toUpperCase() + activeView.slice(1)">{{
view_type\|title }}</span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-3 h-3 text-stone-400" />

<div class="absolute left-0 top-full mt-1 bg-white rounded-lg shadow-lg ring-1 ring-stone-200 py-1 z-50 min-w-[100px]"
x-show="viewOpen" x-cloak=""
x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 -translate-y-1"
x-transition:enter-end="opacity-100 translate-y-0">

<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D?mode=calendar&amp;view=month&amp;date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D"
class="block w-full text-left px-3 py-1.5 text-xs font-medium text-stone-600 hover:bg-stone-50 transition-colors no-underline {% if view_type == &#39;month&#39; %}text-orange-600 bg-orange-50{% endif %}">Month</a>
<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D?mode=calendar&amp;view=week&amp;date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D"
class="block w-full text-left px-3 py-1.5 text-xs font-medium text-stone-600 hover:bg-stone-50 transition-colors no-underline {% if view_type == &#39;week&#39; %}text-orange-600 bg-orange-50{% endif %}">Week</a>
<a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=workspace.id%20%%7D?mode=calendar&amp;view=day&amp;date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D"
class="block w-full text-left px-3 py-1.5 text-xs font-medium text-stone-600 hover:bg-stone-50 transition-colors no-underline {% if view_type == &#39;day&#39; %}text-orange-600 bg-orange-50{% endif %}">Day</a>

</div>

</div>

<div class="cal-filters-scroll flex items-center gap-2 ml-auto overflow-x-auto flex-nowrap"
style="-webkit-overflow-scrolling: touch; scrollbar-width: none;">

<div class="relative flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iY2FsLWZpbHRlci1pY29uIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTkgNUg3YTIgMiAwIDAwLTIgMnYxMmEyIDIgMCAwMDIgMmgxMGEyIDIgMCAwMDItMlY3YTIgMiAwIDAwLTItMmgtMk05IDVhMiAyIDAgMDAyIDJoMmEyIDIgMCAwMDItMk05IDVhMiAyIDAgMDEyLTJoMmEyIDIgMCAwMTIgMiIgLz48L3N2Zz4="
class="cal-filter-icon" /> All Posts {% for value, label in
status_choices %} {{ label }} {% endfor %}

</div>

<div class="relative flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iY2FsLWZpbHRlci1pY29uIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjQiPjwvY2lyY2xlPjxwYXRoIGQ9Ik0xNiA4djVhMyAzIDAgMDA2IDB2LTFhMTAgMTAgMCAxMC0zLjkyIDcuOTQiIC8+PC9zdmc+"
class="cal-filter-icon" /> Channels {% for acc in social_accounts %} {{
acc.account_name\|default:acc.account_handle }} {% endfor %}

</div>

<div class="relative flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iY2FsLWZpbHRlci1pY29uIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTcgN2guMDFNNyAzaDVjLjUxMiAwIDEuMDI0LjE5NSAxLjQxNC41ODZsNyA3YTIgMiAwIDAxMCAyLjgyOGwtNyA3YTIgMiAwIDAxLTIuODI4IDBsLTctN0ExLjk5NCAxLjk5NCAwIDAxMyAxMlY3YTQgNCAwIDAxNC00eiIgLz48L3N2Zz4="
class="cal-filter-icon" /> Tags {% for tag in all_tags %} \#{{ tag }} {%
endfor %}

</div>

<div class="relative flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iY2FsLWZpbHRlci1pY29uIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjEwIj48L2NpcmNsZT48cGF0aCBkPSJNMTIgNnY2bDQgMiIgLz48L3N2Zz4="
class="cal-filter-icon" /> {% for tz in timezone_choices %} {{
tz\|cut:"America/"\|cut:"Europe/"\|cut:"Asia/"\|cut:"US/"\|cut:"Pacific/"\|cut:"Australia/"
}}{% if tz == workspace_timezone %} (workspace){% endif %} {% endfor %}

</div>

</div>

</div>

<div class="bg-white border-b border-stone-200 shadow-sm"
x-show="showEventForm" x-cloak=""
x-transition:enter="transition ease-out duration-150"
x-transition:enter-start="opacity-0 -translate-y-2"
x-transition:enter-end="opacity-100 translate-y-0">

{% include "calendar/partials/event_form.html" %}

</div>

<div id="calendar-content" class="flex-1 overflow-y-auto min-h-0">

{% if view_type == 'month' %} {% include
"calendar/partials/month_grid.html" %} {% elif view_type == 'week' %} {%
include "calendar/partials/week_grid.html" %} {% elif view_type == 'day'
%} {% include "calendar/partials/day_grid.html" %} {% elif view_type ==
'list' %} {% include "calendar/partials/list_view.html" %} {% else %} {%
include "calendar/partials/month_grid.html" %} {% endif %}

</div>

<div class="px-3 sm:px-4 lg:px-6 pt-4 lg:pt-6">

<div class="flex flex-wrap items-center justify-end gap-x-1.5 gap-y-2 text-[11px]">

<span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-md"><span class="w-3 h-3 rounded-full"
style="background:#A8A29E"></span><span style="color:#57534E">Draft</span></span>
<span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-md"><span class="w-3 h-3 rounded-full"
style="background:#F97316"></span><span style="color:#C2410C">Pending
Review</span></span>
<span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-md"><span class="w-3 h-3 rounded-full"
style="background:#14B8A6"></span><span style="color:#0F766E">Approved</span></span>
<span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-md"><span class="w-3 h-3 rounded-full"
style="background:#3B82F6"></span><span style="color:#1D4ED8">Scheduled</span></span>
<span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-md"><span class="w-3 h-3 rounded-full"
style="background:#6366F1"></span><span style="color:#4338CA">Publishing</span></span>
<span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-md"><span class="w-3 h-3 rounded-full"
style="background:#22C55E"></span><span style="color:#15803D">Published</span></span>
<span class="inline-flex items-center gap-1.5 px-2 py-1 rounded-md"><span class="w-3 h-3 rounded-full"
style="background:#EF4444"></span><span style="color:#B91C1C">Failed</span></span>

</div>

</div>

</div>
