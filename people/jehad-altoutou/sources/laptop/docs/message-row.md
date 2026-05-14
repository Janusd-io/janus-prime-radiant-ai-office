---
type: source
source_type: laptop
title: _message_row
slug: message-row
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_message_row.html
original_size: 3448
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _message_row

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_message_row.html` on 2026-05-14._

{% load humanize %}

<div id="msg-{{ message.id }}"
class="inbox-row {% if message.status == 'unread' %}is-unread{% endif %}"
@click="selectMessage('{{ message.id }}', '{% url 'inbox:message_detail' workspace_id=workspace.id message_id=message.id %}')"
role="button" tabindex="0">

<div class="flex-shrink-0 pt-0.5" @click.stop="">

</div>

<div class="flex-shrink-0 pt-0.5">

{% include "partials/\_platform_icon.html" with
platform=message.social_account.platform size="sm" %}

</div>

<div class="flex-shrink-0">

{% if message.sender_avatar_url %}
<img src="%7B%7B%20message.sender_avatar_url%20%7D%7D"
class="w-8 h-8 rounded-full object-cover" /> {% else %}

<div class="w-8 h-8 rounded-full flex items-center justify-center text-[11px] font-bold text-stone-500"
style="background: var(--surface-2);">

{{ message.sender_name\|make_list\|first\|upper }}

</div>

{% endif %}

</div>

<div class="flex-1 min-w-0">

<div class="flex items-center gap-2 mb-0.5">

<span class="inbox-row-sender text-[13px] font-semibold text-stone-700 truncate">{{
message.sender_name }}</span> {% if message.sender_handle %}
<span class="text-[11px] text-stone-400 truncate">@{{
message.sender_handle }}</span> {% endif %}
<span class="text-[11px] text-stone-400 ml-auto flex-shrink-0"
title="{{ message.received_at|date:'N j, Y g:i A' }}">{{
message.received_at\|timesince }} ago</span>

</div>

{{ message.body\|truncatewords:20 }}

<div class="flex items-center gap-1.5 mt-1.5">

<span class="badge-pill badge-type">{{ message.get_message_type_display
}}</span> <span class="badge-pill badge-status-{{ message.status }}">{{
message.get_status_display }}</span> {% include
"inbox/partials/\_sentiment_badge.html" %} {% if message.assigned_to %}
<span class="badge-pill"
style="background: var(--accent-indigo-soft); color: var(--accent-indigo);">
<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMi41Ij48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xNiA3YTQgNCAwIDExLTggMCA0IDQgMCAwMTggMHpNMTIgMTRhNyA3IDAgMDAtNyA3aDE0YTcgNyAwIDAwLTctN3oiIC8+PC9zdmc+"
class="w-2.5 h-2.5" /> {{
message.assigned_to.get_short_name\|default:message.assigned_to.email\|truncatechars:10
}} </span> {% endif %} {% if sla_config and sla_config.is_active and
message.status != 'resolved' and message.status != 'archived' %}
<span class="sla-countdown ml-auto"
:class="getSlaClass('{{ message.received_at|date:'c' }}')"
x-text="formatSla('{{ message.received_at|date:'c' }}')"></span> {%
endif %}

</div>

</div>

</div>
