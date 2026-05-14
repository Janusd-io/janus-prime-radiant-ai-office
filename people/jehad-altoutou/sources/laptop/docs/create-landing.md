---
type: source
source_type: laptop
title: create_landing
slug: create-landing
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/create_landing.html
original_size: 101868
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
---

# create_landing

_Extracted from `brightbean-studio/templates/composer/create_landing.html` on 2026-05-14._

{% extends "base.html" %} {% load static %} {% block title %}Create - {{
workspace.name }} - Brightbean{% endblock %} {% comment %}Header is
rendered inside the content block to avoid overlap with the -m-6
layout{% endcomment %} {% block extra_head %} <style>
    /* Tab switcher (matches publish-tab pattern) */
    .create-tab {
        padding: 10px 16px; border-radius: 0;
        font-size: 13px; font-weight: 600;
        color: #78716C; background: transparent;
        border: none; cursor: pointer;
        transition: all 150ms ease;
        position: relative;
        border-bottom: 2px solid transparent;
        margin-bottom: -1px;
    }
    .create-tab:hover { color: #1C1917; border-bottom-color: #D6D3D1; }
    .create-tab.active { color: #C2410C; border-bottom-color: #F97316; }

    /* Kanban board */
    .kanban-column {
        min-width: 260px;
        width: 260px;
        flex-shrink: 0;
        display: flex;
        flex-direction: column;
        background: #F5F5F4;
        border-radius: 12px;
        min-height: 50vh;
        max-height: calc(100vh - 200px);
    }
    .kanban-cards {
        flex: 1;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 6px;
        padding: 0 8px 8px;
        min-height: 60px;
    }
    .kanban-cards.drag-over {
        background: #FFF7ED;
        outline: 2px dashed #FDBA74;
        border-radius: 8px;
        margin: 0 4px 4px;
        padding: 0 4px 4px;
    }

    /* Idea card */
    .idea-card {
        background: white;
        border: 1px solid #E7E5E4;
        border-radius: 10px;
        padding: 12px 14px;
        cursor: grab;
        transition: all 150ms ease;
    }
    .idea-card:hover {
        border-color: #D6D3D1;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .idea-card.dragging {
        opacity: 0.5;
        transform: rotate(2deg);
    }

    /* Column dragging */
    .kanban-column.column-dragging {
        opacity: 0.4;
    }
    .kanban-column.column-drag-over {
        outline: 2px dashed #FDBA74;
        outline-offset: -2px;
        background: #FFF7ED;
    }

    /* New idea inline */
    .new-idea-inline {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 8px 12px;
        font-size: 13px;
        font-weight: 500;
        color: #A8A29E;
        cursor: pointer;
        border-radius: 8px;
        transition: all 150ms ease;
    }
    .new-idea-inline:hover {
        color: #57534E;
        background: rgba(0,0,0,0.04);
    }

    /* Tag filter chip */
    .tag-chip {
        display: inline-flex; align-items: center; gap: 4px;
        padding: 4px 10px; border-radius: 9999px;
        font-size: 11px; font-weight: 600;
        background: #FFF7ED; color: #C2410C;
        border: 1px solid #FED7AA;
    }
    .tag-chip button {
        width: 14px; height: 14px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        background: transparent; border: none; cursor: pointer;
        color: #EA580C; font-size: 10px;
    }
    .tag-chip button:hover { background: #FFEDD5; }

    /* Modal overlay */
    .idea-modal-overlay {
        position: fixed; inset: 0;
        background: rgba(0,0,0,0.3);
        display: flex; align-items: center; justify-content: center;
        z-index: 100;
    }
    .idea-modal {
        background: white;
        border-radius: 16px;
        width: 100%;
        max-width: 640px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        display: flex;
        flex-direction: column;
        max-height: calc(100vh - 80px);
        position: relative;
    }
    .idea-modal-close {
        position: absolute;
        top: 16px;
        right: 16px;
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: none;
        background: none;
        border-radius: 6px;
        color: var(--text-tertiary);
        cursor: pointer;
        transition: color 150ms, background 150ms;
        z-index: 1;
    }
    .idea-modal-close:hover {
        color: var(--text-primary);
        background: var(--neutral-100);
    }
    .idea-modal-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 50px 16px 24px;
    }
    .idea-modal-body {
        flex: 1;
        overflow-y: auto;
        padding: 0 24px 16px;
    }
    .idea-modal-footer {
        padding: 16px 24px;
        border-top: 1px solid var(--border);
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 8px;
    }
    .idea-modal-body input.idea-title-input {
        width: 100%;
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        border: none;
        outline: none;
        padding: 0;
        margin-bottom: 12px;
        background: transparent;
    }
    .idea-modal-body input.idea-title-input::placeholder {
        color: var(--neutral-300);
    }
    .idea-modal-body textarea.idea-desc-input {
        width: 100%;
        min-height: 160px;
        font-size: 0.875rem;
        color: var(--text-primary);
        border: none;
        outline: none;
        padding: 0;
        resize: none;
        background: transparent;
        line-height: 1.7;
    }
    .idea-modal-body textarea.idea-desc-input::placeholder {
        color: var(--neutral-300);
    }
    .idea-pill-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 14px;
        border: 1px solid var(--border);
        border-radius: 9999px;
        font-size: 0.8125rem;
        font-weight: 500;
        color: var(--text-primary);
        background: var(--surface-0);
        cursor: pointer;
        transition: background 150ms;
        white-space: nowrap;
    }
    .idea-pill-btn:hover { background: var(--neutral-50); }
    .idea-pill-dropdown {
        position: absolute;
        top: calc(100% + 6px);
        right: 0;
        background: white;
        border-radius: 10px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        border: 1px solid var(--border);
        min-width: 180px;
        max-height: 240px;
        overflow-y: auto;
        z-index: 110;
        padding: 4px;
    }
    .idea-pill-dropdown label,
    .idea-pill-dropdown button {
        display: flex;
        align-items: center;
        gap: 8px;
        width: 100%;
        padding: 7px 10px;
        font-size: 0.8125rem;
        border-radius: 6px;
        cursor: pointer;
        transition: background 100ms;
        border: none;
        background: none;
        color: var(--text-primary);
        text-align: left;
    }
    .idea-pill-dropdown label:hover,
    .idea-pill-dropdown button:hover { background: var(--neutral-50); }
    .idea-media-zone {
        border: 2px dashed var(--border);
        border-radius: 12px;
        padding: 24px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 6px;
        color: var(--text-tertiary);
        font-size: 0.8125rem;
        max-width: 150px;
        margin-top: 16px;
        cursor: pointer;
        transition: border-color 150ms, background 150ms;
    }
    .idea-media-zone.drag-over {
        border-color: var(--primary);
        background: rgba(var(--primary-rgb, 249, 115, 22), 0.05);
    }
    .idea-media-strip-layout {
        margin-top: 16px;
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        align-items: flex-start;
    }
    .idea-media-zone.idea-media-zone-tile {
        margin-top: 0;
        width: 130px;
        max-width: 130px;
        min-height: 130px;
        height: 130px;
        padding: 14px 10px;
    }
    .idea-media-existing-card {
        position: relative;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid var(--border);
        width: 130px;
        height: 130px;
        background: var(--neutral-100);
    }
    .idea-media-existing-card img,
    .idea-media-existing-card video {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }
    .idea-media-existing-card .remove-btn {
        position: absolute;
        top: 8px;
        right: 8px;
        width: 38px;
        height: 38px;
        border: 2px solid #fff;
        border-radius: 9999px;
        background: rgba(38, 38, 38, 0.78);
        color: #fff;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0;
        transition: background 150ms;
    }
    .idea-media-existing-card .remove-btn:hover {
        background: rgba(23, 23, 23, 0.9);
    }
    @media (max-width: 640px) {
        .idea-media-strip-layout {
            gap: 10px;
        }
    }
    .idea-selected-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
        margin-top: 8px;
    }
    .idea-selected-tags .idea-tag-chip {
        display: inline-flex;
        align-items: center;
        gap: 3px;
        padding: 2px 8px;
        border-radius: 9999px;
        font-size: 0.6875rem;
        font-weight: 600;
        background: var(--primary-soft, #FFF7ED);
        color: var(--primary, #C2410C);
        border: 1px solid var(--primary-muted, #FED7AA);
    }
    /* Emoji picker */
    .emoji-picker-popup {
        position: absolute;
        bottom: calc(100% + 8px);
        left: 0;
        background: white;
        border-radius: 12px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        border: 1px solid var(--border);
        width: 280px;
        z-index: 120;
        overflow: hidden;
    }
    .emoji-picker-search {
        padding: 8px 8px 4px;
    }
    .emoji-picker-grid {
        display: grid;
        grid-template-columns: repeat(8, 1fr);
        gap: 2px;
        padding: 4px 8px 8px;
        max-height: 200px;
        overflow-y: auto;
    }
    .emoji-picker-item {
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        border: none;
        background: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background 100ms;
    }
    .emoji-picker-item:hover {
        background: var(--neutral-100);
    }

    .idea-selected-tags .idea-tag-chip button {
        display: flex; align-items: center; justify-content: center;
        width: 12px; height: 12px; border: none; background: none;
        cursor: pointer; color: inherit; padding: 0;
    }
</style> {% endblock %} {% block content %}

<div class="-m-6" x-data="kanbanBoard()"
@use-builtin-template.window="openTemplate($event.detail.id)">

<div class="w-full min-h-[60px] inline-flex flex-row justify-between items-center px-6 pt-6 pb-0 mb-6">

# Create

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> New Idea

</div>

<div class="px-6 pb-0 flex items-center gap-4 border-b border-stone-200">

<div class="flex items-center gap-1 -mb-px">

Ideas

Templates

Feeds

</div>

<div class="flex items-center gap-3 ml-auto">

{% if active_tag %}

<div class="tag-chip">

{{ active_tag }}

×

</div>

{% endif %}

<div class="relative" x-show="activeTab === 'ideas'"
x-data="{ tagFilterOpen: false, tagFilterSearch: '', showCreateTagModal: false, newTagName: '' }">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMjAuNTkgMTMuNDFsLTcuMTcgNy4xN2EyIDIgMCAwMS0yLjgzIDBMMiAxMlYyaDEwbDguNTkgOC41OWEyIDIgMCAwMTAgMi44MnoiIC8+PGxpbmUgeDE9IjciIHkxPSI3IiB4Mj0iNy4wMSIgeTI9IjciPjwvbGluZT48L3N2Zz4="
class="w-3.5 h-3.5" /> Tags <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-3 h-3" />

<div class="absolute right-0 top-full mt-1 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 py-1 z-50 min-w-[200px] max-h-[280px] flex flex-col"
x-show="tagFilterOpen" @click.away="tagFilterOpen = false" x-cloak=""
x-transition="">

<div class="px-2 py-1.5 border-b border-stone-100">

</div>

<div class="overflow-y-auto flex-1">

<span class="block px-3 py-1.5 text-sm text-stone-700 hover:bg-stone-50 rounded-md mx-1"
:href="'{% url 'composer:create_landing' workspace_id=workspace.id %}?tag=' + encodeURIComponent(tag)"
:class="tag === '{{ active_tag|escapejs }}' &amp;&amp; 'font-semibold text-stone-900 bg-stone-50'"
x-text="tag"></span>

<div class="px-3 py-3 text-xs text-stone-400 text-center">

No tags yet

</div>

<div class="px-3 py-2 text-xs text-stone-400 text-center">

No matching tags

</div>

</div>

<div class="border-t border-stone-100 px-1 py-1">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1vcmFuZ2UtNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDR2MTZtOC04SDQiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-orange-500" /> Create new tag

</div>

</div>

<div class="fixed inset-0 z-[200] flex items-center justify-center"
x-show="showCreateTagModal" x-cloak=""
@keydown.escape.window="showCreateTagModal = false">

<div class="fixed inset-0 bg-black/30"
@click="showCreateTagModal = false">

</div>

<div class="relative bg-white rounded-2xl shadow-xl w-full max-w-sm mx-4 p-6"
@click.stop="">

### Create new tag

<div class="flex justify-end gap-2 mt-4">

Cancel

Create

</div>

</div>

</div>

</div>

</div>

</div>

<div class="p-6">

<div x-show="activeTab === 'ideas'">

<div id="kanban-board">

{% include "composer/partials/kanban_board.html" %}

</div>

</div>

<div class="overflow-y-auto -mx-6 -mb-6 px-6 pb-6"
x-show="activeTab === 'templates'" x-cloak=""
style="max-height: calc(100vh - 160px);">

{% include "composer/partials/template_gallery.html" %}

</div>

<div class="h-[calc(100vh-160px)] overflow-hidden"
x-show="activeTab === 'feeds'" x-cloak=""
@open-explore.window="showExploreModal = true; $nextTick(() =&gt; htmx.trigger(document.getElementById('explore-feeds-content'), 'load'))">

<div id="feeds-tab-content" class="h-full"
hx-get="{% url 'composer:feed_list' workspace_id=workspace.id %}"
hx-trigger="intersect once, feedsUpdated from:body" hx-swap="innerHTML">

{% include "composer/partials/feeds_tab.html" %}

</div>

</div>

</div>

<div class="fixed inset-0 z-[200] flex items-center justify-center"
x-show="showExploreModal" x-cloak=""
@keydown.escape.window="showExploreModal = false">

<div class="fixed inset-0 bg-black/30"
@click="showExploreModal = false">

</div>

<div class="relative bg-white rounded-2xl shadow-xl w-full max-w-[720px] mx-4 max-h-[85vh] overflow-hidden"
@click.stop="">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxsaW5lIHgxPSIxOCIgeTE9IjYiIHgyPSI2IiB5Mj0iMTgiPjwvbGluZT48bGluZSB4MT0iNiIgeTE9IjYiIHgyPSIxOCIgeTI9IjE4Ij48L2xpbmU+PC9zdmc+"
class="w-5 h-5" />

<div id="explore-feeds-content"
hx-get="{% url 'composer:feed_explore' workspace_id=workspace.id %}"
hx-trigger="load" hx-swap="innerHTML">

<div class="flex justify-center py-20">

<div class="animate-spin w-6 h-6 border-2 border-stone-300 border-t-orange-500 rounded-full">

</div>

</div>

</div>

</div>

</div>

<div class="idea-modal-overlay" x-show="showCreateModal" x-cloak=""
@click.self="closeCreateModal()"
@keydown.escape.window="closeCreateModal()">

<div class="idea-modal" @click.stop="">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxsaW5lIHgxPSIxOCIgeTE9IjYiIHgyPSI2IiB5Mj0iMTgiPjwvbGluZT48bGluZSB4MT0iNiIgeTE9IjYiIHgyPSIxOCIgeTI9IjE4Ij48L2xpbmU+PC9zdmc+)

{% csrf_token %}

<div class="idea-modal-header">

## Create Idea

<div class="flex items-center gap-2">

<div class="relative" @click.away="createGroupDropdownOpen = false">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cmVjdCB4PSIzIiB5PSIzIiB3aWR0aD0iNyIgaGVpZ2h0PSI3IiAvPjxyZWN0IHg9IjE0IiB5PSIzIiB3aWR0aD0iNyIgaGVpZ2h0PSI3IiAvPjxyZWN0IHg9IjMiIHk9IjE0IiB3aWR0aD0iNyIgaGVpZ2h0PSI3IiAvPjxyZWN0IHg9IjE0IiB5PSIxNCIgd2lkdGg9IjciIGhlaWdodD0iNyIgLz48L3N2Zz4=)
<span x-text="createGroupLabel()"></span>
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBkPSJNNiA5bDYgNiA2LTYiIC8+PC9zdmc+)

