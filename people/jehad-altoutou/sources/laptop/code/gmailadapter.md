---
type: source
source_type: laptop
title: GmailAdapter
slug: gmailadapter
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/GmailAdapter.swift
original_size: 5907
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# GmailAdapter

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/GmailAdapter.swift` on 2026-05-14._

```swift
import Foundation

/// Minimal Gmail adapter — send and search.
///
/// Uses the same access token as `CalendarAdapter` (both live under the single
/// Google OAuth grant). If either scope was denied during consent, the call
/// returns a helpful error instead of a raw 403.
///
/// Auth: `Authorization: Bearer <googleCalendarToken>`.
///
/// This file deliberately does NOT implement mark-read / trash / delete /
/// labels — those require the `gmail.modify` restricted scope which makes
/// production verification significantly more expensive. Add later if needed.
public final class GmailAdapter {
    public static let shared = GmailAdapter()

    private let base = "https://gmail.googleapis.com/gmail/v1/users/me"

    // MARK: - Send

    public func sendEmail(to recipient: String, subject: String, body: String) async throws -> String {
        guard !Config.googleCalendarToken.isEmpty else {
            return "Gmail not connected. Ask the user to open Connections and click Connect with Google."
        }

        // RFC 2822 message, URL-safe base64 encoded, as required by Gmail API.
        let rfc = """
        From: me
        To: \(recipient)
        Subject: \(subject)
        Content-Type: text/plain; charset=UTF-8

        \(body)
        """
        guard let data = rfc.data(using: .utf8) else {
            throw URLError(.cannotDecodeContentData)
        }
        let raw = data
            .base64EncodedString()
            .replacingOccurrences(of: "+", with: "-")
            .replacingOccurrences(of: "/", with: "_")
            .replacingOccurrences(of: "=", with: "")

        let url = URL(string: "\(base)/messages/send")!
        var req = URLRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(Config.googleCalendarToken)", forHTTPHeaderField: "Authorization")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        req.httpBody = try JSONSerialization.data(withJSONObject: ["raw": raw])

        let (respData, response) = try await URLSession.shared.data(for: req)
        guard (response as? HTTPURLResponse)?.statusCode == 200 else {
            let text = String(data: respData, encoding: .utf8) ?? "?"
            if text.contains("insufficient") || text.contains("ACCESS_TOKEN_SCOPE_INSUFFICIENT") {
                return "Gmail send permission was declined during sign-in. Reconnect Google to grant Gmail access."
            }
            return "Gmail send failed: \(text.prefix(240))"
        }
        return "Email sent to \(recipient)."
    }

    // MARK: - Search / read recent

    public struct MessageSummary {
        public let id: String
        public let snippet: String
        public let from: String
        public let subject: String
        public let date: String
    }

    /// Search using Gmail's standard query language (e.g. `from:jehad is:unread`).
    /// Returns up to `limit` message summaries (id, from, subject, snippet).
    public func search(query: String, limit: Int = 10) async throws -> [MessageSummary] {
        guard !Config.googleCalendarToken.isEmpty else { return [] }

        var listURL = URLComponents(string: "\(base)/messages")!
        listURL.queryItems = [
            URLQueryItem(name: "q", value: query),
            URLQueryItem(name: "maxResults", value: String(limit))
        ]
        var listReq = URLRequest(url: listURL.url!)
        listReq.setValue("Bearer \(Config.googleCalendarToken)", forHTTPHeaderField: "Authorization")

        let (listData, listResp) = try await URLSession.shared.data(for: listReq)
        guard (listResp as? HTTPURLResponse)?.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }
        let listJSON = try JSONSerialization.jsonObject(with: listData) as? [String: Any]
        let ids: [String] = ((listJSON?["messages"] as? [[String: Any]]) ?? [])
            .compactMap { $0["id"] as? String }

        // Fetch metadata for each (Gmail charges per message so we keep it slim).
        var out: [MessageSummary] = []
        for id in ids {
            var detailURL = URLComponents(string: "\(base)/messages/\(id)")!
            detailURL.queryItems = [
                URLQueryItem(name: "format", value: "metadata"),
                URLQueryItem(name: "metadataHeaders", value: "From"),
                URLQueryItem(name: "metadataHeaders", value: "Subject"),
                URLQueryItem(name: "metadataHeaders", value: "Date")
            ]
            var detailReq = URLRequest(url: detailURL.url!)
            detailReq.setValue("Bearer \(Config.googleCalendarToken)", forHTTPHeaderField: "Authorization")
            guard let (detailData, _) = try? await URLSession.shared.data(for: detailReq),
                  let obj = try? JSONSerialization.jsonObject(with: detailData) as? [String: Any]
            else { continue }

            let snippet = obj["snippet"] as? String ?? ""
            let payload = obj["payload"] as? [String: Any]
            let headers = (payload?["headers"] as? [[String: Any]]) ?? []
            func header(_ name: String) -> String {
                headers.first(where: { ($0["name"] as? String) == name })?["value"] as? String ?? ""
            }
            out.append(.init(
                id: id,
                snippet: snippet,
                from: header("From"),
                subject: header("Subject"),
                date: header("Date")
            ))
        }
        return out
    }

    /// Formats `search(query:)` output for the LLM.
    public func searchFormatted(query: String, limit: Int = 10) async throws -> String {
        let msgs = try await search(query: query, limit: limit)
        if msgs.isEmpty { return "No messages matched '\(query)'." }
        return msgs.map { "• \($0.from) — \($0.subject) — \($0.snippet.prefix(140))" }
            .joined(separator: "\n")
    }
}

```