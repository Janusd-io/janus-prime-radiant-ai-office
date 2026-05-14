---
type: source
source_type: laptop
title: _account_card
slug: account-card
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/social_accounts/partials/_account_card.html
original_size: 6064
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _account_card

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/social_accounts/partials/_account_card.html` on 2026-05-14._

{% comment %} Single connected account card - HTMX-swappable. Usage: {%
include "social_accounts/partials/\_account_card.html" with
account=account workspace_id=workspace_id %} {% endcomment %} {% load
social_accounts_tags %}

<div id="account-{{ account.id }}"
class="group relative bg-white rounded-xl border border-stone-200 p-5 transition-all duration-200 hover:shadow">

<div class="flex items-start gap-4">

<div class="flex-shrink-0">

{% if account.avatar_url %}
<img src="%7B%7B%20account.avatar_url%20%7D%7D"
class="w-11 h-11 rounded-full object-cover ring-2 ring-stone-100"
alt="{{ account.account_name|default:account.account_handle }}" /> {%
else %}

<div class="w-11 h-11 rounded-full bg-stone-100 flex items-center justify-center text-stone-400">

{% include "social_accounts/partials/\_platform_icon.html" with
platform=account.platform size="5" %}

</div>

{% endif %}

</div>

<div class="flex-1 min-w-0">

<div class="flex items-center gap-2 mb-1">

### {{ account.account_name\|default:account.account_handle }}

<span class="flex-shrink-0 text-stone-400"> {% include
"social_accounts/partials/\_platform_icon.html" with
platform=account.platform size="4" %} </span>

</div>

{% if account.account_handle %}

@{{ account.account_handle\|cut:"@" }}

{% endif %}

<div class="flex items-center gap-3 mt-2">

{% include "social_accounts/partials/\_status_badge.html" with
status=account.connection_status error=account.last_error %} {% if
account.follower_count %} <span class="text-xs text-stone-400">{{
account.follower_count\|format_number }} followers</span> {% endif %}

</div>

</div>

<div class="flex items-center gap-2"
x-data="{ confirmDisconnect: false }">

{% if account.needs_reconnect %}

{% csrf_token %}

Reconnect

{% endif %}

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-4 h-4" />

<div class="absolute right-4 top-12 z-10 w-64 bg-white rounded-xl shadow-xl border border-stone-200 p-4"
x-show="confirmDisconnect" x-cloak=""
@click.away="confirmDisconnect = false">

Disconnect **{{ account.account_name\|default:account.account_handle
}}**? Historical data will be preserved.

<div class="flex gap-2 justify-end">

Cancel

{% csrf_token %}

<img
src="data:image/svg+xml;base64,PHN2ZyB4LXNob3c9ImRpc2Nvbm5lY3RpbmciIGNsYXNzPSJhbmltYXRlLXNwaW4gaC0zIHctMyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJub25lIiB2aWV3Ym94PSIwIDAgMjQgMjQiPjxjaXJjbGUgY2xhc3M9Im9wYWNpdHktMjUiIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iNCI+PC9jaXJjbGU+PHBhdGggY2xhc3M9Im9wYWNpdHktNzUiIGZpbGw9ImN1cnJlbnRDb2xvciIgZD0iTTQgMTJhOCA4IDAgMDE4LThWMEM1LjM3MyAwIDAgNS4zNzMgMCAxMmg0eiIgLz48L3N2Zz4="
class="animate-spin h-3 w-3" />
<span x-text="disconnecting ? 'Disconnecting…' : 'Disconnect'">Disconnect</span>

</div>

</div>

</div>

</div>

{% if account.last_error and account.connection_status == "error" %}

<div class="mt-3 px-3 py-2 bg-red-50 rounded-lg">

{{ account.last_error }}

</div>

{% endif %} {% if account.connection_status == "connected" %}

<div class="border-t border-stone-100 mt-4 pt-4">

<div class="mb-3">

#### Posting Schedule

Set recurring time slots for when queued posts are automatically
published.

</div>

{% include "social_accounts/partials/\_posting_slots_grid.html" with
account=account workspace_id=workspace_id %}

</div>

{% endif %}

</div>
