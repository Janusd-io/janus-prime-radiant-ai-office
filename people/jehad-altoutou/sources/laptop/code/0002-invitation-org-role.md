---
type: source
source_type: laptop
title: 0002_invitation_org_role
slug: 0002-invitation-org-role
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/members/migrations/0002_invitation_org_role.py
original_size: 482
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# 0002_invitation_org_role

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/members/migrations/0002_invitation_org_role.py` on 2026-05-14._

```python
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitation",
            name="org_role",
            field=models.CharField(
                choices=[("owner", "Owner"), ("admin", "Admin"), ("member", "Member")],
                default="member",
                max_length=20,
            ),
        ),
    ]

```