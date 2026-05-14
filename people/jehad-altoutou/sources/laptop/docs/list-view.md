---
type: source
source_type: laptop
title: list_view
slug: list-view
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/list_view.html
original_size: 4219
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# list_view

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/calendar/partials/list_view.html` on 2026-05-14._

{% comment %} List view - table format of posts. Context: posts,
workspace. {% endcomment %}

<div class="bg-white overflow-x-auto"
style="animation: slideUp 200ms cubic-bezier(0.16,1,0.3,1) both">

{% if posts %}

Status

</div>

Date

Caption

Platforms

Author

{% for post in posts %}

<span class="post-chip status-{{ post.status }} inline-flex">
<span class="chip-dot"></span> {{ post.get_status_display }} </span>

{% if post.scheduled_at %} {{ post.scheduled_at\|date:"M d, Y" }}\
<span class="text-stone-400">{{ post.scheduled_at\|date:"H:i" }}</span>
{% else %} <span class="text-stone-300">Not scheduled</span> {% endif %}

{{ post.caption_snippet\|default:"(no caption)" }}

<div class="flex gap-1">

{% for pp in post.platform_posts.all %}
<span class="w-5 h-5 rounded-[5px] flex items-center justify-center"> {%
include "partials/\_platform_icon.html" with
platform=pp.social_account.platform size="sm" %} </span> {% endfor %}

</div>

{{ post.author.display_name\|default:"-" }}

{% endfor %}

{% else %} {% if not has_connected_accounts %} {% include
"calendar/partials/\_no_channels_empty_state.html" %} {% else %}

<div class="text-center py-20 px-6">

<div class="w-16 h-16 mx-auto rounded-2xl bg-stone-100 flex items-center justify-center mb-4">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy03IGgtNyB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTggN1YzbTggNFYzbS05IDhoMTBNNSAyMWgxNGEyIDIgMCAwMDItMlY3YTIgMiAwIDAwLTItMkg1YTIgMiAwIDAwLTIgMnYxMmEyIDIgMCAwMDIgMnoiIC8+PC9zdmc+"
class="w-7 h-7 text-stone-300" />

</div>

No content scheduled yet

Create your first post to see it on the calendar

<a
href="%7B%%20url%20&#39;composer:compose&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 px-5 py-1.5 text-sm font-semibold text-orange-600 bg-orange-50 border border-orange-200 rounded-full hover:bg-orange-100 hover:border-orange-300 active:bg-orange-100 transition-all duration-150"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> Create Post</a>

</div>

{% endif %} {% endif %}
