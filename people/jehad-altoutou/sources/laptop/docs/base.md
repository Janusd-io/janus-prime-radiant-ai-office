---
type: source
source_type: laptop
title: Brightbean Studio — base
slug: base
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/base.html
original_size: 86252
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# base

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/base.html` on 2026-05-14._

<div class="lg:border lg:border-stone-200 lg:m-2.5 bg-white lg:rounded-xl flex-1 p-3 sm:p-4 lg:p-6 overflow-y-auto flex flex-col"
role="main">

{% block page_header %}{% endblock %} {% if messages %}

<div class="mb-4 space-y-2">

{% for message in messages %}

<div class="rounded-md p-4 {% if message.tags == 'error' %}bg-red-50 text-red-800{% elif message.tags == 'success' %}bg-green-50 text-green-800{% else %}bg-blue-50 text-blue-800{% endif %}">

{{ message }}

</div>

{% endfor %}

</div>

{% endif %}

<div class="flex-1 min-h-0 flex flex-col overflow-y-auto overflow-x-hidden">

{% block content %}{% endblock %}

</div>

</div>

<div class="auth-bg min-h-screen flex items-center justify-center py-12 px-4"
role="main" style="font-family: var(--font-body);">

{% block auth_content %}{% endblock %}

</div>
