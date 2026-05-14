---
type: source
source_type: laptop
title: f81f30aaae0cee48e9dae5cc853b997c9aa3ac5ee9fcd1704d2c5f925ff16f7b
slug: f81f30aaae0cee48e9dae5cc853b997c9aa3ac5ee9fcd1704d2c5f925ff16f7b
created: 2026-04-17
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/graphify-out/cache/f81f30aaae0cee48e9dae5cc853b997c9aa3ac5ee9fcd1704d2c5f925ff16f7b.json
original_size: 962
original_ext: .json
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:36Z"
---

# f81f30aaae0cee48e9dae5cc853b997c9aa3ac5ee9fcd1704d2c5f925ff16f7b

_Extracted from `brightbean-studio/graphify-out/cache/f81f30aaae0cee48e9dae5cc853b997c9aa3ac5ee9fcd1704d2c5f925ff16f7b.json` on 2026-05-14._

```json
{"nodes": [{"id": "apps_inbox_apps_py", "label": "apps.py", "file_type": "code", "source_file": "apps/inbox/apps.py", "source_location": "L1"}, {"id": "apps_inboxconfig", "label": "InboxConfig", "file_type": "code", "source_file": "apps/inbox/apps.py", "source_location": "L4"}, {"id": "appconfig", "label": "AppConfig", "file_type": "code", "source_file": "", "source_location": ""}], "edges": [{"source": "apps_inbox_apps_py", "target": "django_apps", "relation": "imports_from", "confidence": "EXTRACTED", "source_file": "apps/inbox/apps.py", "source_location": "L1", "weight": 1.0}, {"source": "apps_inbox_apps_py", "target": "apps_inboxconfig", "relation": "contains", "confidence": "EXTRACTED", "source_file": "apps/inbox/apps.py", "source_location": "L4", "weight": 1.0}, {"source": "apps_inboxconfig", "target": "appconfig", "relation": "inherits", "confidence": "EXTRACTED", "source_file": "apps/inbox/apps.py", "source_location": "L4", "weight": 1.0}]}
```