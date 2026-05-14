---
type: source
source_type: laptop
title: _connection_link_created
slug: connection-link-created
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/brightbean-studio/templates/onboarding/partials/_connection_link_created.html
original_size: 2285
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:41Z"
sensitivity: dept
sensitivity_confidence: 0.70
sensitivity_reason: "Brightbean Studio partial HTML template — boilerplate, no PII"
project: brightbean-studio

---

# _connection_link_created

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/onboarding/partials/_connection_link_created.html` on 2026-05-14._

<div style="
    background: var(--success-50);
    border: 1px solid rgba(34,197,94,0.15);
    border-radius: var(--radius-lg);
    padding: 16px 20px;
    margin-bottom: 16px;
">

<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0idmFyKC0tc3VjY2Vzcy01MDApIiB2aWV3Ym94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cGF0aCBkPSJNMjIgMTEuMDhWMTJhMTAgMTAgMCAxMS01LjkzLTkuMTQiIC8+PHBvbHlsaW5lIHBvaW50cz0iMjIgNCAxMiAxNC4wMSA5IDExLjAxIj48L3BvbHlsaW5lPjwvc3ZnPg==)
<span style="font-size: 0.875rem; font-weight: 600; color: var(--success-700);">Connection
link created</span>

</div>

<div style="display: flex; gap: 8px; align-items: center;"
x-data="{ copied: false }">

<span x-show="!copied">Copy</span> <span x-show="copied" x-cloak=""
style="color: var(--success-700);">Copied!</span>

</div>

Expires {{ link.expires_at\|date:"M j, Y" }}. Share this link with your
client so they can connect their social accounts.

</div>
