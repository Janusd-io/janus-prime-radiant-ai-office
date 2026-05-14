---
type: source
source_type: laptop
title: calendar
slug: calendar
created: 2026-04-17
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/calendar.html
original_size: 16779
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
---

# calendar

_Extracted from `brightbean-studio/templates/calendar/calendar.html` on 2026-05-14._

{% extends "base.html" %} {% load static %} {% block title %}Publish -
{{ workspace.name }} - Brightbean{% endblock %} {% block page_header %}

<div class="flex flex-wrap items-center justify-between gap-3 mb-4 lg:mb-[25px]">

# Publish

<div class="flex items-center gap-3">

<div class="flex items-center bg-stone-50 rounded-full p-0.5"
x-data="{ activeMode: '{{ mode|default:'calendar' }}' }">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgaW5saW5lIC1tdC1weCBtci0xIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTQgNmgxNk00IDEwaDE2TTQgMTRoMTZNNCAxOGgxNiIgLz48L3N2Zz4="
class="w-3.5 h-3.5 inline -mt-px mr-1" /> List

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgaW5saW5lIC1tdC1weCBtci0xIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxyZWN0IHg9IjMiIHk9IjQiIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgcng9IjIiIHJ5PSIyIiAvPjxsaW5lIHgxPSIxNiIgeTE9IjIiIHgyPSIxNiIgeTI9IjYiPjwvbGluZT48bGluZSB4MT0iOCIgeTE9IjIiIHgyPSI4IiB5Mj0iNiI+PC9saW5lPjxsaW5lIHgxPSIzIiB5MT0iMTAiIHgyPSIyMSIgeTI9IjEwIj48L2xpbmU+PC9zdmc+"
class="w-3.5 h-3.5 inline -mt-px mr-1" /> Calendar

</div>

</div>

</div>