<div class="idea-pill-dropdown" x-show="createGroupDropdownOpen"
x-cloak="" x-transition="">

{% for col in columns %}

{{ col.label }} <img
src="data:image/svg+xml;base64,PHN2ZyB4LXNob3c9ImNyZWF0ZVNlbGVjdGVkR3JvdXAgPT09ICYjMzk7e3sgY29sLmlkIH19JiMzOTsiIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyLjUiIGNsYXNzPSJtbC1hdXRvIiBzdHlsZT0iY29sb3I6IHZhcigtLXByaW1hcnkpOyI+PHBvbHlsaW5lIHBvaW50cz0iMjAgNiA5IDE3IDQgMTIiPjwvcG9seWxpbmU+PC9zdmc+"
class="ml-auto" />

{% endfor %}

</div>

</div>

<div class="relative" @click.away="createTagDropdownOpen = false">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMjAuNTkgMTMuNDFsLTcuMTcgNy4xN2EyIDIgMCAwMS0yLjgzIDBMMiAxMlYyaDEwbDguNTkgOC41OWEyIDIgMCAwMTAgMi44MnoiIC8+PGxpbmUgeDE9IjciIHkxPSI3IiB4Mj0iNy4wMSIgeTI9IjciPjwvbGluZT48L3N2Zz4=)
Tags
<span class="inline-flex items-center justify-center w-4 h-4 rounded-full text-[10px] font-bold text-white"
x-show="createSelectedTags.length" style="background: var(--primary);"
x-text="createSelectedTags.length"></span>
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBkPSJNNiA5bDYgNiA2LTYiIC8+PC9zdmc+)

