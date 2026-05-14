---
type: source
source_type: laptop
title: publish_approvals
slug: publish-approvals
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/publish_approvals.html
original_size: 12145
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
---

# publish_approvals

_Extracted from `brightbean-studio/templates/calendar/partials/publish_approvals.html` on 2026-05-14._

{% comment %} Approvals tab partial for the Publish page. Shows pending
approval platform posts with filter sub-tabs. Loaded via HTMX into
\#tab-content. All members can view; action buttons shown conditionally
based on can_approve permission. {% endcomment %}

<div x-data="{ selectedPosts: [], showBulkBar: false }"
x-effect="showBulkBar = selectedPosts.length &gt; 0"
style="animation: slideUp 200ms cubic-bezier(0.16,1,0.3,1) both">

<div class="flex flex-wrap gap-1.5 mb-5">

All <span class="ml-1 opacity-75">{{
pending_review_count\|add:pending_client_count\|add:approved_count\|add:rejected_count\|add:changes_requested_count
}}</span>

Pending Review <span class="ml-1 opacity-75">{{ pending_review_count
}}</span>

Pending Client <span class="ml-1 opacity-75">{{ pending_client_count
}}</span>

Approved <span class="ml-1 opacity-75">{{ approved_count }}</span>

Rejected <span class="ml-1 opacity-75">{{ rejected_count }}</span>

Changes Requested <span class="ml-1 opacity-75">{{
changes_requested_count }}</span>

</div>

<div id="approval-list" class="space-y-3">

{% for pp in platform_posts %}

<div class="bg-white rounded-xl border border-stone-200 p-4 hover:border-stone-300 transition-colors">

<div class="flex items-center gap-3">

{% if can_approve %}

{% endif %} {% with first_att=pp.post.media_attachments.all.0 %} {% if
first_att %}

<div class="w-12 h-12 rounded-lg overflow-hidden bg-stone-100 flex-shrink-0 relative">

{% if first_att.media_asset.thumbnail %}
<img src="%7B%7B%20first_att.media_asset.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover" /> {% elif
first_att.media_asset.media_type == 'image' or
first_att.media_asset.media_type == 'gif' %}
<img src="%7B%7B%20first_att.media_asset.file.url%20%7D%7D"
class="w-full h-full object-cover" /> {% else %}

<div class="w-full h-full flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTE0Ljc1MiAxMS4xNjhsLTMuMTk3LTIuMTMyQTEgMSAwIDAwMTAgOS44N3Y0LjI2M2ExIDEgMCAwMDEuNTU1LjgzMmwzLjE5Ny0yLjEzMmExIDEgMCAwMDAtMS42NjR6IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-stone-300" />

</div>

{% endif %} {% if first_att.media_asset.media_type == 'video' and
first_att.media_asset.thumbnail %}

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-5 h-5 rounded-full bg-black/50 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUgdGV4dC13aGl0ZSBtbC0wLjUiIGZpbGw9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNNSAzbDE0IDktMTQgOVYzeiIgLz48L3N2Zz4="
class="w-2.5 h-2.5 text-white ml-0.5" />

</div>

</div>

{% endif %} {% if pp.post.media_attachments.count \> 1 %}

<div class="absolute bottom-0 right-0 bg-black/60 text-white text-[9px] font-bold px-1 rounded-tl">

+{{ pp.post.media_attachments.count\|add:"-1" }}

</div>

{% endif %}

</div>

{% endif %} {% endwith %}

<div class="flex-1 min-w-0">

<div class="flex items-center gap-2 mb-1">

<span class="post-chip status-{{ pp.status }} inline-flex">
<span class="chip-dot"></span> {{ pp.post.get_status_display }} </span>
<span class="w-5 h-5 rounded-[5px] flex items-center justify-center"> {%
include "partials/\_platform_icon.html" with
platform=pp.social_account.platform size="sm" %} </span>
<span class="text-xs text-stone-500">{{
pp.social_account.account_name\|default:pp.social_account.account_handle
}}</span> {% if pp.post.scheduled_at %}
<span class="text-xs text-stone-400 tabular-nums">{{
pp.post.scheduled_at\|date:"M d, Y H:i" }}</span> {% endif %}

</div>

<a
href="%7B%%20url%20&#39;composer:compose_edit&#39;%20workspace_id=workspace.id%20post_id=pp.post_id%20%%7D?account=%7B%7B%20pp.social_account_id%20%7D%7D"
class="text-sm text-stone-700 hover:text-stone-900 line-clamp-1">{{
pp.post.title|default:pp.post.caption_snippet|default:"(no caption)"
}}</a>

by {{ pp.post.author.display_name\|default:"Unknown" }}

</div>

{% if can_approve %}

<div class="flex items-center gap-2 flex-shrink-0">

{% csrf_token %}

Approve

<a
href="%7B%%20url%20&#39;composer:compose_edit&#39;%20workspace_id=workspace.id%20post_id=pp.post_id%20%%7D?account=%7B%7B%20pp.social_account_id%20%7D%7D"
class="px-3 py-1.5 text-xs font-semibold rounded-full border border-stone-200 text-stone-600 hover:border-stone-300 transition-colors">Review</a>

</div>

{% endif %}

</div>

</div>

{% empty %}

<div class="text-center py-16">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibXgtYXV0byB3LTEyIGgtMTIgdGV4dC1zdG9uZS0zMDAgbWItMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTkgMTIuNzVMMTEuMjUgMTUgMTUgOS43NU0yMSAxMmE5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="mx-auto w-12 h-12 text-stone-300 mb-3" />

No posts pending approval

Posts submitted for review will appear here

</div>

{% endfor %}

</div>

{% if can_approve %}

<div class="fixed bottom-6 left-1/2 -translate-x-1/2 z-40"
x-show="showBulkBar" x-cloak=""
x-transition:enter="transition ease-out duration-200"
x-transition:enter-start="translate-y-full opacity-0"
x-transition:enter-end="translate-y-0 opacity-100"
x-transition:leave="transition ease-in duration-150"
x-transition:leave-start="translate-y-0 opacity-100"
x-transition:leave-end="translate-y-full opacity-0">

<div class="flex items-center gap-3 px-5 py-3 bg-stone-900 text-white rounded-2xl shadow-xl">

<span class="text-sm font-medium"
x-text="selectedPosts.length + ' selected'"></span>

<div class="w-px h-5 bg-stone-700">

</div>

{% csrf_token %}

<div class="flex items-center gap-2">

Approve All

Reject All

</div>

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-4 h-4" />

</div>

</div>

{% endif %}

</div>