{% endblock %} {% block extra_head %} <style>
    /* Fix parent overflow clipping the calendar */
    main:has(#publish-body) > div { overflow: visible !important; }

    /* Calendar-specific styles */
    .cal-day {
        min-height: 80px;
        border-right: 1px solid #E7E5E4;
        border-bottom: 1px solid #E7E5E4;
        padding: 6px;
        transition: background 150ms ease;
        background: white;
    }
    @media (min-width: 768px) {
        .cal-day { min-height: 130px; padding: 8px; }
    }
    .cal-day:hover { background: #FAFAF9; }
    .cal-day.past { background: #F5F5F4; }
    .cal-day.past:hover { background: #EEEEEC; }
    .cal-day.today { background: #FFF7ED; }
    .cal-day.other-month { opacity: 0.4; }
    .cal-day .day-num {
        font-size: 13px; font-weight: 600;
        width: 28px; height: 28px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        margin-bottom: 4px;
        color: #44403C;
    }
    .cal-day.past .day-num { color: #78716C; }
    .cal-day.today .day-num {
        background: #F97316; color: white;
    }

    .post-chip {
        display: flex; align-items: center; gap: 4px;
        padding: 3px 6px; border-radius: 6px;
        font-size: 11px; font-weight: 500;
        margin-bottom: 2px; cursor: pointer;
        transition: all 150ms ease;
        text-decoration: none;
        max-width: 100%; overflow: hidden;
    }
    .post-chip:hover { transform: translateX(1px); }
    .post-chip .chip-dot { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0; }

    /* Status colors */
    .status-draft      { background: #F5F5F4; color: #57534E; border: 1px solid #E7E5E4; }
    .status-draft .chip-dot { background: #A8A29E; }
    .status-pending_review, .status-pending_client { background: #FFF7ED; color: #C2410C; border: 1px solid #FED7AA; }
    .status-pending_review .chip-dot, .status-pending_client .chip-dot { background: #F97316; }
    .status-scheduled  { background: #EFF6FF; color: #1D4ED8; border: 1px solid #BFDBFE; }
    .status-scheduled .chip-dot { background: #3B82F6; }
    .status-published  { background: #F0FDF4; color: #15803D; border: 1px solid #BBF7D0; }
    .status-published .chip-dot { background: #22C55E; }
    .status-approved   { background: #F0FDFA; color: #0F766E; border: 1px solid #99F6E4; }
    .status-approved .chip-dot { background: #14B8A6; }
    .status-changes_requested { background: #FFF7ED; color: #C2410C; border: 1px solid #FED7AA; }
    .status-changes_requested .chip-dot { background: #F97316; }
    .status-rejected   { background: #FEF2F2; color: #B91C1C; border: 1px solid #FECACA; }
    .status-rejected .chip-dot { background: #EF4444; }
    .status-publishing { background: #EEF2FF; color: #4338CA; border: 1px solid #C7D2FE; }
    .status-publishing .chip-dot { background: #6366F1; }
    .status-partially_published { background: #FEFCE8; color: #A16207; border: 1px solid #FEF08A; }
    .status-partially_published .chip-dot { background: #EAB308; }
    .status-failed     { background: #FEF2F2; color: #B91C1C; border: 1px solid #FECACA; }
    .status-failed .chip-dot { background: #EF4444; }

    /* View switcher */
    .view-btn {
        padding: 6px 14px; border-radius: 9999px;
        font-size: 12px; font-weight: 600;
        color: #78716C; border: none; background: transparent;
        cursor: pointer; transition: all 150ms ease;
    }
    .view-btn:hover { color: #1C1917; background: #F5F5F4; }
    .view-btn.active { color: #C2410C; background: #FFF7ED; border: 1px solid #FDBA74; box-shadow: 0 1px 2px rgba(194, 65, 12, 0.08); }

    /* Filter chips */
    .filter-chip {
        display: inline-flex; align-items: center; gap: 4px;
        padding: 4px 10px; border-radius: 9999px;
        font-size: 11px; font-weight: 600;
        background: #FFF7ED; color: #C2410C;
        border: 1px solid #FED7AA;
    }
    .filter-chip button {
        width: 14px; height: 14px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        background: transparent; border: none; cursor: pointer;
        color: #EA580C; font-size: 10px;
    }
    .filter-chip button:hover { background: #FFEDD5; }

    /* Publish tab styles */
    .publish-tab {
        padding: 10px 16px; border-radius: 0;
        font-size: 13px; font-weight: 600;
        color: #78716C; background: transparent;
        border: none; cursor: pointer;
        transition: all 150ms ease;
        position: relative;
        border-bottom: 2px solid transparent;
        margin-bottom: -1px;
    }
    .publish-tab:hover { color: #1C1917; border-bottom-color: #D6D3D1; }
    .publish-tab.active { color: #C2410C; border-bottom-color: #F97316; }

    /* Hide scrollbar on filter containers */
    .cal-filters-scroll::-webkit-scrollbar { display: none; }

    /* Filter dropdowns (shared by list and calendar modes) */
    .publish-filter-select,
    .cal-filter-select {
        padding: 6px 28px 6px 10px; border-radius: 8px;
        font-size: 12px; font-weight: 600;
        color: #57534E; background: white;
        border: 1px solid #E7E5E4;
        cursor: pointer; transition: all 150ms ease;
        appearance: none;
        white-space: nowrap;
        flex-shrink: 0;
        background-image: url("data:image/svg+xml,%3Csvg width='10' height='6' viewBox='0 0 10 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1L5 5L9 1' stroke='%2378716C' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: right 8px center;
    }
    .publish-filter-select.has-icon,
    .cal-filter-select.has-icon { padding-left: 28px; }
    .publish-filter-select:hover,
    .cal-filter-select:hover { border-color: #D6D3D1; }
    .publish-filter-select:focus,
    .cal-filter-select:focus { outline: none; border-color: #F97316; box-shadow: 0 0 0 2px rgba(249,115,22,0.15); }
    .publish-filter-icon,
    .cal-filter-icon {
        position: absolute; left: 9px; top: 50%; transform: translateY(-50%);
        width: 14px; height: 14px; color: #78716C; pointer-events: none;
    }

    /* Platform icon badges */
    .pi-facebook   { background: #1877F2; }
    .pi-instagram  { background: linear-gradient(135deg, #F58529, #DD2A7B, #8134AF); }
    .pi-linkedin   { background: #0A66C2; }
    .pi-tiktok     { background: #010101; }
    .pi-youtube    { background: #FF0000; }
    .pi-pinterest  { background: #E60023; }
    .pi-threads    { background: #000000; }
    .pi-bluesky    { background: #0085FF; }
    .pi-google_business { background: #4285F4; }
    .pi-mastodon   { background: #6364FF; }

    /* Add-post button on calendar cells - default (has posts): small top-right */
    .cal-add-btn {
        display: none;
        position: absolute; top: 6px; right: 6px;
        width: 22px; height: 22px; border-radius: 50%;
        background: #F97316; color: white; border: none;
        align-items: center; justify-content: center;
        cursor: pointer; font-size: 14px; line-height: 1;
        box-shadow: 0 2px 6px rgba(249,115,22,0.35);
        transition: transform 100ms ease, background 100ms ease;
        z-index: 5;
    }
    .cal-add-btn:hover { background: #EA580C; transform: scale(1.1); }
    .cal-add-cell { position: relative; }
    .cal-add-cell.has-posts:hover .cal-add-btn { display: flex; }

    /* Empty cells: larger centered button */
    .cal-add-cell:not(.has-posts) .cal-add-btn {
        top: 50%; left: 50%; right: auto;
        transform: translate(-50%, -50%);
        width: 32px; height: 32px;
        background: #F97316; color: white;
        box-shadow: 0 2px 6px rgba(249,115,22,0.35);
        border: none;
    }
    .cal-add-cell:not(.has-posts) .cal-add-btn svg { width: 16px; height: 16px; }
    .cal-add-cell:not(.has-posts):hover .cal-add-btn {
        display: flex;
    }
    .cal-add-cell:not(.has-posts) .cal-add-btn:hover {
        background: #EA580C;
        transform: translate(-50%, -50%) scale(1.1);
        box-shadow: 0 6px 20px rgba(249,115,22,0.35);
    }

    /* Day/week grids (non-month cells): hide add button entirely when cell has posts */
    .cal-add-cell.has-posts:not(.cal-day) .cal-add-btn,
    .cal-add-cell.has-posts:not(.cal-day):hover .cal-add-btn { display: none; }

    /* Inline variant (day/week grid): flow in normal layout, no translate centering */
    .cal-add-cell:not(.has-posts) .cal-add-btn.cal-add-btn--inline,
    .cal-add-cell:not(.has-posts) .cal-add-btn.cal-add-btn--inline:hover {
        top: auto; left: auto; right: auto;
        transform: none;
    }
    .cal-add-cell:not(.has-posts) .cal-add-btn.cal-add-btn--inline:hover {
        transform: scale(1.1);
    }

    /* Draggable feedback */
    .post-chip.dragging { opacity: 0.5; transform: rotate(2deg); }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(8px); }
        to   { opacity: 1; transform: translateY(0); }
    }
</style> {% endblock %} {% block content %}

<div id="publish-body" class="flex-1 flex flex-col min-h-0">

{% if mode == 'list' %} {% include
"calendar/partials/publish_list_shell.html" %} {% else %} {% include
"calendar/partials/publish_calendar_shell.html" %} {% endif %}

</div>

{% endblock %} {% block extra_js %}

{% endblock %}
