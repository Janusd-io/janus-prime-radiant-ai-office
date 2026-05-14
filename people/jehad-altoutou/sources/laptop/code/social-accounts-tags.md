---
type: source
source_type: laptop
title: social_accounts_tags
slug: social-accounts-tags
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/social_accounts/templatetags/social_accounts_tags.py
original_size: 1734
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# social_accounts_tags

_Extracted from `brightbean-studio/apps/social_accounts/templatetags/social_accounts_tags.py` on 2026-05-14._

```python
from collections import defaultdict

from django import template

register = template.Library()


@register.filter
def format_number(value):
    """Format a number with K/M suffixes for compact display."""
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value

    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return str(value)


# Sunday-first display order: model uses 0=Mon..6=Sun
_DISPLAY_ORDER = [6, 0, 1, 2, 3, 4, 5]
_DAY_NAMES = {
    0: ("Monday", "Mon"),
    1: ("Tuesday", "Tue"),
    2: ("Wednesday", "Wed"),
    3: ("Thursday", "Thu"),
    4: ("Friday", "Fri"),
    5: ("Saturday", "Sat"),
    6: ("Sunday", "Sun"),
}


@register.simple_tag
def get_posting_slots_display(account):
    """Build a Sunday-first list of day dicts with grouped posting slots.

    Each entry: {value, name, short_name, slots, is_active, has_slots}.
    Expects account.posting_slots to be prefetched.
    """
    slots_by_day = defaultdict(list)
    for slot in account.posting_slots.all():
        slots_by_day[slot.day_of_week].append(slot)

    days = []
    for day_val in _DISPLAY_ORDER:
        day_slots = sorted(slots_by_day.get(day_val, []), key=lambda s: s.time)
        all_active = all(s.is_active for s in day_slots) if day_slots else True
        full_name, short_name = _DAY_NAMES[day_val]
        days.append(
            {
                "value": day_val,
                "name": full_name,
                "short_name": short_name,
                "slots": day_slots,
                "is_active": all_active,
                "has_slots": len(day_slots) > 0,
            }
        )
    return days

```