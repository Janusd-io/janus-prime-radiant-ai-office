---
type: source
source_type: laptop
title: DraggableModifier
slug: draggablemodifier
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/DraggableModifier.swift
original_size: 1185
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# DraggableModifier

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/DraggableModifier.swift` on 2026-05-14._

```swift
import SwiftUI
import AppKit

/// A `NSHostingView` subclass that opts into AppKit's automatic window-drag
/// behavior. Setting `mouseDownCanMoveWindow = true` tells AppKit: "when the
/// user clicks-and-drags inside me and the click doesn't hit an interactive
/// control, move the whole window."
///
/// The reason the earlier drag code didn't work: a standard `NSHostingView`
/// returns `false` for this property, and SwiftUI's internal hit-test absorbs
/// every mouse-down before an NSView in `.background()` ever sees it. Handling
/// the drag at the host level bypasses that problem entirely. Buttons and text
/// fields still work because AppKit only starts the drag when the click would
/// otherwise land on empty/decorative content.
final class DraggableHostingView<V: View>: NSHostingView<V> {
    override var mouseDownCanMoveWindow: Bool { true }
}

/// No-op modifier kept only so existing `.nativeWindowDrag()` call sites keep
/// compiling. Window dragging is now handled at the host-view level.
struct DraggableModifier: ViewModifier {
    func body(content: Content) -> some View { content }
}

extension View {
    func nativeWindowDrag() -> some View { self }
}

```