---
type: source
source_type: laptop
title: dashboard
slug: dashboard
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/client_portal/dashboard.html
original_size: 4639
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
---

# dashboard

_Extracted from `brightbean-studio/templates/client_portal/dashboard.html` on 2026-05-14._

{% extends "client_portal/portal_base.html" %} {% block title
%}Dashboard - {{ workspace.name }}{% endblock %} {% block content %}

<div>

<div class="mb-8">

# Welcome back

Here's what's happening with {{ workspace.name }}

</div>

<div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">

<a href="%7B%%20url%20&#39;client_portal:approval_queue&#39;%20%%7D"
class="rounded-xl border p-5 transition-all hover:shadow-lg hover:-translate-y-0.5"
style="background: var(--surface-0); border-color: var(--border);"></a>

<div class="flex items-center justify-between mb-3">

<div class="w-10 h-10 rounded-lg flex items-center justify-center"
style="background: var(--primary-soft);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgc3R5bGU9ImNvbG9yOiB2YXIoLS1wcmltYXJ5KTsiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTIgNnY2aDQuNW00LjUgMGE5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="w-5 h-5" />

</div>

{% if pending_count \> 0 %}
<span class="w-2.5 h-2.5 rounded-full animate-pulse"
style="background: var(--primary);"></span> {% endif %}

</div>

{{ pending_count }}

Posts awaiting your review

<a href="%7B%%20url%20&#39;client_portal:published&#39;%20%%7D"
class="rounded-xl border p-5 transition-all hover:shadow-lg hover:-translate-y-0.5"
style="background: var(--surface-0); border-color: var(--border);"></a>

<div class="w-10 h-10 rounded-lg flex items-center justify-center mb-3"
style="background: var(--success-50);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgc3R5bGU9ImNvbG9yOiB2YXIoLS1zdWNjZXNzLTUwMCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTkgMTIuNzVMMTEuMjUgMTUgMTUgOS43NU0yMSAxMmE5IDkgMCAxMS0xOCAwIDkgOSAwIDAxMTggMHoiIC8+PC9zdmc+"
class="w-5 h-5" />

</div>

{{ recent_published\|length }}

Recently published

<a href="%7B%%20url%20&#39;client_portal:activity&#39;%20%%7D"
class="rounded-xl border p-5 transition-all hover:shadow-lg hover:-translate-y-0.5"
style="background: var(--surface-0); border-color: var(--border);"></a>

<div class="w-10 h-10 rounded-lg flex items-center justify-center mb-3"
style="background: var(--info-50);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgc3R5bGU9ImNvbG9yOiB2YXIoLS1pbmZvLTUwMCk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTMuNzUgMTJoMTYuNW0tMTYuNSAzLjc1aDE2LjVNMy43NSAxOS41aDE2LjVNNS42MjUgNC41aDEyLjc1YTEuODc1IDEuODc1IDAgMDEwIDMuNzVINS42MjVhMS44NzUgMS44NzUgMCAwMTAtMy43NXoiIC8+PC9zdmc+"
class="w-5 h-5" />

</div>

{{ my_actions\|length }}

Recent actions

</div>

{% if pending_count \> 0 %}

<div class="rounded-xl border p-5"
style="background: var(--primary-soft); border-color: var(--primary-muted);">

<div class="flex items-center justify-between">

<div>

You have {{ pending_count }} post{{ pending_count\|pluralize }} waiting
for review

Review and approve content before it's published

</div>

<a href="%7B%%20url%20&#39;client_portal:approval_queue&#39;%20%%7D"
class="px-4 py-2 text-[0.8125rem] font-semibold rounded-full text-white transition-all hover:-translate-y-0.5"
style="background: var(--primary); box-shadow: var(--shadow-primary);">Review
Now</a>

</div>

</div>

{% endif %}

</div>

{% endblock %}
