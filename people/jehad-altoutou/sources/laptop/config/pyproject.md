---
type: source
source_type: laptop
title: Vibevoice — pyproject
slug: pyproject
created: 2026-03-31
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/VibeVoice/pyproject.toml
original_size: 1194
original_ext: .toml
category: config
extracted_with: config-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: vibevoice

---
<!-- jb:project-callout -->
> Part of [[vibevoice|VibeVoice]] — automatically linked by /janus-brain.


# pyproject

_Extracted from `[[vibevoice|VibeVoice]]/pyproject.toml` on 2026-05-14._

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "vibevoice"
version = "1.0.0"
authors = [
  { name="vibevoice team", email="VibeVoice@microsoft.com" },
]
description = "Open-Source Frontier Voice AI."
readme = "README.md"
requires-python = ">=3.9"
classifiers = [
    "Programming Language :: Python :: 3",
    # "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "torch",
    "transformers>=4.51.3,<5.0.0",
    "accelerate",
    "llvmlite>=0.40.0",
    "numba>=0.57.0",
    "diffusers",
    "tqdm",
    "numpy",
    "scipy",
    "librosa",
    "ml-collections",
    "absl-py",
    "gradio",
    "av",
    "aiortc",
    "uvicorn[standard]",
    "fastapi",
    "pydub",
    "requests",
]


[project.optional-dependencies]
streamingtts = [
  "transformers==4.51.3", 
]

[project.entry-points."vllm.general_plugins"]
vibevoice = "vllm_plugin:register_vibevoice"

[project.urls]
"Homepage" = "https://github.com/microsoft/VibeVoice"
"Bug Tracker" = "https://github.com/microsoft/VibeVoice/issues"

[tool.setuptools.packages.find]
where = ["."]
include = ["vibevoice*", "vllm_plugin*"]

```