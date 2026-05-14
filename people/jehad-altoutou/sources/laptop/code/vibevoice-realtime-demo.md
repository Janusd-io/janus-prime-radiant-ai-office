---
type: source
source_type: laptop
title: vibevoice_realtime_demo
slug: vibevoice-realtime-demo
created: 2026-03-31
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/VibeVoice/demo/vibevoice_realtime_demo.py
original_size: 645
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# vibevoice_realtime_demo

_Extracted from `VibeVoice/demo/vibevoice_realtime_demo.py` on 2026-05-14._

```python
import argparse, os, uvicorn

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=3000)
    p.add_argument("--model_path", type=str, default="microsoft/VibeVoice-Realtime-0.5B")
    p.add_argument("--device", type=str, default="cuda", choices=["cpu", "cuda", "mpx", "mps"])
    p.add_argument("--reload", action="store_true", help="Reload the model or not")
    args = p.parse_args()
    
    os.environ["MODEL_PATH"] = args.model_path
    os.environ["MODEL_DEVICE"] = args.device

    uvicorn.run("web.app:app", host="0.0.0.0", port=args.port, reload=args.reload)

if __name__ == "__main__":
    main()

```