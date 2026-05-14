---
type: source
source_type: laptop
title: compose
slug: compose
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/composer/compose.html
original_size: 130504
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# compose

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/composer/compose.html` on 2026-05-14._

{% extends "base.html" %} {% load static %} {% block title %}{% if
is_edit %}Edit Post{% else %}New Post{% endif %} - {{ workspace.name
}} - Brightbean{% endblock %} {% comment %}Header is rendered inside the
content block to avoid overlap with the -m-6 layout{% endcomment %} {%
block extra_head %} <style>
    /* ── Composer-specific overrides ──────────────────────────── */
    /* Remove parent padding/overflow so the composer can fill the full area */
    main:has(.composer-main) { padding: 0 !important; overflow: hidden !important; }
    main:has(.composer-main) > div { overflow: hidden !important; }
    .composer-main { padding: 0 !important; overflow: hidden; }

    /* Panels */
    .panel-center { flex: 1; min-width: 0; }
    .panel-right  {
        /* Mobile: off-canvas drawer sliding in from the right */
        position: fixed; inset: 0 0 0 auto;
        width: 100%; max-width: 380px;
        z-index: 58;
        transform: translateX(100%);
        transition: transform 200ms cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: -8px 0 24px rgba(23,20,18,0.08);
    }
    .panel-right.is-open { transform: translateX(0); }
    @media (min-width: 1024px) {
        .panel-right {
            position: static; inset: auto;
            width: 340px; max-width: none;
            flex-shrink: 0;
            transform: none; transition: none;
            box-shadow: none;
        }
    }
    .panel-right-backdrop {
        position: fixed; inset: 0;
        background: #000;
        z-index: 57;
    }
    @media (min-width: 1024px) {
        .panel-right-backdrop { display: none !important; }
    }

    /* Platform account checkbox pill - compact for header row */
    .acct-pill {
        display: flex; align-items: center; gap: 6px;
        padding: 5px 10px; border-radius: 9999px;
        border: 1.5px solid #E7E5E4;
        background: #FFFFFF;
        cursor: pointer; user-select: none;
        transition: all 150ms cubic-bezier(0.16, 1, 0.3, 1);
        white-space: nowrap;
    }
    .acct-pill:hover { border-color: #D6D3D1; background: #FAFAF9; }
    .acct-pill.selected {
        border-color: #F97316; background: #FFF7ED;
        box-shadow: 0 0 0 3px rgba(249,115,22,0.08);
    }
    .acct-pill .checkmark {
        width: 16px; height: 16px; border-radius: 4px;
        border: 1.5px solid #D6D3D1; flex-shrink: 0;
        display: flex; align-items: center; justify-content: center;
        transition: all 150ms ease;
    }
    .acct-pill.selected .checkmark {
        background: #F97316; border-color: #F97316;
    }
    .acct-pill.selected .checkmark svg { display: block; }
    .acct-pill .checkmark svg { display: none; }

    /* Platform icon circles */
    .platform-icon {
        width: 26px; height: 26px; border-radius: 7px;
        display: flex; align-items: center; justify-content: center;
        font-size: 11px; font-weight: 700; color: white; flex-shrink: 0;
        letter-spacing: -0.02em;
    }
    .pi-facebook   { background: #1877F2; }
    .pi-instagram  { background: [[linear|linear]]-gradient(135deg, #F58529, #DD2A7B, #8134AF); }
    .pi-[[linkedin|linkedin]]   { background: #0A66C2; }
    .pi-linkedin_personal { background: #0A66C2; }
    .pi-linkedin_company  { background: #0A66C2; }
    .pi-tiktok     { background: #010101; }
    .pi-youtube    { background: #FF0000; }
    .pi-pinterest  { background: #E60023; }
    .pi-threads    { background: #000000; }
    .pi-bluesky    { background: #0085FF; }
    .pi-google_business { background: #4285F4; }
    .pi-mastodon   { background: #6364FF; }

    /* Character counter bar */
    .char-bar {
        height: 3px; border-radius: 2px;
        background: #E7E5E4; overflow: hidden;
        transition: all 200ms ease;
    }
    .char-bar-fill {
        height: 100%; border-radius: 2px;
        transition: width 150ms ease, background 150ms ease;
    }

    /* Caption area - the star of the show */
    .caption-wrap {
        border: 1.5px solid #E7E5E4;
        border-radius: 12px;
        background: #FFFFFF;
        transition: border-color 150ms ease, box-shadow 150ms ease;
        position: relative;
    }
    .caption-wrap:hover { border-color: #D6D3D1; }
    .caption-wrap:focus-within {
        border-color: #F97316;
        box-shadow: 0 0 0 3px rgba(249,115,22,0.1);
    }
    .caption-editor {
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 15px; line-height: 1.65;
        padding: 16px 18px 8px;
        background: transparent;
        color: #1C1917;
        border: none;
        resize: none; min-height: 180px;
        outline: none;
        width: 100%;
    }
    .caption-editor::placeholder { color: #A8A29E; }

    /* First-comment editor - thinner variant */
    .comment-editor {
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 14px; line-height: 1.55;
        padding: 10px 14px;
        border: 1.5px solid #E7E5E4;
        border-radius: 10px;
        background: #FFFFFF;
        color: #1C1917;
        resize: none; min-height: 0;
        outline: none;
        width: 100%;
        transition: border-color 150ms ease, box-shadow 150ms ease;
    }
    .comment-editor::placeholder { color: #A8A29E; }
    .comment-editor:hover { border-color: #D6D3D1; }
    .comment-editor:focus {
        border-color: #F97316;
        box-shadow: 0 0 0 3px rgba(249,115,22,0.1);
    }

    /* Media dropzone - compact inline version */
    .media-dropzone-inline {
        border: 1.5px dashed #D6D3D1;
        border-radius: 8px;
        padding: 8px 12px;
        display: flex; align-items: center; gap: 8px;
        transition: all 200ms ease;
        cursor: pointer;
        margin: 0 16px 12px;
    }
    .media-dropzone-inline:hover,
    .media-dropzone-inline.dragover {
        border-color: #F97316;
        background: #FFF7ED;
    }

    /* Media thumbnail grid */
    .media-thumb {
        width: 56px; height: 56px;
        border-radius: 8px;
        overflow: hidden;
        position: relative;
        border: 1px solid #E7E5E4;
    }
    .media-thumb img { width: 100%; height: 100%; object-fit: cover; }
    .media-thumb .remove-btn {
        position: absolute; top: 3px; right: 3px;
        width: 18px; height: 18px; border-radius: 50%;
        background: rgba(0,0,0,0.55); color: white;
        display: flex; align-items: center; justify-content: center;
        font-size: 10px; cursor: pointer;
        transition: background 150ms ease;
        z-index: 2;
    }
    .media-thumb .remove-btn:hover { background: #EF4444; }

    /* Upload progress overlay */
    .media-thumb .upload-overlay {
        position: absolute; inset: 0;
        background: rgba(0,0,0,0.45);
        display: flex; align-items: center; justify-content: center;
        z-index: 1;
    }
    .media-thumb .upload-overlay svg { filter: drop-shadow(0 1px 2px rgba(0,0,0,0.3)); }
    .media-thumb .upload-progress-ring { transition: stroke-dashoffset 150ms ease; }
    .media-thumb.upload-failed { border-color: #EF4444; }
    .media-thumb.upload-failed .upload-overlay { background: rgba(239,68,68,0.25); }
    .media-thumb .retry-btn {
        position: absolute; inset: 0;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        gap: 2px; cursor: pointer; z-index: 3;
        background: rgba(0,0,0,0.5); color: white;
        font-size: 9px; font-weight: 600;
        border: none; border-radius: 8px;
    }
    .media-thumb .retry-btn:hover { background: rgba(0,0,0,0.65); }

    /* Preview panel cards */
    .preview-card {
        background: #FFFFFF;
        border: 1px solid #E7E5E4;
        border-radius: 14px;
        overflow: hidden;
        transition: all 200ms cubic-bezier(0.16, 1, 0.3, 1);
    }
    .preview-card:hover {
        box-shadow: 0 10px 15px rgba(23,20,18,0.08), 0 4px 6px rgba(23,20,18,0.04);
        border-color: transparent;
    }

    /* Action bar */
    .action-bar {
        background: #FFFFFF;
        border-top: 1px solid #E7E5E4;
        padding: 12px 16px;
        display: flex; align-items: center; gap: 6px;
        position: relative;
        z-index: 51;
    }
    @media (min-width: 640px) {
        .action-bar { padding: 20px 24px; gap: 8px; }
    }

    /* Subtle entrance animation - uses 'both' but resets transform at 100% to avoid
       creating a permanent stacking context (which traps z-index of child popovers). */
    @keyframes slideUp {
        0%   { opacity: 0; transform: translateY(8px); }
        100% { opacity: 1; transform: none; }
    }
    .animate-in { animation: slideUp 300ms cubic-bezier(0.16, 1, 0.3, 1) forwards; }
    .animate-in-d1 { animation-delay: 50ms; opacity: 0; }
    .animate-in-d2 { animation-delay: 100ms; opacity: 0; }
    .animate-in-d3 { animation-delay: 150ms; opacity: 0; }

    /* Toast notification */
    .toast-saved {
        position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%);
        background: #1C1917; color: white;
        padding: 8px 16px; border-radius: 9999px;
        font-size: 13px; font-weight: 500;
        box-shadow: 0 10px 15px rgba(23,20,18,0.2);
        z-index: 100;
    }

    /* Scrollbar refinement */
    .panel-scroll::-webkit-scrollbar { width: 4px; }
    .panel-scroll::-webkit-scrollbar-track { background: transparent; }
    .panel-scroll::-webkit-scrollbar-thumb { background: #D6D3D1; border-radius: 2px; }
    .panel-scroll::-webkit-scrollbar-thumb:hover { background: #A8A29E; }
</style> {% endblock %} {% block content %}

<div class="composer-main flex flex-col flex-1" x-data="composerApp()"
@keydown.meta.s.prevent="saveDraft()"
@keydown.ctrl.s.prevent="saveDraft()">

<div class="flex items-center gap-3 px-4 sm:px-6 py-3 border-b border-stone-100 flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4" />

# {% if is_edit %}Edit{% else %}Create{% endif %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0yLjAzNiAxMi4zMjJhMS4wMTIgMS4wMTIgMCAwMTAtLjYzOUMzLjQyMyA3LjUxIDcuMzYgNC41IDEyIDQuNWM0LjYzOCAwIDguNTczIDMuMDA3IDkuOTYzIDcuMTc4LjA3LjIwNy4wNy40MzEgMCAuNjM5QzIwLjU3NyAxNi40OSAxNi42NCAxOS41IDEyIDE5LjVjLTQuNjM4IDAtOC41NzMtMy4wMDctOS45NjMtNy4xNzh6IiAvPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE1IDEyYTMgMyAwIDExLTYgMCAzIDMgMCAwMTYgMHoiIC8+PC9zdmc+"
class="w-4 h-4" /> Preview
<span class="inline-flex items-center justify-center min-w-[18px] h-[18px] px-1 rounded-full bg-orange-100 text-orange-700 text-[10px] font-bold tabular-nums"
x-show="selectedAccounts.length &gt; 0"
x-text="selectedAccounts.length"></span>

</div>

<div class="flex flex-1 min-h-0">

<div class="panel-center flex flex-col bg-stone-50 min-h-0">

<div class="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4 sm:space-y-5 panel-scroll relative"
style="z-index: 0;">

<div class="flex items-center gap-2 flex-wrap">

{% for account in social_accounts %} <span class="checkmark"> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0ZXh0LXdoaXRlIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIzIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTUgMTNsNCA0TDE5IDciIC8+PC9zdmc+"
class="w-3 h-3 text-white" /> </span>

<div class="relative flex-shrink-0">

{% if account.avatar_url %}
<img src="%7B%7B%20account.avatar_url%20%7D%7D"
class="w-7 h-7 rounded-full object-cover"
alt="{{ account.account_name|default:account.account_handle }}" /> {%
else %}

<div class="w-7 h-7 rounded-full bg-stone-100 flex items-center justify-center text-stone-400">

{% include "partials/\_platform_icon.html" with
platform=account.platform size="sm" %}

</div>

{% endif %}

<div class="absolute -bottom-0.5 -right-0.5 w-4 h-4 bg-white rounded-full flex items-center justify-center">

{% include "partials/\_platform_icon.html" with
platform=account.platform size="sm" %}

</div>

</div>

<span class="text-sm font-medium text-stone-700 truncate">{{
account.account_name\|default:account.account_handle }}</span> {% empty
%} <span class="text-xs text-stone-400">No accounts connected</span> {%
endfor %}

</div>

<div x-show="anyPlatformNeedsTitle" x-transition="" x-cloak="">

Title

<div class="flex items-center justify-end mt-1">

<span class="text-[11px] tabular-nums font-medium"
:class="title.length &gt; titleMaxLength ? 'text-red-500' : 'text-stone-400'"
x-text="title.length + ' / ' + titleMaxLength"></span>

</div>

</div>

<div x-data="{ showTemplatePicker: false }">

<div class="flex items-center justify-between mb-2">

Caption

<div class="flex items-center gap-2 relative">

{% if post and is_edit %}

<div x-data="{ showSaveTemplate: false }">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNOCA3SDVhMiAyIDAgMDAtMiAydjlhMiAyIDAgMDAyIDJoMTRhMiAyIDAgMDAyLTJWOWEyIDIgMCAwMC0yLTJoLTNtLTEgNGwtMyAzbTAgMGwtMy0zbTMgM1Y0IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5" /> Save as Template

<div class="absolute z-50 mt-1 right-0 p-3 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 w-72 max-w-[calc(100vw-2rem)]"
x-show="showSaveTemplate" x-cloak="" x-transition=""
@click.outside="showSaveTemplate = false">

<div x-data="{ tplName: '', tplDesc: '' }">

Save Template

</div>

</div>

</div>

{% endif %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNOSAxMmg2bS02IDRoNm0yIDVIN2EyIDIgMCAwMS0yLTJWNWEyIDIgMCAwMTItMmg1LjU4NmExIDEgMCAwMS43MDcuMjkzbDUuNDE0IDUuNDE0YTEgMSAwIDAxLjI5My43MDdWMTlhMiAyIDAgMDEtMiAyeiIgLz48L3N2Zz4="
class="w-3.5 h-3.5" /> Use Template

<div class="absolute z-50 top-full mt-1 right-0 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 w-80 max-w-[calc(100vw-2rem)] max-h-80 overflow-y-auto"
x-show="showTemplatePicker" x-cloak="" x-transition=""
@click.outside="showTemplatePicker = false"
hx-get="{% url 'composer:template_picker' workspace_id=workspace.id %}"
hx-trigger="intersect once" hx-target="this">

<div class="p-4 text-center text-xs text-stone-400">

Loading templates…

</div>

</div>

</div>

</div>

<div class="caption-wrap">

<div id="media-list" class="flex flex-wrap gap-2 px-4 pb-2">

{% if post %} {% include "composer/partials/media_list.html" %} {% elif
pending_assets %} {% include "composer/partials/media_list_pending.html"
%} {% endif %}

</div>

<div class="media-dropzone-inline"
@dragover.prevent="$el.classList.add('dragover')"
@dragleave="$el.classList.remove('dragover')"
@drop.prevent="handleFileDrop($event); $el.classList.remove('dragover')"
@click="$refs.fileInput.click()">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSB0ZXh0LXN0b25lLTMwMCBmbGV4LXNocmluay0wIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMS41IiBkPSJNNCAxNmw0LjU4Ni00LjU4NmEyIDIgMCAwMTIuODI4IDBMMTYgMTZtLTItMmwxLjU4Ni0xLjU4NmEyIDIgMCAwMTIuODI4IDBMMjAgMTRtLTYtNmguMDFNNiAyMGgxMmEyIDIgMCAwMDItMlY2YTIgMiAwIDAwLTItMkg2YTIgMiAwIDAwLTIgMnYxMmEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-5 h-5 text-stone-300 flex-shrink-0" />
<span class="text-xs text-stone-400">Drag & drop or
<span class="text-orange-500 font-medium">select files</span></span>

</div>

<div class="flex items-center justify-between px-4 py-2 border-t border-stone-100">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTkgMTFINW0xNCAwYTIgMiAwIDAxMiAydjZhMiAyIDAgMDEtMiAySDVhMiAyIDAgMDEtMi0ydi02YTIgMiAwIDAxMi0ybTE0IDBWOWEyIDIgMCAwMC0yLTJNNSAxMVY5YTIgMiAwIDAxMi0ybTAgMFY1YTIgMiAwIDAxMi0yaDZhMiAyIDAgMDEyIDJ2Mk03IDdoMTAiIC8+PC9zdmc+"
class="w-3.5 h-3.5" /> Media Library

<span class="text-xs tabular-nums font-medium"
:class="(() =&gt; { const min = Math.min(...selectedAccounts.map(id =&gt; charLimits[id]?.limit || 9999)); return caption.length &gt; min ? 'text-red-500' : 'text-stone-400'; })()"
x-text="(() =&gt; { const limits = selectedAccounts.map(id =&gt; charLimits[id]?.limit).filter(Boolean); const min = limits.length ? Math.min(...limits) : null; return min ? caption.length + ' / ' + min : caption.length; })()">
</span>

</div>

</div>

</div>

<div class="border border-stone-200 rounded-xl bg-white p-4 space-y-3"
x-show="charLimits[accId]?.platform === 'pinterest'"
x-data="{ boards: [], boardsLoading: false, boardsLoaded: false }"
x-effect="if (charLimits[accId]?.platform === 'pinterest' &amp;&amp; !boardsLoaded) {
                             boardsLoading = true;
                             fetch(`/workspace/{{ workspace.id }}/compose/pinterest-boards/${accId}/`)
                                 .then(r =&gt; r.json())
                                 .then(data =&gt; { boards = data.boards || []; boardsLoaded = true; })
                                 .catch(() =&gt; {})
                                 .finally(() =&gt; { boardsLoading = false; });
                         }">

<div class="flex items-center gap-2">

<span class="platform-icon w-5 h-5 rounded-[5px] flex items-center justify-center"
:class="'pi-' + (charLimits[accId]?.platform || '')"
x-html="platformIconSvg(charLimits[accId]?.platform || '')"></span>
<span class="text-xs font-semibold text-stone-600"
x-text="charLimits[accId]?.name + ' - Pin Settings'"></span>

</div>

<div>

Select Board <span class="text-red-400">\*</span> Select a board…

Loading boards…

No boards found. Create a board on Pinterest first.

</div>

<div>

Destination Link

Where people go when they click the pin

</div>

<div>

Tag Products

Requires a connected product catalog

</div>

<div class="border-t border-stone-100 pt-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0cmFuc2l0aW9uLXRyYW5zZm9ybSIgOmNsYXNzPSJhZHZhbmNlZE9wZW5bYWNjSWRdID8gJiMzOTtyb3RhdGUtOTAmIzM5OyA6ICYjMzk7JiMzOTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgZD0iTTkgNWw3IDctNyA3IiAvPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvc3ZnPg=="
class="w-3 h-3 transition-transform" /> Advanced

<div class="mt-3 space-y-3" x-show="advancedOpen[accId]"
x-transition="">

<span class="text-sm text-stone-700">Allow people to comment</span>

<span class="text-sm text-stone-700">Show similar products</span>

<div>

Alt Text

</div>

<div>

Video Cover Image

<div class="flex items-center gap-2">

<span x-text="platformExtras[accId]?.cover_image_asset_id ? 'Change' : 'Pick from Library'"></span>

<span x-text="thumbnailUploading[accId] ? 'Uploading…' : 'Upload'"></span>

Remove

</div>

Required for video pins. PNG or JPG, same dimensions as video.

</div>

</div>

</div>

</div>

<div class="border border-stone-200 rounded-xl bg-white p-4 space-y-3"
x-show="charLimits[accId]?.platform === 'youtube'">

<div class="flex items-center gap-2">

<span class="platform-icon w-5 h-5 rounded-[5px] flex items-center justify-center"
:class="'pi-' + (charLimits[accId]?.platform || '')"
x-html="platformIconSvg(charLimits[accId]?.platform || '')"></span>
<span class="text-xs font-semibold text-stone-600"
x-text="charLimits[accId]?.name + ' - Video Settings'"></span>

</div>

<div>

Custom Thumbnail

<div class="mb-2">

</div>

<div class="mb-2 w-full max-w-[240px] aspect-video rounded-lg border-2 border-dashed border-stone-200 bg-stone-50 flex flex-col items-center justify-center gap-1 cursor-pointer hover:border-orange-300 hover:bg-orange-50 transition-colors"
@click="triggerThumbnailUpload(accId)">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTQgMTZsNC41ODYtNC41ODZhMiAyIDAgMDEyLjgyOCAwTDE2IDE2bS0yLTJsMS41ODYtMS41ODZhMiAyIDAgMDEyLjgyOCAwTDIwIDE0bS02LTZoLjAxTTYgMjBoMTJhMiAyIDAgMDAyLTJWNmEyIDIgMCAwMC0yLTJINmEyIDIgMCAwMC0yIDJ2MTJhMiAyIDAgMDAyIDJ6IiAvPjwvc3ZnPg=="
class="w-6 h-6 text-stone-300" />
<span class="text-[11px] text-stone-400">Click to upload
thumbnail</span>

</div>

<div class="flex items-center gap-2">

<span x-text="platformExtras[accId]?.thumbnail_asset_id ? 'Change' : 'Pick from Library'"></span>

<span x-text="thumbnailUploading[accId] ? 'Uploading…' : 'Upload'"></span>

Remove

</div>

</div>

<div>

Visibility Public Unlisted Private

</div>

<div class="border-t border-stone-100 pt-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyB0cmFuc2l0aW9uLXRyYW5zZm9ybSIgOmNsYXNzPSJhZHZhbmNlZE9wZW5bYWNjSWRdID8gJiMzOTtyb3RhdGUtOTAmIzM5OyA6ICYjMzk7JiMzOTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgZD0iTTkgNWw3IDctNyA3IiAvPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDwvc3ZnPg=="
class="w-3 h-3 transition-transform" /> Advanced

<div class="mt-3 space-y-3" x-show="advancedOpen[accId]"
x-transition="">

<span class="text-sm text-stone-700"> Made for Kids
<span class="block text-[11px] text-stone-400 font-normal">Required by
COPPA - mark if this video is directed at children under 13</span>
</span>

<div>

Tags

Comma-separated

</div>

</div>

</div>

</div>

<div class="flex flex-wrap gap-1.5"
x-show="selectedAccounts.length &gt; 0">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-3 h-3" />
<span x-text="'Customize ' + (charLimits[accId]?.platform || '')"></span>

</div>

<div class="border border-stone-200 rounded-xl bg-white p-4"
x-show="overrides[accId]" x-transition="">

<div class="flex items-center gap-2 mb-3">

<span class="platform-icon w-5 h-5 rounded-[5px] flex items-center justify-center"
:class="'pi-' + (charLimits[accId]?.platform || '')"
x-html="platformIconSvg(charLimits[accId]?.platform || '')"></span>
<span class="text-xs font-semibold text-stone-600"
x-text="charLimits[accId]?.name + ' - Custom Override'"></span>

Remove override

</div>

<div class="mb-3">

</div>

</div>

<div x-show="anyPlatformSupportsFirstComment" x-transition=""
x-cloak="">

First Comment

</div>

{% if categories %}

<div>

Category No category {% for cat in categories %} ● {{ cat.name }} {%
endfor %}

</div>

{% endif %}

------------------------------------------------------------------------

<div class="relative" x-data="{
                    tags: {{ post.tags|default:'[]'|safe }},
                    tagDropdownOpen: false,
                    tagSearch: '',
                    allTags: [{% for tag in all_tags %}'{{ tag.name|escapejs }}'{% if not forloop.last %},{% endif %}{% endfor %}],
                    get filteredTags() {
                        const q = this.tagSearch.toLowerCase();
                        return this.allTags.filter(t =&gt; !q || t.toLowerCase().includes(q));
                    },
                    toggleTag(name) {
                        const idx = this.tags.indexOf(name);
                        if (idx &gt;= 0) { this.tags.splice(idx, 1); }
                        else { this.tags.push(name); }
                    },
                    createTag() {
                        const name = this.tagSearch.trim();
                        if (!name) return;
                        if (!this.allTags.includes(name)) { this.allTags.push(name); this.allTags.sort(); }
                        if (!this.tags.includes(name)) { this.tags.push(name); }
                        this.tagSearch = '';
                        /* Persist to server */
                        fetch('{% url " composer:tag_create"="" ',=""
_persisttag(name)="" (!this.alltags.includes(name))=""
this.alltags.push(name);="" this.alltags.sort();="" if=""
(!this.tags.includes(name))="" this.tags.push(name);="" }=""
fetch('{%="" url="" "composer:tag_create"="" workspace_id="workspace.id"
%}',="" method:="" 'post',="" headers:="" {="" 'x-csrftoken':=""
document.queryselector('[name="csrfmiddlewaretoken]').value,"
'content-type':="" 'application="" x-www-form-urlencoded'="" },=""
body:="" 'name=" + encodeURIComponent(name),
                        });
                    },
                }&quot; @click.away=&quot;tagDropdownOpen = false&quot;&gt;
                    &lt;div class=&quot;flex items-center gap-2 mb-2&quot;&gt;
                        &lt;label class=&quot;text-sm font-semibold text-stone-500 uppercase tracking-wider&quot;&gt;Tags&lt;/label&gt;
                        &lt;span class=&quot;text-[10px] font-semibold text-stone-400 bg-stone-100 px-2 py-0.5 rounded-full uppercase tracking-wider&quot;&gt;Internal team only&lt;/span&gt;
                    &lt;/div&gt;
                    &lt;input type=&quot;hidden&quot; name=&quot;tags&quot; :value=&quot;tags.join("
,')"="">

<div class="flex flex-wrap items-center gap-1.5 w-full min-h-[42px] px-3 py-2 rounded-xl border border-stone-200 bg-white transition-all duration-150 cursor-pointer"
:class="tagDropdownOpen &amp;&amp; 'border-orange-500 ring-2 ring-orange-100'"
@click="tagDropdownOpen = !tagDropdownOpen; if(tagDropdownOpen) $nextTick(() =&gt; { $refs.tagSearchInput.focus(); $refs.tagSearchInput.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); })">

<span x-text="tag"></span>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMyI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNNiAxOEwxOCA2TTYgNmwxMiAxMiIgLz48L3N2Zz4="
class="w-2.5 h-2.5" />

<span class="text-sm text-stone-400" x-show="!tags.length">Select
tags...</span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBtbC1hdXRvIHRleHQtc3RvbmUtNDAwIHNocmluay0wIHRyYW5zaXRpb24tdHJhbnNmb3JtIGR1cmF0aW9uLTE1MCIgOmNsYXNzPSJ0YWdEcm9wZG93bk9wZW4gJmFtcDsmYW1wOyAmIzM5O3JvdGF0ZS0xODAmIzM5OyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA5bC03IDctNy03IiAvPjwvc3ZnPg=="
class="w-4 h-4 ml-auto text-stone-400 shrink-0 transition-transform duration-150" />

</div>

<div class="mt-1 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 py-1 max-h-[220px] overflow-y-auto"
x-show="tagDropdownOpen" x-cloak="" x-transition="" @click.stop="">

<div class="px-2 py-1.5 border-b border-stone-100">

</div>

<span x-text="tag"></span>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1vcmFuZ2UtNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDR2MTZtOC04SDQiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-orange-500" /> Create
"<span class="font-semibold" x-text="tagSearch.trim()"></span>"

<div class="border-t border-stone-100 mt-1 pt-1">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1vcmFuZ2UtNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDR2MTZtOC04SDQiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-orange-500" /> Create
"<span class="font-semibold" x-text="tagSearch.trim()"></span>"

</div>

<div class="px-3 py-2 text-xs text-stone-400">

No tags yet. Type to create one.

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

{% if can_view_internal_notes %}

<div>

<div class="flex items-center gap-2 mb-2">

Notes
<span class="text-[10px] font-semibold text-stone-400 bg-stone-100 px-2 py-0.5 rounded-full uppercase tracking-wider">Internal
team only</span>

</div>

</div>

{% endif %}

</div>

<div class="action-bar">

{% if is_edit %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA3bC0uODY3IDEyLjE0MkEyIDIgMCAwMTE2LjEzOCAyMUg3Ljg2MmEyIDIgMCAwMS0xLjk5NS0xLjg1OEw1IDdtNSA0djZtNC02djZtMS0xMFY0YTEgMSAwIDAwLTEtMWgtNGExIDEgMCAwMC0xIDF2M000IDdoMTYiIC8+PC9zdmc+"
class="w-4 h-4" /> <span class="hidden sm:inline">Delete</span>

{% endif %}

<div id="autosave-status"
class="text-xs text-stone-400 mr-auto hidden sm:flex items-center gap-1.5">

<span class="w-1.5 h-1.5 rounded-full bg-stone-300"
:class="{ 'bg-emerald-400': lastSaved }"></span>
<span x-text="lastSaved ? 'Saved ' + lastSaved : 'Not saved yet'"></span>

</div>

<div class="mr-auto sm:hidden">

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik04IDdINWEyIDIgMCAwMC0yIDJ2OWEyIDIgMCAwMDIgMmgxNGEyIDIgMCAwMDItMlY5YTIgMiAwIDAwLTItMmgtM20tMSA0bC0zIDNtMCAwbC0zLTNtMyAzVjQiIC8+PC9zdmc+"
class="w-4 h-4" /> <span class="hidden sm:inline">Save Draft</span>

{% if show_submit_button %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik05IDEyLjc1TDExLjI1IDE1IDE1IDkuNzVNMjEgMTJhOSA5IDAgMTEtMTggMCA5IDkgMCAwMTE4IDB6IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> <span class="hidden sm:inline">Submit for
Approval</span> <span class="sm:hidden">For Approval</span>

{% endif %} {% if show_resubmit_button %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNi4wMjMgOS4zNDhoNC45OTJ2LS4wMDFNMi45ODUgMTkuNjQ0di00Ljk5Mm0wIDBoNC45OTJtLTQuOTkzIDBsMy4xODEgMy4xODNhOC4yNSA4LjI1IDAgMDAxMy44MDMtMy43TTQuMDMxIDkuODY1YTguMjUgOC4yNSAwIDAxMTMuODAzLTMuN2wzLjE4MSAzLjE4MiIgLz48L3N2Zz4="
class="w-4 h-4" /> <span class="hidden sm:inline">Resubmit</span>

{% endif %}

<div id="publish-anchor" class="relative inline-flex flex-shrink-0">

<img
src="data:image/svg+xml;base64,PHN2ZyBpZD0icHVibGlzaC1tb2RlLWljb24iIGNsYXNzPSJ3LTQgaC00IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgZD0iTTEyIDZ2Nmg0LjVtNC41IDBhOSA5IDAgMTEtMTggMCA5IDkgMCAwMTE4IDB6IiAvPjwvc3ZnPg=="
id="publish-mode-icon" class="w-4 h-4" /> <span id="publish-mode-label"
class="hidden sm:inline">Next available</span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyBvcGFjaXR5LTYwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMi41IiBkPSJNMTkgOWwtNyA3LTctNyIgLz48L3N2Zz4="
class="w-3 h-3 opacity-60" />

<span id="publish-action-label">Add to Queue</span>

<div id="publish-popover"
class="hidden absolute bottom-full right-0 mb-2 w-72 max-w-[calc(100vw-2rem)] bg-white rounded-xl shadow-xl border border-stone-200/80"
style="z-index: 50;">

<div id="publish-menu" class="p-1.5">

<div class="w-8 h-8 rounded-lg bg-blue-50 flex items-center justify-center flex-shrink-0 mt-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LWJsdWUtNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgZD0iTTEyIDZ2Nmg0LjVtNC41IDBhOSA5IDAgMTEtMTggMCA5IDkgMCAwMTE4IDB6IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-blue-500" />

</div>

<div>

<div class="text-sm font-semibold text-stone-800">

Next Available

</div>

<div class="text-xs text-stone-400 mt-0.5">

Place in next available slot

</div>

</div>

<div class="w-8 h-8 rounded-lg bg-amber-50 flex items-center justify-center flex-shrink-0 mt-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LWFtYmVyLTUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0zIDRoMTNNMyA4aDltLTkgNGg2bTQgMGw0LTRtMCAwbDQgNG0tNC00djEyIiAvPjwvc3ZnPg=="
class="w-4 h-4 text-amber-500" />

</div>

<div>

<div class="text-sm font-semibold text-stone-800">

Prioritise

</div>

<div class="text-xs text-stone-400 mt-0.5">

Add to top of queue

</div>

</div>

<div class="w-8 h-8 rounded-lg bg-emerald-50 flex items-center justify-center flex-shrink-0 mt-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LWVtZXJhbGQtNTAwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgZD0iTTUgM2wxNCA5LTE0IDlWM3oiIC8+PC9zdmc+"
class="w-4 h-4 text-emerald-500" />

</div>

<div>

<div class="text-sm font-semibold text-stone-800">

Now

</div>

<div class="text-xs text-stone-400 mt-0.5">

Publish immediately

</div>

</div>

<div class="w-8 h-8 rounded-lg bg-violet-50 flex items-center justify-center flex-shrink-0 mt-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXZpb2xldC01MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNOCA3VjNtOCA0VjNtLTkgOGgxME01IDIxaDE0YTIgMiAwIDAwMi0yVjdhMiAyIDAgMDAtMi0ySDVhMiAyIDAgMDAtMiAydjEyYTIgMiAwIDAwMiAyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-violet-500" />

</div>

<div>

<div class="text-sm font-semibold text-stone-800">

Set Date and Time

</div>

<div class="text-xs text-stone-400 mt-0.5">

Choose a specific time

</div>

</div>

</div>

<div id="publish-schedule-view" class="hidden p-4">

<div class="flex items-center gap-2 mb-4">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTUwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4 text-stone-500" />

<span class="text-sm font-semibold text-stone-800">Schedule Post</span>

</div>

<div class="space-y-3">

<div>

Date

</div>

<div>

Time

</div>

<div class="text-xs text-stone-400 flex items-center gap-1">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA4djRsMyAzbTYtM2E5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="w-3 h-3" /> Timezone: {{ workspace.effective_timezone }}

</div>

</div>

<div id="schedule-error" class="hidden text-xs text-red-500 mt-1">

</div>

Set Schedule

</div>

</div>

</div>

</div>

{% if post and approval_history %}

<div class="mt-4 border-t border-stone-200 pt-4">

{% if post.status == 'pending_review' %}

<div class="flex items-center gap-2 px-3 py-2 rounded-lg bg-orange-50 border border-orange-100 mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LW9yYW5nZS01MDAgZmxleC1zaHJpbmstMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA2djZoNC41bTQuNSAwYTkgOSAwIDExLTE4IDAgOSA5IDAgMDExOCAweiIgLz48L3N2Zz4="
class="w-4 h-4 text-orange-500 flex-shrink-0" />
<span class="text-sm font-medium text-orange-700">Awaiting internal
review</span>

</div>

{% elif post.status == 'pending_client' %}

<div class="flex items-center gap-2 px-3 py-2 rounded-lg bg-amber-50 border border-amber-100 mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LWFtYmVyLTUwMCBmbGV4LXNocmluay0wIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDZ2Nmg0LjVtNC41IDBhOSA5IDAgMTEtMTggMCA5IDkgMCAwMTE4IDB6IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-amber-500 flex-shrink-0" />
<span class="text-sm font-medium text-amber-700">Awaiting client
approval</span>

</div>

{% elif post.status == 'changes_requested' %}

<div class="flex items-center gap-2 px-3 py-2 rounded-lg bg-orange-50 border border-orange-100 mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LW9yYW5nZS01MDAgZmxleC1zaHJpbmstMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNi44NjIgNC40ODdsMS42ODctMS42ODhhMS44NzUgMS44NzUgMCAxMTIuNjUyIDIuNjUyTDEwLjU4MiAxNi4wN2E0LjUgNC41IDAgMDEtMS44OTcgMS4xM0w2IDE4bC44LTIuNjg1YTQuNSA0LjUgMCAwMTEuMTMtMS44OTdsOC45MzItOC45MzF6IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-orange-500 flex-shrink-0" />
<span class="text-sm font-medium text-orange-700">Changes requested -
edit and resubmit</span>

</div>

{% elif post.status == 'rejected' %}

<div class="flex items-center gap-2 px-3 py-2 rounded-lg bg-red-50 border border-red-100 mb-3">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXJlZC01MDAgZmxleC1zaHJpbmstMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-4 h-4 text-red-500 flex-shrink-0" />
<span class="text-sm font-medium text-red-700">Rejected - edit and
resubmit or delete</span>

</div>

{% endif %} {% if can_approve and post.status in
'pending_review,pending_client' %}

<div class="flex gap-2 mb-3" x-data="{ showReviewComment: false }">

{% csrf_token %}

Approve

Request Changes

<div class="absolute mt-9 z-10 bg-white rounded-lg shadow-lg border border-stone-200 p-3 w-80"
x-show="showReviewComment" x-cloak="">

{% csrf_token %}

Submit

</div>

</div>

{% endif %}

#### Approval History

<div class="space-y-2 mb-4">

{% for action in approval_history %}

<div class="flex items-start gap-2">

<div class="w-1.5 h-1.5 rounded-full mt-1.5 flex-shrink-0 {% if action.action == 'approved' %}bg-emerald-400{% elif action.action == 'rejected' %}bg-red-400{% elif action.action == 'changes_requested' %}bg-amber-400{% else %}bg-stone-300{% endif %}">

</div>

<div>

<span class="font-semibold">{{ action.user.display_name }}</span> {{
action.get_action_display\|lower }}

{% if action.comment %}

"{{ action.comment\|truncatechars:80 }}"

{% endif %}

{{ action.created_at\|timesince }} ago

</div>

</div>

{% endfor %}

</div>

{% if post_comments or post %}

#### Comments

<div id="composer-comments">

{% include "approvals/partials/comment_list.html" with
comments=post_comments post=post %}

</div>

<div class="mt-3">

{% include "approvals/partials/comment_form.html" with post=post
workspace=workspace %}

</div>

{% endif %}

</div>

{% endif %}

<div id="autosave-trigger"
hx-post="{% if post %}{% url 'composer:autosave_edit' workspace_id=workspace.id post_id=post.id %}{% else %}{% url 'composer:autosave' workspace_id=workspace.id %}{% endif %}"
hx-trigger="every 30s" hx-target="#autosave-status"
hx-include="#composer-form" hx-swap="innerHTML" style="display:none;">

</div>

</div>

<div class="panel-right-backdrop" x-show="showPreviewPanel" x-cloak=""
@click="showPreviewPanel = false"
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0"
x-transition:enter-end="opacity-100"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="opacity-100"
x-transition:leave-end="opacity-0">

</div>

<div class="panel-right border-l border-stone-200 bg-stone-50 lg:bg-stone-50 flex flex-col"
:class="{ 'is-open': showPreviewPanel }">

<div class="px-4 py-3 border-b border-stone-100 flex items-center justify-between">

### Preview

<div class="flex items-center gap-2">

<span class="text-xs text-stone-400 tabular-nums"
x-show="selectedAccounts.length &gt; 0"
x-text="selectedAccounts.length + (selectedAccounts.length === 1 ? ' platform' : ' platforms')">
</span>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-4 h-4" />

</div>

</div>

<div id="preview-panel"
class="flex-1 overflow-y-auto p-4 space-y-4 panel-scroll"
hx-get="{% url 'composer:preview' workspace_id=workspace.id %}"
hx-trigger="previewUpdate from:body" hx-include="#composer-form"
hx-vals="js:{&quot;title&quot;: document.querySelector(&quot;input[name=title]&quot;)?.value || &quot;&quot;, &quot;caption&quot;: document.querySelector(&quot;[name=caption]&quot;)?.value || &quot;&quot;, &quot;selected_accounts&quot;: document.querySelector(&quot;[name=selected_accounts]&quot;)?.value || &quot;&quot;, &quot;_autosave_post_id&quot;: document.querySelector(&quot;[name=_autosave_post_id]&quot;)?.value || &quot;&quot;}">

{% include "composer/partials/preview_panel.html" %}

</div>

</div>

</div>

<div class="fixed inset-0 z-[60] flex items-center justify-center"
x-show="showMediaPicker" x-cloak=""
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0"
x-transition:enter-end="opacity-100"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="opacity-100"
x-transition:leave-end="opacity-0">

<div class="absolute inset-0 bg-stone-900/40 backdrop-blur-sm"
@click="showMediaPicker = false">

</div>

<div class="relative bg-white rounded-2xl shadow-xl border border-stone-200 w-[calc(100vw-1rem)] sm:w-[640px] mx-2 sm:mx-0 max-h-[85vh] sm:max-h-[70vh] overflow-hidden"
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100">

<div class="px-4 sm:px-6 py-4 border-b border-stone-100 flex items-center justify-between">

## Media Library

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-4 h-4" />

</div>

<div class="p-4 sm:p-6 overflow-y-auto max-h-[calc(85vh-72px)] sm:max-h-[calc(70vh-72px)]"
hx-get="{% if post %}{% url 'composer:media_picker_post' workspace_id=workspace.id post_id=post.id %}{% else %}{% url 'composer:media_picker' workspace_id=workspace.id %}{% endif %}"
hx-trigger="intersect once" hx-swap="innerHTML">

<div class="flex items-center justify-center py-12 text-stone-400">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSBhbmltYXRlLXNwaW4iIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjbGFzcz0ib3BhY2l0eS0yNSIgY3g9IjEyIiBjeT0iMTIiIHI9IjEwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSI0Ij48L2NpcmNsZT48cGF0aCBjbGFzcz0ib3BhY2l0eS03NSIgZmlsbD0iY3VycmVudENvbG9yIiBkPSJNNCAxMmE4IDggMCAwMTgtOFYwQzUuMzczIDAgMCA1LjM3MyAwIDEyaDR6IiAvPjwvc3ZnPg=="
class="w-5 h-5 animate-spin" />

</div>

</div>

</div>

</div>

<div class="fixed inset-0 z-[60] flex items-center justify-center"
x-show="showThumbnailPicker" x-cloak=""
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0"
x-transition:enter-end="opacity-100"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="opacity-100"
x-transition:leave-end="opacity-0">

<div class="absolute inset-0 bg-stone-900/40 backdrop-blur-sm"
@click="showThumbnailPicker = false">

</div>

<div class="relative bg-white rounded-2xl shadow-xl border border-stone-200 w-[calc(100vw-1rem)] sm:w-[640px] mx-2 sm:mx-0 max-h-[85vh] sm:max-h-[70vh] overflow-hidden">

<div class="px-4 sm:px-6 py-4 border-b border-stone-100 flex items-center justify-between">

## Select Thumbnail

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-4 h-4" />

</div>

<div class="p-4 sm:p-6 overflow-y-auto max-h-[calc(85vh-72px)] sm:max-h-[calc(70vh-72px)]"
x-init="$watch('showThumbnailPicker', v =&gt; { if (v) htmx.ajax('GET', '{% url "
composer:thumbnail_picker"="" workspace_id="workspace.id" %}',="" {=""
target:="" $el,="" swap:="" 'innerhtml'="" })="" })"="">

<div class="flex items-center justify-center py-12 text-stone-400">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSBhbmltYXRlLXNwaW4iIGZpbGw9Im5vbmUiIHZpZXdib3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjbGFzcz0ib3BhY2l0eS0yNSIgY3g9IjEyIiBjeT0iMTIiIHI9IjEwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSI0Ij48L2NpcmNsZT48cGF0aCBjbGFzcz0ib3BhY2l0eS03NSIgZmlsbD0iY3VycmVudENvbG9yIiBkPSJNNCAxMmE4IDggMCAwMTgtOFYwQzUuMzczIDAgMCA1LjM3MyAwIDEyaDR6IiAvPjwvc3ZnPg=="
class="w-5 h-5 animate-spin" />

</div>

</div>

</div>

</div>

<div class="toast-saved" x-show="showSaveToast" x-cloak=""
x-transition:enter="transition ease-out duration-300"
x-transition:enter-start="opacity-0 translate-y-4"
x-transition:enter-end="opacity-100 translate-y-0"
x-transition:leave="transition ease-in duration-200"
x-transition:leave-start="opacity-100 translate-y-0"
x-transition:leave-end="opacity-0 translate-y-4">

<span class="flex items-center gap-1.5"> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgdGV4dC1lbWVyYWxkLTQwMCIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTE2LjcwNyA1LjI5M2ExIDEgMCAwMTAgMS40MTRsLTggOGExIDEgMCAwMS0xLjQxNCAwbC00LTRhMSAxIDAgMDExLjQxNC0xLjQxNEw4IDEyLjU4Nmw3LjI5My03LjI5M2ExIDEgMCAwMTEuNDE0IDB6IiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIC8+PC9zdmc+"
class="w-3.5 h-3.5 text-emerald-400" /> Post saved </span>

</div>

<div class="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 px-4 py-2.5 rounded-xl text-sm font-medium shadow-lg"
x-show="formError" x-cloak=""
style="background: var(--error-500, #EF4444); color: white;"
x-transition:enter="transition ease-out duration-300"
x-transition:enter-start="opacity-0 translate-y-4"
x-transition:enter-end="opacity-100 translate-y-0"
x-transition:leave="transition ease-in duration-200"
x-transition:leave-start="opacity-100 translate-y-0"
x-transition:leave-end="opacity-0 translate-y-4">

<span class="flex items-center gap-1.5"> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTIgOXYybTAgNGguMDFtLTYuOTM4IDRoMTMuODU2YzEuNTQgMCAyLjUwMi0xLjY2NyAxLjczMi0zTDEzLjczMiA0Yy0uNzctMS4zMzMtMi42OTQtMS4zMzMtMy40NjQgMEwzLjM0IDE2Yy0uNzcgMS4zMzMuMTkyIDMgMS43MzIgM3oiIC8+PC9zdmc+"
class="w-3.5 h-3.5" /> <span x-text="formError"></span> </span>

</div>

{% if is_edit %}

<div x-data="{ showDeleteModal: false, deleting: false }"
style="display: contents;"
@open-delete-modal.window="showDeleteModal = true">

<div class="fixed inset-0 z-[60] flex items-center justify-center"
x-show="showDeleteModal" x-cloak=""
@keydown.escape.window="showDeleteModal = false">

<div class="fixed inset-0 bg-black/30 backdrop-blur-sm"
@click="showDeleteModal = false" x-show="showDeleteModal"
x-transition:enter="transition ease-out duration-150"
x-transition:enter-start="opacity-0"
x-transition:enter-end="opacity-100"
x-transition:leave="transition ease-in duration-100"
x-transition:leave-start="opacity-100"
x-transition:leave-end="opacity-0">

</div>

<div class="relative bg-white rounded-2xl shadow-xl border border-stone-200 p-6 w-full max-w-sm mx-4"
x-show="showDeleteModal"
x-transition:enter="transition ease-out duration-150"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-100"
x-transition:leave-start="opacity-100 scale-100"
x-transition:leave-end="opacity-0 scale-95">

<div class="text-center">

<div class="w-12 h-12 mx-auto rounded-full bg-red-50 flex items-center justify-center mb-4">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiB0ZXh0LXJlZC01MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA3bC0uODY3IDEyLjE0MkEyIDIgMCAwMTE2LjEzOCAyMUg3Ljg2MmEyIDIgMCAwMS0xLjk5NS0xLjg1OEw1IDdtNSA0djZtNC02djZtMS0xMFY0YTEgMSAwIDAwLTEtMWgtNGExIDEgMCAwMC0xIDF2M000IDdoMTYiIC8+PC9zdmc+"
class="w-6 h-6 text-red-500" />

</div>

### Delete post?

This action cannot be undone. The post and all associated data will be
permanently removed.

</div>

<div class="flex gap-3">

Cancel

{ deleting = false; }); " :class="deleting && 'opacity-50
cursor-not-allowed'" class="flex-1 px-4 py-2 text-sm font-semibold
text-white bg-red-500 rounded-full hover:bg-red-600 transition-colors
cursor-pointer"\>
<span x-text="deleting ? 'Deleting...' : 'Delete'"></span>

</div>

</div>

</div>

</div>

{% endif %}

</div>

{% endblock %} {% block extra_js %}

{% endblock %}
