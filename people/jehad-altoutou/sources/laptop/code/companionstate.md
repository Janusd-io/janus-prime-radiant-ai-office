---
type: source
source_type: laptop
title: CompanionState
slug: companionstate
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/CompanionState.swift
original_size: 427
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# CompanionState

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/CompanionState.swift` on 2026-05-14._

```swift
import Foundation
import Combine

public enum CompanionState: Equatable {
    case idle
    case listening
    case thinking
    case speaking
    case needsApproval
    case success
    case error
    case connectTool
    /// Plays a friendly hello wave — used for the first launch of the day
    /// and by the `/wave` debug trigger. Auto-transitions to `.idle` after
    /// the wave finishes (~1.8s).
    case greeting
}

```