---
type: source
source_type: laptop
title: _message_panel
slug: message-panel
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_message_panel.html
original_size: 5643
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
project: brightbean-studio

---

# _message_panel

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/partials/_message_panel.html` on 2026-05-14._

{% load humanize %}

<div class="flex flex-col h-full">

<div class="px-5 py-4 border-b border-stone-100 flex-shrink-0">

<div class="flex items-start justify-between gap-4">

<div class="flex items-center gap-3 min-w-0">

{% if message.sender_avatar_url %}
<img src="%7B%7B%20message.sender_avatar_url%20%7D%7D"
class="w-10 h-10 rounded-full object-cover flex-shrink-0" /> {% else %}

<div class="w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold text-stone-500 flex-shrink-0"
style="background: var(--surface-2);">

{{ message.sender_name\|make_list\|first\|upper }}

</div>

{% endif %}

<div class="min-w-0">

<div class="flex items-center gap-2">

<span class="text-sm font-semibold text-stone-900">{{
message.sender_name }}</span> {% if message.sender_handle %}
<span class="text-[12px] text-stone-400">@{{ message.sender_handle
}}</span> {% endif %}

</div>

<div class="flex items-center gap-2 mt-0.5">

<div class="flex items-center gap-1">

{% include "partials/\_platform_icon.html" with
platform=message.social_account.platform size="sm" %}
<span class="text-[11px] text-stone-500">{{
message.social_account.account_name\|default:message.social_account.account_handle
}}</span>

</div>

<span class="text-[11px] text-stone-400">{{ message.received_at\|date:"N
j, Y g:i A" }}</span>

</div>

</div>

</div>

<div class="flex items-center gap-2 flex-shrink-0">

<div class="relative" x-data="{ statusOpen: false }">

{{ message.get_status_display }} <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0yLjUgaC0yLjUgbWwtMC41IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjMiPjxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTE5IDlsLTcgNy03LTciIC8+PC9zdmc+"
class="w-2.5 h-2.5 ml-0.5" />

<div class="absolute right-0 top-full mt-1 bg-white rounded-lg shadow-lg ring-1 ring-stone-200 py-1 z-50 min-w-[120px]"
x-show="statusOpen" @click.away="statusOpen = false" x-cloak=""
x-transition="">

{% for value, label in status_choices %}

{{ label }}

{% endfor %}

</div>

</div>

{% include "inbox/partials/\_assignment_dropdown.html" %}

</div>

</div>

</div>

<div class="flex-1 overflow-y-auto px-5 py-4">

<div class="bg-stone-50 rounded-xl p-4 mb-4 border border-stone-100">

<div class="flex items-center gap-2 mb-2">

<span class="badge-pill badge-type">{{ message.get_message_type_display
}}</span> {% include "inbox/partials/\_sentiment_badge.html" %} {% if
sla_config and sla_config.is_active and message.status != 'resolved' and
message.status != 'archived' %} {% include
"inbox/partials/\_sla_badge.html" %} {% endif %}

</div>

{{ message.body }}

</div>

<div id="inbox-thread" class="space-y-3">

{% for item_type, item, timestamp in thread %} {% if item_type ==
"reply" %} {% include "inbox/partials/\_reply_item.html" with reply=item
%} {% elif item_type == "note" %} {% include
"inbox/partials/\_note_item.html" with note=item %} {% endif %} {%
endfor %}

</div>

{% for child in child_messages %}

<div class="mt-3 pl-4 border-l-2 border-stone-200">

<div class="flex items-center gap-2 mb-1">

<span class="text-[12px] font-semibold text-stone-700">{{
child.sender_name }}</span> <span class="text-[11px] text-stone-400">{{
child.received_at\|timesince }} ago</span>

</div>

{{ child.body }}

</div>

{% endfor %}

</div>

{% include "inbox/partials/\_reply_composer.html" %}

</div>
