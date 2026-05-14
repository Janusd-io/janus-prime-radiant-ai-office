---
type: source
source_type: laptop
title: sentiment
slug: sentiment
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/inbox/sentiment.py
original_size: 1521
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# sentiment

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/inbox/sentiment.py` on 2026-05-14._

```python
"""Keyword-based sentiment analysis engine for inbox messages."""

POSITIVE_KEYWORDS = [
    "love",
    "great",
    "amazing",
    "thank",
    "thanks",
    "excellent",
    "awesome",
    "perfect",
    "best",
    "fantastic",
    "wonderful",
    "beautiful",
    "brilliant",
    "incredible",
    "outstanding",
    "impressive",
    "helpful",
    "appreciate",
    "happy",
    "glad",
    "excited",
    "recommend",
    "superb",
    "delighted",
    "thrilled",
]

NEGATIVE_KEYWORDS = [
    "hate",
    "terrible",
    "awful",
    "worst",
    "disappointed",
    "broken",
    "scam",
    "refund",
    "horrible",
    "disgusting",
    "pathetic",
    "useless",
    "angry",
    "furious",
    "unacceptable",
    "frustrating",
    "annoying",
    "poor",
    "waste",
    "trash",
    "spam",
    "fake",
    "misleading",
    "rude",
    "unprofessional",
]


def analyze_sentiment(text: str) -> str:
    """Analyze sentiment of text using keyword matching.

    Returns 'positive', 'negative', or 'neutral'.
    """
    if not text:
        return "neutral"

    import re

    text_lower = text.lower()
    # Strip punctuation from each word so "great!" matches "great"
    words = set(re.sub(r"[^\w\s]", "", text_lower).split())

    pos_count = sum(1 for kw in POSITIVE_KEYWORDS if kw in words)
    neg_count = sum(1 for kw in NEGATIVE_KEYWORDS if kw in words)

    if neg_count > pos_count:
        return "negative"
    elif pos_count > neg_count:
        return "positive"
    return "neutral"

```