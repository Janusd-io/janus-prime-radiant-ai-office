---
type: source
source_type: laptop
title: timestep_sampler
slug: timestep-sampler
created: 2026-03-31
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/VibeVoice/vibevoice/schedule/timestep_sampler.py
original_size: 701
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: vibevoice

---

# timestep_sampler

_Extracted from `[[vibevoice|VibeVoice]]/vibevoice/schedule/timestep_sampler.py` on 2026-05-14._

```python
import math
import torch


class UniformSampler:
    def __init__(self, timesteps = 1000):
        self.timesteps = timesteps
    def sample(self, batch_size, device):
        return torch.randint(0, self.timesteps, (batch_size,), device=device)
    
class LogitNormalSampler:
    def __init__(self, timesteps = 1000, m = 0, s = 1):
        self.timesteps = timesteps
        timesteps = torch.linspace(0, 1, timesteps)
        logit = torch.log(timesteps / (1 - timesteps))
        self.prob = torch.exp(-0.5 * (logit - m) ** 2 / s ** 2) / (s * math.sqrt(2 * math.pi))
    def sample(self, batch_size, device):
        return torch.multinomial(self.prob, batch_size, replacement=True).to(device)
    
```