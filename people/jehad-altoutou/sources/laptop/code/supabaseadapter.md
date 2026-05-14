---
type: source
source_type: laptop
title: SupabaseAdapter
slug: supabaseadapter
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/SupabaseAdapter.swift
original_size: 4579
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# SupabaseAdapter

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/SupabaseAdapter.swift` on 2026-05-14._

```swift
import Foundation

public final class SupabaseAdapter {
    public static let shared = SupabaseAdapter()
    private init() {}
    
    // The keys provided by the enterprise cloud
    private let supabaseURL = "https://gxqwoljddzpajjlwrkig.supabase.co/rest/v1/nomi_mesh"
    private let anonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd4cXdvbGpkZHpwYWpqbHdya2lnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ5NDAxNDksImV4cCI6MjA5MDUxNjE0OX0.Icmuv4xAv0__kIu0ojDlrDpAByi33ebjlnTm_diyri0"
    
    private func baseRequest(url: URL, method: String) -> URLRequest {
        var req = URLRequest(url: url)
        req.httpMethod = method
        req.setValue(anonKey, forHTTPHeaderField: "apikey")
        req.setValue("Bearer \(anonKey)", forHTTPHeaderField: "Authorization")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        return req
    }
    
    /// 1. Send an initial message to a target user
    public func dispatchMeshMessage(to target: String, content: String) async throws -> String {
        guard let url = URL(string: supabaseURL) else { throw URLError(.badURL) }
        var req = baseRequest(url: url, method: "POST")
        req.setValue("return=representation", forHTTPHeaderField: "Prefer")
        
        let payload: [String: Any] = [
            "from_user": Config.identity,
            "to_user": target,
            "content": content,
            "status": "pending"
        ]
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode >= 200 && http.statusCode < 300 else {
            ActivityLogger.shared.record(action: "Supabase Error", target: "Dispatch", status: String(data: data, encoding: .utf8) ?? "Err")
            throw URLError(.badServerResponse)
        }
        
        return "Message routed to \(target) through the Cloud Mesh successfully. Polling for their response..."
    }
    
    /// 2. Michael replies to Jehovah's message
    public func replyMeshMessage(id: String, replyText: String) async throws -> String {
        guard let url = URL(string: "\(supabaseURL)?id=eq.\(id)") else { throw URLError(.badURL) }
        var req = baseRequest(url: url, method: "PATCH")
        
        let payload: [String: Any] = [
            "reply": replyText,
            "status": "replied"
        ]
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode >= 200 && http.statusCode < 300 else {
             throw URLError(.badServerResponse)
        }
        return "Reply dispatched through the Cloud Mesh."
    }
    
    /// 3. Poll for messages meant FOR me
    public func fetchIncomingMessages() async throws -> [[String: Any]] {
        let endpoint = "\(supabaseURL)?to_user=eq.\(Config.identity)&status=eq.pending"
        guard let url = URL(string: endpoint) else { throw URLError(.badURL) }
        let req = baseRequest(url: url, method: "GET")
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else { return [] }
        return try JSONSerialization.jsonObject(with: data) as? [[String: Any]] ?? []
    }
    
    /// 4. Poll for replies back to MY original messages
    public func fetchMyReplies() async throws -> [[String: Any]] {
        let endpoint = "\(supabaseURL)?from_user=eq.\(Config.identity)&status=eq.replied"
        guard let url = URL(string: endpoint) else { throw URLError(.badURL) }
        let req = baseRequest(url: url, method: "GET")
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else { return [] }
        return try JSONSerialization.jsonObject(with: data) as? [[String: Any]] ?? []
    }
    
    /// 5. Clean up logic so we don't read duplicates
    public func archiveMessage(id: String) async throws {
        guard let url = URL(string: "\(supabaseURL)?id=eq.\(id)") else { throw URLError(.badURL) }
        var req = baseRequest(url: url, method: "PATCH")
        let payload: [String: Any] = ["status": "archived"]
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        let _ = try? await URLSession.shared.data(for: req)
    }
}

```