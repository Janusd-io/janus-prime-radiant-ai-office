---
type: source
source_type: laptop
title: NomiStateEngine
slug: nomistateengine
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/NomiStateEngine.swift
original_size: 28463
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# NomiStateEngine

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Core/NomiStateEngine.swift` on 2026-05-14._

```swift
import SwiftUI
import Combine
import ScreenCaptureKit

@MainActor
class NomiStateEngine: ObservableObject {
    @Published var currentState: CompanionState = .idle
    @Published var isHovered: Bool = false
    @Published var isExpanded: Bool = false
    @Published var hoverIntensity: Double = 0.0
    @Published var latestResponse: String = ""
    
    // Approval Buffer
    @Published var pendingActionName: String = ""
    @Published var pendingActionDetails: String = ""
    private var pendingToolCallId: String? = nil
    @Published var latestToast: String? = nil
    @Published var approvalAction: String? = nil
    @Published var connectingServiceName: String = ""
    
    // Services
    // private let voiceEngine = VoiceEngine()
    
    init() {
        startMeshPolling()
        startCalendarDaemon()
        startPostMeetingDaemon()
        startNotionSyncDaemon()

        wireSpeechEngine()
        wireVoiceEngine()
        scheduleDailyGreetingIfNeeded()

        // Honor the user's listening preference. Default is push-to-talk (no ambient
        // mic), which keeps the orange mic indicator off until ⌘⌥Space is pressed.
        Task { @MainActor in
            let authorized = await SpeechEngine.shared.requestAuthorization()
            guard authorized else { return }
            if Config.listeningMode == .ambient {
                SpeechEngine.shared.startAmbient()
            }
        }

        NotificationCenter.default.addObserver(
            forName: .nomiShouldCollapse,
            object: nil,
            queue: .main
        ) { [weak self] _ in
            Task { @MainActor in
                guard let self = self else { return }
                if self.currentState == .idle { self.isExpanded = false }
            }
        }
    }

    private func wireSpeechEngine() {
        SpeechEngine.shared.onWakeWord = { [weak self] in
            guard let self = self else { return }
            Task { @MainActor in
                NSSound(named: "Ping")?.play()
                self.beginDictation()
            }
        }

        SpeechEngine.shared.onDictation = { [weak self] text, isFinal in
            guard let self = self else { return }
            Task { @MainActor in
                if isFinal {
                    let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
                    if !trimmed.isEmpty {
                        self.processInputText(trimmed)
                    } else {
                        self.transitionState(to: .idle)
                    }
                }
            }
        }

        SpeechEngine.shared.onError = { [weak self] error in
            guard let self = self else { return }
            Task { @MainActor in
                self.showErrorState(error.localizedDescription)
            }
        }
    }

    /// Plays the hello wave once per calendar day, briefly after launch.
    /// Expands the card so the wave is actually visible, then collapses back.
    private func scheduleDailyGreetingIfNeeded() {
        let key = "nomi.lastGreetingDay"
        let today = Calendar.current.startOfDay(for: Date()).timeIntervalSince1970
        let last = UserDefaults.standard.double(forKey: key)
        guard today > last else { return }
        UserDefaults.standard.set(today, forKey: key)

        Task { @MainActor in
            try? await Task.sleep(nanoseconds: 900_000_000)
            self.isExpanded = true
            self.transitionState(to: .greeting)
            try? await Task.sleep(nanoseconds: 2_400_000_000)
            if self.currentState == .greeting {
                self.transitionState(to: .idle)
                self.isExpanded = self.isHovered
            }
        }
    }

    private func wireVoiceEngine() {
        VoiceEngine.shared.onFailure = { [weak self] message in
            guard let self = self else { return }
            Task { @MainActor in
                self.showErrorState("Voice: \(message)")
            }
        }
    }

    /// Fired by the ⌘⌥Space global hotkey. Starts dictation from any state.
    func triggerPushToTalk() {
        switch currentState {
        case .listening:
            SpeechEngine.shared.stop()
            transitionState(to: .idle)
        default:
            beginDictation()
        }
    }

