---
type: source
source_type: laptop
title: published
slug: published
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/published.html
original_size: 2927
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
---

# published

_Extracted from `brightbean-studio/templates/client_portal/published.html` on 2026-05-14._

{% extends "client_portal/portal_base.html" %} {% load humanize %} {%
block title %}Published Content - {{ workspace.name }}{% endblock %} {%
block content %}

<div>

<div class="mb-6">

# Published Content

Posts that have been published to your social channels

</div>

<div class="space-y-3">

{% for post in posts %}

<div class="rounded-xl border p-5 transition-all hover:shadow-md"
style="background: var(--surface-0); border-color: var(--border);">

<div class="flex items-start gap-4">

{% with first_media=post.media_attachments.first %} {% if first_media
and first_media.media_asset.thumbnail %}
<img src="%7B%7B%20first_media.media_asset.thumbnail.url%20%7D%7D"
class="w-16 h-16 rounded-lg object-cover flex-shrink-0"
style="border: 1px solid var(--border);" /> {% endif %} {% endwith %}

<div class="flex-1 min-w-0">

<div class="flex items-center gap-2 mb-1">

{% for pp in post.platform_posts.all %}
<span class="text-[0.6875rem] font-semibold px-2 py-0.5 rounded-full"
style="background: var(--surface-2); color: var(--text-secondary);"> {{
pp.social_account.get_platform_display }} </span> {% endfor %}
<span class="text-[0.6875rem] ml-auto flex-shrink-0"
style="color: var(--text-tertiary);"> {{ post.published_at\|date:"M j,
Y" }} </span>

</div>

{{ post.caption_snippet }}

</div>

</div>

</div>

{% empty %}

<div class="text-center py-16">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibXgtYXV0byB3LTE0IGgtMTQgbWItMyIgc3R5bGU9ImNvbG9yOiB2YXIoLS1uZXV0cmFsLTMwMCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjEuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTIgNy41aDEuNW0tMS41IDNoMS41bS03LjUgM2g3LjVtLTcuNSAzaDcuNW0zLTloMy4zNzVjLjYyMSAwIDEuMTI1LjUwNCAxLjEyNSAxLjEyNVYxOGEyLjI1IDIuMjUgMCAwMS0yLjI1IDIuMjVNMTYuNSA3LjVWMThhMi4yNSAyLjI1IDAgMDAyLjI1IDIuMjVNMTYuNSA3LjVWNC44NzVjMC0uNjIxLS41MDQtMS4xMjUtMS4xMjUtMS4xMjVINC4xMjVDMy41MDQgMy43NSAzIDQuMjU0IDMgNC44NzVWMThhMi4yNSAyLjI1IDAgMDAyLjI1IDIuMjVoMTMuNU02IDcuNWgzdjNINnYtM3oiIC8+PC9zdmc+"
class="mx-auto w-14 h-14 mb-3" />

No published posts yet

Published content will appear here

</div>

{% endfor %}

</div>

</div>

{% endblock %}
