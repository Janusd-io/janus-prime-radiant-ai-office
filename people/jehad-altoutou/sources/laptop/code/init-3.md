---
type: source
source_type: laptop
title: __init__
slug: init-3
created: 2026-03-31
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/VibeVoice/vibevoice/processor/__init__.py
original_size: 378
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# __init__

_Extracted from `[[vibevoice|VibeVoice]]/vibevoice/processor/__init__.py` on 2026-05-14._

```python
# vibevoice/processor/__init__.py
from .vibevoice_processor import VibeVoiceProcessor
from .vibevoice_streaming_processor import VibeVoiceStreamingProcessor
from .vibevoice_tokenizer_processor import VibeVoiceTokenizerProcessor, AudioNormalizer

__all__ = [
    "VibeVoiceProcessor",
    "VibeVoiceStreamingProcessor",
    "VibeVoiceTokenizerProcessor",
    "AudioNormalizer",
]
```