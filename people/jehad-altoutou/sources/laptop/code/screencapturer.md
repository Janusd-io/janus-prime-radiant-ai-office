---
type: source
source_type: laptop
title: ScreenCapturer
slug: screencapturer
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/ScreenCapturer.swift
original_size: 2280
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# ScreenCapturer

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/ScreenCapturer.swift` on 2026-05-14._

```swift
import Foundation
import AppKit
import ScreenCaptureKit

/// In-process screenshot via ScreenCaptureKit (macOS 14+).
///
/// The earlier implementation shelled out to `/usr/sbin/screencapture`, which
/// meant TCC permission had to be granted to both Nomi *and* the subprocess,
/// and ad-hoc signing made that subprocess inheritance brittle. ScreenCaptureKit
/// runs in-process, so TCC only evaluates Nomi itself.
public enum ScreenCapturer {

    public enum CaptureError: Error, LocalizedError {
        case noDisplays
        case encodeFailed
        case accessDenied(String)

        public var errorDescription: String? {
            switch self {
            case .noDisplays:            return "No displays found to capture."
            case .encodeFailed:          return "Couldn't encode the screenshot as JPEG."
            case .accessDenied(let m):   return "Screen recording permission not granted. \(m)"
            }
        }
    }

    /// Captures the display that currently shows Nomi (or the main display
    /// if that can't be determined) and returns JPEG bytes at ~60% quality.
    public static func capturePrimaryJPEG() async throws -> Data {
        let content: SCShareableContent
        do {
            content = try await SCShareableContent.excludingDesktopWindows(
                false,
                onScreenWindowsOnly: true
            )
        } catch {
            throw CaptureError.accessDenied(error.localizedDescription)
        }

        guard let display = content.displays.first else {
            throw CaptureError.noDisplays
        }

        let filter = SCContentFilter(display: display, excludingWindows: [])
        let config = SCStreamConfiguration()
        config.width  = display.width
        config.height = display.height
        config.showsCursor = false

        let image = try await SCScreenshotManager.captureImage(
            contentFilter: filter,
            configuration: config
        )

        let rep = NSBitmapImageRep(cgImage: image)
        rep.size = NSSize(width: image.width, height: image.height)
        guard let data = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.55]) else {
            throw CaptureError.encodeFailed
        }
        return data
    }
}

```