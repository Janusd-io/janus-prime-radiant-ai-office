---
type: source
source_type: laptop
title: approval_queue
slug: approval-queue
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/approval_queue.html
original_size: 9799
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# approval_queue

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/client_portal/approval_queue.html` on 2026-05-14._

{% extends "client_portal/portal_base.html" %} {% block title %}Approve
Posts - {{ workspace.name }}{% endblock %} {% block content %}

<div hx-trigger="portalAction from:body"
hx-get="{% url 'client_portal:approval_queue' %}"
hx-target="#portal-posts" hx-select="#portal-posts" hx-swap="outerHTML">

<div class="mb-6">

# Posts for Review

Approve or request changes on scheduled content

</div>

<div id="portal-posts" class="space-y-4">

{% for post in posts %}

<div class="rounded-xl border overflow-hidden transition-all hover:shadow-md"
style="background: var(--surface-0); border-color: var(--border);"
x-data="{ showDetail: false, showRejectForm: false, showChangesForm: false }">

<div class="p-5 cursor-pointer" @click="showDetail = !showDetail">

<div class="flex items-center gap-2 mb-2">

{% for pp in post.platform_posts.all %}
<span class="text-[0.6875rem] font-semibold px-2 py-0.5 rounded-full"
style="background: var(--surface-2); color: var(--text-secondary);"> {{
pp.social_account.get_platform_display }} </span> {% endfor %} {% if
post.scheduled_at %} <span class="text-[0.6875rem] ml-auto"
style="color: var(--text-tertiary);"> Scheduled for {{
post.scheduled_at\|date:"M j, Y \a\t g:i A" }} </span> {% endif %}

</div>

{{ post.caption }}

{% if post.media_attachments.all %}

<div class="flex gap-2 mt-3 flex-wrap">

{% for pm in post.media_attachments.all %} {% if
pm.media_asset.thumbnail %}
<img src="%7B%7B%20pm.media_asset.thumbnail.url%20%7D%7D"
class="w-20 h-20 rounded-lg object-cover"
style="border: 1px solid var(--border);" alt="{{ pm.alt_text }}" /> {%
elif pm.media_asset.file %}

<div class="w-20 h-20 rounded-lg flex items-center justify-center"
style="background: var(--surface-1); border: 1px solid var(--border);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy02IGgtNiIgc3R5bGU9ImNvbG9yOiB2YXIoLS10ZXh0LWdob3N0KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0yLjI1IDE1Ljc1bDUuMTU5LTUuMTU5YTIuMjUgMi4yNSAwIDAxMy4xODIgMGw1LjE1OSA1LjE1OW0tMS41LTEuNWwxLjQwOS0xLjQwOWEyLjI1IDIuMjUgMCAwMTMuMTgyIDBsMi45MDkgMi45MDlNMy43NSAyMWgxNi41QTIuMjUgMi4yNSAwIDAwMjIuNSAxOC43NVY1LjI1QTIuMjUgMi4yNSAwIDAwMjAuMjUgM0gzLjc1QTIuMjUgMi4yNSAwIDAwMS41IDUuMjV2MTMuNUEyLjI1IDIuMjUgMCAwMDMuNzUgMjF6IiAvPjwvc3ZnPg=="
class="w-6 h-6" />

</div>

{% endif %} {% endfor %}

</div>

{% endif %}

<div class="flex items-center gap-1.5 mt-3">

<span class="text-[0.75rem]" style="color: var(--text-tertiary);">by {{
post.author.display_name }}</span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgbWwtYXV0byB0cmFuc2l0aW9uLXRyYW5zZm9ybSIgOmNsYXNzPSJzaG93RGV0YWlsICZhbXA7JmFtcDsgJiMzOTtyb3RhdGUtMTgwJiMzOTsiIHN0eWxlPSJjb2xvcjogdmFyKC0tdGV4dC1naG9zdCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE5IDlsLTcgNy03LTciIC8+PC9zdmc+"
class="w-3.5 h-3.5 ml-auto transition-transform" />

</div>

</div>

<div x-show="showDetail" x-cloak="" x-collapse="">

{% if post.visible_comments %}

<div class="px-5 pb-3 border-t" style="border-color: var(--surface-2);">

Comments

{% for comment in post.visible_comments %}

<div class="flex gap-2 mb-2">

<div class="w-6 h-6 rounded-full flex items-center justify-center text-[9px] font-bold text-white flex-shrink-0"
style="background: var(--primary);">

{{ comment.author.display_name\|default:"?"\|make_list\|first\|upper }}

</div>

<div>

<span class="text-[0.75rem] font-semibold"
style="color: var(--text-primary);">{{
comment.author.display_name\|default:"Unknown" }}</span>

{{ comment.body }}

</div>

</div>

{% endfor %}

</div>

{% endif %}

<div class="px-5 py-4 flex flex-wrap gap-2 border-t"
style="border-color: var(--surface-2); background: var(--surface-1);">

Approve

Request Changes

Reject

</div>

<div class="px-5 py-4 border-t" x-show="showChangesForm" x-cloak=""
x-collapse="" style="border-color: var(--surface-2);">

What changes would you like?

<div class="flex gap-2">

Submit Feedback

Cancel

</div>

</div>

<div class="px-5 py-4 border-t" x-show="showRejectForm" x-cloak=""
x-collapse="" style="border-color: var(--surface-2);">

Reason for rejection

<div class="flex gap-2">

Reject Post

Cancel

</div>

</div>

</div>

</div>

{% empty %}

<div class="text-center py-16">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ibXgtYXV0byB3LTE0IGgtMTQgbWItMyIgc3R5bGU9ImNvbG9yOiB2YXIoLS1uZXV0cmFsLTMwMCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjEuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNOSAxMi43NUwxMS4yNSAxNSAxNSA5Ljc1TTIxIDEyYTkgOSAwIDExLTE4IDAgOSA5IDAgMDExOCAweiIgLz48L3N2Zz4="
class="mx-auto w-14 h-14 mb-3" />

All caught up!

No posts are waiting for your review right now

</div>

{% endfor %}

</div>

</div>

{% endblock %}
