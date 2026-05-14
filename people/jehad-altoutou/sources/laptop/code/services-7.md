---
type: source
source_type: laptop
title: Services
slug: services-7
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/Services.swift
original_size: 31291
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# Services

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/Services.swift` on 2026-05-14._

```swift
import Foundation
import AVFoundation
import OSLog

public enum AIResponse {
    case text(String)
    case toolAction(name: String, argsJSON: String, toolCallId: String)
}

public final class AIOrchestrator {
    public static let shared = AIOrchestrator()
    
    private let openAIEndpoint = URL(string: "https://api.openai.com/v1/chat/completions")!
    private var conversationHistory: [ChatMessage] = []
    
    // Define Nomi's Capabilities
    private let availableTools: [ToolDefinition] = [
        ToolDefinition(type: "function", function: FunctionDef(
            name: "create_linear_issue",
            description: "Create an issue or task in Linear.",
            parameters: FunctionParameters(
                type: "object",
                properties: [
                    "title": FunctionParameters.Property(type: "string", description: "The title of the issue"),
                    "description": FunctionParameters.Property(type: "string", description: "The detail of the task")
                ],
                required: ["title", "description"]
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "schedule_calendar_event",
            description: "Schedule a new event on Google Calendar.",
            parameters: FunctionParameters(
                type: "object",
                properties: [
                    "title": FunctionParameters.Property(type: "string", description: "Event title"),
                    "startTimeISO": FunctionParameters.Property(type: "string", description: "Start time in ISO8601 format"),
                    "durationMinutes": FunctionParameters.Property(type: "string", description: "Duration in minutes as string (default 15)"),
                    "attendeeEmail": FunctionParameters.Property(type: "string", description: "Optional attendee email to invite to the event")
                ],
                required: ["title", "startTimeISO", "durationMinutes"]
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "read_calendar",
            description: "Read upcoming events from Google Calendar.",
            parameters: FunctionParameters(
                type: "object",
                properties: [:],
                required: nil
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "search_notion",
            description: "Search the company Notion knowledge base using a query string.",
            parameters: FunctionParameters(
                type: "object",
                properties: [
                    "query": FunctionParameters.Property(type: "string", description: "Search query")
                ],
                required: ["query"]
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "read_notion_page",
            description: "Read the specific content inside a Notion document. You must search for the ID first.",
            parameters: FunctionParameters(
                type: "object",
                properties: [
                    "page_id": FunctionParameters.Property(type: "string", description: "The UUID of the Notion page")
                ],
                required: ["page_id"]
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "fetch_fireflies_transcripts",
            description: "Fetch the summaries and transcripts of recent meetings from Fireflies.ai.",
            parameters: FunctionParameters(
                type: "object",
                properties: [:],
                required: nil
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "start_recording",
            description: "Automatically cross-references the user's active calendar meeting right now and injects the Fireflies bot to start recording their screen.",
            parameters: FunctionParameters(
                type: "object",
                properties: [:],
                required: nil
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "fireflies_get_transcript",
            description: "Fetch the detailed transcript for a specific meeting ID including raw sentences.",
            parameters: FunctionParameters(
                type: "object",
                properties: [
                    "id": FunctionParameters.Property(type: "string", description: "The Fireflies transcript ID")
                ],
                required: ["id"]
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "analyze_and_publish_transcript",
            description: "Used to format and save meeting summaries. If the topic is an ops meeting or AIO Standup, mark it 'ops'. Otherwise mark it 'unrelated_topic' with a very specific 'topic_name' so we can append future meetings to the same file. title is the meeting title.",
            parameters: FunctionParameters(
                type: "object",
                properties: [
                    "title": FunctionParameters.Property(type: "string", description: "Meeting title"),
                    "type": FunctionParameters.Property(type: "string", description: "'ops' or 'unrelated_topic'"),
                    "topic_name": FunctionParameters.Property(type: "string", description: "If 'unrelated_topic', provide a 2-3 word topic name to group notes later."),
                    "summary_markdown": FunctionParameters.Property(type: "string", description: "A beautifully formatted markdown representation of the meeting tasks, decisions, and bullets.")
                ],
                required: ["title", "type", "topic_name", "summary_markdown"]
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "analyze_screen_context",
            description: "Takes a live screenshot of the user's desktop to visually verify UI configurations or capture diagram contexts.",
            parameters: FunctionParameters(type: "object", properties: [:], required: nil)
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "send_email",
            description: "Send an email on the user's behalf via their Gmail account. Always confirm recipient, subject, and body before sending.",
            parameters: FunctionParameters(
                type: "object",
                properties: [
                    "to":      FunctionParameters.Property(type: "string", description: "Recipient email address"),
                    "subject": FunctionParameters.Property(type: "string", description: "Email subject line"),
                    "body":    FunctionParameters.Property(type: "string", description: "Email body as plain text")
                ],
                required: ["to", "subject", "body"]
            )
        )),
        ToolDefinition(type: "function", function: FunctionDef(
            name: "search_email",
            description: "Search the user's Gmail inbox using Gmail's query syntax (e.g. 'from:alice is:unread', 'subject:invoice newer_than:7d'). Returns up to 10 summaries.",
            parameters: FunctionParameters(
                type: "object",
                properties: [
                    "query": FunctionParameters.Property(type: "string", description: "Gmail search query")
                ],
                required: ["query"]
            )
        ))
    ]
    
    public init() {
        let formatter = ISO8601DateFormatter()
        formatter.timeZone = TimeZone.current
        let currentDate = formatter.string(from: Date())
        let timeZoneName = TimeZone.current.identifier
        
        let systemPrompt = """
        You are Nomi, a digital desktop companion.
        You live in the MacBook notch. You are extremely concise, cute, calm, and intelligent.
        Respond in 1 to 2 very short sentences max.

        TOOL USE IS MANDATORY — NEVER RESPOND WITH TEXT IF A TOOL APPLIES:

        • Anything about the user's screen — "can you see my screen", "look at this", \
        "what's on my screen", "check my desktop", "read this", "analyze this" — \
        you MUST call analyze_screen_context immediately. Never say "I can't see \
        your screen" or "I can analyze it if you want". Just call the tool.

        • Anything about calendar, meetings, events, or today's schedule — call \
        read_calendar or schedule_calendar_event.

        • Anything about Notion docs, notes, or the knowledge base — call \
        search_notion or read_notion_page.

        • Sending email — call send_email. Searching email — call search_email.

        • Creating a task or issue — call create_linear_issue.

        • Starting a meeting recording — call start_recording.

        • A [SYSTEM ALERT - TRANSCRIPT READY] message — call the transcript tools \
        silently, then briefly confirm to the user.

        If the user's intent could match a tool, call the tool. Text replies are \
        only for casual conversation where no tool is relevant.

        CURRENT LOCAL TIME: \(currentDate)
        USER TIMEZONE: \(timeZoneName)
        """
        conversationHistory.append(ChatMessage(role: "system", content: systemPrompt, tool_calls: nil, name: nil, tool_call_id: nil))
    }
    
    public func processInput(_ prompt: String) async throws -> AIResponse {
        conversationHistory.append(ChatMessage(role: "user", content: prompt, tool_calls: nil, name: nil, tool_call_id: nil))
        
        let requestBody = ChatCompletionRequest(
            model: "gpt-4o-mini",
            messages: conversationHistory,
            temperature: 0.7,
            tools: availableTools
        )
        
        var request = URLRequest(url: openAIEndpoint)
        request.httpMethod = "POST"
        request.addValue("Bearer \(Config.openAIKey)", forHTTPHeaderField: "Authorization")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONEncoder().encode(requestBody)
        
        let (data, response) = try await URLSession.shared.data(for: request)
        
        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }
        
        let completionResponse = try JSONDecoder().decode(ChatCompletionResponse.self, from: data)
        guard let choice = completionResponse.choices.first else {
            throw URLError(.cannotParseResponse)
        }
        
        // Append exactly what OpenAI returned to history
        conversationHistory.append(choice.message)
        
        if choice.finish_reason == "tool_calls", let firstCall = choice.message.tool_calls?.first {
            return .toolAction(name: firstCall.function.name, argsJSON: firstCall.function.arguments, toolCallId: firstCall.id)
        } else if let reply = choice.message.content?.stringValue {
            return .text(reply)
        }
        throw URLError(.cannotParseResponse)
    }
    
    public func submitToolResult(toolCallId: String, result: String) async throws -> AIResponse {
        conversationHistory.append(ChatMessage(role: "tool", content: result, tool_calls: nil, name: "tool", tool_call_id: toolCallId))
        
        // Re-ping OpenAI asking what to say next now that the tool result is in
        let requestBody = ChatCompletionRequest(model: "gpt-4o-mini", messages: conversationHistory, temperature: 0.7, tools: availableTools)
        var request = URLRequest(url: openAIEndpoint)
        request.httpMethod = "POST"
        request.addValue("Bearer \(Config.openAIKey)", forHTTPHeaderField: "Authorization")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONEncoder().encode(requestBody)
        
        let (data, _) = try await URLSession.shared.data(for: request)
        let completionResponse = try JSONDecoder().decode(ChatCompletionResponse.self, from: data)
        
        guard let reply = completionResponse.choices.first?.message.content?.stringValue else { throw URLError(.cannotParseResponse) }
        conversationHistory.append(ChatMessage(role: "assistant", content: reply, tool_calls: nil, name: nil, tool_call_id: nil))
        
        return .text(reply)
    }
    
    public func submitVisionToolResult(toolCallId: String, base64Image: String) async throws -> AIResponse {
        // Mock the tool action response so the API resolves the forced call state
        conversationHistory.append(ChatMessage(role: "tool", content: "Successfully captured the user's screen. Now look at the subsequent user message containing the image.", tool_calls: nil, name: "tool", tool_call_id: toolCallId))
        
        // Inject the image array
        let multiModalPayload = [
            MultiModalItem(type: "text", text: "Here is the screenshot of my active display."),
            MultiModalItem(type: "image_url", image_url: MultiModalItem.ImageUrl(url: "data:image/jpeg;base64,\(base64Image)"))
        ]
        conversationHistory.append(ChatMessage(role: "user", multiModalContent: multiModalPayload))
        
        let requestBody = ChatCompletionRequest(model: "gpt-4o-mini", messages: conversationHistory, temperature: 0.7, tools: availableTools)
        var request = URLRequest(url: openAIEndpoint)
        request.httpMethod = "POST"
        request.addValue("Bearer \(Config.openAIKey)", forHTTPHeaderField: "Authorization")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONEncoder().encode(requestBody)
        
        let (data, response) = try await URLSession.shared.data(for: request)
        if let str = String(data:data, encoding: .utf8) { print(str) }
        let completionResponse = try JSONDecoder().decode(ChatCompletionResponse.self, from: data)
        
        guard let reply = completionResponse.choices.first?.message.content?.stringValue else { throw URLError(.cannotParseResponse) }
        conversationHistory.append(ChatMessage(role: "assistant", content: reply, tool_calls: nil, name: nil, tool_call_id: nil))
        
        return .text(reply)
    }
}

/// Voice output. ElevenLabs is the only supported synthesizer — we deliberately
/// removed the `AVSpeechSynthesizer` fallback because the robotic Apple voice was
/// masking real ElevenLabs failures and damaging the product feel.
///
/// Failures are loud: the exact HTTP status and response body are logged via
/// `os.Logger` (filter `subsystem:com.antigravity.nomi category:Voice` in Console.app),
/// and `onFailure` fires with a human-readable reason so the UI can surface a toast.
public final class VoiceEngine: NSObject, AVAudioPlayerDelegate, @unchecked Sendable {

    public static let shared = VoiceEngine()

    /// Invoked on the main queue when synthesis fails. Wire this to a toast.
    public var onFailure: (@Sendable (String) -> Void)?

    private let log = Logger(subsystem: "com.antigravity.nomi", category: "Voice")
    private var audioPlayer: AVAudioPlayer?
    private var completionHook: (() -> Void)?

    public override init() { super.init() }

    public enum VoiceError: Error, LocalizedError {
        case missingKey
        case missingVoice
        case http(status: Int, body: String)
        case transport(Error)
        case decode(String)

        public var errorDescription: String? {
            switch self {
            case .missingKey:                return "ElevenLabs API key is not configured."
            case .missingVoice:              return "ElevenLabs voice ID is not configured."
            case .http(let s, let b):        return "ElevenLabs HTTP \(s): \(b.prefix(240))"
            case .transport(let e):          return "Network error: \(e.localizedDescription)"
            case .decode(let s):             return "Could not decode audio: \(s)"
            }
        }
    }

    public func speak(_ text: String) async {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty else { return }

        // Primary: ElevenLabs. Beautiful voice when the account is healthy.
        do {
            let data = try await fetchMP3(for: trimmed)
            try await playMP3(data)
            return
        } catch {
            log.warning("ElevenLabs failed, falling back to OpenAI TTS: \(error.localizedDescription, privacy: .public)")
        }

        // Fallback: OpenAI TTS. Neural quality, not robotic. Uses the same
        // OpenAI key Nomi already has — no user configuration needed. Covers
        // the ElevenLabs free-tier shutdown, rate limits, and outages.
        do {
            let data = try await fetchOpenAITTS(for: trimmed)
            try await playMP3(data)
        } catch {
            let message = (error as? VoiceError)?.localizedDescription ?? error.localizedDescription
            log.error("Voice fallback also failed: \(message, privacy: .public)")
            let onFailure = self.onFailure
            DispatchQueue.main.async { onFailure?(message) }
        }
    }

    // MARK: - HTTP

    private func fetchMP3(for text: String) async throws -> Data {
        guard !Config.elevenLabsKey.isEmpty else { throw VoiceError.missingKey }
        guard !Config.voiceID.isEmpty       else { throw VoiceError.missingVoice }

        // Streaming endpoint delivers first bytes ~5x faster than the non-streaming
        // endpoint. We still buffer the full response before playback for now;
        // chunked playback via AVAudioPlayerNode is a Phase-2 enhancement.
        let url = URL(string: "https://api.elevenlabs.io/v1/text-to-speech/\(Config.voiceID)/stream")!

        let body = TTSRequest(
            text: text,
            model_id: Config.elevenLabsModel,
            voice_settings: TTSRequest.VoiceSettings(stability: 0.45, similarity_boost: 0.8)
        )

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue(Config.elevenLabsKey, forHTTPHeaderField: "xi-api-key")
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue("audio/mpeg", forHTTPHeaderField: "Accept")
        request.httpBody = try JSONEncoder().encode(body)
        request.timeoutInterval = 20

        let data: Data
        let response: URLResponse
        do {
            (data, response) = try await URLSession.shared.data(for: request)
        } catch {
            throw VoiceError.transport(error)
        }

        let http = response as? HTTPURLResponse
        let status = http?.statusCode ?? 0
        guard status == 200 else {
            let bodyText = String(data: data, encoding: .utf8) ?? "<binary \(data.count) bytes>"
            throw VoiceError.http(status: status, body: bodyText)
        }
        return data
    }

    // MARK: - OpenAI TTS fallback

    private func fetchOpenAITTS(for text: String) async throws -> Data {
        guard !Config.openAIKey.isEmpty else { throw VoiceError.missingKey }

        var req = URLRequest(url: URL(string: "https://api.openai.com/v1/audio/speech")!)
        req.httpMethod = "POST"
        req.setValue("Bearer \(Config.openAIKey)", forHTTPHeaderField: "Authorization")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        // tts-1 is 3x cheaper than tts-1-hd and latency ~400ms faster.
        // "nova" is the warmest-sounding voice in the OpenAI catalogue;
        // alternatives: alloy, echo, fable, onyx, shimmer.
        let body: [String: Any] = [
            "model": "tts-1",
            "input": text,
            "voice": "nova",
            "response_format": "mp3"
        ]
        req.httpBody = try JSONSerialization.data(withJSONObject: body)
        req.timeoutInterval = 20

        let (data, response) = try await URLSession.shared.data(for: req)
        let status = (response as? HTTPURLResponse)?.statusCode ?? 0
        guard status == 200 else {
            let body = String(data: data, encoding: .utf8) ?? "<binary>"
            throw VoiceError.http(status: status, body: body)
        }
        return data
    }

    // MARK: - Playback

    private func playMP3(_ data: Data) async throws {
        try await withCheckedThrowingContinuation { (cont: CheckedContinuation<Void, Error>) in
            do {
                let player = try AVAudioPlayer(data: data)
                player.delegate = self
                self.audioPlayer = player
                self.completionHook = { cont.resume() }
                player.play()
            } catch {
                cont.resume(throwing: VoiceError.decode(error.localizedDescription))
            }
        }
    }

    public func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool) {
        completionHook?()
        completionHook = nil
    }

    public func audioPlayerDecodeErrorDidOccur(_ player: AVAudioPlayer, error: Error?) {
        log.error("AVAudioPlayer decode error: \(error?.localizedDescription ?? "unknown", privacy: .public)")
        completionHook?()
        completionHook = nil
    }
}

struct LinearGraphQLPayload: Codable {
    let query: String
    let variables: [String: String]?
}

public final class LinearAdapter {
    public static let shared = LinearAdapter()
    private let endpoint = URL(string: "https://api.linear.app/graphql")!
    
    // Caches the default team ID so we don't fetch it every time
    private var cachedTeamId: String?
    
    private func fetchFirstTeamId() async throws -> String {
        if let cached = cachedTeamId { return cached }
        let payload = LinearGraphQLPayload(query: "query { teams { nodes { id } } }", variables: nil)
        let data = try await performLinearRequest(payload)
        
        let json = try JSONSerialization.jsonObject(with: data) as? [String: Any]
        guard let dataNode = json?["data"] as? [String: Any],
              let teams = dataNode["teams"] as? [String: Any],
              let nodes = teams["nodes"] as? [[String: Any]],
              let firstTeamId = nodes.first?["id"] as? String else {
            throw URLError(.cannotParseResponse)
        }
        self.cachedTeamId = firstTeamId
        return firstTeamId
    }
    
    public func createIssue(title: String, description: String) async throws -> String {
        let teamId = try await fetchFirstTeamId()
        
        let mutation = """
        mutation IssueCreate($title: String!, $description: String!, $teamId: String!) {
          issueCreate(input: {
            title: $title,
            description: $description,
            teamId: $teamId
          }) {
            success
            issue { id title url }
          }
        }
        """
        
        let payload = LinearGraphQLPayload(query: mutation, variables: [
            "title": title,
            "description": description,
            "teamId": teamId
        ])
        
        let _ = try await performLinearRequest(payload)
        return "SUCCESS! Linear issue created."
    }
    
    private func performLinearRequest(_ payload: LinearGraphQLPayload) async throws -> Data {
        var request = URLRequest(url: endpoint)
        request.httpMethod = "POST"
        request.addValue(Config.linearAPIKey, forHTTPHeaderField: "Authorization")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONEncoder().encode(payload)
        let (data, response) = try await URLSession.shared.data(for: request)
        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            let err = String(data:data, encoding: .utf8) ?? "Err"
            print("Linear Error: \(err)")
            throw URLError(.badServerResponse)
        }
        return data
    }
}

public struct CalendarEvent {
    public let id: String
    public let title: String
    public let startDate: Date
    public let hangoutLink: String?
}

public final class CalendarAdapter {
    public static let shared = CalendarAdapter()
    
    public func fetchUpcomingEventModels() async throws -> [CalendarEvent] {
        guard !Config.googleCalendarToken.isEmpty else { return [] }
        
        var components = URLComponents(string: "https://www.googleapis.com/calendar/v3/calendars/primary/events")!
        components.queryItems = [
            URLQueryItem(name: "timeMin", value: ISO8601DateFormatter().string(from: Date())),
            URLQueryItem(name: "timeMax", value: ISO8601DateFormatter().string(from: Date().addingTimeInterval(86400 * 3))),
            URLQueryItem(name: "maxResults", value: "15"),
            URLQueryItem(name: "singleEvents", value: "true"),
            URLQueryItem(name: "orderBy", value: "startTime")
        ]
        
        var request = URLRequest(url: components.url!)
        request.httpMethod = "GET"
        request.addValue("Bearer \(Config.googleCalendarToken)", forHTTPHeaderField: "Authorization")
        
        let (data, response) = try await URLSession.shared.data(for: request)
        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            if (response as? HTTPURLResponse)?.statusCode == 401 {
                throw URLError(.userAuthenticationRequired)
            }
            throw URLError(.badServerResponse)
        }
        
        var output: [CalendarEvent] = []
        if let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
           let items = json["items"] as? [[String: Any]] {
            
            let strictFormatter = ISO8601DateFormatter()
            strictFormatter.formatOptions = [.withInternetDateTime]
            
            for item in items {
                let id = item["id"] as? String ?? ""
                let title = item["summary"] as? String ?? "Untitled"
                
                var hangoutLink = item["hangoutLink"] as? String
                if hangoutLink == nil {
                    // Fallback to searching location and description for HTTP video links (Zoom/Teams)
                    if let loc = item["location"] as? String, loc.contains("http") {
                        hangoutLink = CalendarAdapter.extractURL(from: loc)
                    } else if let desc = item["description"] as? String, desc.contains("http") {
                        hangoutLink = CalendarAdapter.extractURL(from: desc)
                    }
                }
                
                var eventStart: Date?
                if let startDict = item["start"] as? [String: Any] {
                    if let dtStr = startDict["dateTime"] as? String {
                        eventStart = strictFormatter.date(from: dtStr)
                    } else if let dateStr = startDict["date"] as? String {
                        let fmt = DateFormatter()
                        fmt.dateFormat = "yyyy-MM-dd"
                        eventStart = fmt.date(from: dateStr)
                    }
                }
                
                if let validStart = eventStart {
                    output.append(CalendarEvent(id: id, title: title, startDate: validStart, hangoutLink: hangoutLink))
                }
            }
        }
        return output
    }
    
    public func fetchEvents() async throws -> String {
        do {
            let models = try await fetchUpcomingEventModels()
            if models.isEmpty { return "No upcoming events found." }
            
            let formatter = DateFormatter()
            formatter.timeStyle = .short
            let summary = models.prefix(5).map { "\($0.title) (at \(formatter.string(from: $0.startDate)))" }.joined(separator: ", ")
            return "Found events: \(summary)"
        } catch URLError.userAuthenticationRequired {
            return "SYSTEM ERROR: Google Calendar Token is EXPIRED (HTTP 401). Explain this clearly to the user instead of saying no meetings."
        } catch {
            return "SYSTEM ERROR: Google Calendar fetch failed (\(error))."
        }
    }
    
    private static func extractURL(from text: String) -> String? {
        guard let detector = try? NSDataDetector(types: NSTextCheckingResult.CheckingType.link.rawValue) else { return nil }
        let matches = detector.matches(in: text, options: [], range: NSRange(location: 0, length: text.utf16.count))
        return matches.first?.url?.absoluteString
    }
    
    public func scheduleEvent(title: String, startTimeISO: String, durationMinutes: String, attendeeEmail: String? = nil) async throws -> String {
        guard !Config.googleCalendarToken.isEmpty else { return "Google Calendar Token Missing" }
        
        let minutes = Double(durationMinutes) ?? 15.0
        
        // OpenAI often sends timestamps without timezones. We build a permissive parser block.
        var finalStartDate: Date? = nil
        let strictFormatter = ISO8601DateFormatter()
        strictFormatter.formatOptions = [.withInternetDateTime]
        if let d = strictFormatter.date(from: startTimeISO) { finalStartDate = d }
        
        if finalStartDate == nil {
            // Append Z if they forgot it
            if !startTimeISO.contains("Z") && !startTimeISO.contains("+") {
                finalStartDate = strictFormatter.date(from: startTimeISO + "Z")
            }
        }
        
        guard let startDate = finalStartDate else {
             return "SYSTEM ERROR: You provided an invalid ISO8601 Date. You MUST append 'Z' or a timezone offset. E.g. \(startTimeISO)Z"
        }
        
        let endDate = startDate.addingTimeInterval(minutes * 60)
        let endISO = strictFormatter.string(from: endDate)
        
        var payload: [String: Any] = [
            "summary": title,
            "start": ["dateTime": startTimeISO],
            "end": ["dateTime": endISO]
        ]
        
        if let email = attendeeEmail, !email.isEmpty {
            payload["attendees"] = [["email": email]]
        }
        
        let endpoint = URL(string: "https://www.googleapis.com/calendar/v3/calendars/primary/events")!
        var request = URLRequest(url: endpoint)
        request.httpMethod = "POST"
        request.addValue("Bearer \(Config.googleCalendarToken)", forHTTPHeaderField: "Authorization")
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try JSONSerialization.data(withJSONObject: payload)
        
        let (data, response) = try await URLSession.shared.data(for: request)
        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            let errorText = String(data: data, encoding: .utf8) ?? "Err"
            ActivityLogger.shared.record(action: "Google Api Error", target: "API Request", status: errorText.prefix(200).description)
            throw URLError(.badServerResponse)
        }
        return "SUCCESS! Event has been scheduled."
    }
}

```