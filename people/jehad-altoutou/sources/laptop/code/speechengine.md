---
type: source
source_type: laptop
title: SpeechEngine
slug: speechengine
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/SpeechEngine.swift
original_size: 15013
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# SpeechEngine

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/Services/SpeechEngine.swift` on 2026-05-14._

```swift
import Foundation
import AVFoundation
import Speech
import OSLog

public enum ListeningMode: String, Sendable {
    case off
    case pushToTalk
    case ambient
}

public enum SpeechEngineState: Equatable, Sendable {
    case idle
    case ambient
    case dictation
}

public enum SpeechEngineError: Error, LocalizedError {
    case notAuthorized
    case recognizerUnavailable
    case onDeviceUnsupported
    case audioEngineFailed(String)

    public var errorDescription: String? {
        switch self {
        case .notAuthorized:        return "Microphone or speech recognition permission denied."
        case .recognizerUnavailable: return "Speech recognizer is not available on this device."
        case .onDeviceUnsupported:  return "This Mac does not support on-device speech recognition."
        case .audioEngineFailed(let m): return "Audio engine failed: \(m)"
        }
    }
}

/// Production speech engine.
///
/// Design invariants:
///   1. The `AVAudioEngine` tap is installed exactly **once** per engine lifetime, and is
///      rebuilt only in response to `AVAudioEngineConfigurationChange` (e.g., AirPods
///      connect/disconnect). This prevents the mic-indicator flicker and Bluetooth HFP
///      re-negotiation that plagued the previous implementation.
///   2. Recognition uses `requiresOnDeviceRecognition = true`, which removes the
///      60-second timeout on Apple Silicon / macOS 14+. No restart timer exists.
///   3. An RMS voice-activity gate suppresses forwarding to the recognizer during
///      silence, driving idle CPU toward zero.
///   4. Audio is always converted to 16 kHz mono Float32 before being appended, so the
///      recognizer is isolated from hardware-format changes.
public final class SpeechEngine: @unchecked Sendable {

    public static let shared = SpeechEngine()

    // MARK: Observable state (simple callbacks — no Combine required)

    /// Emitted whenever the engine's state changes.
    public var onStateChange: (@Sendable (SpeechEngineState) -> Void)?
    /// Emitted when the wake phrase is detected. Always on main queue.
    public var onWakeWord: (@Sendable () -> Void)?
    /// Partial and final transcripts during dictation. `isFinal == true` indicates the
    /// engine has stopped; the caller should transition state.
    public var onDictation: (@Sendable (_ text: String, _ isFinal: Bool) -> Void)?
    /// Fatal errors — speech/mic permission denied, engine failed to start, etc.
    public var onError: (@Sendable (SpeechEngineError) -> Void)?

    public private(set) var state: SpeechEngineState = .idle {
        didSet { if oldValue != state { onStateChange?(state) } }
    }

    // MARK: Wake phrases — normalized, space-padded for whole-word matching.

    private let wakePhrases: [String] = [
        " hey nomi ", " ok nomi ", " hi nomi ", " nomi ",
        // Common mis-recognitions worth catching:
        " know me ", " naomi ", " noni "
    ]

    // MARK: Internals

    private let log = Logger(subsystem: "com.antigravity.nomi", category: "Speech")
    private let queue = DispatchQueue(label: "com.antigravity.nomi.speech", qos: .userInitiated)

    private let recognizer: SFSpeechRecognizer?
    private var request: SFSpeechAudioBufferRecognitionRequest?
    private var task: SFSpeechRecognitionTask?

    private let audioEngine = AVAudioEngine()
    private var converter: AVAudioConverter?
    private var tapFormat: AVAudioFormat?
    private var configChangeObserver: NSObjectProtocol?

    /// Target format fed to `SFSpeechAudioBufferRecognitionRequest`.
    private let targetFormat: AVAudioFormat = {
        AVAudioFormat(
            commonFormat: .pcmFormatFloat32,
            sampleRate: 16_000,
            channels: 1,
            interleaved: false
        )!
    }()

    // VAD
    private let voiceThreshold: Float = 0.012
    private let voiceHangoverSeconds: TimeInterval = 1.5
    private var lastVoiceAt: Date = .distantPast

    // Wake-phrase sliding buffer
    private var wakeWindow: String = ""
    private let wakeWindowMaxChars = 80

    private init() {
        self.recognizer = SFSpeechRecognizer(locale: Locale(identifier: "en-US"))
        observeConfigurationChange()
    }

    // MARK: - Authorization

    public func requestAuthorization() async -> Bool {
        let speechOK: Bool = await withCheckedContinuation { cont in
            SFSpeechRecognizer.requestAuthorization { status in
                cont.resume(returning: status == .authorized)
            }
        }
        guard speechOK else { return false }

        switch AVCaptureDevice.authorizationStatus(for: .audio) {
        case .authorized: return true
        case .notDetermined:
            return await AVCaptureDevice.requestAccess(for: .audio)
        default: return false
        }
    }

