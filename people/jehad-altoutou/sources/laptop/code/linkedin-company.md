---
type: source
source_type: laptop
title: linkedin_company
slug: linkedin-company
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/providers/linkedin_company.py
original_size: 782
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# linkedin_company

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/providers/linkedin_company.py` on 2026-05-14._

```python
"""LinkedIn provider variant for Company Page posting.

Uses the Community Management API app with organization scopes. Posts to
Company Pages the authenticated member administers via
``w_organization_social`` and ``rw_organization_admin``.
"""

from __future__ import annotations

from .linkedin import LinkedInProvider


class LinkedInCompanyProvider(LinkedInProvider):
    """LinkedIn provider scoped to Company Page posting."""

    @property
    def platform_name(self) -> str:
        return "LinkedIn (Company Page)"

    @property
    def required_scopes(self) -> list[str]:
        return [
            "r_basicprofile",
            "w_member_social",
            "w_organization_social",
            "r_organization_social",
            "rw_organization_admin",
        ]

```