    private func beginDictation() {
        transitionState(to: .listening)
        SpeechEngine.shared.startDictation()
    }
    
    private var notifiedEvents = Set<String>()
    
    private func startCalendarDaemon() {
        Task {
            while true {
                try? await Task.sleep(nanoseconds: 30_000_000_000) // 30s
                guard let events = try? await CalendarAdapter.shared.fetchUpcomingEventModels() else { continue }
                
                let now = Date()
                for e in events {
                    let diffMinutes = e.startDate.timeIntervalSince(now) / 60.0
                    
                    if diffMinutes > 14 && diffMinutes <= 16 {
                        let id = "\(e.id)_15"
                        if !notifiedEvents.contains(id) {
                            notifiedEvents.insert(id)
                            triggerCalendarAlert(event: e, minutes: 15)
                        }
                    } else if diffMinutes > 4 && diffMinutes <= 6 {
                        let id = "\(e.id)_5"
                        if !notifiedEvents.contains(id) {
                            notifiedEvents.insert(id)
                            triggerCalendarAlert(event: e, minutes: 5)
                        }
                    }
                }
            }
        }
    }
    
    private func startPostMeetingDaemon() {
        Task {
            while true {
                try? await Task.sleep(nanoseconds: 600_000_000_000) // 10 minutes interval
                guard let transcripts = try? await FirefliesAdapter.shared.fetchRecentTranscriptModels() else { continue }
                
                var processed = UserDefaults.standard.stringArray(forKey: "NomiProcessedTranscripts") ?? []
                for t in transcripts {
                    if !processed.contains(t.id) {
                        processed.append(t.id)
                        UserDefaults.standard.set(processed, forKey: "NomiProcessedTranscripts")
                        
                        // Fire the LLM Analysis pipeline
                        let prompt = """
                        [SYSTEM ALERT - TRANSCRIPT READY]: A new meeting transcript '\(t.title)' has just finished generating in Fireflies. 
                        Your objective is to fetch the full transcript details using the tool `fireflies_get_transcript` for ID: \(t.id).
                        Once you have the details, use the internal `analyze_and_publish_transcript` logic to update Notion. 
                        DO NOT ask the user for permission. Process it silently and then notify the user that their Notion Notebook was updated!
                        """
                        Task {
                            await MainActor.run { self.transitionState(to: .thinking) }
                            if let resp = try? await AIOrchestrator.shared.processInput(prompt) {
                                await self.handleAIResponse(resp)
                            }
                        }
                        
                        // We only process one at a time to avoid overwhelming the LLM
                        break
                    }
                }
            }
        }
    }
    
    private func startNotionSyncDaemon() {
        Task {
            while true {
                try? await Task.sleep(nanoseconds: 300_000_000_000) // 5 minutes
                guard let completedArr = try? await NotionAdapter.shared.pollForCompletedTasks(), !completedArr.isEmpty else { continue }
                
                var cache = UserDefaults.standard.stringArray(forKey: "NomiCheckedTasks") ?? []
                var newlyCompleted: [String] = []
                
                for taskStr in completedArr {
                    if !cache.contains(taskStr) {
                        cache.append(taskStr)
                        newlyCompleted.append(taskStr)
                    }
                }
                
                if !newlyCompleted.isEmpty {
                    UserDefaults.standard.set(cache, forKey: "NomiCheckedTasks")
                    
                    let summary = newlyCompleted.joined(separator: ", ")
                    let prompt = """
                    [SYSTEM ALERT - REVERSE SYNC]: The user just manually completed the following task(s) on their Notion Board: '\(summary)'.
                    YOUR GOAL: Congratulate them out loud instantly! 
                    Be extremely encouraging, funny, and highly energetic. Use varied responses so it doesn't sound repetitive every time they finish a task. 
                    Act like an excited assistant!
                    """
                    
                    Task {
                        await MainActor.run { self.transitionState(to: .thinking) }
                        if let resp = try? await AIOrchestrator.shared.processInput(prompt) {
                            await self.handleAIResponse(resp)
                        }
                    }
                }
            }
        }
    }
    