    // MARK: - Public control

    /// Start ambient wake-word listening. Idempotent.
    public func startAmbient() {
        queue.async { [weak self] in self?._startAmbient() }
    }

    /// Begin active dictation. If ambient was running it is cleanly pivoted.
    public func startDictation() {
        queue.async { [weak self] in self?._startDictation() }
    }

    /// Stop all listening. The audio engine is also stopped so the mic indicator turns off.
    public func stop() {
        queue.async { [weak self] in self?._stop() }
    }

    // MARK: - Private control (serialized on `queue`)

    private func _startAmbient() {
        guard state != .ambient else { return }
        guard let recognizer, recognizer.isAvailable else {
            emit(.recognizerUnavailable); return
        }
        guard recognizer.supportsOnDeviceRecognition else {
            // We refuse to run 24/7 ambient listening against the cloud. It was the
            // original bug's root cause — Apple's cloud recognizer enforces a 60s
            // timeout and degrades Bluetooth audio quality. On-device only.
            emit(.onDeviceUnsupported); return
        }

        do {
            try ensureAudioEngineRunning()
            try startRecognitionTask(forDictation: false)
            DispatchQueue.main.async { [weak self] in self?.state = .ambient }
            log.info("SpeechEngine: ambient listening started (on-device).")
        } catch let e as SpeechEngineError {
            emit(e)
        } catch {
            emit(.audioEngineFailed(error.localizedDescription))
        }
    }

    private func _startDictation() {
        tearDownRecognitionTask()
        do {
            try ensureAudioEngineRunning()
            try startRecognitionTask(forDictation: true)
            DispatchQueue.main.async { [weak self] in self?.state = .dictation }
            log.info("SpeechEngine: dictation started.")
        } catch let e as SpeechEngineError {
            emit(e)
        } catch {
            emit(.audioEngineFailed(error.localizedDescription))
        }
    }

    private func _stop() {
        tearDownRecognitionTask()
        if audioEngine.isRunning {
            audioEngine.stop()
        }
        DispatchQueue.main.async { [weak self] in self?.state = .idle }
        log.info("SpeechEngine: stopped.")
    }

    // MARK: - Audio engine

    private func ensureAudioEngineRunning() throws {
        if audioEngine.isRunning { return }

        let input = audioEngine.inputNode
        let hwFormat = input.outputFormat(forBus: 0)

        // Guard against the hardware reporting a zero-channel / zero-rate format, which
        // happens briefly during device switches.
        guard hwFormat.sampleRate > 0, hwFormat.channelCount > 0 else {
            throw SpeechEngineError.audioEngineFailed("Input format not ready (rate=\(hwFormat.sampleRate), ch=\(hwFormat.channelCount)).")
        }

        if tapFormat?.isEqual(hwFormat) != true {
            input.removeTap(onBus: 0)
            input.installTap(onBus: 0, bufferSize: 2048, format: hwFormat) { [weak self] buffer, _ in
                self?.queue.async { self?.handleCapture(buffer) }
            }
            converter = AVAudioConverter(from: hwFormat, to: targetFormat)
            tapFormat = hwFormat
            log.debug("SpeechEngine: installed tap — rate=\(hwFormat.sampleRate), ch=\(hwFormat.channelCount)")
        }

        audioEngine.prepare()
        do {
            try audioEngine.start()
        } catch {
            throw SpeechEngineError.audioEngineFailed(error.localizedDescription)
        }
    }

    private func observeConfigurationChange() {
        configChangeObserver = NotificationCenter.default.addObserver(
            forName: .AVAudioEngineConfigurationChange,
            object: audioEngine,
            queue: nil
        ) { [weak self] _ in
            guard let self else { return }
            self.queue.async { self.handleConfigurationChange() }
        }
    }

    private func handleConfigurationChange() {
        log.info("SpeechEngine: AVAudioEngineConfigurationChange — rebuilding.")
        let previousState = state

        tearDownRecognitionTask()
        if audioEngine.isRunning { audioEngine.stop() }
        audioEngine.inputNode.removeTap(onBus: 0)
        tapFormat = nil
        converter = nil

        guard previousState != .idle else { return }

        do {
            try ensureAudioEngineRunning()
            try startRecognitionTask(forDictation: previousState == .dictation)
        } catch let e as SpeechEngineError {
            emit(e)
        } catch {
            emit(.audioEngineFailed(error.localizedDescription))
        }
    }

    // MARK: - Recognition

