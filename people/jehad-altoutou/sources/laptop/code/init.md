---
type: source
source_type: laptop
title: __init__
slug: init
created: 2026-03-31
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/VibeVoice/vibevoice/__init__.py
original_size: 422
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# __init__

_Extracted from `[[vibevoice|VibeVoice]]/vibevoice/__init__.py` on 2026-05-14._

```python
# vibevoice/__init__.py
from vibevoice.modular import (
    VibeVoiceStreamingForConditionalGenerationInference,
    VibeVoiceStreamingConfig,
)
from vibevoice.processor import (
    VibeVoiceStreamingProcessor,
    VibeVoiceTokenizerProcessor,
)

__all__ = [
    "VibeVoiceStreamingForConditionalGenerationInference",
    "VibeVoiceStreamingConfig",
    "VibeVoiceStreamingProcessor",
    "VibeVoiceTokenizerProcessor",
]
```