<div class="idea-pill-dropdown" x-show="createTagDropdownOpen"
x-cloak="" x-transition="">

<div style="padding: 4px 6px; border-bottom: 1px solid var(--border);">

</div>

<span x-text="tag"></span>

<div class="px-3 py-2 text-xs" style="color: var(--text-tertiary);">

No tags yet. Type to create one.

</div>

<div class="border-t"
style="border-color: var(--border); margin-top: 2px; padding-top: 2px;">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg==)
Create "<span x-text="createTagSearch.trim()"></span>"

</div>

<div class="border-t border-stone-100 px-1 py-1">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1vcmFuZ2UtNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDR2MTZtOC04SDQiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-orange-500" /> Create new tag

</div>

</div>

</div>

</div>

</div>

<div class="idea-selected-tags" style="padding: 0 24px 8px;">

<span x-text="tag"></span>

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSI4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjMiPjxsaW5lIHgxPSIxOCIgeTE9IjYiIHgyPSI2IiB5Mj0iMTgiPjwvbGluZT48bGluZSB4MT0iNiIgeTE9IjYiIHgyPSIxOCIgeTI9IjE4Ij48L2xpbmU+PC9zdmc+)

</div>

<div class="idea-modal-body"
@click="createGroupDropdownOpen = false; createTagDropdownOpen = false">