    private func startRecognitionTask(forDictation: Bool) throws {
        guard let recognizer else { throw SpeechEngineError.recognizerUnavailable }

        let req = SFSpeechAudioBufferRecognitionRequest()
        req.shouldReportPartialResults = true
        if recognizer.supportsOnDeviceRecognition {
            req.requiresOnDeviceRecognition = true
        } else {
            throw SpeechEngineError.onDeviceUnsupported
        }
        if #available(macOS 13, *) {
            req.addsPunctuation = forDictation
        }
        if forDictation {
            req.taskHint = .dictation
        } else {
            req.taskHint = .search
        }
        self.request = req
        self.wakeWindow = ""

        self.task = recognizer.recognitionTask(with: req) { [weak self] result, error in
            guard let self else { return }
            self.queue.async {
                self.handleRecognition(result: result, error: error, forDictation: forDictation)
            }
        }
    }

    private func tearDownRecognitionTask() {
        request?.endAudio()
        task?.cancel()
        task = nil
        request = nil
        wakeWindow = ""
    }

    // MARK: - Capture pipeline

    private func handleCapture(_ buffer: AVAudioPCMBuffer) {
        guard let request, let converter else { return }

        // VAD gate — if silence, skip the whole convert/append path.
        let rms = Self.rms(of: buffer)
        if rms > voiceThreshold {
            lastVoiceAt = Date()
        }
        let withinVoiceWindow = Date().timeIntervalSince(lastVoiceAt) < voiceHangoverSeconds
        guard withinVoiceWindow else { return }

        // Down-convert to 16 kHz mono Float32.
        let ratio = targetFormat.sampleRate / buffer.format.sampleRate
        let capacity = AVAudioFrameCount(Double(buffer.frameLength) * ratio) + 1024
        guard let out = AVAudioPCMBuffer(pcmFormat: targetFormat, frameCapacity: capacity) else { return }

        var supplied = false
        var convError: NSError?
        let status = converter.convert(to: out, error: &convError) { _, flag in
            if supplied {
                flag.pointee = .noDataNow
                return nil
            }
            supplied = true
            flag.pointee = .haveData
            return buffer
        }

        switch status {
        case .haveData, .inputRanDry:
            request.append(out)
        case .endOfStream:
            break
        case .error:
            log.error("SpeechEngine: converter error — \(convError?.localizedDescription ?? "unknown")")
        @unknown default:
            break
        }
    }

    private func handleRecognition(result: SFSpeechRecognitionResult?, error: Error?, forDictation: Bool) {
        if let result {
            let transcript = result.bestTranscription.formattedString

            if forDictation {
                DispatchQueue.main.async { [weak self] in
                    self?.onDictation?(transcript, result.isFinal)
                }
                if result.isFinal {
                    _stop()
                }
            } else {
                // Ambient — slide window, scan for wake phrase.
                let normalized = " " + transcript.lowercased() + " "
                wakeWindow = String((wakeWindow + normalized).suffix(wakeWindowMaxChars))
                if wakePhrases.contains(where: { wakeWindow.contains($0) }) {
                    log.info("SpeechEngine: wake phrase matched — firing.")
                    wakeWindow = ""
                    DispatchQueue.main.async { [weak self] in self?.onWakeWord?() }
                }
            }
        }

        if let error {
            let nsErr = error as NSError
            // Codes 203 (no speech), 216 (cancelled), 301 (stopped), 1110 (no speech),
            // 1700 (connection) can all be benign end-of-task signals.
            let benign: Set<Int> = [203, 216, 301, 1110]
            if !benign.contains(nsErr.code) {
                log.error("SpeechEngine: recognition error \(nsErr.code) — \(nsErr.localizedDescription)")
            }

            // Atomic re-arm: only the recognition task is torn down. The audio engine
            // and its tap stay up, so no mic-indicator flicker, no HFP renegotiation.
            switch state {
            case .ambient:
                tearDownRecognitionTask()
                do { try startRecognitionTask(forDictation: false) }
                catch let e as SpeechEngineError { emit(e) }
                catch { emit(.audioEngineFailed(error.localizedDescription)) }
            case .dictation:
                _stop()
            case .idle:
                break
            }
        }
    }

    // MARK: - Helpers

    private static func rms(of buffer: AVAudioPCMBuffer) -> Float {
        guard let channels = buffer.floatChannelData else { return 0 }
        let frames = Int(buffer.frameLength)
        guard frames > 0 else { return 0 }
        var sum: Float = 0
        let data = channels[0]
        var i = 0
        while i < frames {
            let s = data[i]
            sum += s * s
            i += 1
        }
        return (sum / Float(frames)).squareRoot()
    }

    private func emit(_ e: SpeechEngineError) {
        log.error("SpeechEngine error: \(e.localizedDescription)")
        DispatchQueue.main.async { [weak self] in self?.onError?(e) }
    }
}

```