    private func triggerCalendarAlert(event: CalendarEvent, minutes: Int) {
        let msg = "[SYSTEM NOTIFICATION]: The user has a meeting '\(event.title)' starting in \(minutes) minutes. Read this alert to them out loud right now, and ask if they are ready to invoke the `start_recording` tool."
        Task {
            await MainActor.run { self.transitionState(to: .thinking) }
            if let resp = try? await AIOrchestrator.shared.processInput(msg) {
                await self.handleAIResponse(resp)
            }
        }
    }
    
    private func startMeshPolling() {
        Task {
            while true {
                try? await Task.sleep(nanoseconds: 5_000_000_000)
                
                // 1. Incoming Messages
                if let msgs = try? await SupabaseAdapter.shared.fetchIncomingMessages(), let first = msgs.first {
                    guard let id = first["id"] as? String, 
                          let from = first["from_user"] as? String, 
                          let content = first["content"] as? String else { continue }
                    
                    try? await SupabaseAdapter.shared.archiveMessage(id: id)
                    
                    let prompt = "[SYSTEM ALERT - MESH PROTOCOL]: You just received an incoming Walkie-Talkie message from \(from)'s Nomi. The message instruction is: \"\(content)\". Read this out loud to your user immediately, ask them if they approve/confirm, and then you MUST use the `reply_mesh_message` tool to reply back to \(from)'s Nomi with network_id: \(id)."
                    
                    await MainActor.run {
                        self.transitionState(to: .thinking)
                    }
                    
                    if let response = try? await AIOrchestrator.shared.processInput(prompt) {
                        await self.handleAIResponse(response)
                    }
                }
                
                // 2. Incoming Replies to our messages
                if let replies = try? await SupabaseAdapter.shared.fetchMyReplies(), let firstReply = replies.first {
                    guard let id = firstReply["id"] as? String, 
                          let target = firstReply["to_user"] as? String, 
                          let replyText = firstReply["reply"] as? String else { continue }
                    
                    try? await SupabaseAdapter.shared.archiveMessage(id: id)
                    
                    let prompt = "[SYSTEM ALERT - MESH PROTOCOL]: \(target)'s Nomi just replied to your previous request. The reply states: \"\(replyText)\". Inform your user of this outcome out loud, and execute any calendar scheduling if they confirmed it!"
                    
                    await MainActor.run {
                        self.transitionState(to: .thinking)
                    }
                    
                    if let response = try? await AIOrchestrator.shared.processInput(prompt) {
                        await self.handleAIResponse(response)
                    }
                }
            }
        }
    }
    
    func processInputText(_ text: String) {
        let trimmedLower = text.lowercased().trimmingCharacters(in: .whitespacesAndNewlines)
        if trimmedLower.hasPrefix("/connect") {
            let parts = text.split(separator: " ")
            if parts.count > 1 {
                self.connectingServiceName = String(parts[1])
            } else {
                self.connectingServiceName = "Service"
            }
            withAnimation(.spring(response: 0.4, dampingFraction: 0.7)) {
                self.currentState = .connectTool
                self.isExpanded = true
            }
            return
        }
        
        if currentState == .thinking || currentState == .connectTool { return }
        transitionState(to: .thinking)
        
        Task {
            do {
                let aiResponse = try await AIOrchestrator.shared.processInput(text)
                await handleAIResponse(aiResponse)
            } catch {
                await MainActor.run { self.showErrorState("Network connection failed") }
            }
        }
    }
    
