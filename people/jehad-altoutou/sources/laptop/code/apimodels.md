---
type: source
source_type: laptop
title: APIModels
slug: apimodels
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/APIModels.swift
original_size: 3076
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# APIModels

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/APIModels.swift` on 2026-05-14._

```swift
import Foundation

// MARK: - OpenAI Data Models

struct ChatCompletionRequest: Codable {
    let model: String
    let messages: [ChatMessage]
    let temperature: Double
    var tools: [ToolDefinition]? = nil
}

enum MessageContent: Codable {
    case text(String)
    case multiModal([MultiModalItem])
    
    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let str = try? container.decode(String.self) {
            self = .text(str)
        } else if let arr = try? container.decode([MultiModalItem].self) {
            self = .multiModal(arr)
        } else {
            self = .text("")
        }
    }
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        switch self {
        case .text(let str):
            try container.encode(str)
        case .multiModal(let arr):
            try container.encode(arr)
        }
    }
    
    var stringValue: String? {
        if case .text(let str) = self { return str }
        return nil
    }
}

struct MultiModalItem: Codable {
    let type: String
    var text: String? = nil
    var image_url: ImageUrl? = nil
    
    struct ImageUrl: Codable {
        let url: String
    }
}

struct ChatMessage: Codable {
    let role: String
    var content: MessageContent?
    var tool_calls: [ToolCall]? = nil
    var name: String? = nil
    var tool_call_id: String? = nil
    
    // Legacy convenince init for text
    init(role: String, content: String? = nil, tool_calls: [ToolCall]? = nil, name: String? = nil, tool_call_id: String? = nil) {
        self.role = role
        self.content = content != nil ? .text(content!) : nil
        self.tool_calls = tool_calls
        self.name = name
        self.tool_call_id = tool_call_id
    }
    
    init(role: String, multiModalContent: [MultiModalItem]) {
        self.role = role
        self.content = .multiModal(multiModalContent)
    }
}

struct ChatCompletionResponse: Codable {
    struct Choice: Codable {
        let message: ChatMessage
        let finish_reason: String?
    }
    let choices: [Choice]
}

struct ToolDefinition: Codable {
    let type: String
    let function: FunctionDef
}

struct FunctionDef: Codable {
    let name: String
    let description: String
    let parameters: FunctionParameters
}

struct FunctionParameters: Codable {
    let type: String // usually "object"
    let properties: [String: Property]
    let required: [String]?
    
    struct Property: Codable {
        let type: String
        let description: String
    }
}

struct ToolCall: Codable {
    let id: String
    let type: String
    let function: FunctionCall
}

struct FunctionCall: Codable {
    let name: String
    let arguments: String // JSON string map of properties
}

// MARK: - ElevenLabs Data Models

struct TTSRequest: Codable {
    let text: String
    let model_id: String
    let voice_settings: VoiceSettings
    
    struct VoiceSettings: Codable {
        let stability: Double
        let similarity_boost: Double
    }
}

```