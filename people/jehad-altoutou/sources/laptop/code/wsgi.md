---
type: source
source_type: laptop
title: wsgi
slug: wsgi
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/config/wsgi.py
original_size: 178
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:36Z"
---

# wsgi

_Extracted from `brightbean-studio/config/wsgi.py` on 2026-05-14._

```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()

```