---
type: source
source_type: laptop
title: NotionAdapter
slug: notionadapter
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/NotionAdapter.swift
original_size: 14106
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# NotionAdapter

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/NotionAdapter.swift` on 2026-05-14._

```swift
import Foundation

public final class NotionAdapter {
    public static let shared = NotionAdapter()
    private init() {}
    
    private let baseURL = "https://api.notion.com/v1"
    
    private var headers: [String: String] {
        return [
            "Authorization": "Bearer \(Config.notionAPIKey)",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        ]
    }
    
    /// Searches the connected Notion workspace
    public func search(query: String) async throws -> String {
        guard let url = URL(string: "\(baseURL)/search") else { throw URLError(.badURL) }
        var req = URLRequest(url: url)
        req.httpMethod = "POST"
        for (k,v) in headers { req.setValue(v, forHTTPHeaderField: k) }
        
        let payload: [String: Any] = [
            "query": query,
            "sort": ["direction": "descending", "timestamp": "last_edited_time"],
            "page_size": 10
        ]
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            let errorText = String(data: data, encoding: .utf8) ?? ""
            return "Failed to search Notion workspace (Status: \((response as? HTTPURLResponse)?.statusCode ?? 0)). Details: \(errorText)"
        }
        
        guard let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
              let results = json["results"] as? [[String: Any]] else {
            return "No results found in Notion."
        }
        
        var out = "Notion Search Results:\n"
        if results.isEmpty {
            return "Notion returned ZERO results for this query. The user either misspelled the title, or MORE LIKELY, they failed to manually grant the Integration access to this page."
        }
        
        for item in results {
            let id = item["id"] as? String ?? "unknown"
            let object = item["object"] as? String ?? ""
            var title = "Untitled"
            
            if let props = item["properties"] as? [String: Any] {
                // Notion property tree is deeply nested
                for (_, propVal) in props {
                    if let propDict = propVal as? [String: Any],
                       let type = propDict["type"] as? String, type == "title",
                       let titleArr = propDict["title"] as? [[String: Any]] {
                        title = titleArr.compactMap { $0["plain_text"] as? String }.joined(separator: "")
                        break
                    }
                }
            }
            if title == "Untitled", let rawTitle = item["title"] as? String {
                title = rawTitle
            }
            out += "- [\(object)] \(title) (ID: \(id))\n"
        }
        
