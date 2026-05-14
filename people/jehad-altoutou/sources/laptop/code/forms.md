---
type: source
source_type: laptop
title: Brightbean Studio — forms
slug: forms
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/inbox/forms.py
original_size: 2471
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# forms

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/inbox/forms.py` on 2026-05-14._

```python
"""Forms for the Unified Social Inbox."""

from django import forms

from .models import InboxMessage, InboxSLAConfig, SavedReply


class ReplyForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "placeholder": "Write a reply...",
                "class": "form-input w-full",
            }
        ),
    )


class InternalNoteForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "placeholder": "Add an internal note...",
                "class": "form-input w-full",
            }
        ),
    )


class AssignForm(forms.Form):
    assigned_to = forms.UUIDField(required=False)


class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=InboxMessage.Status.choices)


class SentimentForm(forms.Form):
    sentiment = forms.ChoiceField(choices=InboxMessage.Sentiment.choices)


class BulkActionForm(forms.Form):
    message_ids = forms.CharField()
    action = forms.ChoiceField(
        choices=[
            ("mark_read", "Mark as Read"),
            ("resolve", "Resolve"),
            ("archive", "Archive"),
            ("assign", "Assign"),
        ]
    )
    value = forms.CharField(required=False)

    def clean_message_ids(self):
        raw = self.cleaned_data["message_ids"]
        return [mid.strip() for mid in raw.split(",") if mid.strip()]


class SavedReplyForm(forms.ModelForm):
    class Meta:
        model = SavedReply
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-input w-full",
                    "placeholder": "Reply title",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-input w-full",
                    "rows": 4,
                    "placeholder": "Reply body. Use {sender_name}, {account_name}, {post_url} for variables.",
                }
            ),
        }


class SLAConfigForm(forms.ModelForm):
    class Meta:
        model = InboxSLAConfig
        fields = ["target_response_minutes", "is_active", "auto_resolve_on_reply"]
        widgets = {
            "target_response_minutes": forms.NumberInput(
                attrs={
                    "class": "form-input w-full",
                    "min": 1,
                }
            ),
        }

```