---
type: source
source_type: laptop
title: ConnectToolCardView
slug: connecttoolcardview
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/ConnectToolCardView.swift
original_size: 8710
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# ConnectToolCardView

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/ConnectToolCardView.swift` on 2026-05-14._

```swift
import SwiftUI
import AppKit

/// The notch-side Connect card. Shown when the user types `/connect <service>`
/// or when the state engine enters `.connectTool`. One button, one flow.
///
/// Tapping Connect triggers the real OAuth flow via `OAuthCoordinator`. No
/// developer-tool URLs, no Google OAuth Playground, no token pasting for
/// services that support OAuth. Fireflies is the one exception and surfaces
/// a short hint telling the user to use the full Connections panel.
struct ConnectToolCardView: View {
    @ObservedObject var engine: NomiStateEngine

    @State private var isBusy = false
    @State private var status: String = ""
    @State private var appeared = false
    @State private var checkRingProgress: CGFloat = 0
    @State private var iconScale: CGFloat = 1.0

    private var service: ConnectableService? {
        OAuthCoordinator.parse(engine.connectingServiceName)
    }

    var body: some View {
        VStack(spacing: 16) {

            // ── Service icon badge
            ZStack {
                if isConnected {
                    Circle()
                        .trim(from: 0, to: checkRingProgress)
                        .stroke(
                            LinearGradient(
                                colors: [serviceColor.opacity(0.6), serviceColor],
                                startPoint: .topLeading, endPoint: .bottomTrailing
                            ),
                            style: StrokeStyle(lineWidth: 2, lineCap: .round)
                        )
                        .rotationEffect(.degrees(-90))
                        .frame(width: 64, height: 64)
                }

                Circle()
                    .fill(isConnected ? serviceColor.opacity(0.15) : Color.white.opacity(0.07))
                    .frame(width: 56, height: 56)
                    .overlay(
                        Circle().stroke(
                            isConnected ? serviceColor.opacity(0.4) : Color.white.opacity(0.12),
                            lineWidth: 1
                        )
                    )

                Image(systemName: isConnected ? "checkmark" : serviceIcon)
                    .font(.system(size: 20, weight: .semibold))
                    .foregroundStyle(
                        isConnected
                        ? LinearGradient(colors: [serviceColor, serviceColor.opacity(0.7)],
                                         startPoint: .topLeading, endPoint: .bottomTrailing)
                        : LinearGradient(colors: [.white.opacity(0.7), .white.opacity(0.45)],
                                         startPoint: .topLeading, endPoint: .bottomTrailing)
                    )
                    .scaleEffect(iconScale)
            }
            .padding(.top, 12)

            // ── Status text
            Group {
                if isConnected {
                    Text("Connected to \(displayName)")
                        .font(.system(size: 14, weight: .semibold, design: .rounded))
                        .foregroundColor(serviceColor)
                } else {
                    VStack(spacing: 4) {
                        Text(displayName)
                            .font(.system(size: 15, weight: .bold, design: .rounded))
                            .foregroundColor(.white)
                        Text(status.isEmpty ? "Not connected yet" : status)
                            .font(.system(size: 12, design: .rounded))
                            .foregroundColor(.white.opacity(0.55))
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 10)
                            .fixedSize(horizontal: false, vertical: true)
                    }
                }
            }

            // ── Connect button
            if !isConnected {
                Button(action: connect) {
                    HStack(spacing: 6) {
                        if isBusy {
                            ProgressView().controlSize(.small).tint(.white)
                        } else {
                            Image(systemName: "arrow.up.forward.app")
                                .font(.system(size: 12, weight: .semibold))
                        }
                        Text(isBusy ? "Opening browser…" : "Connect")
                            .font(.system(size: 13, weight: .bold, design: .rounded))
                    }
                    .foregroundColor(.white)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 10)
                    .background(
                        LinearGradient(
                            colors: [serviceColor.opacity(0.75), serviceColor.opacity(0.5)],
                            startPoint: .topLeading, endPoint: .bottomTrailing
                        )
                        .clipShape(RoundedRectangle(cornerRadius: 12))
                    )
                    .shadow(color: serviceColor.opacity(0.35), radius: 8, x: 0, y: 4)
                }
                .buttonStyle(PlainButtonStyle())
                .disabled(isBusy || service == nil)
                .padding(.horizontal, 2)
            }

            // ── Dismiss
            Button(action: dismiss) {
                Text(isConnected ? "Done" : "Cancel")
                    .font(.system(size: 12, weight: .medium, design: .rounded))
                    .foregroundColor(.white.opacity(0.4))
            }
            .buttonStyle(PlainButtonStyle())
            .padding(.bottom, 8)
        }
        .padding(.horizontal, 20)
        .opacity(appeared ? 1 : 0)
        .offset(y: appeared ? 0 : 12)
        .onAppear {
            withAnimation(.spring(response: 0.45, dampingFraction: 0.75)) { appeared = true }
            if isConnected {
                withAnimation(.easeOut(duration: 0.8).delay(0.2)) { checkRingProgress = 1 }
                withAnimation(.spring(response: 0.3, dampingFraction: 0.5).delay(0.3)) { iconScale = 1.2 }
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.6) {
                    withAnimation(.spring(response: 0.3, dampingFraction: 0.6)) { iconScale = 1.0 }
                }
            }
        }
    }

    // MARK: - Actions

    private func connect() {
        guard let service else {
            status = "I don't know how to connect '\(engine.connectingServiceName)'."
            return
        }

        if service == .fireflies {
            // No OAuth — direct the user to the Connections panel, which has
            // the paste field.
            if let url = service.tokenIssuePageURL { NSWorkspace.shared.open(url) }
            status = "Open the Connections panel from the menubar to paste your Fireflies key."
            return
        }

        isBusy = true
        status = ""
        Task {
            let outcome = await OAuthCoordinator.connect(service)
            await MainActor.run {
                isBusy = false
                switch outcome {
                case .connected:
                    engine.showSuccessToast("Connected to \(service.displayName) ✓")
                case .cancelled:
                    status = "Cancelled. Try again when you're ready."
                case .notConfigured:
                    status = "Nomi is still being set up for \(service.displayName)."
                case .failed(let msg):
                    status = msg
                }
            }
        }
    }

    private func dismiss() {
        withAnimation(.spring(response: 0.4, dampingFraction: 0.7)) {
            engine.currentState = .idle
            engine.isExpanded = false
        }
    }

    // MARK: - Helpers

    private var displayName: String {
        service?.displayName ?? engine.connectingServiceName
    }

    private var isConnected: Bool {
        service?.isConnected ?? false
    }

    private var serviceColor: Color {
        switch service {
        case .linear:         return Color(hue: 0.68, saturation: 0.8, brightness: 0.95)
        case .googleCalendar: return Color(hue: 0.03, saturation: 0.8, brightness: 0.95)
        case .notion:         return Color.white.opacity(0.85)
        case .fireflies:      return Color(hue: 0.07, saturation: 0.85, brightness: 0.95)
        case nil:             return Color(hue: 0.60, saturation: 0.6, brightness: 0.9)
        }
    }

    private var serviceIcon: String {
        switch service {
        case .linear:         return "checkmark.square"
        case .googleCalendar: return "calendar"
        case .notion:         return "doc.text"
        case .fireflies:      return "waveform.badge.mic"
        case nil:             return "link.badge.plus"
        }
    }
}

```