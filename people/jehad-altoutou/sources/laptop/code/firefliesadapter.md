---
type: source
source_type: laptop
title: FirefliesAdapter
slug: firefliesadapter
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/FirefliesAdapter.swift
original_size: 7980
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# FirefliesAdapter

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/FirefliesAdapter.swift` on 2026-05-14._

```swift
import Foundation

public final class FirefliesAdapter {
    public static let shared = FirefliesAdapter()
    private init() {}
    
    private let apiURL = "https://api.fireflies.ai/graphql"
    private var token: String { Config.firefliesAPIKey }
    
    /// Fetches recent transcript summaries natively from GraphQL
    public func pullRecentMeetings() async throws -> String {
        guard let url = URL(string: apiURL) else { throw URLError(.badURL) }
        var req = URLRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let query = """
        query {
            transcripts(limit: 5) {
                id
                title
                date
                summary {
                    action_items
                    overview
                    shorthand_bullet
                }
            }
        }
        """
        
        let payload: [String: Any] = ["query": query]
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            return "Failed to authenticate or fetch GraphQL from Fireflies."
        }
        
        guard let json = try JSONSerialization.jsonObject(with: data) as? [String: Any] else {
            return "Could not deserialize JSON."
        }
        
        if let errors = json["errors"] as? [[String: Any]] {
            let errorMsgs = errors.compactMap { $0["message"] as? String }.joined(separator: ", ")
            return "Fireflies GraphQL Error: \(errorMsgs)"
        }
        
        guard let dataNode = json["data"] as? [String: Any],
              let transcripts = dataNode["transcripts"] as? [[String: Any]] else {
            return "Could not parse transcripts."
        }
        
        var out = "Recent Fireflies Meetings:\n"
        for t in transcripts {
            let title = t["title"] as? String ?? "Untitled"
            let date = t["date"] as? Double ?? 0
            let dateString = Date(timeIntervalSince1970: date / 1000).formatted(date: .abbreviated, time: .shortened)
            
            out += "## \(title) (\(dateString))\n"
            if let sum = t["summary"] as? [String: Any] {
                if let ov = sum["overview"] as? String { out += "Overview: \(ov)\n" }
                if let bp = sum["shorthand_bullet"] as? String { out += "Notes: \(bp)\n" }
                if let ac = sum["action_items"] as? String { out += "Action Items: \(ac)\n" }
            }
            out += "\n"
        }
        
        return out
    }
    
    public struct TranscriptMetadata {
        public let id: String
        public let title: String
        public let date: Double
    }
    
    public func fetchRecentTranscriptModels() async throws -> [TranscriptMetadata] {
        guard let url = URL(string: apiURL) else { throw URLError(.badURL) }
        var req = URLRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        let query = "query { transcripts(limit: 5) { id title date } }"
        req.httpBody = try JSONSerialization.data(withJSONObject: ["query": query])
        let (data, _) = try await URLSession.shared.data(for: req)
        guard let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
              let dataNode = json["data"] as? [String: Any],
              let transcripts = dataNode["transcripts"] as? [[String: Any]] else {
            return []
        }
        return transcripts.compactMap { t in
            guard let id = t["id"] as? String, let title = t["title"] as? String, let date = t["date"] as? Double else { return nil }
            return TranscriptMetadata(id: id, title: title, date: date)
        }
    }
    
    public func addToLiveMeeting(url: String, title: String) async throws -> String {
        guard let endpoint = URL(string: apiURL) else { throw URLError(.badURL) }
        var req = URLRequest(url: endpoint)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let query = """
        mutation AddToLiveMeeting($url: String!, $title: String!) {
            addToLiveMeeting(meeting_link: $url, title: $title) {
                success
            }
        }
        """
        
        let payload: [String: Any] = [
            "query": query,
            "variables": ["url": url, "title": title]
        ]
        
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            return "Failed to send Fireflies to live meeting (HTTP \((response as? HTTPURLResponse)?.statusCode ?? 0))."
        }
        
        if let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
           let errs = json["errors"] as? [[String: Any]] {
            let errorMsgs = errs.compactMap { $0["message"] as? String }.joined(separator: ", ")
            return "Fireflies Error: \(errorMsgs)"
        }
        return "SUCCESS! Fred, the Fireflies bot, has been dispatched and will join the selected meeting link momentarily to start recording."
    }
    
    // removed fallback since success object is strongly typed
    
    public func getTranscript(id: String) async throws -> String {
        guard let url = URL(string: apiURL) else { throw URLError(.badURL) }
        var req = URLRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let query = """
        query Transcript($id: String!) {
            transcript(id: $id) {
                title
                date
                summary {
                    action_items
                    overview
                    shorthand_bullet
                }
                sentences {
                    speaker_name
                    text
                }
            }
        }
        """
        
        let payload: [String: Any] = ["query": query, "variables": ["id": id]]
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, _) = try await URLSession.shared.data(for: req)
        if let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
           let dataNode = json["data"] as? [String: Any],
           let t = dataNode["transcript"] as? [String: Any] {
            
            var out = "Transcript: \(t["title"] as? String ?? "Untitled")\n\n"
            
            if let sum = t["summary"] as? [String: Any] {
                out += "=== FIREFLIES SUMMARY ===\n"
                out += "Overview: \(sum["overview"] as? String ?? "")\n"
                out += "Bullets: \(sum["shorthand_bullet"] as? String ?? "")\n"
                out += "Tasks: \(sum["action_items"] as? String ?? "")\n\n"
            }
            
            if let sentences = t["sentences"] as? [[String: Any]] {
                out += "=== RAW DISCUSSION ===\n"
                for s in sentences {
                    let speaker = s["speaker_name"] as? String ?? "Unknown"
                    let text = s["text"] as? String ?? ""
                    out += "[\(speaker)]: \(text)\n"
                }
            }
            return out
        }
        return "Failed to parse transcript details."
    }
}

```