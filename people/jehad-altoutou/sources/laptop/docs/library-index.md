---
type: source
source_type: laptop
title: library_index
slug: library-index
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/library_index.html
original_size: 20761
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# library_index

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/library_index.html` on 2026-05-14._

{% extends "layouts/workspace_settings.html" %} {% load static %} {%
block title %}Media Library - {{ workspace.name }}{% endblock %} {%
block extra_head %} <style>
  /* ── Media Library Tokens (inherit from brand) ── */
  .ml-dropzone {
    border: 2px dashed var(--border, #E7E5E4);
    border-radius: var(--radius-xl, 0.75rem);
    transition: border-color var(--dur-base, 200ms) var(--ease-out, ease),
                background var(--dur-base, 200ms) var(--ease-out, ease);
  }
  .ml-dropzone.drag-over {
    border-color: var(--primary, #F97316);
    background: var(--primary-soft, #FFF7ED);
  }
  .ml-asset-card {
    background: var(--surface-0, #FFF);
    border: 1px solid var(--border, #E7E5E4);
    border-radius: var(--radius-xl, 0.75rem);
    transition: all var(--dur-base, 200ms) var(--ease-out, ease);
  }
  .ml-asset-card:hover {
    box-shadow: var(--shadow-lg, 0 10px 15px rgba(23,20,18,0.08));
    border-color: transparent;
    transform: translateY(-2px);
  }
  .ml-folder-item {
    transition: all var(--dur-fast, 150ms) ease;
  }
  .ml-folder-item:hover { background: var(--surface-1, #FAFAF9); }
  .ml-folder-item.active {
    background: var(--primary-soft, #FFF7ED);
    color: var(--brand-700, #C2410C);
    font-weight: 600;
  }
  .ml-sidebar {
    background: var(--surface-0, #FFF);
    border-right: 1px solid var(--border, #E7E5E4);
  }
  .ml-filter-pill {
    font-size: 0.75rem;
    font-weight: 600;
    padding: 5px 12px;
    border-radius: 9999px;
    border: 1px solid var(--border, #E7E5E4);
    background: var(--surface-0, #FFF);
    color: var(--text-secondary, #57534E);
    cursor: pointer;
    transition: all var(--dur-fast, 150ms) ease;
  }
  .ml-filter-pill:hover { border-color: var(--border-hover, #D6D3D1); }
  .ml-filter-pill.active {
    background: var(--primary, #F97316);
    color: var(--text-inverse, #FFF);
    border-color: var(--primary, #F97316);
  }
  .ml-progress-bar {
    background: var(--surface-2, #F5F5F4);
    border-radius: 9999px;
    overflow: hidden;
    height: 4px;
  }
  .ml-progress-fill {
    height: 100%;
    background: var(--primary, #F97316);
    border-radius: 9999px;
    transition: width 150ms ease;
  }
  .ml-detail-overlay {
    background: rgba(23, 20, 18, 0.3);
    backdrop-filter: blur(4px);
  }
  .ml-type-badge {
    font-size: 9px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 2px 6px;
    border-radius: var(--radius-sm, 0.25rem);
  }
  .ml-thumb-placeholder {
    background: [[linear|linear]]-gradient(135deg, var(--surface-2, #F5F5F4) 0%, var(--surface-1, #FAFAF9) 100%);
  }
  @keyframes ml-shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
  }
  .ml-shimmer {
    background: linear-gradient(90deg, var(--surface-2, #F5F5F4) 25%, var(--surface-1, #FAFAF9) 50%, var(--surface-2, #F5F5F4) 75%);
    background-size: 200% 100%;
    animation: ml-shimmer 1.5s ease infinite;
  }
</style> {% endblock %} {% block page_title %}Media Library{% endblock
%} {% block content %}

<div class="flex flex-1 min-h-0 -m-3 sm:-m-4 lg:-m-6 -mb-3 sm:-mb-4 lg:-mb-6"
x-data="{ ...mediaLibrary(), folderSidebarOpen: false }">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTQgNmEyIDIgMCAwMTItMmgybDIgMmg2YTIgMiAwIDAxMiAydjJNNCA2djEwYTIgMiAwIDAwMiAyaDEyYTIgMiAwIDAwMi0yVjEwYTIgMiAwIDAwLTItMkg0eiIgLz48L3N2Zz4="
class="w-4 h-4" /> Folders

<div class="fixed inset-0 bg-black/30 z-40 lg:hidden"
x-show="folderSidebarOpen" x-cloak="" @click="folderSidebarOpen = false"
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0"
x-transition:enter-end="opacity-100"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="opacity-100"
x-transition:leave-end="opacity-0">

</div>

<div class="ml-sidebar w-56 flex-shrink-0 flex flex-col overflow-y-auto rounded-tl-xl rounded-bl-xl fixed inset-y-0 left-0 z-50 transition-transform duration-200 lg:relative lg:z-auto lg:translate-x-0"
:class="folderSidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'"
@click="if (window.innerWidth &lt; 1024 &amp;&amp; $event.target.closest('a')) { folderSidebarOpen = false }">

<div class="p-4">

<div class="flex items-center justify-between mb-3">

<span class="text-xs font-bold uppercase tracking-wider"
style="color: var(--text-tertiary, #78716C);">Folders</span>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" />

</div>

<a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D"
class="ml-folder-item flex items-center gap-2 px-3 py-2 rounded-lg text-sm cursor-pointer {% if not current_folder %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBmbGV4LXNocmluay0wIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMS41IiBkPSJNNCA2YTIgMiAwIDAxMi0yaDJsMiAyaDZhMiAyIDAgMDEyIDJ2Mk00IDZ2MTBhMiAyIDAgMDAyIDJoMTJhMiAyIDAgMDAyLTJWMTBhMiAyIDAgMDAtMi0ySDR6IiAvPjwvc3ZnPg=="
class="w-4 h-4 flex-shrink-0" /> All Media</a> <a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D?starred=1"
class="ml-folder-item flex items-center gap-2 px-3 py-2 rounded-lg text-sm cursor-pointer {% if is_starred %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBmbGV4LXNocmluay0wIiBmaWxsPSJ7JSBpZiBpc19zdGFycmVkICV9Y3VycmVudENvbG9yeyUgZWxzZSAlfW5vbmV7JSBlbmRpZiAlfSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTExLjA0OSAyLjkyN2MuMy0uOTIxIDEuNjAzLS45MjEgMS45MDIgMGwxLjUxOSA0LjY3NGExIDEgMCAwMC45NS42OWg0LjkxNWMuOTY5IDAgMS4zNzEgMS4yNC41ODggMS44MWwtMy45NzYgMi44ODhhMSAxIDAgMDAtLjM2MyAxLjExOGwxLjUxOCA0LjY3NGMuMy45MjItLjc1NSAxLjY4OC0xLjUzOCAxLjExOGwtMy45NzYtMi44ODhhMSAxIDAgMDAtMS4xNzYgMGwtMy45NzYgMi44ODhjLS43ODMuNTctMS44MzgtLjE5Ny0xLjUzOC0xLjExOGwxLjUxOC00LjY3NGExIDEgMCAwMC0uMzYzLTEuMTE4bC0zLjk3Ni0yLjg4OGMtLjc4NC0uNTctLjM4LTEuODEuNTg4LTEuODFoNC45MTRhMSAxIDAgMDAuOTUxLS42OWwxLjUxOS00LjY3NHoiIC8+PC9zdmc+"
class="w-4 h-4 flex-shrink-0" /> Starred</a>

<div class="my-3 border-t"
style="border-color: var(--surface-2, #F5F5F4);">

</div>

<div id="folder-tree"
hx-get="{% url 'media_library:index' workspace_id=workspace.id %}folders/create/"
hx-trigger="folderUpdated from:body" hx-target="#folder-tree">

{% include "media_library/\_folder_tree.html" %}

</div>

<div class="mt-2" x-show="showNewFolder" x-cloak="">

{% include "media_library/\_folder_form.html" %}

</div>

</div>

</div>

<div class="flex-1 flex flex-col overflow-hidden">

<div class="flex flex-wrap items-center gap-2 sm:gap-3 px-3 sm:px-4 lg:px-6 py-3 border-b rounded-tr-xl"
style="border-color: var(--border, #E7E5E4); background: var(--surface-0, #FFF);">

<div class="relative flex-1 min-w-[160px] sm:max-w-sm">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYWJzb2x1dGUgbGVmdC0zIHRvcC0xLzIgLXRyYW5zbGF0ZS15LTEvMiB3LTQgaC00IiBzdHlsZT0iY29sb3I6IHZhcigtLXRleHQtZ2hvc3QsICNBOEEyOUUpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0yMSAyMWwtNi02bTItNWE3IDcgMCAxMS0xNCAwIDcgNyAwIDAxMTQgMHoiIC8+PC9zdmc+"
class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4" />

</div>

<div class="flex items-center gap-1.5 overflow-x-auto flex-nowrap">

<a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D%7B%%20if%20current_folder%20%%7D?folder=%7B%7B%20current_folder%20%7D%7D%7B%%20endif%20%%7D"
class="ml-filter-pill {% if not current_type %}active{% endif %}">All</a>
{% for type_val, type_label in file_types %} <a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D?type=%7B%7B%20type_val%20%7D%7D%7B%%20if%20current_folder%20%%7D&amp;folder=%7B%7B%20current_folder%20%7D%7D%7B%%20endif%20%%7D"
class="ml-filter-pill {% if current_type == type_val %}active{% endif %}">{{
type_label }}</a> {% endfor %}

</div>

<div class="flex-1">

</div>

Newest first Oldest first Name A-Z Name Z-A Largest first Smallest first

<div class="flex border rounded-lg overflow-hidden"
style="border-color: var(--border, #E7E5E4);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGQ9Ik01IDNhMiAyIDAgMDAtMiAydjJhMiAyIDAgMDAyIDJoMmEyIDIgMCAwMDItMlY1YTIgMiAwIDAwLTItMkg1ek01IDExYTIgMiAwIDAwLTIgMnYyYTIgMiAwIDAwMiAyaDJhMiAyIDAgMDAyLTJ2LTJhMiAyIDAgMDAtMi0ySDV6TTExIDVhMiAyIDAgMDEyLTJoMmEyIDIgMCAwMTIgMnYyYTIgMiAwIDAxLTIgMmgtMmEyIDIgMCAwMS0yLTJWNXpNMTEgMTNhMiAyIDAgMDEyLTJoMmEyIDIgMCAwMTIgMnYyYTIgMiAwIDAxLTIgMmgtMmEyIDIgMCAwMS0yLTJ2LTJ6IiAvPjwvc3ZnPg=="
class="w-4 h-4" />

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjAgMjAiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTMgNGExIDEgMCAwMTEtMWgxMmExIDEgMCAxMTAgMkg0YTEgMSAwIDAxLTEtMXptMCA0YTEgMSAwIDAxMS0xaDEyYTEgMSAwIDExMCAySDRhMSAxIDAgMDEtMS0xem0wIDRhMSAxIDAgMDExLTFoMTJhMSAxIDAgMTEwIDJINGExIDEgMCAwMS0xLTF6bTAgNGExIDEgMCAwMTEtMWgxMmExIDEgMCAxMTAgMkg0YTEgMSAwIDAxLTEtMXoiIGNsaXAtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4="
class="w-4 h-4" />

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> Upload

</div>

<div class="mx-3 sm:mx-4 lg:mx-6 mt-4" x-show="uploading || dragOver"
x-cloak="" @dragover.prevent="dragOver = true"
@dragleave.prevent="dragOver = false"
@drop.prevent="handleDrop($event)">

<div class="ml-dropzone p-8 text-center cursor-pointer"
:class="{ 'drag-over': dragOver }" role="button" tabindex="0"
@click="if (!uploading) $refs.fileInput.click()"
@keydown.enter.prevent="if (!uploading) $refs.fileInput.click()"
@keydown.space.prevent="if (!uploading) $refs.fileInput.click()">

<div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0xMCBoLTEwIG14LWF1dG8gbWItMyIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0LCAjQThBMjlFKTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik03IDE2YTQgNCAwIDAxLS44OC03LjkwM0E1IDUgMCAxMTE1LjkgNkwxNiA2YTUgNSAwIDAxMSA5LjlNMTUgMTNsLTMtM20wIDBsLTMgM20zLTN2MTIiIC8+PC9zdmc+"
class="w-10 h-10 mx-auto mb-3" />

Drop files here to upload

Images up to 20MB, videos up to 1GB

</div>

<div class="space-y-2 max-w-md mx-auto text-left">

<div class="flex items-center gap-3 py-1.5">

<div class="w-8 h-8 rounded-lg flex items-center justify-center text-xs font-bold"
:style="'background: var(--surface-2, #F5F5F4); color: var(--text-tertiary, #78716C);'">

<span x-text="file.name.split('.').pop().toUpperCase().slice(0,3)"></span>

</div>

<div class="flex-1 min-w-0">

<div class="ml-progress-bar mt-1">

<div class="ml-progress-fill"
:style="'width: ' + (file.progress || 0) + '%'">

</div>

</div>

</div>

<span class="text-xs font-semibold" x-show="file.status === 'complete'"
style="color: var(--success-500, #22C55E);">Done</span>
<span class="text-xs font-semibold" x-show="file.status === 'error'"
style="color: var(--error-500, #EF4444);"
x-text="file.error || 'Failed'"></span>

</div>

</div>

</div>

</div>

<div class="flex-1 overflow-y-auto px-3 sm:px-4 lg:px-6 py-4"
@dragover.prevent="dragOver = true"
@dragleave.self.prevent="dragOver = false"
@drop.prevent="handleDrop($event)">

<div id="asset-grid">

{% include "media_library/\_asset_grid.html" %}

</div>

</div>

</div>

<div class="fixed inset-0 z-50 flex justify-end" x-show="detailOpen"
x-cloak="" @keydown.escape.window="detailOpen = false">

<div class="ml-detail-overlay absolute inset-0"
@click="detailOpen = false" x-show="detailOpen"
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="opacity-0"
x-transition:enter-end="opacity-100"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="opacity-100"
x-transition:leave-end="opacity-0">

</div>

<div id="detail-panel"
class="relative w-full sm:max-w-lg bg-white shadow-xl overflow-y-auto"
x-show="detailOpen"
x-transition:enter="transition ease-out duration-250"
x-transition:enter-start="translate-x-full"
x-transition:enter-end="translate-x-0"
x-transition:leave="transition ease-in duration-200"
x-transition:leave-start="translate-x-0"
x-transition:leave-end="translate-x-full">

</div>

</div>

</div>

{% endblock %} {% block extra_js %}

{% endblock %}
