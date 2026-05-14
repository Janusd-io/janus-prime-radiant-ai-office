---
type: source
source_type: laptop
title: testFireflies
slug: testfireflies
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/testFireflies.swift
original_size: 828
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# testFireflies

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/testFireflies.swift` on 2026-05-14._

```swift
import Foundation

let token = UserDefaults.standard.string(forKey: "firefliesAPIKey") ?? "MISSING"
print("TOKEN IN DEFAULTS: \(token.isEmpty ? "EMPTY" : token.prefix(10) + "...")")
// Even if missing, let's test a dummy token or log the exact error Fireflies returns
let urlStr = "https://api.fireflies.ai/graphql"
guard let endpoint = URL(string: urlStr) else { exit(1) }
var req = URLRequest(url: endpoint)
req.httpMethod = "POST"
// We'll use the user's Nomi Fireflies token if we can, but since this runs out of sandbox it might not have access to Nomi's UserDefaults.
// I will just use Nomi's default token logic if possible? No, UserDefaults.standard out of sandbox is inaccessible.
// Let's just grep NomiStateLogger or just run a swift script that reads FirefliesAPIKey using Nomi's standard mechanisms? No, I can't.


```