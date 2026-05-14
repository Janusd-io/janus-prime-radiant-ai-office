---
type: source
source_type: laptop
title: _reply_item
slug: reply-item
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_reply_item.html
original_size: 1024
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
---

# _reply_item

_Extracted from `brightbean-studio/templates/inbox/partials/_reply_item.html` on 2026-05-14._

{% load humanize %}

<div class="flex gap-2.5 items-start">

<div class="w-7 h-7 rounded-full flex items-center justify-center text-[10px] font-bold text-white flex-shrink-0"
style="background: var(--primary);">

{{ reply.author.email\|make_list\|first\|upper }}

</div>

<div class="flex-1 min-w-0">

<div class="bg-white border border-stone-200 rounded-xl rounded-tl-sm px-3.5 py-2.5"
style="box-shadow: var(--shadow-xs);">

<div class="flex items-center gap-2 mb-1">

<span class="text-[12px] font-semibold text-stone-800">{{
reply.author.get_short_name\|default:reply.author.email }}</span>
<span class="badge-pill"
style="background: var(--primary-soft); color: var(--brand-700);">Reply</span>
<span class="text-[11px] text-stone-400 ml-auto">{{
reply.sent_at\|timesince }} ago</span>

</div>

{{ reply.body }}

</div>

</div>

</div>
