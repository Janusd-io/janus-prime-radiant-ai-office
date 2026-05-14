---
type: source
source_type: laptop
title: holidays
slug: holidays
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/calendar/holidays.py
original_size: 1096
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# holidays

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/calendar/holidays.py` on 2026-05-14._

```python
"""Holiday/awareness day calendar overlay (F-2.3).

Loads a bundled JSON dataset of international awareness days and
public holidays. Used to render a subtle overlay on the calendar.
"""

import json
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def _load_holidays():
    """Load holidays.json once and cache."""
    data_path = Path(__file__).parent / "data" / "holidays.json"
    with open(data_path) as f:
        return json.load(f)


def get_holidays_for_range(start_date, end_date):
    """Return holidays falling within the date range.

    Returns a dict keyed by (month, day) tuples, with values being
    lists of holiday dicts (multiple holidays can fall on the same day).
    """
    holidays = _load_holidays()
    result = {}

    current = start_date
    from datetime import timedelta

    while current <= end_date:
        matching = [h for h in holidays if h["month"] == current.month and h["day"] == current.day]
        if matching:
            result[current.isoformat()] = matching
        current += timedelta(days=1)

    return result

```