---
type: source
source_type: laptop
title: NomiApp
slug: nomiapp
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/App/NomiApp.swift
original_size: 4562
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# NomiApp

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/App/NomiApp.swift` on 2026-05-14._

```swift
import SwiftUI
import AppKit

@main
struct NomiApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

    var body: some Scene {
        // The Settings scene is reachable via ⌘, when any Nomi window is key.
        Settings {
            ConnectionsView()
        }
    }
}

final class AppDelegate: NSObject, NSApplicationDelegate {
    var windowController: NotchWindowController<NotchContainerView>?
    var engine: NomiStateEngine?
    var statusItem: NSStatusItem?
    var connectionsWindow: NSWindow?
    var diagnosticsWindow: NSWindow?

    func applicationDidFinishLaunching(_ notification: Notification) {
        CrashLogger.setup()

        // Proactively kick off all three permission prompts so the user sees
        // them on first launch rather than discovering later that nothing
        // works. The prompts are idempotent — subsequent launches are silent
        // once decisions are on file.
        CGRequestScreenCaptureAccess()
        Task.detached {
            _ = await SpeechEngine.shared.requestAuthorization()
        }

        NSApp.setActivationPolicy(.accessory)

        let engine = NomiStateEngine()
        self.engine = engine
        let contentView = NotchContainerView(engine: engine)

        let controller = NotchWindowController(rootView: contentView)
        controller.showWindow(self)
        self.windowController = controller

        installStatusItem()

        GlobalHotkey.shared.register { [weak engine] in
            engine?.triggerPushToTalk()
        }

        // If the user has never connected anything, nudge them to the Connections panel.
        if !Config.UserService.allCases.contains(where: { Config.isConnected($0) }) {
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.7) { [weak self] in
                self?.openConnections()
            }
        }
    }

    func applicationWillTerminate(_ notification: Notification) {
        SpeechEngine.shared.stop()
        GlobalHotkey.shared.unregister()
    }

    // MARK: - Status bar icon

    private func installStatusItem() {
        let item = NSStatusBar.system.statusItem(withLength: NSStatusItem.variableLength)
        if let button = item.button {
            button.image = NSImage(systemSymbolName: "waveform", accessibilityDescription: "Nomi")
        }
        let menu = NSMenu()
        menu.addItem(NSMenuItem(title: "Connections…", action: #selector(openConnections), keyEquivalent: ","))
        menu.addItem(NSMenuItem(title: "Diagnostics…", action: #selector(openDiagnostics), keyEquivalent: "d"))
        menu.addItem(NSMenuItem.separator())
        menu.addItem(NSMenuItem(title: "Snap to notch", action: #selector(snapToNotch), keyEquivalent: "n"))
        menu.addItem(NSMenuItem(title: "Move to active display", action: #selector(pinToActive), keyEquivalent: "m"))
        menu.addItem(NSMenuItem.separator())
        menu.addItem(NSMenuItem(title: "Quit Nomi", action: #selector(NSApplication.terminate(_:)), keyEquivalent: "q"))
        item.menu = menu
        self.statusItem = item
    }

    @objc func snapToNotch() {
        windowController?.snapToNotch()
    }

    @objc func pinToActive() {
        windowController?.pinToActiveDisplay()
    }

    @objc func openDiagnostics() {
        if let window = diagnosticsWindow {
            window.makeKeyAndOrderFront(nil)
            NSApp.activate(ignoringOtherApps: true)
            return
        }
        let hosting = NSHostingController(rootView: DiagnosticsView())
        let window = NSWindow(contentViewController: hosting)
        window.title = "Nomi — Diagnostics"
        window.styleMask = [.titled, .closable, .miniaturizable]
        window.isReleasedWhenClosed = false
        window.center()
        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
        self.diagnosticsWindow = window
    }

    @objc func openConnections() {
        if let window = connectionsWindow {
            window.makeKeyAndOrderFront(nil)
            NSApp.activate(ignoringOtherApps: true)
            return
        }

        let hosting = NSHostingController(rootView: ConnectionsView())
        let window = NSWindow(contentViewController: hosting)
        window.title = "Nomi — Connections"
        window.styleMask = [.titled, .closable, .miniaturizable]
        window.isReleasedWhenClosed = false
        window.center()
        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
        self.connectionsWindow = window
    }
}

```