    @MainActor
    private func handleAIResponse(_ response: AIResponse) async {
        switch response {
        case .text(let reply):
            self.latestResponse = reply
            self.transitionState(to: .speaking)
            
            Task {
                await VoiceEngine.shared.speak(reply)
                await MainActor.run { self.transitionState(to: .idle) }
            }
            
        case .toolAction(let name, let argsJSON, let toolCallId):
            let args = (try? JSONSerialization.jsonObject(with: argsJSON.data(using: .utf8) ?? Data())) as? [String: Any] ?? [:]
            if name == "create_linear_issue" {
                self.pendingActionName = "Create Linear Issue"
            } else if name == "schedule_calendar_event" {
                let summary = args["summary"] as? String ?? ""
                let start = args["start"] as? String ?? ""
                let attendeeEmail = args["attendeeEmail"] as? String
                self.approvalAction = "Schedule: \(summary)\nAt: \(start)"
                if let e = attendeeEmail {
                    self.approvalAction! += "\nInviting: \(e)"
                }
            } else if name == "dispatch_mesh_message" {
                let t = args["target"] as? String ?? ""
                let c = args["content"] as? String ?? ""
                self.approvalAction = "Contact: \(t)\nTo ask: \(c)"
            } else if name == "reply_mesh_message" {
                let r = args["reply_text"] as? String ?? ""
                self.approvalAction = "Reply to Mesh:\n\(r)"
            } else if name == "search_notion" {
                let q = args["query"] as? String ?? ""
                self.approvalAction = "Search Notion for:\n\(q)"
            } else if name == "read_notion_page" {
                let id = args["page_id"] as? String ?? ""
                self.approvalAction = "Read Notion Doc:\n\(id)"
            } else if name == "fetch_fireflies_transcripts" {
                self.approvalAction = "Extract Meeting Data\nfrom Fireflies.ai"
            } else if name == "start_recording" {
                self.approvalAction = "Join Meeting & Record"
            } else if name == "fireflies_get_transcript" {
                self.approvalAction = "Read specific transcript"
            } else if name == "analyze_and_publish_transcript" {
                self.approvalAction = "Write Tasks to Notion"
            } else if name == "analyze_screen_context" {
                self.approvalAction = "Analyzing Active Display"
            } else if name == "send_email" {
                let to   = args["to"] as? String ?? ""
                let subj = args["subject"] as? String ?? ""
                self.approvalAction = "Send email to \(to)\nSubject: \(subj)"
            } else if name == "search_email" {
                let q = args["query"] as? String ?? ""
                self.approvalAction = "Search Gmail for:\n\(q)"
            }
            
            if self.pendingActionName.isEmpty {
                self.pendingActionName = name
            }
            self.pendingActionDetails = argsJSON
            self.pendingToolCallId = toolCallId
            
            self.transitionState(to: .needsApproval)
            
            // Read-only tools auto-execute so the user doesn't have to tap through.
            // Write/destructive tools (send_email, schedule_calendar_event,
            // create_linear_issue, etc.) stay behind explicit approval.
            if name == "read_calendar" || name == "search_email" {
                self.approveAction()
            }
            if name == "start_recording" || name == "fireflies_get_transcript" || name == "analyze_and_publish_transcript" || name == "analyze_screen_context" {
                self.approveAction() // Seamless execution as requested
            }
        }
    }
    
