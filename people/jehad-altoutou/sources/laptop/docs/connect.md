---
type: source
source_type: laptop
title: connect
slug: connect
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/social_accounts/connect.html
original_size: 5580
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
---

# connect

_Extracted from `brightbean-studio/templates/social_accounts/connect.html` on 2026-05-14._

{% extends "base.html" %} {% block page_title %}Connect Social Account{%
endblock %} {% block content %}

<div class="max-w-4xl">

<div class="mb-8">

<a
href="%7B%%20url%20&#39;social_accounts:list&#39;%20workspace_id=workspace_id%20%%7D"
class="inline-flex items-center gap-1.5 text-sm text-stone-500 hover:text-stone-700 transition-colors mb-4"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xNSAxOWwtNy03IDctNyIgLz48L3N2Zz4="
class="w-4 h-4" /> Back to Social Accounts</a>

## Connect a Platform

Select a platform to connect your social media account.

</div>

<div class="overflow-y-auto pr-1">

<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">

{% for value, label in platform_choices %}

<div class="relative bg-white rounded-xl border border-stone-200 p-5 transition-all duration-200 {% if value in configured_platforms %}{% else %}opacity-60{% endif %}">

<div class="flex items-start gap-4">

<div class="flex-shrink-0 w-10 h-10 rounded-lg flex items-center justify-center {% if value == 'facebook' %}bg-blue-50 text-blue-600 {% elif value == 'instagram' %}bg-gradient-to-br from-purple-50 to-pink-50 text-pink-600 {% elif value == 'linkedin_personal' %}bg-blue-50 text-blue-700 {% elif value == 'linkedin_company' %}bg-blue-50 text-blue-700 {% elif value == 'tiktok' %}bg-stone-900 text-white {% elif value == 'youtube' %}bg-red-50 text-red-600 {% elif value == 'pinterest' %}bg-red-50 text-red-500 {% elif value == 'threads' %}bg-stone-100 text-stone-800 {% elif value == 'bluesky' %}bg-sky-50 text-sky-500 {% elif value == 'google_business' %}bg-blue-50 text-blue-500 {% elif value == 'mastodon' %}bg-indigo-50 text-indigo-600 {% endif %}">

{% include "social_accounts/partials/\_platform_icon.html" with
platform=value size="5" %}

</div>

<div class="flex-1 min-w-0">

### {{ label }}

{% if value == 'facebook' %}Pages & Groups {% elif value == 'instagram'
%}Business & Creator {% elif value == 'linkedin_personal' %}Personal
profile {% elif value == 'linkedin_company' %}Company pages {% elif
value == 'tiktok' %}Video content {% elif value == 'youtube' %}Videos &
Shorts {% elif value == 'pinterest' %}Pins & Boards {% elif value ==
'threads' %}Text & Media {% elif value == 'bluesky' %}AT Protocol {%
elif value == 'google_business' %}Local posts {% elif value ==
'mastodon' %}Federated social {% endif %}

</div>

</div>

{% if value in configured_platforms %}

{% csrf_token %}

Connect <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTQgNWw3IDdtMCAwbC03IDdtNy03SDMiIC8+PC9zdmc+"
class="w-3.5 h-3.5" />

{% else %}

<div class="mt-4">

<a href="%7B%%20url%20&#39;credentials:list&#39;%20%%7D"
class="w-full inline-flex items-center justify-center gap-2 px-4 py-1.5 text-xs font-semibold text-stone-600 bg-stone-50 border border-stone-200 rounded-full hover:bg-stone-100 hover:border-stone-300 transition-all duration-200"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTAuMzI1IDQuMzE3Yy40MjYtMS43NTYgMi45MjQtMS43NTYgMy4zNSAwYTEuNzI0IDEuNzI0IDAgMDAyLjU3MyAxLjA2NmMxLjU0My0uOTQgMy4zMS44MjYgMi4zNyAyLjM3YTEuNzI0IDEuNzI0IDAgMDAxLjA2NiAyLjU3M2MxLjc1Ni40MjYgMS43NTYgMi45MjQgMCAzLjM1YTEuNzI0IDEuNzI0IDAgMDAtMS4wNjYgMi41NzNjLjk0IDEuNTQzLS44MjYgMy4zMS0yLjM3IDIuMzdhMS43MjQgMS43MjQgMCAwMC0yLjU3MyAxLjA2NmMtLjQyNiAxLjc1Ni0yLjkyNCAxLjc1Ni0zLjM1IDBhMS43MjQgMS43MjQgMCAwMC0yLjU3My0xLjA2NmMtMS41NDMuOTQtMy4zMS0uODI2LTIuMzctMi4zN2ExLjcyNCAxLjcyNCAwIDAwLTEuMDY2LTIuNTczYy0xLjc1Ni0uNDI2LTEuNzU2LTIuOTI0IDAtMy4zNWExLjcyNCAxLjcyNCAwIDAwMS4wNjYtMi41NzNjLS45NC0xLjU0My44MjYtMy4zMSAyLjM3LTIuMzcuOTk2LjYwOCAyLjI5Ni4wNyAyLjU3Mi0xLjA2NXoiIC8+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMyI+PC9jaXJjbGU+PC9zdmc+"
class="w-3.5 h-3.5" /> Set Up Credentials</a>

</div>

{% endif %}

</div>

{% endfor %}

</div>

</div>

</div>

{% endblock %}
