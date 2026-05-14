---
type: source
source_type: laptop
title: linkedin_personal
slug: linkedin-personal
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/providers/linkedin_personal.py
original_size: 661
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---

# linkedin_personal

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/providers/linkedin_personal.py` on 2026-05-14._

```python
"""LinkedIn provider variant for personal profile posting.

Uses the Community Management API app with personal member scopes.
Posts to the authenticated member's own profile via ``w_member_social``.
"""

from __future__ import annotations

from .linkedin import LinkedInProvider


class LinkedInPersonalProvider(LinkedInProvider):
    """LinkedIn provider scoped to personal member posting."""

    @property
    def platform_name(self) -> str:
        return "LinkedIn (Personal)"

    @property
    def required_scopes(self) -> list[str]:
        return [
            "r_basicprofile",
            "w_member_social",
            "r_member_social",
        ]

```