<div class="idea-media-strip-layout">

<div class="idea-media-existing-card">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi43IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxsaW5lIHgxPSIxOCIgeTE9IjYiIHgyPSI2IiB5Mj0iMTgiPjwvbGluZT48bGluZSB4MT0iNiIgeTE9IjYiIHgyPSIxOCIgeTI9IjE4Ij48L2xpbmU+PC9zdmc+)

</div>

<div class="idea-media-zone"
:class="{ 'idea-media-zone-tile': true, 'drag-over': _mediaDragOver }"
@click="$refs.ideaFileInput.click()"
@dragover.prevent="_mediaDragOver = true"
@dragleave.prevent="_mediaDragOver = false"
@drop.prevent="_mediaDragOver = false; _handleMediaDrop($event)">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxyZWN0IHg9IjMiIHk9IjMiIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgcng9IjIiIHJ5PSIyIiAvPjxjaXJjbGUgY3g9IjguNSIgY3k9IjguNSIgcj0iMS41Ij48L2NpcmNsZT48cG9seWxpbmUgcG9pbnRzPSIyMSAxNSAxNiAxMCA1IDIxIj48L3BvbHlsaW5lPjwvc3ZnPg==)
<span x-show="!createMediaAssets.length">Drag & drop</span>
<span x-show="createMediaAssets.length">Add another file</span> or
**select a file**