    func approveAction() {
        guard currentState == .needsApproval, let id = pendingToolCallId else { return }
        let args = pendingActionDetails
        transitionState(to: .thinking)
        
        Task {
            do {
                var nativeResult = ""
                let argsDict = (try? JSONSerialization.jsonObject(with: args.data(using: .utf8) ?? Data())) as? [String: Any] ?? [:]
                
                if pendingActionName == "Create Linear Issue" {
                    struct LinearArgs: Codable { let title: String; let description: String }
                    guard let data = args.data(using: .utf8) else { throw URLError(.cannotDecodeRawData) }
                    let parsed = try JSONDecoder().decode(LinearArgs.self, from: data)
                    nativeResult = try await LinearAdapter.shared.createIssue(title: parsed.title, description: parsed.description)
                } 
                else if pendingActionName == "Schedule Calendar Event" {
                    let summary = argsDict["summary"] as? String ?? argsDict["title"] as? String ?? ""
                    let startStr = argsDict["start"] as? String ?? argsDict["startTimeISO"] as? String ?? ""
                    let email = argsDict["attendeeEmail"] as? String
                    
                    nativeResult = try await CalendarAdapter.shared.scheduleEvent(title: summary, startTimeISO: startStr, durationMinutes: "15", attendeeEmail: email)
                }
                else if pendingActionName == "Read Calendar" {
                    nativeResult = try await CalendarAdapter.shared.fetchEvents()
                }
                else if pendingActionName == "dispatch_mesh_message" {
                    let target = argsDict["target"] as? String ?? ""
                    let content = argsDict["content"] as? String ?? ""
                    nativeResult = try await SupabaseAdapter.shared.dispatchMeshMessage(to: target, content: content)
                }
                else if pendingActionName == "reply_mesh_message" {
                    let id = argsDict["network_id"] as? String ?? ""
                    let text = argsDict["reply_text"] as? String ?? ""
                    nativeResult = try await SupabaseAdapter.shared.replyMeshMessage(id: id, replyText: text)
                }
                else if pendingActionName == "search_notion" {
                    let q = argsDict["query"] as? String ?? ""
                    nativeResult = try await NotionAdapter.shared.search(query: q)
                }
                else if pendingActionName == "read_notion_page" {
                    let p = argsDict["page_id"] as? String ?? ""
                    nativeResult = try await NotionAdapter.shared.readPage(id: p)
                }
                else if pendingActionName == "fetch_fireflies_transcripts" {
                    nativeResult = try await FirefliesAdapter.shared.pullRecentMeetings()
                }
                else if pendingActionName == "fireflies_get_transcript" {
                    let id = argsDict["id"] as? String ?? ""
                    nativeResult = try await FirefliesAdapter.shared.getTranscript(id: id)
                }
                else if pendingActionName == "analyze_and_publish_transcript" {
                    let title = argsDict["title"] as? String ?? "Untitled"
                    let type = argsDict["type"] as? String ?? "unrelated_topic"
                    let topic = argsDict["topic_name"] as? String ?? ""
                    let summaryMarkdown = argsDict["summary_markdown"] as? String ?? ""
                    
                    nativeResult = try await NotionAdapter.shared.publishMeetingNotes(title: title, type: type, topic: topic, rawMarkdown: summaryMarkdown)
                }
                else if pendingActionName == "start_recording" {
                    let models = try await CalendarAdapter.shared.fetchUpcomingEventModels()
                    let now = Date()
                    let activeObj = models.first { abs($0.startDate.timeIntervalSince(now)) < 3600 }
                    if let meeting = activeObj, let link = meeting.hangoutLink {
                        if let url = URL(string: link) { 
                            let script = """
                            tell application "Google Chrome"
                                activate
                                if (count of windows) > 0 then
                                    tell window 1 to make new tab with properties {URL:"\(link)"}
                                else
                                    make new window
                                    set URL of active tab of window 1 to "\(link)"
                                end if
                            end tell
                            """
                            let p = Process()
                            p.executableURL = URL(fileURLWithPath: "/usr/bin/osascript")
                            p.arguments = ["-e", script]
                            if (try? p.run()) == nil { NSWorkspace.shared.open(url) }
                        }
                        nativeResult = try await FirefliesAdapter.shared.addToLiveMeeting(url: link, title: meeting.title)
                    } else {
                        nativeResult = "Failed: No active meeting found with a hangoutLink right now."
                    }
                }
                else if pendingActionName == "send_email" {
                    let to   = argsDict["to"] as? String ?? ""
                    let subj = argsDict["subject"] as? String ?? ""
                    let body = argsDict["body"] as? String ?? ""
                    nativeResult = try await GmailAdapter.shared.sendEmail(to: to, subject: subj, body: body)
                }
                else if pendingActionName == "search_email" {
                    let q = argsDict["query"] as? String ?? ""
                    nativeResult = try await GmailAdapter.shared.searchFormatted(query: q)
                }
                else if pendingActionName == "analyze_screen_context" {
                    do {
                        let jpeg = try await ScreenCapturer.capturePrimaryJPEG()
                        let b64 = jpeg.base64EncodedString()
                        ActivityLogger.shared.record(action: self.pendingActionName, target: "ScreenCapture", status: "Success")
                        let finalResponse = try await AIOrchestrator.shared.submitVisionToolResult(toolCallId: id, base64Image: b64)
                        await handleAIResponse(finalResponse)
                        return
                    } catch {
                        nativeResult = "Screen capture failed: \(error.localizedDescription). Grant Screen Recording in System Settings, then restart Nomi."
                    }
                }
                
                ActivityLogger.shared.record(action: self.pendingActionName, target: "API Request", status: "Success")
                
                // Sync with Brain
                let finalResponse = try await AIOrchestrator.shared.submitToolResult(toolCallId: id, result: nativeResult)
                await handleAIResponse(finalResponse)
            } catch {
                let errStr = (error as NSError).userInfo[NSLocalizedDescriptionKey] as? String ?? error.localizedDescription
                await MainActor.run { self.showErrorState("Execution Failed: \(errStr)") }
            }
        }
    }
    
