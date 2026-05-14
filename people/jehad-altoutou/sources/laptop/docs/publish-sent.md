---
type: source
source_type: laptop
title: publish_sent
slug: publish-sent
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/publish_sent.html
original_size: 6294
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---

# publish_sent

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/calendar/partials/publish_sent.html` on 2026-05-14._

{% comment %} Sent tab partial for the Publish page. Shows all
published/partially_published platform posts. Loaded via HTMX into
\#tab-content. {% endcomment %}

<div style="animation: slideUp 200ms cubic-bezier(0.16,1,0.3,1) both">

{% if platform_posts %}

Media

</div>

Status

Published

Caption

Platform

Author

{% for pp in platform_posts %}

{% with first_att=pp.post.media_attachments.all.0 %} {% if first_att %}

<div class="w-10 h-10 rounded-lg overflow-hidden bg-stone-100 flex-shrink-0 relative">

{% if first_att.media_asset.thumbnail %}
<img src="%7B%7B%20first_att.media_asset.thumbnail.url%20%7D%7D"
class="w-full h-full object-cover" /> {% elif
first_att.media_asset.media_type == 'image' or
first_att.media_asset.media_type == 'gif' %}
<img src="%7B%7B%20first_att.media_asset.file.url%20%7D%7D"
class="w-full h-full object-cover" /> {% else %}

{% endif %} {% if first_att.media_asset.media_type == 'video' %}

<div class="absolute inset-0 flex items-center justify-center">

<div class="w-4 h-4 rounded-full bg-black/50 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yIGgtMiB0ZXh0LXdoaXRlIG1sLXB4IiBmaWxsPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTUgM2wxNCA5LTE0IDlWM3oiIC8+PC9zdmc+"
class="w-2 h-2 text-white ml-px" />

</div>

</div>

{% endif %} {% if pp.post.media_attachments.count \> 1 %}

<div class="absolute bottom-0 right-0 bg-black/60 text-white text-[9px] font-bold px-1 rounded-tl">

+{{ pp.post.media_attachments.count\|add:"-1" }}

</div>

{% endif %}

</div>

{% else %}

<div class="w-10 h-10 rounded-lg bg-stone-50 flex items-center justify-center">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCB0ZXh0LXN0b25lLTIwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTQgMTZsNC41ODYtNC41ODZhMiAyIDAgMDEyLjgyOCAwTDE2IDE2bS0yLTJsMS41ODYtMS41ODZhMiAyIDAgMDEyLjgyOCAwTDIwIDE0bS02LTZoLjAxTTYgMjBoMTJhMiAyIDAgMDAyLTJWNmEyIDIgMCAwMC0yLTJINmEyIDIgMCAwMC0yIDJ2MTJhMiAyIDAgMDAyIDJ6IiAvPjwvc3ZnPg=="
class="w-4 h-4 text-stone-200" />

</div>

{% endif %} {% endwith %}

<span class="post-chip status-{{ pp.status }} inline-flex">
<span class="chip-dot"></span> {{ pp.post.get_status_display }} </span>

{% if pp.post.scheduled_at %} {{ pp.post.scheduled_at\|date:"M d, Y" }}\
<span class="text-stone-400">{{ pp.post.scheduled_at\|date:"H:i"
}}</span> {% else %} <span class="text-stone-300">-</span> {% endif %}

{{ pp.post.title\|default:pp.post.caption_snippet\|default:"(no
caption)" }}

<div class="flex items-center gap-1.5">

<span class="w-5 h-5 rounded-[5px] flex items-center justify-center"> {%
include "partials/\_platform_icon.html" with
platform=pp.social_account.platform size="sm" %} </span>
<span class="text-xs text-stone-500">{{
pp.social_account.account_name\|default:pp.social_account.account_handle
}}</span>

</div>

{{ pp.post.author.display_name\|default:"-" }}

{% endfor %}

{% else %} {% if not has_connected_accounts %} {% include
"calendar/partials/\_no_channels_empty_state.html" %} {% else %}

<div class="text-center py-20 px-6">

<div class="w-16 h-16 mx-auto rounded-2xl bg-stone-100 flex items-center justify-center mb-4">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy03IGgtNyB0ZXh0LXN0b25lLTMwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTkgMTIuNzVMMTEuMjUgMTUgMTUgOS43NU0yMSAxMmE5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="w-7 h-7 text-stone-300" />

</div>

No sent posts yet

Published posts will appear here after they go live

</div>

{% endif %} {% endif %}