</div>

</div>

</div>

<div class="idea-modal-footer"
@click="createGroupDropdownOpen = false; createTagDropdownOpen = false">

<span style="margin-right: auto; display: flex; align-items: center; gap: 8px; color: var(--text-tertiary);">
<span style="width: 1px; height: 20px; background: var(--border);"></span>
</span>

<div class="relative">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjEwIj48L2NpcmNsZT48cGF0aCBkPSJNOCAxNHMxLjUgMiA0IDIgNC0yIDQtMiIgLz48bGluZSB4MT0iOSIgeTE9IjkiIHgyPSI5LjAxIiB5Mj0iOSI+PC9saW5lPjxsaW5lIHgxPSIxNSIgeTE9IjkiIHgyPSIxNS4wMSIgeTI9IjkiPjwvbGluZT48L3N2Zz4=)

<div class="emoji-picker-popup" x-show="emojiPickerOpen" x-cloak=""
@click.away="emojiPickerOpen = false"
x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100">

<div class="emoji-picker-search">

</div>

<div class="emoji-picker-grid">

</div>

</div>

</div>

<span style="width: 1px; height: 20px; background: var(--border);"></span>

Create Post

Save Idea

</div>

</div>

</div>

<div class="idea-modal-overlay" x-show="editingIdea" x-cloak=""
@click.self="editingIdea = null"
@keydown.escape.window="editingIdea = null">