        return out
    }
    
    /// Pulls blocks for a specific page ID
    public func readPage(id: String) async throws -> String {
        guard let url = URL(string: "\(baseURL)/blocks/\(id)/children?page_size=50") else { throw URLError(.badURL) }
        var req = URLRequest(url: url)
        req.httpMethod = "GET"
        for (k,v) in headers { req.setValue(v, forHTTPHeaderField: k) }
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            let errorText = String(data: data, encoding: .utf8) ?? ""
            return "Failed to read specific Notion page (Status: \((response as? HTTPURLResponse)?.statusCode ?? 0)). Details: \(errorText)"
        }
        
        guard let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
              let results = json["results"] as? [[String: Any]] else {
            return "Could not parse page children."
        }
        
        var content = "Page Content Extrapolated:\n"
        for block in results {
            let type = block["type"] as? String ?? ""
            if let payload = block[type] as? [String: Any],
               let richText = payload["rich_text"] as? [[String: Any]] {
                let parts = richText.compactMap { $0["plain_text"] as? String }
                content += parts.joined() + "\n"
            }
        }
        return content
    }
    
    // MARK: - Mutations
    
    public func publishMeetingNotes(title: String, type: String, topic: String, rawMarkdown: String) async throws -> String {
        let targetId = Config.notionPrivateRootId
        guard !targetId.isEmpty else { return "ERROR: Nomi's target notebook ID is empty. Please configure 'notionTargetNotebookId' first." }
        
        let blocks = convertMarkdownToNotionBlocks(rawMarkdown)
        
        if type == "ops" || topic.isEmpty {
            // Standalone Ops Meeting Page
            _ = try await createPage(parentId: targetId, title: title, blocks: blocks)
            return "SUCCESS: Ops meeting '\(title)' was saved as a nested page in the AI Office Operations Notebook."
        } else {
            // Unrelated Topic Clustering
            var topicMap = UserDefaults.standard.dictionary(forKey: "NomiTopicPages") as? [String: String] ?? [:]
            let normalizedTopic = topic.lowercased().trimmingCharacters(in: .whitespacesAndNewlines)
            
            if let existingPageId = topicMap[normalizedTopic] {
                // Append blocks to existing topic page
                var appendedBlocks: [[String: Any]] = [
                    ["object": "block", "type": "divider", "divider": [String:Any]()],
                    ["object": "block", "type": "heading_2", "heading_2": ["rich_text": [ ["type": "text", "text": ["content": title]] ]]]
                ]
                appendedBlocks.append(contentsOf: blocks)
                try await appendBlocks(to: existingPageId, blocks: appendedBlocks)
                return "SUCCESS: Meeting notes appended to existing topic cluster: '\(topic.capitalized)'."
            } else {
                let newId = try await createPage(parentId: targetId, title: "Topic: \(topic.capitalized)", blocks: [])
                topicMap[normalizedTopic] = newId
                UserDefaults.standard.set(topicMap, forKey: "NomiTopicPages")
                
                var appendedBlocks: [[String: Any]] = [
                    ["object": "block", "type": "heading_2", "heading_2": ["rich_text": [ ["type": "text", "text": ["content": title]] ]]]
                ]
                appendedBlocks.append(contentsOf: blocks)
                try await appendBlocks(to: newId, blocks: appendedBlocks)
                return "SUCCESS: Created a new topic cluster page for '\(topic.capitalized)' and saved meeting notes."
            }
        }
    }
    
    private func createPage(parentId: String, title: String, blocks: [[String: Any]]) async throws -> String {
        guard let url = URL(string: "\(baseURL)/pages") else { throw URLError(.badURL) }
        var req = URLRequest(url: url)
        req.httpMethod = "POST"
        for (k,v) in headers { req.setValue(v, forHTTPHeaderField: k) }
        
        // Assume parent is a Page (Notion requires knowing whether it's database_id or page_id, since the user gave a notebook link, it's a page)
        let payload: [String: Any] = [
            "parent": ["page_id": parentId],
            "properties": [
                "title": [
                    "title": [
                        ["text": ["content": title]]
                    ]
                ]
            ],
            "children": blocks
        ]
        
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        let (data, response) = try await URLSession.shared.data(for: req)
        
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            let errorText = String(data: data, encoding: .utf8) ?? ""
            throw NSError(domain: "NotionAPI", code: (response as? HTTPURLResponse)?.statusCode ?? 500, userInfo: [NSLocalizedDescriptionKey: errorText])
        }
        
        let json = try JSONSerialization.jsonObject(with: data) as? [String: Any]
        return json?["id"] as? String ?? ""
    }
    
    private func appendBlocks(to pageId: String, blocks: [[String: Any]]) async throws {
        guard let url = URL(string: "\(baseURL)/blocks/\(pageId)/children") else { throw URLError(.badURL) }
        var req = URLRequest(url: url)
        req.httpMethod = "PATCH"
        for (k,v) in headers { req.setValue(v, forHTTPHeaderField: k) }
        
        let payload: [String: Any] = ["children": blocks]
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
            let errorText = String(data: data, encoding: .utf8) ?? ""
            throw NSError(domain: "NotionAPI", code: (response as? HTTPURLResponse)?.statusCode ?? 500, userInfo: [NSLocalizedDescriptionKey: errorText])
        }
    }
    
    private func convertMarkdownToNotionBlocks(_ markdown: String) -> [[String: Any]] {
        var blocks: [[String: Any]] = []
        let lines = markdown.components(separatedBy: .newlines)
        
        for line in lines {
            let trimmed = line.trimmingCharacters(in: .whitespaces)
            if trimmed.isEmpty { continue }
            
            if trimmed.hasPrefix("- [ ]") || trimmed.hasPrefix("- []") {
                let text = trimmed.replacingOccurrences(of: "- [ ]", with: "").trimmingCharacters(in: .whitespaces)
                blocks.append(["object": "block", "type": "to_do", "to_do": ["rich_text": [["type": "text", "text": ["content": text]]]]])
            } else if trimmed.hasPrefix("- [x]") || trimmed.hasPrefix("- [X]") {
                let text = trimmed.replacingOccurrences(of: "- [x]", with: "").trimmingCharacters(in: .whitespaces)
                blocks.append(["object": "block", "type": "to_do", "to_do": ["rich_text": [["type": "text", "text": ["content": text]]], "checked": true]])
            } else if trimmed.hasPrefix("### ") {
                let text = String(trimmed.dropFirst(4))
                blocks.append(["object": "block", "type": "heading_3", "heading_3": ["rich_text": [["type": "text", "text": ["content": text]]]]])
            } else if trimmed.hasPrefix("## ") {
                let text = String(trimmed.dropFirst(3))
                blocks.append(["object": "block", "type": "heading_2", "heading_2": ["rich_text": [["type": "text", "text": ["content": text]]]]])
            } else if trimmed.hasPrefix("# ") {
                let text = String(trimmed.dropFirst(2))
                blocks.append(["object": "block", "type": "heading_1", "heading_1": ["rich_text": [["type": "text", "text": ["content": text]]]]])
            } else if trimmed.hasPrefix("- ") || trimmed.hasPrefix("* ") {
                let text = String(trimmed.dropFirst(2))
                blocks.append(["object": "block", "type": "bulleted_list_item", "bulleted_list_item": ["rich_text": [["type": "text", "text": ["content": text]]]]])
            } else if trimmed.hasPrefix("> ") {
                let text = String(trimmed.dropFirst(2))
                blocks.append(["object": "block", "type": "quote", "quote": ["rich_text": [["type": "text", "text": ["content": text]]]]])
            } else {
                blocks.append(["object": "block", "type": "paragraph", "paragraph": ["rich_text": [["type": "text", "text": ["content": trimmed]]]]])
            }
        }
        return blocks
    }
    
    public func pollForCompletedTasks() async throws -> [String] {
        guard let url = URL(string: "\(baseURL)/search") else { return [] }
        var req = URLRequest(url: url)
        req.httpMethod = "POST"
        for (k,v) in headers { req.setValue(v, forHTTPHeaderField: k) }
        
        // Scan the 3 most recently tweaked pages
        let payload: [String: Any] = [
            "sort": ["direction": "descending", "timestamp": "last_edited_time"],
            "page_size": 3
        ]
        req.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, response) = try await URLSession.shared.data(for: req)
        guard let http = response as? HTTPURLResponse, http.statusCode == 200,
              let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
              let results = json["results"] as? [[String: Any]] else { return [] }
        
        var completed: [String] = []
        for page in results {
            guard let id = page["id"] as? String else { continue }
            // Now fetch blocks for these recent pages
            guard let blocksUrl = URL(string: "\(baseURL)/blocks/\(id)/children?page_size=100") else { continue }
            var bReq = URLRequest(url: blocksUrl)
            bReq.httpMethod = "GET"
            for (k,v) in headers { bReq.setValue(v, forHTTPHeaderField: k) }
            
            if let (bData, bResp) = try? await URLSession.shared.data(for: bReq),
               let bHttp = bResp as? HTTPURLResponse, bHttp.statusCode == 200,
               let bJson = try JSONSerialization.jsonObject(with: bData) as? [String: Any],
               let bResults = bJson["results"] as? [[String: Any]] {
                
                for block in bResults {
                    if let type = block["type"] as? String, type == "to_do",
                       let todo = block["to_do"] as? [String: Any],
                       let checked = todo["checked"] as? Bool, checked == true,
                       let rText = todo["rich_text"] as? [[String: Any]] {
                        
                        let text = rText.compactMap { $0["plain_text"] as? String }.joined()
                        completed.append(text)
                    }
                }
            }
        }
        return completed
    }
}

```