    func rejectAction() {
        guard currentState == .needsApproval, let id = pendingToolCallId else { return }
        transitionState(to: .thinking)
        Task {
            do {
                ActivityLogger.shared.record(action: pendingActionName, target: pendingActionDetails, status: "Rejected")
                let cancelResponse = try await AIOrchestrator.shared.submitToolResult(toolCallId: id, result: "User explicitly rejected the action. Acknowledge this politely.")
                await handleAIResponse(cancelResponse)
            } catch {
                await MainActor.run { self.transitionState(to: .idle) }
            }
        }
    }
    
    func requireApproval(for action: String) {
        self.approvalAction = action
        self.transitionState(to: .needsApproval)
        self.isExpanded = true
    }
    
    func handleApproval(approved: Bool) {
        self.approvalAction = nil
        if approved {
            self.transitionState(to: .thinking)
            // Execute action...
            Task {
                try? await Task.sleep(nanoseconds: 1_000_000_000)
                self.showSuccessToast("Executed successfully")
            }
        } else {
            self.transitionState(to: .idle)
            self.isExpanded = false
        }
    }
    
    func showSuccessToast(_ message: String) {
        self.latestToast = message
        self.transitionState(to: .success)
        
        Task {
            try? await Task.sleep(nanoseconds: 2_000_000_000)
            if self.currentState == .success {
                self.transitionState(to: .idle)
                self.latestToast = nil
            }
        }
    }
    
    func showErrorState(_ message: String) {
        self.latestToast = message
        self.transitionState(to: .error)
        
        Task {
            try? await Task.sleep(nanoseconds: 3_000_000_000)
            if self.currentState == .error {
                self.transitionState(to: .idle)
                self.latestToast = nil
            }
        }
    }
    
    func toggleListening() {
        if currentState == .listening {
            transitionState(to: .idle)
            SpeechEngine.shared.stop()
        } else {
            Task { @MainActor in
                let authorized = await SpeechEngine.shared.requestAuthorization()
                if authorized {
                    self.beginDictation()
                } else {
                    self.showErrorState("Microphone permission denied")
                }
            }
        }
    }

    func transitionState(to newState: CompanionState) {
        withAnimation(.spring(response: 0.4, dampingFraction: 0.7)) {
            self.currentState = newState

            if newState == .speaking || newState == .thinking || newState == .listening || newState == .connectTool || newState == .greeting {
                self.isExpanded = true
            } else if newState == .idle {
                self.isExpanded = self.isHovered
                // Return to ambient listening only if the user has opted in. In
                // push-to-talk mode we stay silent until the hotkey fires, which
                // keeps the orange mic indicator off during idle.
                if Config.listeningMode == .ambient {
                    SpeechEngine.shared.startAmbient()
                } else {
                    SpeechEngine.shared.stop()
                }
            }
        }
    }
}

```