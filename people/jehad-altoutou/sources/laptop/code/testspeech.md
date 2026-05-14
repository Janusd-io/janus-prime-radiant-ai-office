---
type: source
source_type: laptop
title: testSpeech
slug: testspeech
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/testSpeech.swift
original_size: 599
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# testSpeech

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/testSpeech.swift` on 2026-05-14._

```swift
import AppKit

class Tester: NSObject, NSSpeechRecognizerDelegate {
    let r = NSSpeechRecognizer()
    override init() {
        super.init()
        guard let r = r else { print("NSSpeechRecognizer init failed"); exit(1) }
        r.commands = ["hello test"]
        r.delegate = self
        r.startListening()
        print("Listening for 'hello test'...")
    }
    func speechRecognizer(_ sender: NSSpeechRecognizer, didRecognizeCommand command: String) {
        print("Recognized: \(command)")
        exit(0)
    }
}
let t = Tester()
RunLoop.main.run(until: Date(timeIntervalSinceNow: 5))

```