<div class="idea-modal" @click.stop="">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxsaW5lIHgxPSIxOCIgeTE9IjYiIHgyPSI2IiB5Mj0iMTgiPjwvbGluZT48bGluZSB4MT0iNiIgeTE9IjYiIHgyPSIxOCIgeTI9IjE4Ij48L2xpbmU+PC9zdmc+)

{% csrf_token %}

<div class="idea-modal-header">

## Edit Idea

<div class="flex items-center gap-2">

<div class="relative" @click.away="editGroupDropdownOpen = false">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cmVjdCB4PSIzIiB5PSIzIiB3aWR0aD0iNyIgaGVpZ2h0PSI3IiAvPjxyZWN0IHg9IjE0IiB5PSIzIiB3aWR0aD0iNyIgaGVpZ2h0PSI3IiAvPjxyZWN0IHg9IjMiIHk9IjE0IiB3aWR0aD0iNyIgaGVpZ2h0PSI3IiAvPjxyZWN0IHg9IjE0IiB5PSIxNCIgd2lkdGg9IjciIGhlaWdodD0iNyIgLz48L3N2Zz4=)
<span x-text="editGroupLabel()"></span>
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBkPSJNNiA5bDYgNiA2LTYiIC8+PC9zdmc+)

<div class="idea-pill-dropdown" x-show="editGroupDropdownOpen"
x-cloak="" x-transition="">

{% for col in columns %}

{{ col.label }} <img
src="data:image/svg+xml;base64,PHN2ZyB4LXNob3c9ImVkaXRTZWxlY3RlZEdyb3VwID09PSAmIzM5O3t7IGNvbC5pZCB9fSYjMzk7IiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41IiBjbGFzcz0ibWwtYXV0byIgc3R5bGU9ImNvbG9yOiB2YXIoLS1wcmltYXJ5KTsiPjxwb2x5bGluZSBwb2ludHM9IjIwIDYgOSAxNyA0IDEyIj48L3BvbHlsaW5lPjwvc3ZnPg=="
class="ml-auto" />

{% endfor %}

</div>

</div>

<div class="relative" @click.away="editTagDropdownOpen = false">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMjAuNTkgMTMuNDFsLTcuMTcgNy4xN2EyIDIgMCAwMS0yLjgzIDBMMiAxMlYyaDEwbDguNTkgOC41OWEyIDIgMCAwMTAgMi44MnoiIC8+PGxpbmUgeDE9IjciIHkxPSI3IiB4Mj0iNy4wMSIgeTI9IjciPjwvbGluZT48L3N2Zz4=)
Tags
<span class="inline-flex items-center justify-center w-4 h-4 rounded-full text-[10px] font-bold text-white"
x-show="editSelectedTags.length" style="background: var(--primary);"
x-text="editSelectedTags.length"></span>
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBkPSJNNiA5bDYgNiA2LTYiIC8+PC9zdmc+)

<div class="idea-pill-dropdown" x-show="editTagDropdownOpen" x-cloak=""
x-transition="">

<div style="padding: 4px 6px; border-bottom: 1px solid var(--border);">

</div>

<span x-text="tag"></span>

<div class="px-3 py-2 text-xs" style="color: var(--text-tertiary);">

No tags yet. Type to create one.

</div>

