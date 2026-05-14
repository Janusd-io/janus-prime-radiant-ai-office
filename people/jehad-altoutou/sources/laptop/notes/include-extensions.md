---
type: source
source_type: laptop
title: include-extensions
slug: include-extensions
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/config/include-extensions.txt
original_size: 774
original_ext: .txt
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Public file-extension allowlist shipped in the skill repo."
project: janus-brain-bootstrap

---

# include-extensions

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/config/include-extensions.txt` on 2026-05-14._

# File extensions to include in enrichment. Anything not on this list is
# excluded by default (binary-skip). Case-insensitive.

# Text / notes
.md
.markdown
.txt
.rst
.org
.tex
.rtf
.adoc
.asciidoc

# Office / portable docs
.pdf
.docx
.doc
.odt
.pptx
.ppt
.odp
.xlsx
.xls
.ods
.csv
.tsv
.epub
.html
.htm

# Code (lightly enriched — focus on docstrings + module purpose, not line-by-line)
.py
.ipynb
.ts
.tsx
.js
.jsx
.mjs
.cjs
.go
.rs
.java
.kt
.swift
.c
.h
.cpp
.hpp
.cc
.cs
.rb
.php
.scala
.sh
.bash
.zsh
.fish
.lua
.r
.R
.jl
.dart
.vue
.svelte
.astro

# Config / data (kept because they often encode decisions)
.json
.yaml
.yml
.toml
.ini
.conf
.env.example
.sql
.graphql
.proto

# Images (OCR + visual understanding)
.png
.jpg
.jpeg
.heic
.heif
.webp
.tiff
.bmp
.gif
