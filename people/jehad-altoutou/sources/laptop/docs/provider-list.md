---
type: source
source_type: laptop
title: provider_list
slug: provider-list
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/allauth/elements/provider_list.html
original_size: 293
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:39Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# provider_list

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/allauth/elements/provider_list.html` on 2026-05-14._

{% load allauth socialaccount %} {% get_providers as
socialaccount_providers %} {% for provider in socialaccount_providers %}
{% provider_login_url provider process=process as href %} {% element
provider id=provider.id name=provider.name href=href %} {% endelement %}
{% endfor %}