<div class="border-t"
style="border-color: var(--border); margin-top: 2px; padding-top: 2px;">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iMTIiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg==)
Create "<span x-text="editTagSearch.trim()"></span>"

</div>

<div class="border-t border-stone-100 px-1 py-1">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1vcmFuZ2UtNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDR2MTZtOC04SDQiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-orange-500" /> Create new tag

</div>

</div>

</div>

</div>

</div>

<div class="idea-selected-tags" style="padding: 0 24px 8px;">

<span x-text="tag"></span>

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSI4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjMiPjxsaW5lIHgxPSIxOCIgeTE9IjYiIHgyPSI2IiB5Mj0iMTgiPjwvbGluZT48bGluZSB4MT0iNiIgeTE9IjYiIHgyPSIxOCIgeTI9IjE4Ij48L2xpbmU+PC9zdmc+)

</div>

<div class="idea-modal-body"
@click="editGroupDropdownOpen = false; editTagDropdownOpen = false">

<div class="idea-media-strip-layout">

<div class="idea-media-existing-card">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi43IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxsaW5lIHgxPSIxOCIgeTE9IjYiIHgyPSI2IiB5Mj0iMTgiPjwvbGluZT48bGluZSB4MT0iNiIgeTE9IjYiIHgyPSIxOCIgeTI9IjE4Ij48L2xpbmU+PC9zdmc+)

</div>

<div class="idea-media-zone"
:class="{ 'idea-media-zone-tile': true, 'drag-over': _editMediaDragOver }"
@click="$refs.editIdeaFileInput.click()"
@dragover.prevent="_editMediaDragOver = true"
@dragleave.prevent="_editMediaDragOver = false"
@drop.prevent="_editMediaDragOver = false; _handleEditMediaDrop($event)">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxyZWN0IHg9IjMiIHk9IjMiIHdpZHRoPSIxOCIgaGVpZ2h0PSIxOCIgcng9IjIiIHJ5PSIyIiAvPjxjaXJjbGUgY3g9IjguNSIgY3k9IjguNSIgcj0iMS41Ij48L2NpcmNsZT48cG9seWxpbmUgcG9pbnRzPSIyMSAxNSAxNiAxMCA1IDIxIj48L3BvbHlsaW5lPjwvc3ZnPg==)
<span x-show="!editMediaAssets.length">Drag & drop</span>
<span x-show="editMediaAssets.length">Add another file</span> or
**select a file**

</div>

</div>

</div>

<div class="idea-modal-footer"
@click="editGroupDropdownOpen = false; editTagDropdownOpen = false">

Delete

Create Post

Save Idea

</div>

</div>

</div>

<div class="fixed inset-0 z-[250] flex items-center justify-center"
x-show="showDeleteIdeaConfirm" x-cloak="" style="display: none;"
@keydown.escape.window="if (showDeleteIdeaConfirm) { showDeleteIdeaConfirm = false; }">

<div class="fixed inset-0 bg-black/30 backdrop-blur-sm"
x-show="showDeleteIdeaConfirm"
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0"
x-transition:enter-end="opacity-100"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="opacity-100"
x-transition:leave-end="opacity-0"
@click="showDeleteIdeaConfirm = false">

</div>

<div class="relative bg-white rounded-2xl shadow-xl w-full max-w-sm mx-4 p-6 text-center"
x-show="showDeleteIdeaConfirm"
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="opacity-100 scale-100"
x-transition:leave-end="opacity-0 scale-95" @click.stop="">

<div class="mx-auto mb-3 w-10 h-10 rounded-full bg-red-50 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LXJlZC01MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPgogICAgICAgICAgICAgICAgICAgICAgICA8cG9seWxpbmUgcG9pbnRzPSIzIDYgNSA2IDIxIDYiPjwvcG9seWxpbmU+PHBhdGggZD0iTTE5IDZ2MTRhMiAyIDAgMCAxLTIgMkg3YTIgMiAwIDAgMS0yLTJWNm0zIDBWNGEyIDIgMCAwIDEgMi0yaDRhMiAyIDAgMCAxIDIgMnYyIiAvPjxsaW5lIHgxPSIxMCIgeTE9IjExIiB4Mj0iMTAiIHkyPSIxNyI+PC9saW5lPjxsaW5lIHgxPSIxNCIgeTE9IjExIiB4Mj0iMTQiIHkyPSIxNyI+PC9saW5lPgogICAgICAgICAgICAgICAgICAgIDwvc3ZnPg=="
class="w-5 h-5 text-red-500" />

