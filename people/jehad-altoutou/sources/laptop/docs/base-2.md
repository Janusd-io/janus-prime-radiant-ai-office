---
type: source
source_type: laptop
title: base
slug: base-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/allauth/layouts/base.html
original_size: 618
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---

# base

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/allauth/layouts/base.html` on 2026-05-14._

{% extends "base.html" %} {% block html_style %}{% endblock %} {% block
title %}{% block head_title %}{% endblock %} - Brightbean{% endblock %}
{% block auth_content %}

<div class="auth-card">

{% if messages %}

<div class="mb-6 space-y-2">

{% for message in messages %}

<div class="{% if message.tags == 'error' %}alert-error{% elif message.tags == 'success' %}alert-success{% else %}alert-info{% endif %}">

{{ message }}

</div>

{% endfor %}

</div>

{% endif %} {% block content %}{% endblock %}

</div>

{% endblock %} {% block extra_body %}{% endblock %}
