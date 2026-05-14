---
type: source
source_type: laptop
title: testCapture
slug: testcapture
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/testCapture.swift
original_size: 202
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# testCapture

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/testCapture.swift` on 2026-05-14._

```swift
import AppKit
import CoreGraphics
let rect = CGRect.infinite
let cgImage = CGWindowListCreateImage(rect, .optionOnScreenOnly, kCGNullWindowID, .nominalResolution)
if cgImage != nil { print("success") }

```