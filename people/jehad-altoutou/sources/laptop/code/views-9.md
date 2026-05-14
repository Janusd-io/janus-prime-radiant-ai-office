---
type: source
source_type: laptop
title: views
slug: views-9
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/settings_manager/views.py
original_size: 199
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# views

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/settings_manager/views.py` on 2026-05-14._

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def settings_index(request):
    return render(request, "settings_manager/index.html")

```