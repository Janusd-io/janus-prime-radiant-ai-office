---
type: source
source_type: laptop
title: NotchWindowController
slug: notchwindowcontroller
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/App/NotchWindowController.swift
original_size: 8570
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# NotchWindowController

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/App/NotchWindowController.swift` on 2026-05-14._

```swift
import AppKit
import SwiftUI
import OSLog

/// Borderless non-activating panel that floats above everything.
/// Panel — not Window — so it can sit over fullscreen apps without stealing focus.
final class NotchPanel: NSPanel {
    override var canBecomeKey: Bool { true }
    override var canBecomeMain: Bool { false }
}

/// Placement model.
///   `.auto`   — snap to the notched built-in display (classic behavior).
///   `.custom` — user has dragged Nomi somewhere, remember exactly where.
///
/// `.custom` persists across app launches via `UserDefaults`. If the display it
/// was pinned to is gone on next launch (undocked, external cable pulled), we
/// fall back to `.auto` automatically instead of dumping the window off-screen.
enum NotchPlacement: Equatable {
    case auto
    case custom(origin: CGPoint, displayID: UInt32)
}

final class NotchWindowController<RootView: View>: NSWindowController, NSWindowDelegate {

    private let log = Logger(subsystem: "com.antigravity.nomi", category: "Window")

    private let hostingView: DraggableHostingView<RootView>
    private var screenObserver: NSObjectProtocol?
    private let placementKey = "nomi.windowPlacement.v1"
    private var placement: NotchPlacement = .auto
    /// Set while we're moving the window ourselves, so `windowDidMove` doesn't
    /// interpret the programmatic move as a user drag.
    private var isProgrammaticMove = false

    init(rootView: RootView) {
        self.hostingView = DraggableHostingView(rootView: rootView)

        let panel = NotchPanel(
            contentRect: NSRect(x: 0, y: 0, width: 340, height: 430),
            styleMask: [.borderless, .nonactivatingPanel],
            backing: .buffered,
            defer: false
        )
        panel.contentView = hostingView
        panel.backgroundColor = .clear
        panel.isOpaque = false
        panel.hasShadow = false
        // Works together with DraggableHostingView.mouseDownCanMoveWindow.
        panel.isMovableByWindowBackground = true
        panel.isMovable = true
        panel.level = .statusBar
        panel.collectionBehavior = [.canJoinAllSpaces, .stationary, .ignoresCycle, .fullScreenAuxiliary]
        panel.hidesOnDeactivate = false
        panel.isFloatingPanel = true
        panel.becomesKeyOnlyIfNeeded = true
        panel.acceptsMouseMovedEvents = true

        super.init(window: panel)
        panel.delegate = self

        loadPlacement()
        applyPlacement()

        screenObserver = NotificationCenter.default.addObserver(
            forName: NSApplication.didChangeScreenParametersNotification,
            object: nil,
            queue: .main
        ) { [weak self] _ in self?.handleScreenChange() }
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) unused") }

    deinit {
        if let screenObserver {
            NotificationCenter.default.removeObserver(screenObserver)
        }
    }

    // MARK: - Public placement API

    /// Re-pin to the notch. Called from the menubar "Snap to notch" item.
    func snapToNotch() {
        placement = .auto
        savePlacement()
        applyPlacement()
    }

    /// Move to the screen currently under the cursor, horizontally centered at its top.
    func pinToActiveDisplay() {
        let mouse = NSEvent.mouseLocation
        guard let screen = NSScreen.screens.first(where: { $0.frame.contains(mouse) }) ?? NSScreen.main else { return }
        guard let window else { return }
        let size = window.frame.size
        let origin = CGPoint(
            x: screen.frame.minX + (screen.frame.width - size.width) / 2,
            y: screen.frame.maxY - size.height
        )
        placement = .custom(origin: origin, displayID: displayID(for: screen))
        savePlacement()
        applyPlacement()
    }

    // MARK: - Placement application

