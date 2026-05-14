---
type: source
source_type: laptop
title: testDate
slug: testdate
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/testDate.swift
original_size: 1127
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# testDate

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/testDate.swift` on 2026-05-14._

```swift
import Foundation
print(Date())
print(ISO8601DateFormatter().string(from: Date()))
let token = "ya29.a0Aa7MYioEvM08p_G9rjCwLx-X3pxPreRxUpjMzlGnbYNWv5CI1RoeZrg2TrRoUv_FEV0nyM5e9SVJMOTrdWLJLzXxoElIHGHuAHCgdDSldcaeeR4N5Wpu4CEMY4_7RnXcIdI5z3hT2dO3h47whgpWj1ZyRP9Ul6jFGSXgiAPJ440kEbbHVeoPrpcobCjJN9qUlJ1uBzYaCgYKARoSARMSFQHGX2MieDcXDkT9XK0mGBuj08zkfA0206"
var components = URLComponents(string: "https://www.googleapis.com/calendar/v3/calendars/primary/events")!
// SET TIME MIN TO 1 MINUTE AGO
components.queryItems = [
    URLQueryItem(name: "timeMin", value: "2026-04-06T00:00:00Z"), 
    URLQueryItem(name: "maxResults", value: "5"),
    URLQueryItem(name: "singleEvents", value: "true"),
    URLQueryItem(name: "orderBy", value: "startTime")
]
var req = URLRequest(url: components.url!)
req.httpMethod = "GET"
req.addValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
let sem = DispatchSemaphore(value: 0)
URLSession.shared.dataTask(with: req) { data, response, error in 
    defer { sem.signal() }
    guard let data = data else { return }
    print(String(data: data, encoding: .utf8) ?? "")
}.resume()
sem.wait()

```