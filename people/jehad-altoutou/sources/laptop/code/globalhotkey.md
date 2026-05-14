---
type: source
source_type: laptop
title: GlobalHotkey
slug: globalhotkey
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/App/GlobalHotkey.swift
original_size: 3418
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# GlobalHotkey

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/App/GlobalHotkey.swift` on 2026-05-14._

```swift
import AppKit
import Carbon.HIToolbox
import OSLog

/// Registers a single system-wide hotkey (default: ⌘⌥Space) that fires a closure.
///
/// Uses Carbon's `RegisterEventHotKey`, which is still the stable, sandbox-compatible
/// way to register global hotkeys on macOS. The `NSEvent.addGlobalMonitorForEvents`
/// alternative silently drops events when the focused app intercepts them; Carbon
/// hotkeys do not.
public final class GlobalHotkey {

    public static let shared = GlobalHotkey()

    private let log = Logger(subsystem: "com.antigravity.nomi", category: "Hotkey")
    private var hotKeyRef: EventHotKeyRef?
    private var eventHandler: EventHandlerRef?
    private var callback: (() -> Void)?

    private static let signature: OSType = {
        let s = "NOMI".unicodeScalars.reduce(0) { ($0 << 8) + OSType($1.value & 0xff) }
        return s
    }()
    private static let hotKeyID = EventHotKeyID(signature: signature, id: 1)

    private init() {}

    /// Installs a global hotkey. Replaces any existing registration.
    ///
    /// - Parameters:
    ///   - keyCode: Carbon virtual key code (default `kVK_Space`).
    ///   - modifiers: Carbon modifier mask (default ⌘⌥).
    ///   - handler: Runs on the main actor.
    public func register(
        keyCode: Int = kVK_Space,
        modifiers: Int = cmdKey | optionKey,
        handler: @escaping () -> Void
    ) {
        unregister()
        self.callback = handler

        var eventSpec = EventTypeSpec(
            eventClass: OSType(kEventClassKeyboard),
            eventKind: UInt32(kEventHotKeyPressed)
        )

        let ctx = Unmanaged.passUnretained(self).toOpaque()
        InstallEventHandler(
            GetApplicationEventTarget(),
            { _, event, userData -> OSStatus in
                guard let event, let userData else { return OSStatus(eventNotHandledErr) }
                var id = EventHotKeyID()
                let s = GetEventParameter(
                    event,
                    EventParamName(kEventParamDirectObject),
                    EventParamType(typeEventHotKeyID),
                    nil,
                    MemoryLayout<EventHotKeyID>.size,
                    nil,
                    &id
                )
                guard s == noErr, id.id == GlobalHotkey.hotKeyID.id else {
                    return OSStatus(eventNotHandledErr)
                }
                let me = Unmanaged<GlobalHotkey>.fromOpaque(userData).takeUnretainedValue()
                DispatchQueue.main.async { me.callback?() }
                return noErr
            },
            1,
            &eventSpec,
            ctx,
            &eventHandler
        )

        let status = RegisterEventHotKey(
            UInt32(keyCode),
            UInt32(modifiers),
            Self.hotKeyID,
            GetApplicationEventTarget(),
            0,
            &hotKeyRef
        )
        if status != noErr {
            log.error("GlobalHotkey registration failed (status=\(status)).")
        } else {
            log.info("GlobalHotkey registered.")
        }
    }

    public func unregister() {
        if let ref = hotKeyRef {
            UnregisterEventHotKey(ref)
            hotKeyRef = nil
        }
        if let handler = eventHandler {
            RemoveEventHandler(handler)
            eventHandler = nil
        }
        callback = nil
    }

    deinit { unregister() }
}

```