---
type: source
source_type: laptop
title: account_select
slug: account-select
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/social_accounts/account_select.html
original_size: 4409
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# account_select

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/social_accounts/account_select.html` on 2026-05-14._

{% extends "base.html" %} {% block page_title %}Select Account{%
endblock %} {% block content %}

<div class="max-w-2xl">

<div class="mb-8">

<div class="mx-auto w-12 h-12 rounded-xl bg-blue-50 flex items-center justify-center mb-4">

{% include "social_accounts/partials/\_platform_icon.html" with
platform=platform size="6" %}

</div>

## Select Account{{ pages\|length\|pluralize }}

Your {{ platform\|title }} login has access to multiple accounts. Select
which one{{ pages\|length\|pluralize }} to connect.

</div>

{% csrf_token %}

<div class="space-y-3 mb-8">

{% for page in pages %}

{% if page.picture %} <img src="%7B%7B%20page.picture%20%7D%7D"
class="w-10 h-10 rounded-full object-cover ring-2 ring-stone-100"
alt="{{ page.name }}" /> {% else %}

<div class="w-10 h-10 rounded-full bg-stone-100 flex items-center justify-center text-stone-400">

{% include "social_accounts/partials/\_platform_icon.html" with
platform=platform size="5" %}

</div>

{% endif %}

<div class="flex-1 min-w-0">

### {{ page.name }}

{% if page.category %}

{{ page.category }}

{% endif %}

</div>

{% if page.followers_count %} <span class="text-xs text-stone-400">{{
page.followers_count }} followers</span> {% endif %} {% endfor %}

</div>

<div class="flex items-center gap-3">

<span id="connect-btn-text">Connect Selected</span> <img
src="data:image/svg+xml;base64,PHN2ZyBpZD0iY29ubmVjdC1idG4tY2hlY2siIGNsYXNzPSJ3LTQgaC00IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMiIgZD0iTTUgMTNsNCA0TDE5IDciIC8+PC9zdmc+"
id="connect-btn-check" class="w-4 h-4" /> <img
src="data:image/svg+xml;base64,PHN2ZyBpZD0iY29ubmVjdC1idG4tc3Bpbm5lciIgY2xhc3M9InctNCBoLTQgYW5pbWF0ZS1zcGluIGhpZGRlbiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJub25lIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxjaXJjbGUgY2xhc3M9Im9wYWNpdHktMjUiIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iNCI+PC9jaXJjbGU+PHBhdGggY2xhc3M9Im9wYWNpdHktNzUiIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTQgMTJhOCA4IDAgMDE4LThWMEM1LjM3MyAwIDAgNS4zNzMgMCAxMmg0em0yIDUuMjkxQTcuOTYyIDcuOTYyIDAgMDE0IDEySDBjMCAzLjA0MiAxLjEzNSA1LjgyNCAzIDcuOTM4bDMtMi42NDd6IiAvPjwvc3ZnPg=="
id="connect-btn-spinner" class="w-4 h-4 animate-spin hidden" />

<a
href="%7B%%20url%20&#39;social_accounts:list&#39;%20workspace_id=workspace_id%20%%7D"
class="px-4 py-2.5 text-sm font-semibold text-stone-600 hover:text-stone-800 transition-colors">Cancel</a>

</div>

</div>

{% endblock %}
