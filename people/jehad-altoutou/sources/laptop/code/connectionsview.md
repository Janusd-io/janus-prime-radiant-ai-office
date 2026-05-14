---
type: source
source_type: laptop
title: ConnectionsView
slug: connectionsview
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/ConnectionsView.swift
original_size: 7636
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# ConnectionsView

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/ConnectionsView.swift` on 2026-05-14._

```swift
import SwiftUI
import AppKit

/// The Connections panel. One row per service. Each row has a single
/// "Connect" button — no token fields, no developer console references,
/// no mention of OAuth, client IDs, or scopes.
///
/// For services that have OAuth (Google, Linear, Notion) clicking Connect
/// opens the provider's real sign-in page. For Fireflies (no OAuth exists)
/// clicking Connect opens their developer-settings page AND reveals a
/// paste field, because that's the only flow they offer. It's still one
/// click to start; we just can't automate the last step.
struct ConnectionsView: View {

    @State private var busyService: ConnectableService?
    @State private var statusByService: [ConnectableService: String] = [:]
    @State private var firefliesPasteVisible: Bool = Config.isConnected(.fireflies) == false && false
    @State private var firefliesToken: String = ""
    @State private var refreshKey = UUID()

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            header
                .padding(.horizontal, 28)
                .padding(.top, 24)
                .padding(.bottom, 16)

            Divider()

            ScrollView {
                VStack(spacing: 0) {
                    ForEach(ConnectableService.allCases, id: \.self) { service in
                        ServiceRow(
                            service: service,
                            isBusy: busyService == service,
                            status: statusByService[service],
                            showFirefliesPaste: service == .fireflies && firefliesPasteVisible,
                            firefliesToken: $firefliesToken,
                            onConnect:    { await connect(service) },
                            onDisconnect: { disconnect(service) },
                            onSaveFireflies: { saveFirefliesToken() }
                        )
                        .id(service.hashValue.hashValue &+ refreshKey.hashValue)
                        Divider().padding(.leading, 28)
                    }
                }
            }
        }
        .frame(width: 540, height: 620)
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("Connect your accounts")
                .font(.system(size: 22, weight: .semibold))
            Text("One click per service. Your sign-in happens in your browser; Nomi never sees your password. Tokens are stored in the macOS Keychain.")
                .font(.system(size: 12))
                .foregroundStyle(.secondary)
                .fixedSize(horizontal: false, vertical: true)
        }
    }

    private func connect(_ service: ConnectableService) async {
        // Fireflies has no OAuth — show the paste field instead.
        if service == .fireflies {
            if let url = service.tokenIssuePageURL {
                NSWorkspace.shared.open(url)
            }
            firefliesPasteVisible = true
            statusByService[service] = "Generate a key in the page that just opened, then paste it below."
            return
        }

        busyService = service
        statusByService[service] = "Opening browser…"
        let outcome = await OAuthCoordinator.connect(service)
        busyService = nil

        switch outcome {
        case .connected:
            statusByService[service] = nil
        case .cancelled:
            statusByService[service] = "Cancelled. Click Connect again when you're ready."
        case .notConfigured:
            statusByService[service] = "Nomi is still being set up for \(service.displayName). The Nomi team is working on it."
        case .failed(let msg):
            statusByService[service] = "Didn't work: \(msg)"
        }
        refreshKey = UUID()  // force isConnected re-query
    }

    private func disconnect(_ service: ConnectableService) {
        Config.setUserSecret("", for: service.userServiceKey)
        statusByService[service] = nil
        if service == .fireflies {
            firefliesPasteVisible = false
            firefliesToken = ""
        }
        refreshKey = UUID()
    }

    private func saveFirefliesToken() {
        let trimmed = firefliesToken.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty else { return }
        Config.setUserSecret(trimmed, for: .fireflies)
        firefliesPasteVisible = false
        firefliesToken = ""
        statusByService[.fireflies] = nil
        refreshKey = UUID()
    }
}

// MARK: - ServiceRow

private struct ServiceRow: View {
    let service: ConnectableService
    let isBusy: Bool
    let status: String?
    let showFirefliesPaste: Bool
    @Binding var firefliesToken: String
    let onConnect: () async -> Void
    let onDisconnect: () -> Void
    let onSaveFireflies: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack(alignment: .center, spacing: 14) {
                Image(systemName: icon)
                    .font(.system(size: 18, weight: .medium))
                    .frame(width: 28, height: 28)
                    .foregroundStyle(tint)

                VStack(alignment: .leading, spacing: 2) {
                    Text(service.displayName)
                        .font(.system(size: 15, weight: .semibold))
                    Text(service.isConnected ? "Connected" : "Not connected")
                        .font(.system(size: 12))
                        .foregroundStyle(service.isConnected ? .green : .secondary)
                }

                Spacer()

                if service.isConnected {
                    Button("Disconnect", action: onDisconnect)
                        .buttonStyle(.bordered)
                } else if isBusy {
                    ProgressView().controlSize(.small)
                } else {
                    Button {
                        Task { await onConnect() }
                    } label: {
                        Text("Connect")
                            .font(.system(size: 13, weight: .semibold))
                            .frame(minWidth: 80)
                    }
                    .buttonStyle(.borderedProminent)
                    .tint(tint)
                }
            }

            if let status, !status.isEmpty {
                Text(status)
                    .font(.system(size: 11))
                    .foregroundStyle(.secondary)
                    .padding(.leading, 42)
                    .fixedSize(horizontal: false, vertical: true)
            }

            if showFirefliesPaste {
                HStack {
                    SecureField("Paste key from the page that just opened…", text: $firefliesToken)
                        .textFieldStyle(.roundedBorder)
                    Button("Save", action: onSaveFireflies)
                        .disabled(firefliesToken.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
                }
                .padding(.leading, 42)
            }
        }
        .padding(.horizontal, 28)
        .padding(.vertical, 16)
    }

    private var icon: String {
        switch service {
        case .googleCalendar: return "calendar"
        case .linear:         return "checkmark.square"
        case .notion:         return "doc.text"
        case .fireflies:      return "waveform.badge.mic"
        }
    }

    private var tint: Color {
        switch service {
        case .googleCalendar: return .blue
        case .linear:         return .indigo
        case .notion:         return .primary
        case .fireflies:      return .orange
        }
    }
}

```