</div>

### Delete idea?

This action cannot be undone. The idea and all associated data will be
permanently removed.

<div class="flex gap-3">

Cancel

<span x-show="!deletingIdea">Delete</span>
<span x-show="deletingIdea">Deleting…</span>

</div>

</div>

</div>

<div class="fixed inset-0 z-[220] flex items-center justify-center"
x-show="showIdeaCreateTagModal" x-cloak=""
@keydown.escape.window="closeIdeaCreateTagModal()">

<div class="fixed inset-0 bg-black/30"
@click="closeIdeaCreateTagModal()">

</div>

<div class="relative bg-white rounded-2xl shadow-xl w-full max-w-sm mx-4 p-6"
@click.stop="">

### Create new tag

<div class="flex justify-end gap-2 mt-4">

Cancel

Create

</div>

</div>

</div>

<div class="idea-modal-overlay" x-show="viewingTemplate" x-cloak=""
@click.self="viewingTemplate = null"
@keydown.escape.window="viewingTemplate = null">

<div class="idea-modal" @click.stop="" style="max-width: 560px;">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48bGluZSB4MT0iMTgiIHkxPSI2IiB4Mj0iNiIgeTI9IjE4Ij48L2xpbmU+PGxpbmUgeDE9IjYiIHkxPSI2IiB4Mj0iMTgiIHkyPSIxOCI+PC9saW5lPjwvc3ZnPg==)

<div class="px-6 pt-6 pb-2">

<div class="w-16 h-16 rounded-2xl flex items-center justify-center text-3xl mb-4"
style="background: var(--neutral-50);">

<span x-text="viewingTemplate?.emoji"></span>

</div>

## 

</div>

<div class="px-6 py-4">

<div class="rounded-xl border p-5 bg-green-50/40 border-green-200/60">

<div class="flex items-center justify-end gap-2 mt-4 pt-3"
style="border-top: 1px solid rgba(0,0,0,0.06);">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cmVjdCB4PSI5IiB5PSI5IiB3aWR0aD0iMTMiIGhlaWdodD0iMTMiIHJ4PSIyIiByeT0iMiIgLz48cGF0aCBkPSJNNSAxNUg0YTIgMiAwIDAxLTItMlY0YTIgMiAwIDAxMi0yaDlhMiAyIDAgMDEyIDJ2MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNOS42NjMgMTdoNC42NzNNMTIgM3YxbTYuMzY0IDEuNjM2bC0uNzA3LjcwN00yMSAxMmgtMU00IDEySDNtMy4zNDMtNS42NTdsLS43MDctLjcwN20yLjgyOCA5LjlhNSA1IDAgMTE3LjA3MiAwbC0uNTQ4LjU0N0EzLjM3NCAzLjM3NCAwIDAwMTQgMTguNDY5VjE5YTIgMiAwIDExLTQgMHYtLjUzMWMwLS44OTUtLjM1Ni0xLjc1NC0uOTg4LTIuMzg2bC0uNTQ4LS41NDd6IiAvPjwvc3ZnPg==)
Use Template

</div>

</div>

</div>

<div class="px-6 pb-5 flex items-center gap-3">

<span class="text-xs font-medium text-stone-400">By</span>
<span class="text-xs font-semibold text-stone-600 underline decoration-stone-300 underline-offset-2">Brightbean</span>
<span class="text-stone-300 mx-1">•</span>
<span class="text-xs font-medium text-stone-500" x-text="tag"></span>
<span class="text-stone-300 mx-1">•</span>
<span class="text-xs font-medium text-stone-500"
x-text="viewingTemplate?.category ? viewingTemplate.category.charAt(0).toUpperCase() + viewingTemplate.category.slice(1).replace('-', ' ') : ''"></span>

</div>

</div>

</div>

</div>

{% endblock %} {% block extra_js %}

{% endblock %}
