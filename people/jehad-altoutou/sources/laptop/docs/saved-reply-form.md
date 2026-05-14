---
type: source
source_type: laptop
title: _saved_reply_form
slug: saved-reply-form
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/partials/_saved_reply_form.html
original_size: 1353
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:38Z"
---

# _saved_reply_form

_Extracted from `brightbean-studio/templates/inbox/partials/_saved_reply_form.html` on 2026-05-14._

<div class="max-w-lg">

{% csrf_token %}

<div class="space-y-4">

<div>

Title {{ form.title }}

</div>

<div>

Reply Body {{ form.body }}

Variables: `{sender_name}`, `{account_name}`, `{post_url}`

</div>

</div>

<div class="flex items-center gap-3 mt-6">

{% if saved_reply %}Update{% else %}Create{% endif %} Reply

<a
href="%7B%%20url%20&#39;inbox:saved_replies&#39;%20workspace_id=workspace.id%20%%7D"
class="text-[13px] font-medium text-stone-500 hover:text-stone-700 transition-colors">Cancel</a>

</div>

</div>
