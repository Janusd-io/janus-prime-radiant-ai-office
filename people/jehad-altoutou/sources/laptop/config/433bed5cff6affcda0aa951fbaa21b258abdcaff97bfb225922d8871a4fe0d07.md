---
type: source
source_type: laptop
title: 433bed5cff6affcda0aa951fbaa21b258abdcaff97bfb225922d8871a4fe0d07
slug: 433bed5cff6affcda0aa951fbaa21b258abdcaff97bfb225922d8871a4fe0d07
created: 2026-04-14
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/graphify-out/cache/433bed5cff6affcda0aa951fbaa21b258abdcaff97bfb225922d8871a4fe0d07.json
original_size: 4056
original_ext: .json
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:32Z"
project: assessify

---

# 433bed5cff6affcda0aa951fbaa21b258abdcaff97bfb225922d8871a4fe0d07

_Extracted from `[[assessify|assessify]]/graphify-out/cache/433bed5cff6affcda0aa951fbaa21b258abdcaff97bfb225922d8871a4fe0d07.json` on 2026-05-14._

```json
{"nodes": [{"id": "src_lib_auth_ts", "label": "auth.ts", "file_type": "code", "source_file": "src/lib/auth.ts", "source_location": "L1"}, {"id": "auth_getsecret", "label": "getSecret()", "file_type": "code", "source_file": "src/lib/auth.ts", "source_location": "L10"}, {"id": "auth_generatetoken", "label": "generateToken()", "file_type": "code", "source_file": "src/lib/auth.ts", "source_location": "L17"}, {"id": "auth_parsetoken", "label": "parseToken()", "file_type": "code", "source_file": "src/lib/auth.ts", "source_location": "L24"}, {"id": "auth_createsession", "label": "createSession()", "file_type": "code", "source_file": "src/lib/auth.ts", "source_location": "L44"}, {"id": "auth_destroysession", "label": "destroySession()", "file_type": "code", "source_file": "src/lib/auth.ts", "source_location": "L57"}, {"id": "auth_getsession", "label": "getSession()", "file_type": "code", "source_file": "src/lib/auth.ts", "source_location": "L62"}, {"id": "auth_requireauth", "label": "requireAuth()", "file_type": "code", "source_file": "src/lib/auth.ts", "source_location": "L78"}], "edges": [{"source": "src_lib_auth_ts", "target": "headers", "relation": "imports_from", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L1", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "crypto", "relation": "imports_from", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L2", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "db", "relation": "imports_from", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L3", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "navigation", "relation": "imports_from", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L4", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "auth_getsecret", "relation": "contains", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L10", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "auth_generatetoken", "relation": "contains", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L17", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "auth_parsetoken", "relation": "contains", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L24", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "auth_createsession", "relation": "contains", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L44", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "auth_destroysession", "relation": "contains", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L57", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "auth_getsession", "relation": "contains", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L62", "weight": 1.0}, {"source": "src_lib_auth_ts", "target": "auth_requireauth", "relation": "contains", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L78", "weight": 1.0}, {"source": "auth_generatetoken", "target": "auth_getsecret", "relation": "calls", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L20", "weight": 1.0}, {"source": "auth_parsetoken", "target": "auth_getsecret", "relation": "calls", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L30", "weight": 1.0}, {"source": "auth_createsession", "target": "auth_generatetoken", "relation": "calls", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L45", "weight": 1.0}, {"source": "auth_getsession", "target": "auth_parsetoken", "relation": "calls", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L67", "weight": 1.0}, {"source": "auth_requireauth", "target": "auth_getsession", "relation": "calls", "confidence": "EXTRACTED", "source_file": "src/lib/auth.ts", "source_location": "L79", "weight": 1.0}]}
```