    private func applyPlacement() {
        guard let window else { return }
        isProgrammaticMove = true
        defer { isProgrammaticMove = false }

        switch placement {
        case .custom(let origin, let displayID):
            if let screen = NSScreen.screens.first(where: { self.displayID(for: $0) == displayID }) {
                window.setFrameOrigin(clamped(origin, to: screen, size: window.frame.size))
                return
            }
            log.info("Saved display \(displayID) is gone; falling back to notch.")
            placement = .auto
            savePlacement()
            fallthrough
        case .auto:
            guard let screen = preferredScreen() else { return }
            let size = window.frame.size
            let origin = CGPoint(
                x: screen.frame.minX + (screen.frame.width - size.width) / 2,
                y: screen.frame.maxY - size.height
            )
            window.setFrameOrigin(origin)
        }
    }

    /// Auto-mode preferred screen:
    ///   1. The built-in notched display, if present (safeAreaInsets.top > 0).
    ///   2. The primary display (screens[0], which is the one with the menu bar).
    ///   3. Whatever `NSScreen.main` resolves to.
    ///
    /// We deliberately do NOT use `NSScreen.main` first, because on multi-display
    /// setups `main` is the screen with the active app's key window — which moves
    /// around as the user switches apps, leading to Nomi appearing to jump. The
    /// primary display (screens[0]) is stable.
    private func preferredScreen() -> NSScreen? {
        if let notched = NSScreen.screens.first(where: { $0.safeAreaInsets.top > 0 }) {
            return notched
        }
        return NSScreen.screens.first ?? NSScreen.main
    }

    private func handleScreenChange() {
        // If the user's current placement is still valid, do nothing — they
        // deliberately dragged Nomi and we should respect that. Only re-apply
        // if the pinned display has disappeared.
        if case .custom(_, let id) = placement,
           !NSScreen.screens.contains(where: { displayID(for: $0) == id }) {
            applyPlacement()
        } else if case .auto = placement {
            applyPlacement()
        }
    }

    // MARK: - NSWindowDelegate

    func windowDidMove(_ notification: Notification) {
        guard !isProgrammaticMove, let window else { return }
        guard let screen = window.screen else { return }
        placement = .custom(origin: window.frame.origin, displayID: displayID(for: screen))
        savePlacement()
    }

    func windowDidResignKey(_ notification: Notification) {
        NotificationCenter.default.post(name: .nomiShouldCollapse, object: nil)
    }

    // MARK: - Persistence

    private struct PlacementStorage: Codable {
        let kind: String   // "auto" | "custom"
        let x: CGFloat?
        let y: CGFloat?
        let displayID: UInt32?
    }

    private func loadPlacement() {
        guard
            let data = UserDefaults.standard.data(forKey: placementKey),
            let decoded = try? JSONDecoder().decode(PlacementStorage.self, from: data)
        else { return }

        if decoded.kind == "custom",
           let x = decoded.x, let y = decoded.y, let id = decoded.displayID {
            placement = .custom(origin: CGPoint(x: x, y: y), displayID: id)
        } else {
            placement = .auto
        }
    }

    private func savePlacement() {
        let stored: PlacementStorage
        switch placement {
        case .auto:
            stored = PlacementStorage(kind: "auto", x: nil, y: nil, displayID: nil)
        case .custom(let origin, let id):
            stored = PlacementStorage(kind: "custom", x: origin.x, y: origin.y, displayID: id)
        }
        if let data = try? JSONEncoder().encode(stored) {
            UserDefaults.standard.set(data, forKey: placementKey)
        }
    }

    // MARK: - Helpers

    private func displayID(for screen: NSScreen) -> UInt32 {
        if let n = screen.deviceDescription[NSDeviceDescriptionKey("NSScreenNumber")] as? NSNumber {
            return UInt32(truncating: n)
        }
        return 0
    }

    private func clamped(_ origin: CGPoint, to screen: NSScreen, size: CGSize) -> CGPoint {
        let minX = screen.frame.minX
        let maxX = screen.frame.maxX - size.width
        let minY = screen.frame.minY
        let maxY = screen.frame.maxY - size.height
        return CGPoint(
            x: max(minX, min(origin.x, maxX)),
            y: max(minY, min(origin.y, maxY))
        )
    }
}

extension Notification.Name {
    static let nomiShouldCollapse = Notification.Name("com.antigravity.nomi.shouldCollapse")
}

```