---
type: source
source_type: laptop
title: list
slug: list
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/social_accounts/list.html
original_size: 3021
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# list

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/social_accounts/list.html` on 2026-05-14._

{% extends "layouts/workspace_settings.html" %} {% block page_title
%}Social Accounts{% endblock %} {% block content %}

<div class="max-w-4xl">

<div class="flex flex-wrap items-center justify-between gap-3 mb-6 sm:mb-8">

<div>

## Social Accounts

Manage connected social media accounts for this workspace.

</div>

<a
href="%7B%%20url%20&#39;social_accounts:connect&#39;%20workspace_id=workspace_id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-1.5 text-sm font-semibold text-orange-600 bg-orange-50 border border-orange-200 rounded-full hover:bg-orange-100 hover:border-orange-300 active:bg-orange-100 transition-all duration-150"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> Connect Account</a>

</div>

{% if accounts %}

<div id="accounts-list" class="space-y-3">

{% for account in accounts %} {% include
"social_accounts/partials/\_account_card.html" with account=account
workspace_id=workspace_id %} {% endfor %}

</div>

<div class="mt-6 pt-4 border-t border-stone-200">

{{ accounts\|length }} account{{ accounts\|length\|pluralize }}
connected. Health checks run automatically every 6 hours.

</div>

{% else %}

<div class="text-center py-16 px-6">

<div class="mx-auto w-16 h-16 rounded-2xl bg-orange-50 flex items-center justify-center mb-5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy04IGgtOCB0ZXh0LW9yYW5nZS00MDAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xMy44MjggMTAuMTcyYTQgNCAwIDAwLTUuNjU2IDBsLTQgNGE0IDQgMCAxMDUuNjU2IDUuNjU2bDEuMTAyLTEuMTAxbS0uNzU4LTQuODk5YTQgNCAwIDAwNS42NTYgMGw0LTRhNCA0IDAgMDAtNS42NTYtNS42NTZsLTEuMSAxLjEiIC8+PC9zdmc+"
class="w-8 h-8 text-orange-400" />

</div>

### No accounts connected yet

Connect your social media accounts to start publishing content, tracking
engagement, and managing your inbox.

<a
href="%7B%%20url%20&#39;social_accounts:connect&#39;%20workspace_id=workspace_id%20%%7D"
class="inline-flex items-center gap-1.5 px-4 py-1.5 text-sm font-semibold text-orange-600 bg-orange-50 border border-orange-200 rounded-full hover:bg-orange-100 hover:border-orange-300 active:bg-orange-100 transition-all duration-150"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xMiA0djE2bTgtOEg0IiAvPjwvc3ZnPg=="
class="w-4 h-4" /> Connect Your First Account</a>

</div>

{% endif %}

</div>

{% endblock %}
