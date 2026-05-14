---
type: source
source_type: laptop
title: cross_calendar
slug: cross-calendar
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/organizations/cross_calendar.html
original_size: 20243
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# cross_calendar

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/organizations/cross_calendar.html` on 2026-05-14._

{% extends "layouts/settings.html" %} {% load static %} {% block title
%}Organization Calendar - Brightbean{% endblock %} {% block page_header
%}

# Organization Calendar

{% endblock %} {% block extra_head %} <style>
    /* Fix parent overflow clipping the calendar */
    main:has(.cross-calendar-main) > div { overflow: visible !important; }

    .cross-cal-day {
        min-height: 110px;
        border-right: 1px solid #E7E5E4;
        border-bottom: 1px solid #E7E5E4;
        padding: 6px;
        transition: background 150ms ease;
        position: relative;
    }
    .cross-cal-day:hover { background: #FAFAF9; }
    .cross-cal-day.today { background: #FFF7ED; }
    .cross-cal-day.past { background: #F5F5F4; }
    .cross-cal-day.past:hover { background: #EEEEEC; }
    .cross-cal-day.other-month { opacity: 0.4; }
    .cross-cal-day .day-num {
        font-size: 12px; font-weight: 600;
        width: 24px; height: 24px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        margin-bottom: 4px;
    }
    .cross-cal-day.today .day-num {
        background: #F97316; color: white;
    }
    .cross-cal-day.past .day-num { color: #78716C; }

    .cross-post-chip {
        display: flex; align-items: center; gap: 4px;
        padding: 2px 6px; border-radius: 6px;
        font-size: 10px; font-weight: 500;
        margin-bottom: 2px; cursor: pointer;
        transition: all 150ms ease;
        text-decoration: none;
        max-width: 100%; overflow: hidden;
    }
    .cross-post-chip:hover { transform: translateX(1px); }
    .cross-post-chip .ws-dot { width: 4px; height: 4px; border-radius: 50%; flex-shrink: 0; }

    /* Status colors */
    .status-draft      { background: #F5F5F4; color: #57534E; }
    .status-pending_review, .status-pending_client { background: #FFF7ED; color: #C2410C; }
    .status-scheduled  { background: #EFF6FF; color: #1D4ED8; }
    .status-published  { background: #F0FDF4; color: #15803D; }
    .status-partially_published { background: #F0FDF4; color: #15803D; }
    .status-failed     { background: #FEF2F2; color: #B91C1C; }

    /* Platform icon badges */
    .pi-facebook   { background: #1877F2; }
    .pi-instagram  { background: [[linear|linear]]-gradient(135deg, #F58529, #DD2A7B, #8134AF); }
    .pi-[[linkedin|linkedin]]   { background: #0A66C2; }
    .pi-tiktok     { background: #010101; }
    .pi-youtube    { background: #FF0000; }
    .pi-pinterest  { background: #E60023; }
    .pi-threads    { background: #000000; }
    .pi-bluesky    { background: #0085FF; }
    .pi-google_business { background: #4285F4; }
    .pi-mastodon   { background: #6364FF; }

    /* Add-post button on calendar cells */
    .cal-add-btn {
        display: none;
        position: absolute; top: 4px; right: 4px;
        width: 20px; height: 20px; border-radius: 50%;
        background: #F97316; color: white; border: none;
        align-items: center; justify-content: center;
        cursor: pointer; font-size: 14px; line-height: 1;
        box-shadow: 0 2px 6px rgba(249,115,22,0.35);
        transition: transform 100ms ease, background 100ms ease;
        z-index: 5;
    }
    .cal-add-btn:hover { background: #EA580C; transform: scale(1.1); }
    .cal-add-cell:hover .cal-add-btn { display: flex; }

    /* Filter selects */
    .org-filter-select {
        appearance: none;
        font-size: 11px; font-weight: 600;
        padding: 5px 24px 5px 8px;
        border: 1px solid #E7E5E4;
        border-radius: 6px;
        color: #57534E;
        background: white url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' viewBox='0 0 24 24' fill='none' stroke='%2378716C' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E") no-repeat right 8px center;
        cursor: pointer;
        transition: border-color 150ms ease;
    }
    .org-filter-select:hover { border-color: #A8A29E; }
    .org-filter-select:focus { outline: none; border-color: #F97316; box-shadow: 0 0 0 2px rgba(249,115,22,0.15); }
    .org-filter-select.has-icon { padding-left: 26px; }

    .org-filter-icon {
        position: absolute; left: 8px; top: 50%; transform: translateY(-50%);
        width: 14px; height: 14px; color: #A8A29E; pointer-events: none;
    }
</style> {% endblock %} {% block content %}

<div class="cross-calendar-main"
x-data="{ viewOpen: false, wsOpen: false }">

<div class="bg-white border-b border-stone-200 px-6 py-3 flex items-center gap-3">

<div class="flex items-center gap-2">

<a
href="?view=%7B%7B%20view_type%20%7D%7D&amp;date=%7B%7B%20prev_date%20%7D%7D%7B%%20for%20sid%20in%20selected_workspace_ids%20%%7D&amp;workspace=%7B%7B%20sid%20%7D%7D%7B%%20endfor%20%%7D%7B%%20if%20request.GET.channel%20%%7D&amp;channel=%7B%7B%20request.GET.channel%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20request.GET.tag%20%%7D&amp;tag=%7B%7B%20request.GET.tag%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20request.GET.status%20%%7D&amp;status=%7B%7B%20request.GET.status%20%7D%7D%7B%%20endif%20%%7D"
class="w-7 h-7 flex items-center justify-center rounded-md text-stone-400 hover:text-stone-600 hover:bg-stone-100 transition-colors"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4" /></a> <a
href="?view=%7B%7B%20view_type%20%7D%7D&amp;date=%7B%7B%20next_date%20%7D%7D%7B%%20for%20sid%20in%20selected_workspace_ids%20%%7D&amp;workspace=%7B%7B%20sid%20%7D%7D%7B%%20endfor%20%%7D%7B%%20if%20request.GET.channel%20%%7D&amp;channel=%7B%7B%20request.GET.channel%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20request.GET.tag%20%%7D&amp;tag=%7B%7B%20request.GET.tag%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20request.GET.status%20%%7D&amp;status=%7B%7B%20request.GET.status%20%7D%7D%7B%%20endif%20%%7D"
class="w-7 h-7 flex items-center justify-center rounded-md text-stone-400 hover:text-stone-600 hover:bg-stone-100 transition-colors"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik05IDVsNyA3LTcgNyIgLz48L3N2Zz4="
class="w-4 h-4" /></a>

</div>

<span class="text-sm font-semibold text-stone-800">{{ period_label
}}</span> <a
href="%7B%%20url%20&#39;organizations:cross_workspace_calendar&#39;%20%%7D?view=%7B%7B%20view_type%20%7D%7D%7B%%20for%20sid%20in%20selected_workspace_ids%20%%7D&amp;workspace=%7B%7B%20sid%20%7D%7D%7B%%20endfor%20%%7D"
class="px-3 py-1 text-xs font-semibold text-stone-600 border border-stone-200 rounded-md hover:bg-stone-50 transition-all duration-150 no-underline">Today</a>

<div class="relative" @click.away="viewOpen = false">

{% if view_type == 'week' %}Week{% elif view_type == 'day' %}Day{% else
%}Month{% endif %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-3 h-3 text-stone-400" />

<div class="absolute left-0 top-full mt-1 bg-white rounded-lg shadow-lg ring-1 ring-stone-200 py-1 z-50 min-w-[100px]"
x-show="viewOpen" x-cloak=""
x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 -translate-y-1"
x-transition:enter-end="opacity-100 translate-y-0">

<a
href="?view=month&amp;date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D%7B%%20for%20sid%20in%20selected_workspace_ids%20%%7D&amp;workspace=%7B%7B%20sid%20%7D%7D%7B%%20endfor%20%%7D"
class="block w-full text-left px-3 py-1.5 text-xs font-medium text-stone-600 hover:bg-stone-50 transition-colors no-underline {% if view_type == &#39;month&#39; %}text-orange-600 bg-orange-50{% endif %}"
data-@click="viewOpen = false">Month</a> <a
href="?view=week&amp;date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D%7B%%20for%20sid%20in%20selected_workspace_ids%20%%7D&amp;workspace=%7B%7B%20sid%20%7D%7D%7B%%20endfor%20%%7D"
class="block w-full text-left px-3 py-1.5 text-xs font-medium text-stone-600 hover:bg-stone-50 transition-colors no-underline {% if view_type == &#39;week&#39; %}text-orange-600 bg-orange-50{% endif %}"
data-@click="viewOpen = false">Week</a> <a
href="?view=day&amp;date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D%7B%%20for%20sid%20in%20selected_workspace_ids%20%%7D&amp;workspace=%7B%7B%20sid%20%7D%7D%7B%%20endfor%20%%7D"
class="block w-full text-left px-3 py-1.5 text-xs font-medium text-stone-600 hover:bg-stone-50 transition-colors no-underline {% if view_type == &#39;day&#39; %}text-orange-600 bg-orange-50{% endif %}"
data-@click="viewOpen = false">Day</a>

</div>

</div>

<div class="flex-1">

</div>

<div class="flex items-center gap-2">

<div class="relative">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib3JnLWZpbHRlci1pY29uIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTkgNUg3YTIgMiAwIDAwLTIgMnYxMmEyIDIgMCAwMDIgMmgxMGEyIDIgMCAwMDItMlY3YTIgMiAwIDAwLTItMmgtMk05IDVhMiAyIDAgMDAyIDJoMmEyIDIgMCAwMDItMk05IDVhMiAyIDAgMDEyLTJoMmEyIDIgMCAwMTIgMiIgLz48L3N2Zz4="
class="org-filter-icon" /> All Posts {% for value, label in
status_choices %} {{ label }} {% endfor %}

</div>

<div class="relative">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib3JnLWZpbHRlci1pY29uIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjQiPjwvY2lyY2xlPjxwYXRoIGQ9Ik0xNiA4djVhMyAzIDAgMDA2IDB2LTFhMTAgMTAgMCAxMC0zLjkyIDcuOTQiIC8+PC9zdmc+"
class="org-filter-icon" /> Channels {% for acc in social_accounts %} {{
acc.account_name\|default:acc.account_handle }} ({{
acc.get_platform_display }}) {% endfor %}

</div>

<div class="relative">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib3JnLWZpbHRlci1pY29uIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTcgN2guMDFNNyAzaDVjLjUxMiAwIDEuMDI0LjE5NSAxLjQxNC41ODZsNyA3YTIgMiAwIDAxMCAyLjgyOGwtNyA3YTIgMiAwIDAxLTIuODI4IDBsLTctN0ExLjk5NCAxLjk5NCAwIDAxMyAxMlY3YTQgNCAwIDAxNC00eiIgLz48L3N2Zz4="
class="org-filter-icon" /> Tags {% for t in all_tags %} \#{{ t }} {%
endfor %}

</div>

<div class="relative" @click.away="wsOpen = false">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMyA0YTEgMSAwIDAxMS0xaDE2YTEgMSAwIDAxMSAxdjIuNTg2YTEgMSAwIDAxLS4yOTMuNzA3bC02LjQxNCA2LjQxNGExIDEgMCAwMC0uMjkzLjcwN1YxN2wtNCA0di02LjU4NmExIDEgMCAwMC0uMjkzLS43MDdMMy4yOTMgNy4yOTNBMSAxIDAgMDEzIDYuNTg2VjR6IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> Workspaces{% if selected_workspace_ids %} ({{
selected_workspace_ids\|length }}){% endif %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-3 h-3 text-stone-400" />

<div class="absolute right-0 top-full mt-1 bg-white rounded-lg shadow-lg ring-1 ring-stone-200 py-1 z-50 min-w-[200px]"
x-show="wsOpen" x-cloak=""
x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 -translate-y-1"
x-transition:enter-end="opacity-100 translate-y-0">

<a
href="?view=%7B%7B%20view_type%20%7D%7D&amp;date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D%7B%%20if%20request.GET.status%20%%7D&amp;status=%7B%7B%20request.GET.status%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20request.GET.channel%20%%7D&amp;channel=%7B%7B%20request.GET.channel%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20request.GET.tag%20%%7D&amp;tag=%7B%7B%20request.GET.tag%20%7D%7D%7B%%20endif%20%%7D"
class="block px-3 py-1.5 text-xs font-medium transition-colors no-underline {% if not selected_workspace_ids %}text-orange-600 bg-orange-50{% else %}text-stone-600 hover:bg-stone-50{% endif %}">All
Workspaces</a>

<div class="border-t border-stone-100 my-1">

</div>

{% for ws in workspaces %} <a
href="?view=%7B%7B%20view_type%20%7D%7D&amp;date=%7B%7B%20target_date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D%7B%%20if%20request.GET.status%20%%7D&amp;status=%7B%7B%20request.GET.status%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20request.GET.channel%20%%7D&amp;channel=%7B%7B%20request.GET.channel%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20request.GET.tag%20%%7D&amp;tag=%7B%7B%20request.GET.tag%20%7D%7D%7B%%20endif%20%%7D%7B%%20if%20ws.id%7Cstringformat:&#39;s&#39;%20in%20selected_workspace_ids%20%%7D%7B%%20for%20sid%20in%20selected_workspace_ids%20%%7D%7B%%20if%20sid%20!=%20ws.id%7Cstringformat:&#39;s&#39;%20%%7D&amp;workspace=%7B%7B%20sid%20%7D%7D%7B%%20endif%20%%7D%7B%%20endfor%20%%7D%7B%%20else%20%%7D%7B%%20for%20sid%20in%20selected_workspace_ids%20%%7D&amp;workspace=%7B%7B%20sid%20%7D%7D%7B%%20endfor%20%%7D&amp;workspace=%7B%7B%20ws.id%20%7D%7D%7B%%20endif%20%%7D"
class="flex items-center gap-2 px-3 py-1.5 text-xs font-medium text-stone-600 hover:bg-stone-50 transition-colors no-underline"><span
class="w-3 h-3 rounded-full flex-shrink-0"
style="background: {{ ws.primary_color|default:&#39;#F97316&#39; }};"></span>
<span class="flex-1">{{ ws.name }}</span> {% if ws.id|stringformat:'s'
in selected_workspace_ids or not selected_workspace_ids %} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1vcmFuZ2UtNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNSAxM2w0IDRMMTkgNyIgLz48L3N2Zz4="
class="w-3.5 h-3.5 text-orange-500" /> {% endif %}</a> {% endfor %}

</div>

</div>

</div>

</div>

<div class="px-6 py-2 bg-stone-50 border-b border-stone-200 flex items-center gap-4 flex-wrap">

<span class="text-[10px] font-semibold text-stone-400 uppercase tracking-wide">Workspaces:</span>
{% for ws in workspaces %}
<span class="inline-flex items-center gap-1.5 text-[11px] text-stone-600">
<span class="w-2.5 h-2.5 rounded-full"
style="background: {{ ws.primary_color|default:'#F97316' }};"></span> {{
ws.name }} </span> {% endfor %}

</div>

<div class="px-6 pt-4">

{% if view_type == 'month' %}

<div class="grid grid-cols-7 text-center mb-1">

{% for day_name in day_names %}

<div class="text-[11px] font-semibold text-stone-400 uppercase tracking-wide py-2">

{{ day_name }}

</div>

{% endfor %}

</div>

<div class="border border-stone-200 rounded-xl overflow-hidden">

{% for week in calendar_weeks %}

<div class="grid grid-cols-7">

{% for day in week %}

<div class="cross-cal-day cal-add-cell {% if day.is_today %}today{% elif day.is_past %}past{% endif %} {% if not day.is_current_month %}other-month{% endif %}">

{% if default_workspace and not day.is_past and day.is_current_month %}
<a
href="%7B%%20url%20&#39;composer:compose&#39;%20workspace_id=default_workspace.id%20%%7D?scheduled_date=%7B%7B%20day.date%7Cdate:&#39;Y-m-d&#39;%20%7D%7D"
class="cal-add-btn" title="Create post"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIzIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-3 h-3" /></a> {% endif %}

<div class="day-num">

{{ day.date.day }}

</div>

{% for pp in day.posts %} <a
href="%7B%%20url%20&#39;composer:compose_edit&#39;%20workspace_id=pp.post.workspace_id%20post_id=pp.post_id%20%%7D"
class="cross-post-chip status-{{ pp.status }}"
title="{{ pp.post.workspace.name }}: {{ pp.post.caption_snippet }}"><span
class="ws-dot"
style="background: {{ pp.post.workspace.primary_color|default:&#39;#F97316&#39; }};"></span>
<span
class="w-4 h-4 rounded flex items-center justify-center pi-{{ pp.social_account.platform }} flex-shrink-0 text-white">
{% include "social_accounts/partials/_platform_icon.html" with
platform=pp.social_account.platform size="3" %} </span> {% with
first_media=pp.post.media_attachments.all.0 %} {% if first_media and
first_media.media_asset.thumbnail %} <img
src="%7B%7B%20first_media.media_asset.thumbnail.url%20%7D%7D"
class="w-5 h-5 rounded object-cover flex-shrink-0" /> {% elif
first_media and not first_media.media_asset.is_video %} <img
src="%7B%7B%20first_media.media_asset.file.url%20%7D%7D"
class="w-5 h-5 rounded object-cover flex-shrink-0" /> {% endif %} {%
endwith %} <span class="truncate">{{
pp.post.caption_snippet|truncatechars:28 }}</span></a> {% endfor %} {%
if day.overflow \> 0 %}
<span class="text-[10px] text-stone-400 font-medium pl-1">+{{
day.overflow }} more</span> {% endif %}

</div>

{% endfor %}

</div>

{% endfor %}

</div>

{% elif view_type == 'week' %} {% include
"organizations/partials/week_grid.html" %} {% elif view_type == 'day' %}
{% include "organizations/partials/day_grid.html" %} {% endif %}

</div>

</div>

{% endblock %}
