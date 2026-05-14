---
type: source
source_type: laptop
title: publish_queue
slug: publish-queue
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/publish_queue.html
original_size: 15301
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---

# publish_queue

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/calendar/partials/publish_queue.html` on 2026-05-14._

{% comment %} Queue tab partial for the Publish page. Shows all
scheduled platform posts grouped by date. Loaded via HTMX into
\#tab-content. {% endcomment %} {% load tz %}

<div style="animation: slideUp 200ms cubic-bezier(0.16,1,0.3,1) both">

{% if platform_posts %} {% regroup platform_posts by effective_at.date
as date_groups %} {% for group in date_groups %}

<div class="{% if not forloop.first %}mt-8{% endif %}">

### {% timezone display_timezone %}{{ group.grouper\|date:"l, j F" }}{% endtimezone %}

<div class="space-y-4">

{% for pp in group.list %}

<div class="flex gap-4">

<div class="w-20 shrink-0 pt-3 text-right">

<div class="text-sm font-semibold text-stone-700 tabular-nums">

{% timezone display_timezone %}{{ pp.effective_at\|date:"g:i A" }}{%
endtimezone %}

</div>

<div class="text-[11px] text-stone-400 mt-0.5 flex items-center justify-end gap-1">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xMiA4djRsMyAzbTYtM2E5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="w-3 h-3" /> {% if pp.post.queue_entries.exists %}Queue{% else
%}Custom{% endif %}

</div>

</div>

<div class="flex-1 bg-white rounded-xl border border-stone-200 hover:border-stone-300 transition-colors group">

<div class="p-4 cursor-pointer"
onclick="window.location='{% url 'composer:compose_edit' workspace_id=workspace.id post_id=pp.post_id %}?account={{ pp.social_account_id }}'">

<div class="flex items-center gap-2 mb-2">

<span class="w-6 h-6 rounded-md flex items-center justify-center"> {%
include "partials/\_platform_icon.html" with
platform=pp.social_account.platform size="sm" %} </span>
<span class="text-sm font-semibold text-stone-800"> {{
pp.social_account.account_name\|default:pp.social_account.account_handle
}} </span>

</div>

{{ pp.post.title\|default:pp.post.caption_snippet\|default:"(no
caption)" }}

{% if pp.post.media_attachments.exists %}

<div class="flex gap-1.5 mt-2.5">

{% for att in pp.post.media_attachments.all\|slice:":4" %}

<div class="w-12 h-12 rounded-lg overflow-hidden bg-stone-100 flex-shrink-0 relative">

{% if att.media_asset.thumbnail %}
<img src="%7B%7B%20att.media_asset.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover" /> {% elif att.media_asset.media_type
== 'image' or att.media_asset.media_type == 'gif' %}
<img src="%7B%7B%20att.media_asset.file.url%20%7D%7D"
class="w-full h-full object-cover" /> {% else %}

{% endif %} {% if att.media_asset.media_type == 'video' %}

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-5 h-5 rounded-full bg-black/50 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUgdGV4dC13aGl0ZSBtbC0wLjUiIGZpbGw9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNNSAzbDE0IDktMTQgOVYzeiIgLz48L3N2Zz4="
class="w-2.5 h-2.5 text-white ml-0.5" />

</div>

</div>

{% endif %}

</div>

{% endfor %} {% with extra=pp.post.media_attachments.count %} {% if
extra \> 4 %}

<div class="w-12 h-12 rounded-lg bg-stone-100 flex items-center justify-center flex-shrink-0">

<span class="text-xs font-semibold text-stone-400">+{{ extra\|add:"-4"
}}</span>

</div>

{% endif %} {% endwith %}

</div>

{% endif %}

</div>

<div class="flex items-center justify-between border-t border-stone-100 px-4 py-2.5">

<span class="text-xs text-stone-400"> {{ pp.post.created_at\|timesince
}} ago </span>

<div class="flex items-center gap-1.5">

<a
href="%7B%%20url%20&#39;composer:compose_edit&#39;%20workspace_id=workspace.id%20post_id=pp.post_id%20%%7D?account=%7B%7B%20pp.social_account_id%20%7D%7D&amp;action=publish_now"
class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-full border border-stone-200 text-stone-600 hover:border-stone-300 hover:text-stone-800 transition-colors"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgcm90YXRlLTkwIiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDE5bDkgMi05LTE4LTkgMTggOS0yem0wIDB2LTgiIC8+PC9zdmc+"
class="w-3.5 h-3.5 rotate-90" /> Publish</a>

<div class="relative" x-data="{ open: false, menuStyle: {} }"
@click.outside="open = false" @scroll.window="open = false"
@keydown.escape.window="open = false">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDIwIDIwIj48Y2lyY2xlIGN4PSIxMCIgY3k9IjQiIHI9IjEuNSI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iMTAiIGN5PSIxMCIgcj0iMS41Ij48L2NpcmNsZT48Y2lyY2xlIGN4PSIxMCIgY3k9IjE2IiByPSIxLjUiPjwvY2lyY2xlPjwvc3ZnPg=="
class="w-3.5 h-3.5" />

<div class="w-36 bg-white rounded-xl border border-stone-200 shadow-lg py-1"
x-show="open" :style="menuStyle" @click.outside="open = false"
x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
x-transition:leave-start="opacity-100 scale-100"
x-transition:leave-end="opacity-0 scale-95">

<a
href="%7B%%20url%20&#39;composer:compose_edit&#39;%20workspace_id=workspace.id%20post_id=pp.post_id%20%%7D?account=%7B%7B%20pp.social_account_id%20%7D%7D"
class="flex items-center gap-2 px-3 py-2 text-sm text-stone-700 hover:bg-stone-50 transition-colors"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTQwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNS4yMzIgNS4yMzJsMy41MzYgMy41MzZtLTIuMDM2LTUuMDM2YTIuNSAyLjUgMCAxMTMuNTM2IDMuNTM2TDYuNSAyMS4wMzZIM3YtMy41NzJMMTYuNzMyIDMuNzMyeiIgLz48L3N2Zz4="
class="w-4 h-4 text-stone-400" /> Edit</a>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSA3bC0uODY3IDEyLjE0MkEyIDIgMCAwMTE2LjEzOCAyMUg3Ljg2MmEyIDIgMCAwMS0xLjk5NS0xLjg1OEw1IDdtNSA0djZtNC02djZtMS0xMFY0YTEgMSAwIDAwLTEtMWgtNGExIDEgMCAwMC0xIDF2M000IDdoMTYiIC8+PC9zdmc+"
class="w-4 h-4" /> Delete

</div>

</div>

</div>

</div>

</div>

</div>

{% endfor %}

</div>

</div>

{% endfor %} {% else %} {% if not has_connected_accounts %} {% include
"calendar/partials/\_no_channels_empty_state.html" %} {% else %}

<div class="text-center py-20 px-6">

<div class="w-16 h-16 mx-auto rounded-2xl bg-stone-100 flex items-center justify-center mb-4">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy03IGgtNyB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTEyIDh2NGwzIDNtNi0zYTkgOSAwIDExLTE4IDAgOSA5IDAgMDExOCAweiIgLz48L3N2Zz4="
class="w-7 h-7 text-stone-300" />

</div>

No queued posts

Queued posts will appear here when you queue them

<a
href="%7B%%20url%20&#39;composer:compose&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-5 py-1.5 text-sm font-semibold text-orange-600 bg-orange-50 border border-orange-200 rounded-full hover:bg-orange-100 hover:border-orange-300 active:bg-orange-100 transition-all duration-150"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> Create Post</a>

</div>

{% endif %} {% endif %}

</div>

<div x-data="{ showDeleteModal: false, deletePostId: null, deleteAccountId: null, deleting: false }"
style="display: contents;"
@open-delete-modal.window="showDeleteModal = true; deletePostId = $event.detail.postId; deleteAccountId = $event.detail.accountId || null">

<div class="fixed inset-0 z-[60] flex items-center justify-center"
x-show="showDeleteModal"
@keydown.escape.window="showDeleteModal = false" style="display: none;">

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

<span x-text="deleting ? 'Deleting...' : 'Delete'"></span>

</div>

</div>

</div>

</div>
