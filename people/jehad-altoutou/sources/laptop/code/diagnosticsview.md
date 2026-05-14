---
type: source
source_type: laptop
title: DiagnosticsView
slug: diagnosticsview
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/DiagnosticsView.swift
original_size: 10309
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# DiagnosticsView

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/DiagnosticsView.swift` on 2026-05-14._

```swift
import SwiftUI
import AppKit
import AVFoundation
import Speech
import CoreGraphics

/// Diagnostics window. Shows the live TCC permission state for every thing
/// Nomi needs (mic, speech recognition, screen recording), lets the user
/// re-request permissions, and jumps to the right System Settings pane if
/// macOS refuses to prompt again.
///
/// Especially useful on ad-hoc signed builds (what `build.sh` produces),
/// because macOS sometimes forgets permission grants between rebuilds and
/// won't re-prompt. Having a status readout prevents guesswork.
struct DiagnosticsView: View {

    @State private var micStatus: AVAuthorizationStatus = AVCaptureDevice.authorizationStatus(for: .audio)
    @State private var speechStatus: SFSpeechRecognizerAuthorizationStatus = SFSpeechRecognizer.authorizationStatus()
    @State private var screenHasAccess: Bool = CGPreflightScreenCaptureAccess()
    @State private var micTestResult: String = ""
    @State private var isTestingMic = false
    @State private var refreshTimer: Timer?

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            header
                .padding(.horizontal, 28)
                .padding(.top, 24)
                .padding(.bottom, 18)

            Divider()

            VStack(spacing: 0) {
                row(
                    title: "Microphone",
                    subtitle: "Required for voice commands",
                    statusText: micStatusText,
                    statusGood: micStatus == .authorized,
                    primaryAction: micPrimaryAction,
                    openSettings: { openPrivacyPane("Microphone") }
                )
                Divider().padding(.leading, 28)

                row(
                    title: "Speech Recognition",
                    subtitle: "On-device transcription of your voice",
                    statusText: speechStatusText,
                    statusGood: speechStatus == .authorized,
                    primaryAction: speechPrimaryAction,
                    openSettings: { openPrivacyPane("SpeechRecognition") }
                )
                Divider().padding(.leading, 28)

                row(
                    title: "Screen Recording",
                    subtitle: "So Nomi can look at your screen when asked",
                    statusText: screenStatusText,
                    statusGood: screenHasAccess,
                    primaryAction: screenPrimaryAction,
                    openSettings: { openPrivacyPane("ScreenCapture") }
                )
            }

            Divider()

            VStack(alignment: .leading, spacing: 10) {
                HStack {
                    Button(isTestingMic ? "Listening for 4s…" : "Test microphone") {
                        Task { await testMic() }
                    }
                    .disabled(isTestingMic || micStatus != .authorized || speechStatus != .authorized)
                    .buttonStyle(.borderedProminent)

                    Spacer()

                    Button("Refresh") { refreshAll() }
                        .buttonStyle(.bordered)
                }

                if !micTestResult.isEmpty {
                    Text(micTestResult)
                        .font(.system(size: 12))
                        .foregroundStyle(micTestResult.contains("✓") ? .green : .secondary)
                        .fixedSize(horizontal: false, vertical: true)
                }

                Text("Tip: If a permission was just enabled but nothing works yet, quit Nomi and run ./build.sh again — macOS needs the app to relaunch for the new grant to take effect.")
                    .font(.system(size: 11))
                    .foregroundStyle(.secondary)
                    .fixedSize(horizontal: false, vertical: true)
                    .padding(.top, 6)
            }
            .padding(28)

