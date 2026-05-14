---
type: source
source_type: laptop
title: ApprovalCardView
slug: approvalcardview
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/ApprovalCardView.swift
original_size: 5419
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# ApprovalCardView

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/ApprovalCardView.swift` on 2026-05-14._

```swift
import SwiftUI

struct ApprovalCardView: View {
    @ObservedObject var engine: NomiStateEngine
    @State private var appeared = false
    @State private var iconPulse: CGFloat = 1.0

    var body: some View {
        VStack(spacing: 14) {

            // ── Action badge
            HStack(spacing: 6) {
                Image(systemName: actionIcon)
                    .font(.system(size: 10, weight: .bold))
                    .foregroundColor(Color(hue: 0.08, saturation: 0.7, brightness: 1.0))
                Text("Requires Approval")
                    .font(.system(size: 10, weight: .bold, design: .rounded))
                    .foregroundColor(Color(hue: 0.08, saturation: 0.7, brightness: 1.0))
                    .textCase(.uppercase)
                    .tracking(0.8)
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 5)
            .background(
                Capsule()
                    .fill(Color(hue: 0.08, saturation: 0.8, brightness: 0.6, opacity: 0.25))
                    .overlay(Capsule().stroke(Color(hue: 0.08, saturation: 0.7, brightness: 0.9, opacity: 0.4), lineWidth: 1))
            )

            // ── Icon
            ZStack {
                Circle()
                    .fill(Color(hue: 0.08, saturation: 0.6, brightness: 0.5, opacity: 0.2))
                    .frame(width: 52, height: 52)
                    .scaleEffect(iconPulse)

                Image(systemName: actionIcon)
                    .font(.system(size: 22, weight: .semibold))
                    .foregroundStyle(
                        LinearGradient(
                            colors: [.orange, Color(hue: 0.08, saturation: 0.9, brightness: 1.0)],
                            startPoint: .topLeading, endPoint: .bottomTrailing
                        )
                    )
            }

            // ── Action name
            Text(engine.pendingActionName)
                .font(.system(size: 15, weight: .semibold, design: .rounded))
                .foregroundColor(.white)
                .multilineTextAlignment(.center)

            // ── Detail preview
            if let data = engine.pendingActionDetails.data(using: .utf8),
               let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
               let titleVal = json["title"] as? String {
                Text("\"\(titleVal)\"")
                    .font(.system(size: 12, design: .rounded))
                    .foregroundColor(.white.opacity(0.55))
                    .multilineTextAlignment(.center)
                    .lineLimit(2)
                    .padding(.horizontal, 8)
            }

            // ── Buttons
            HStack(spacing: 10) {
                // Decline
                Button(action: { engine.rejectAction() }) {
                    Text("Decline")
                        .font(.system(size: 13, weight: .semibold, design: .rounded))
                        .foregroundColor(.white.opacity(0.75))
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 9)
                        .overlay(
                            RoundedRectangle(cornerRadius: 12)
                                .stroke(Color.white.opacity(0.18), lineWidth: 1)
                        )
                }
                .buttonStyle(PlainButtonStyle())

                // Approve
                Button(action: { engine.approveAction() }) {
                    Text("Approve")
                        .font(.system(size: 13, weight: .bold, design: .rounded))
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 9)
                        .background(
                            LinearGradient(
                                colors: [
                                    Color(hue: 0.38, saturation: 0.7, brightness: 0.8),
                                    Color(hue: 0.50, saturation: 0.6, brightness: 0.85)
                                ],
                                startPoint: .topLeading, endPoint: .bottomTrailing
                            )
                            .clipShape(RoundedRectangle(cornerRadius: 12))
                        )
                        .shadow(color: Color(hue: 0.38, saturation: 0.5, brightness: 0.6, opacity: 0.4),
                                radius: 8, x: 0, y: 4)
                }
                .buttonStyle(PlainButtonStyle())
            }
            .padding(.horizontal, 2)
        }
        .padding(.horizontal, 18)
        .padding(.vertical, 10)
        .opacity(appeared ? 1 : 0)
        .offset(y: appeared ? 0 : 10)
        .onAppear {
            withAnimation(.spring(response: 0.4, dampingFraction: 0.75)) { appeared = true }
            withAnimation(.easeInOut(duration: 1.4).repeatForever(autoreverses: true)) { iconPulse = 1.18 }
        }
    }

    private var actionIcon: String {
        let name = engine.pendingActionName.lowercased()
        if name.contains("linear")   { return "checkmark.square.fill" }
        if name.contains("calendar") { return "calendar.badge.plus" }
        if name.contains("notion")   { return "doc.fill" }
        if name.contains("message")  { return "bubble.left.and.bubble.right.fill" }
        if name.contains("record")   { return "record.circle" }
        return "bolt.fill"
    }
}

```