---
type: source
source_type: laptop
title: 0002_approvalaction_platform_post
slug: 0002-approvalaction-platform-post
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/approvals/migrations/0002_approvalaction_platform_post.py
original_size: 913
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# 0002_approvalaction_platform_post

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/approvals/migrations/0002_approvalaction_platform_post.py` on 2026-05-14._

```python
"""Add optional platform_post FK on ApprovalAction.

Now that editorial status lives on PlatformPost, approval decisions can target
a single platform instead of the whole Post. The new field is nullable so
historical actions (and bundled "apply to all platforms" decisions) are
represented with ``platform_post=NULL``.
"""

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("approvals", "0001_initial"),
        ("composer", "0015_per_account_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="approvalaction",
            name="platform_post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.deletion.CASCADE,
                related_name="approval_actions",
                to="composer.platformpost",
            ),
        ),
    ]

```