            Spacer()
        }
        .frame(width: 540, height: 560)
        .onAppear {
            refreshAll()
            // Poll every 2s so the status updates live when the user flips a
            // toggle in System Settings.
            refreshTimer = Timer.scheduledTimer(withTimeInterval: 2, repeats: true) { _ in
                refreshAll()
            }
        }
        .onDisappear { refreshTimer?.invalidate() }
    }

    // MARK: - UI pieces

    private var header: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("Diagnostics")
                .font(.system(size: 22, weight: .semibold))
            Text("What Nomi can and can't do on this Mac right now. If anything's red, tap Fix and grant the prompt — or open the System Settings pane and toggle the permission manually.")
                .font(.system(size: 12))
                .foregroundStyle(.secondary)
                .fixedSize(horizontal: false, vertical: true)
        }
    }

    private func row(
        title: String,
        subtitle: String,
        statusText: String,
        statusGood: Bool,
        primaryAction: PrimaryAction?,
        openSettings: @escaping () -> Void
    ) -> some View {
        HStack(alignment: .center, spacing: 16) {
            Circle()
                .fill(statusGood ? Color.green : Color.orange)
                .frame(width: 10, height: 10)

            VStack(alignment: .leading, spacing: 2) {
                Text(title).font(.system(size: 14, weight: .semibold))
                Text(subtitle).font(.system(size: 11)).foregroundStyle(.secondary)
                Text(statusText).font(.system(size: 11)).foregroundStyle(statusGood ? .green : .orange)
            }

            Spacer()

            if let action = primaryAction {
                Button(action.label, action: action.run)
                    .buttonStyle(.borderedProminent)
            }

            Button("Open Settings", action: openSettings)
                .buttonStyle(.bordered)
        }
        .padding(.horizontal, 28)
        .padding(.vertical, 14)
    }

    // MARK: - Primary actions

    private struct PrimaryAction {
        let label: String
        let run: () -> Void
    }

    private var micPrimaryAction: PrimaryAction? {
        switch micStatus {
        case .notDetermined:
            return PrimaryAction(label: "Request") {
                AVCaptureDevice.requestAccess(for: .audio) { _ in
                    DispatchQueue.main.async { refreshAll() }
                }
            }
        case .denied, .restricted:
            return nil
        case .authorized:
            return nil
        @unknown default:
            return nil
        }
    }

    private var speechPrimaryAction: PrimaryAction? {
        switch speechStatus {
        case .notDetermined:
            return PrimaryAction(label: "Request") {
                SFSpeechRecognizer.requestAuthorization { _ in
                    DispatchQueue.main.async { refreshAll() }
                }
            }
        case .denied, .restricted, .authorized:
            return nil
        @unknown default:
            return nil
        }
    }

    private var screenPrimaryAction: PrimaryAction? {
        if screenHasAccess { return nil }
        return PrimaryAction(label: "Request") {
            CGRequestScreenCaptureAccess()
            // Status won't update until relaunch, but refreshAll will pick it
            // up on the next poll tick.
        }
    }

    // MARK: - Status text

    private var micStatusText: String {
        switch micStatus {
        case .notDetermined: return "Not asked yet."
        case .restricted:    return "Blocked by parental / profile policy."
        case .denied:        return "Denied. Toggle Nomi on in System Settings → Privacy & Security → Microphone."
        case .authorized:    return "Granted."
        @unknown default:    return "Unknown state."
        }
    }

    private var speechStatusText: String {
        switch speechStatus {
        case .notDetermined: return "Not asked yet."
        case .restricted:    return "Blocked by parental / profile policy."
        case .denied:        return "Denied. Toggle Nomi on in System Settings → Privacy & Security → Speech Recognition."
        case .authorized:    return "Granted."
        @unknown default:    return "Unknown state."
        }
    }

    private var screenStatusText: String {
        screenHasAccess
        ? "Granted."
        : "Not granted. After enabling in System Settings, quit Nomi and relaunch — macOS requires a restart for this permission to take effect."
    }

    // MARK: - Helpers

    private func refreshAll() {
        micStatus      = AVCaptureDevice.authorizationStatus(for: .audio)
        speechStatus   = SFSpeechRecognizer.authorizationStatus()
        screenHasAccess = CGPreflightScreenCaptureAccess()
    }

    private func openPrivacyPane(_ key: String) {
        if let url = URL(string: "x-apple.systempreferences:com.apple.preference.security?Privacy_\(key)") {
            NSWorkspace.shared.open(url)
        }
    }

    /// 4-second mic test. Starts the real speech engine in dictation mode and
    /// reports whether any transcript came back.
    private func testMic() async {
        isTestingMic = true
        micTestResult = "Say something now — I'm listening for 4 seconds…"

        let box = TranscriptBox()
        let previousDictation = SpeechEngine.shared.onDictation
        SpeechEngine.shared.onDictation = { text, _ in
            Task { await box.set(text) }
        }
        SpeechEngine.shared.startDictation()

        try? await Task.sleep(nanoseconds: 4_000_000_000)
        SpeechEngine.shared.stop()
        SpeechEngine.shared.onDictation = previousDictation
        let heard = await box.value
        isTestingMic = false

        if heard.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
            micTestResult = "✗ I didn't hear anything. If the orange mic indicator didn't appear in the menu bar while testing, macOS is silently denying mic access — check Privacy & Security → Microphone and toggle Nomi on/off."
        } else {
            micTestResult = "✓ I heard: \"\(heard)\""
        }
    }
}

private actor TranscriptBox {
    private var text: String = ""
    func set(_ s: String) { text = s }
    var value: String { text }
}

```