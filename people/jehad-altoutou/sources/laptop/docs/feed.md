---
type: source
source_type: laptop
title: feed
slug: feed
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/feed.html
original_size: 15487
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# feed

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/feed.html` on 2026-05-14._

{% extends "base.html" %} {% load humanize %} {% block title %}Inbox -
{{ workspace.name }} - Brightbean{% endblock %} {% block extra_head %}
<style>
    /* Inbox-specific layout: remove parent padding, fill height */
    .inbox-shell { margin: -0.75rem; display: flex; flex-direction: column; height: calc(100% + 1.5rem); }
    .inbox-shell { overflow: hidden; }
    :has(> .inbox-shell) { overflow: visible !important; }
    @media (min-width: 640px) {
        .inbox-shell { margin: -1rem; height: calc(100% + 2rem); }
    }
    @media (min-width: 1024px) {
        .inbox-shell { margin: -1.5rem; height: calc(100% + 3rem); }
    }

    /* Split panel */
    .inbox-split { display: flex; flex: 1; min-height: 0; }
    .inbox-list-pane { width: 100%; border-right: none; display: flex; flex-direction: column; }
    .inbox-detail-pane { display: none; flex-direction: column; overflow: hidden; }

    @media (min-width: 768px) {
        .inbox-list-pane { width: 40%; min-width: 320px; border-right: 1px solid var(--border); }
        .inbox-detail-pane { display: flex; flex: 1; }
        /* On desktop, always show both panels regardless of Alpine state */
        .inbox-list-pane[data-mobile-hidden] { display: flex; }
        .inbox-detail-pane[data-mobile-visible] { display: flex; }
    }

    /* Mobile panel switching */
    @media (max-width: 767px) {
        .inbox-list-pane[data-mobile-hidden] { display: none; }
        .inbox-detail-pane[data-mobile-visible] { display: flex; flex: 1; }
    }

    /* Message rows */
    .inbox-row {
        display: flex; gap: 10px; padding: 12px 16px;
        border-bottom: 1px solid var(--surface-2);
        cursor: pointer; transition: background var(--dur-fast) ease;
        position: relative;
    }
    .inbox-row:hover { background: var(--surface-1); }
    .inbox-row.is-active { background: var(--primary-soft); border-left: 3px solid var(--primary); padding-left: 13px; }
    .inbox-row.is-unread .inbox-row-sender { font-weight: 700; color: var(--text-primary); }
    .inbox-row.is-unread .inbox-row-preview { color: var(--text-primary); }
    .inbox-row.is-unread::before {
        content: ''; position: absolute; left: 6px; top: 50%; transform: translateY(-50%);
        width: 6px; height: 6px; border-radius: 50%; background: var(--primary);
    }

    /* Badges */
    .badge-pill {
        display: inline-flex; align-items: center; gap: 3px;
        font-size: 10px; font-weight: 600; padding: 2px 7px;
        border-radius: var(--radius-full); letter-spacing: 0.01em;
        white-space: nowrap;
    }
    .badge-sentiment-positive { background: var(--success-50); color: var(--success-700); }
    .badge-sentiment-neutral  { background: var(--surface-2); color: var(--text-tertiary); }
    .badge-sentiment-negative { background: var(--error-50); color: var(--error-700); }
    .badge-type { background: var(--surface-2); color: var(--text-secondary); }
    .badge-status-unread  { background: var(--info-50); color: var(--info-700); }
    .badge-status-open    { background: var(--warning-50); color: var(--warning-700); }
    .badge-status-resolved { background: var(--success-50); color: var(--success-700); }
    .badge-status-archived { background: var(--surface-2); color: var(--text-ghost); }
    .badge-sla-overdue { background: var(--error-50); color: var(--error-700); animation: pulse-badge 2s ease infinite; }
    @keyframes pulse-badge { 0%,100% { opacity: 1; } 50% { opacity: 0.7; } }

    /* View tabs */
    .inbox-tab {
        font-size: 13px; font-weight: 500; padding: 6px 14px;
        border-radius: var(--radius-full); color: var(--text-secondary);
        transition: all var(--dur-fast) ease; cursor: pointer;
        text-decoration: none; white-space: nowrap;
    }
    .inbox-tab:hover { background: var(--surface-1); color: var(--text-primary); }
    .inbox-tab.active { background: var(--primary-soft); color: var(--brand-700); font-weight: 600; }

    /* Filter controls */
    .filter-select {
        font-size: 12px; font-weight: 500; color: var(--text-secondary);
        background: var(--surface-1); border: 1px solid var(--border);
        border-radius: var(--radius-md); padding: 4px 24px 4px 8px;
        transition: all var(--dur-fast) ease; cursor: pointer;
        appearance: none;
        background-image: url("data:image/svg+xml,%3Csvg width='10' height='6' viewBox='0 0 10 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1L5 5L9 1' stroke='%2378716C' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: right 8px center;
    }
    .filter-select:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 2px var(--primary-ring); }

    /* Bulk action bar */
    .bulk-bar {
        background: var(--neutral-900); color: white; padding: 8px 16px;
        display: flex; align-items: center; gap: 12px;
        font-size: 13px; font-weight: 500;
        animation: slideUp 200ms var(--ease-out);
    }
    .bulk-bar button {
        font-size: 12px; font-weight: 600; padding: 4px 12px;
        border-radius: var(--radius-full); border: 1px solid rgba(255,255,255,0.2);
        background: transparent; color: white; cursor: pointer;
        transition: all var(--dur-fast) ease;
    }
    .bulk-bar button:hover { background: rgba(255,255,255,0.1); }
    @keyframes slideUp { from { transform: translateY(100%); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

    /* SLA countdown */
    .sla-countdown { font-family: var(--font-mono); font-size: 11px; font-weight: 600; }
    .sla-ok { color: var(--text-tertiary); }
    .sla-warn { color: var(--warning-700); }
    .sla-overdue { color: var(--error-700); }

    /* Empty detail placeholder */
    .inbox-empty-detail {
        flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center;
        color: var(--text-ghost); gap: 12px;
    }
</style> {% endblock %} {% block content %}

<div class="inbox-shell" x-data="inboxController()">

<div class="flex flex-wrap items-center justify-between gap-2 px-3 sm:px-5 py-3 border-b border-stone-200 flex-shrink-0">

<div class="flex items-center gap-3 sm:gap-4">

# Inbox

<div class="flex items-center gap-1 bg-stone-50 rounded-full p-0.5"
x-data="{ active: '{{ current_view|default:'all' }}' }">

<a
href="%7B%%20url%20&#39;inbox:feed&#39;%20workspace_id=workspace.id%20%%7D"
class="inbox-tab"
:class="active === &#39;all&#39; &amp;&amp; &#39;active&#39;"
data-@click="active = &#39;all&#39;"
data-hx-get="{% url &#39;inbox:feed&#39; workspace_id=workspace.id %}?view=all"
data-hx-target="#inbox-message-list" data-hx-swap="innerHTML"
data-hx-push-url="true">All</a> <a
href="%7B%%20url%20&#39;inbox:feed&#39;%20workspace_id=workspace.id%20%%7D?view=mine"
class="inbox-tab"
:class="active === &#39;mine&#39; &amp;&amp; &#39;active&#39;"
data-@click="active = &#39;mine&#39;"
data-hx-get="{% url &#39;inbox:feed&#39; workspace_id=workspace.id %}?view=mine"
data-hx-target="#inbox-message-list" data-hx-swap="innerHTML"
data-hx-push-url="true">My Queue</a> <a
href="%7B%%20url%20&#39;inbox:feed&#39;%20workspace_id=workspace.id%20%%7D?view=unassigned"
class="inbox-tab"
:class="active === &#39;unassigned&#39; &amp;&amp; &#39;active&#39;"
data-@click="active = &#39;unassigned&#39;"
data-hx-get="{% url &#39;inbox:feed&#39; workspace_id=workspace.id %}?view=unassigned"
data-hx-target="#inbox-message-list" data-hx-swap="innerHTML"
data-hx-push-url="true">Unassigned</a>

</div>

</div>

<div class="flex items-center gap-2">

<a
href="%7B%%20url%20&#39;inbox:saved_replies&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-3 py-1.5 text-[12px] font-semibold text-stone-600 bg-white border border-stone-200 rounded-full hover:border-stone-300 hover:bg-stone-50 transition-all duration-150"
title="Saved Replies"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTkgMjFsLTctNS03IDVWNWEyIDIgMCAwMTItMmgxMGEyIDIgMCAwMTIgMnoiIC8+PC9zdmc+"
class="w-3.5 h-3.5" /> <span class="hidden sm:inline">Saved
Replies</span></a> {% if sla_config %} <a
href="%7B%%20url%20&#39;inbox:sla_config&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-3 py-1.5 text-[12px] font-semibold text-stone-600 bg-white border border-stone-200 rounded-full hover:border-stone-300 hover:bg-stone-50 transition-all duration-150"
title="SLA Settings"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCI+PC9jaXJjbGU+PHBvbHlsaW5lIHBvaW50cz0iMTIgNiAxMiAxMiAxNiAxNCI+PC9wb2x5bGluZT48L3N2Zz4="
class="w-3.5 h-3.5" /> <span class="hidden sm:inline">SLA</span></a> {%
endif %}

</div>

</div>

<div class="inbox-split">

<div class="inbox-list-pane"
:data-mobile-hidden="activePanel === 'detail' ? '' : undefined">

{% include "inbox/partials/\_filter_bar.html" %}

<div id="inbox-message-list" class="flex-1 overflow-y-auto">

{% include "inbox/partials/\_message_list.html" %}

</div>

<div class="bulk-bar" x-show="selectedCount &gt; 0" x-cloak="">

<span x-text="selectedCount + ' selected'"></span>

Mark Read

Resolve

Archive

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-4 h-4" />

</div>

</div>

<div id="inbox-detail-panel" class="inbox-detail-pane"
:data-mobile-visible="activePanel === 'detail' ? '' : undefined">

<div class="flex md:hidden items-center gap-2 px-3 py-2.5 border-b border-stone-200 flex-shrink-0">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMTUgMThsLTYtNiA2LTYiIC8+PC9zdmc+)
Back

</div>

<div class="inbox-empty-detail">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMiBoLTEyIiBzdHlsZT0iY29sb3I6IHZhcigtLW5ldXRyYWwtMzAwKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0yMSAxNWEyIDIgMCAwMS0yIDJIN2wtNCA0VjVhMiAyIDAgMDEyLTJoMTRhMiAyIDAgMDEyIDJ6IiAvPjwvc3ZnPg=="
class="w-12 h-12" />

Select a message to view details

</div>

</div>

</div>

</div>

{% endblock %} {% block extra_js %}

{% endblock %}
