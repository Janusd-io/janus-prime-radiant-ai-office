---
type: source
source_type: laptop
title: NomiFaceView
slug: nomifaceview
created: 2026-04-21
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/NomiFaceView.swift
original_size: 23058
original_ext: .swift
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# NomiFaceView

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Nomi-Internal-Intelligence/Sources/UI/NomiFaceView.swift` on 2026-05-14._

```swift
import SwiftUI

/// Nomi's face. She's two glowing eyes + a mouth + optional overlays.
///
/// Personality comes from *motion*, not geometry:
///   - Slow breathing, natural blinks, curious wandering gaze during idle
///   - A look-left / look-right / wide-eyed `!` when the user has been
///     away for a minute ("where's my human?")
///   - Pulsing oval mouth while speaking (replaced the old waveform bars)
///   - Open round eyes during speech (the old crescent eyes looked sleepy
///     and their glows merged into a weird ring artifact)
///   - Cheek blush on happy states, thought bubbles when thinking, small
///     hop on the daily greeting
struct NomiFaceView: View {
    @Binding var state: CompanionState

    // State-driven pose
    @State private var eyeHeightScale: CGFloat = 1.0
    @State private var eyeCurve: CGFloat = 0.0
    @State private var eyeSpacing: CGFloat = 16.0
    @State private var eyeWidthScale: CGFloat = 1.0

    @State private var listenAuraOpacity: Double = 0.0
    @State private var thoughtBubbleOpacity: Double = 0.0
    @State private var blushOpacity: Double = 0.0

    @State private var mouthOpacity: Double = 0.0
    @State private var mouthType: Int = 0   // 1=SpeakingOval, 2=Smile, 3=Frown, 4=BreathOval

    @State private var errorShakeOffsetX: CGFloat = 0.0
    @State private var greetingBounce: CGFloat = 0.0

    // "Where's my human?" search animation
    @State private var isSearching: Bool = false
    @State private var searchStartRefDate: Double = 0
    @State private var searchTask: Task<Void, Never>? = nil

    var body: some View {
        TimelineView(.animation) { tl in
            let t = tl.date.timeIntervalSinceReferenceDate
            Canvas { ctx, size in
                let cx = size.width / 2
                let cy = size.height / 2 - 2 + greetingBounce

                // Listening aura
                if listenAuraOpacity > 0 {
                    let phase = CGFloat(t * 1.5).truncatingRemainder(dividingBy: 1.0)
                    for i in 0..<2 {
                        let rp = (phase + CGFloat(i) * 0.5).truncatingRemainder(dividingBy: 1.0)
                        let r = 16 + rp * 24
                        var g = ctx
                        g.opacity = Double((1 - rp)) * listenAuraOpacity * 0.4
                        g.stroke(
                            Ellipse().path(in: CGRect(x: cx-r, y: cy-r, width: r*2, height: r*2)),
                            with: .color(eyeBaseColor),
                            lineWidth: 1.5
                        )
                    }
                }

                // Thought bubbles
                if thoughtBubbleOpacity > 0 {
                    drawThoughtBubbles(ctx: &ctx, cx: cx, cy: cy - 24, t: t)
                }

                // Gaze — curious wandering (idle) + search overrides
                let searchPose = currentSearchPose(at: t)
                let gaze = searchPose.isActive
                    ? (x: searchPose.gazeX, y: CGFloat(0))
                    : curiousGaze(at: t)

                let eyeScale: CGFloat = searchPose.isActive ? searchPose.eyeScale : 1.0

                // Eyes
                let life = EyeLife(at: t, state: state)
                let eyeY = cy - 4 + life.verticalBreath + gaze.y
                let leftEye = CGPoint(
                    x: cx - eyeSpacing + errorShakeOffsetX + gaze.x,
                    y: eyeY
                )
                let rightEye = CGPoint(
                    x: cx + eyeSpacing + errorShakeOffsetX + gaze.x,
                    y: eyeY
                )
                drawEye(ctx: &ctx, center: leftEye, life: life, scaleMultiplier: eyeScale)
                drawEye(ctx: &ctx, center: rightEye, life: life, scaleMultiplier: eyeScale)

                // Blush
                if blushOpacity > 0 {
                    drawBlush(
                        ctx: &ctx,
                        leftCenter: CGPoint(x: leftEye.x - 2, y: eyeY + 9),
                        rightCenter: CGPoint(x: rightEye.x + 2, y: eyeY + 9),
                        t: t
                    )
                }

                // Mouth
                if mouthOpacity > 0 && !searchPose.isActive {
                    drawMouth(ctx: &ctx, cx: cx + errorShakeOffsetX, cy: cy + 14, t: t)
                }

                // Exclamation mark during search
                if searchPose.exclamation > 0 {
                    drawExclamation(ctx: &ctx, cx: cx, cy: cy - 24, opacity: searchPose.exclamation)
                }
            }
        }
        .frame(width: 100, height: 80)
        .onAppear { applyState(state, animated: false) }
        .onChange(of: state) { _, s in
            applyState(s, animated: true)
            scheduleSearchingLoop(for: s)
        }
    }

    // MARK: - State → visuals

    private func applyState(_ s: CompanionState, animated: Bool) {
        let update = {
            listenAuraOpacity = 0
            thoughtBubbleOpacity = 0
            blushOpacity = 0

            switch s {
            case .idle:
                eyeHeightScale = 1.0; eyeCurve = 0.0; eyeSpacing = 16; eyeWidthScale = 1.0
                mouthOpacity = 0.0; mouthType = 0
            case .listening:
                eyeHeightScale = 1.05; eyeCurve = 0.0; eyeSpacing = 18; eyeWidthScale = 1.1
                mouthOpacity = 0.0; mouthType = 0
                listenAuraOpacity = 1.0
            case .thinking:
                eyeHeightScale = 0.85; eyeCurve = 0.0; eyeSpacing = 16; eyeWidthScale = 0.95
                mouthOpacity = 0.0; mouthType = 0
                thoughtBubbleOpacity = 1.0
            case .speaking:
                // Open, engaged eyes (no crescent — the crescent + glow
                // combination was what read as "sad" and produced the
                // oval-ring artifact between the eyes).
                eyeHeightScale = 0.9; eyeCurve = 0.0; eyeSpacing = 16; eyeWidthScale = 1.0
                mouthOpacity = 1.0; mouthType = 1   // speaking oval
                blushOpacity = 0.25
            case .success:
                eyeHeightScale = 0.5; eyeCurve = 1.0; eyeSpacing = 16; eyeWidthScale = 1.1
                mouthOpacity = 1.0; mouthType = 2   // smile
                blushOpacity = 0.55
            case .error:
                eyeHeightScale = 0.6; eyeCurve = -1.0; eyeSpacing = 16; eyeWidthScale = 1.0
                mouthOpacity = 1.0; mouthType = 3   // frown
                triggerShake()
            case .needsApproval:
                eyeHeightScale = 1.1; eyeCurve = 0.0; eyeSpacing = 16; eyeWidthScale = 0.9
                mouthOpacity = 1.0; mouthType = 4   // slow breathing oval
            case .connectTool:
                eyeHeightScale = 1.0; eyeCurve = 0.0; eyeSpacing = 16; eyeWidthScale = 1.0
                mouthOpacity = 0.0; mouthType = 0
            case .greeting:
                eyeHeightScale = 0.55; eyeCurve = 0.95; eyeSpacing = 16; eyeWidthScale = 1.15
                mouthOpacity = 1.0; mouthType = 2   // smile
                blushOpacity = 0.55
                triggerGreetingBounce()
            }
        }

        if animated {
            withAnimation(.spring(response: 0.45, dampingFraction: 0.72)) { update() }
        } else {
            update()
        }
    }

    private func triggerShake() {
        let offsets: [CGFloat] = [4, -4, 3, -3, 2, -2, 0]
        for (i, v) in offsets.enumerated() {
            DispatchQueue.main.asyncAfter(deadline: .now() + Double(i) * 0.05) {
                withAnimation(.easeInOut(duration: 0.05)) { errorShakeOffsetX = v }
            }
        }
    }

    private func triggerGreetingBounce() {
        let keyframes: [(delay: Double, value: CGFloat, duration: Double)] = [
            (0.00,  0,    0.0),
            (0.05, -7,    0.22),
            (0.28,  0,    0.18),
            (0.50, -3,    0.14),
            (0.68,  0,    0.14)
        ]
        for kf in keyframes {
            DispatchQueue.main.asyncAfter(deadline: .now() + kf.delay) {
                withAnimation(.spring(response: kf.duration, dampingFraction: 0.65)) {
                    greetingBounce = kf.value
                }
            }
        }
    }

    // MARK: - Curious gaze (idle wander)

    /// Gentle eye wandering while idle — every ~4.5s, eyes drift to a fresh
    /// direction, hold, and ease back. Deterministic from `t`, so pausing
    /// and resuming reads identical.
    private func curiousGaze(at t: Double) -> (x: CGFloat, y: CGFloat) {
        guard state == .idle else { return (0, 0) }

        let cycleLen: Double = 4.5
        let cycleIndex = floor(t / cycleLen)
        let phase = t.truncatingRemainder(dividingBy: cycleLen)

        // Pseudo-random but deterministic target per cycle.
        let hash = sin(cycleIndex * 2.39 + 0.73) * 0.5 + 0.5          // 0..1
        let angle = hash * 2 * .pi
        let targetX = CGFloat(cos(angle)) * 3.5
        let targetY = CGFloat(sin(angle)) * 1.4

        // Envelope: ease-in (0 → 1) over 0.6s, hold 1.0s, ease-out over 0.6s, rest.
        let intensity: Double
        if phase < 0.6          { intensity = phase / 0.6 }
        else if phase < 1.6     { intensity = 1.0 }
        else if phase < 2.2     { intensity = 1.0 - (phase - 1.6) / 0.6 }
        else                    { intensity = 0 }

        return (targetX * CGFloat(intensity), targetY * CGFloat(intensity))
    }

    // MARK: - "Where's my human?" search

    /// Schedules a recurring search animation when Nomi sits idle for 60s.
    /// Cancelled the moment she becomes active again.
    private func scheduleSearchingLoop(for s: CompanionState) {
        searchTask?.cancel()
        isSearching = false

        guard s == .idle else { return }

        searchTask = Task { @MainActor in
            // Wait 60s of continuous idle before the first check.
            try? await Task.sleep(nanoseconds: 60_000_000_000)
            guard !Task.isCancelled else { return }

            while !Task.isCancelled {
                searchStartRefDate = Date().timeIntervalSinceReferenceDate
                isSearching = true

                // Total sequence length ~3.8s (see currentSearchPose timings).
                try? await Task.sleep(nanoseconds: 3_800_000_000)
                guard !Task.isCancelled else { break }
                isSearching = false

                // Rest ~90s before wondering again.
                try? await Task.sleep(nanoseconds: 90_000_000_000)
                guard !Task.isCancelled else { break }
            }
        }
    }

    /// Piecewise keyframed pose during the search sequence.
    ///   0.00 – 0.70s : gaze pans 0 → -7 (look left)
    ///   0.70 – 1.40s : gaze pans -7 → +7 (look right)
    ///   1.40 – 1.70s : return to center, eyes scale up
    ///   1.70 – 1.90s : exclamation fades in
    ///   1.90 – 3.20s : hold surprised
    ///   3.20 – 3.80s : exclamation fades out, eyes settle
    private func currentSearchPose(at t: Double) -> (isActive: Bool, gazeX: CGFloat, eyeScale: CGFloat, exclamation: Double) {
        guard isSearching else { return (false, 0, 1, 0) }
        let dt = t - searchStartRefDate

        if dt < 0 || dt > 3.8 { return (false, 0, 1, 0) }

        let easeInOut: (Double) -> Double = { u in
            0.5 - 0.5 * cos(.pi * min(1.0, max(0.0, u)))
        }

        if dt < 0.7 {
            let u = dt / 0.7
            return (true, -7 * CGFloat(easeInOut(u)), 1.0, 0)
        } else if dt < 1.4 {
            let u = (dt - 0.7) / 0.7
            return (true, CGFloat(-7 + 14 * easeInOut(u)), 1.0, 0)
        } else if dt < 1.7 {
            let u = (dt - 1.4) / 0.3
            return (true, CGFloat(7 * (1 - easeInOut(u))), 1.0 + 0.22 * CGFloat(easeInOut(u)), 0)
        } else if dt < 1.9 {
            let u = (dt - 1.7) / 0.2
            return (true, 0, 1.22, easeInOut(u))
        } else if dt < 3.2 {
            return (true, 0, 1.22, 1.0)
        } else {
            let u = (dt - 3.2) / 0.6
            return (true, 0, 1.22 - 0.22 * CGFloat(easeInOut(u)), 1.0 - easeInOut(u))
        }
    }

    // MARK: - Colors

    private var eyeBaseColor: Color {
        switch state {
        case .idle:          return .white
        case .listening:     return Color(hue: 0.55, saturation: 0.3, brightness: 1.0)
        case .thinking:      return Color(hue: 0.75, saturation: 0.4, brightness: 1.0)
        case .speaking:      return Color(hue: 0.52, saturation: 0.3, brightness: 1.0)
        case .success:       return Color(hue: 0.36, saturation: 0.4, brightness: 1.0)
        case .error:         return Color(hue: 0.02, saturation: 0.6, brightness: 1.0)
        case .needsApproval: return Color(hue: 0.08, saturation: 0.5, brightness: 1.0)
        case .connectTool:   return .white
        case .greeting:      return Color(hue: 0.55, saturation: 0.4, brightness: 1.0)
        }
    }

    private var eyeGlowMultiplier: Double { state == .idle ? 0.35 : 0.8 }
    private var blushColor: Color { Color(hue: 0.98, saturation: 0.55, brightness: 1.0) }

    // MARK: - Eyes

    private func drawEye(ctx: inout GraphicsContext, center: CGPoint, life: EyeLife, scaleMultiplier: CGFloat) {
        let baseR: CGFloat = 7
        let w = baseR * eyeWidthScale * life.breathScale * scaleMultiplier
        let h = baseR * eyeHeightScale * life.breathScale * life.blinkScaleY * scaleMultiplier

        let rect = CGRect(x: center.x - w, y: center.y - h, width: w*2, height: h*2)
        var p = Path()

        if abs(eyeCurve) < 0.1 {
            p.addEllipse(in: rect)
        } else {
            let curveAmt = eyeCurve * h * 1.5
            p.move(to: CGPoint(x: rect.minX, y: center.y))
            p.addQuadCurve(to: CGPoint(x: rect.maxX, y: center.y),
                           control: CGPoint(x: center.x, y: center.y - curveAmt))
            p.addQuadCurve(to: CGPoint(x: rect.minX, y: center.y),
                           control: CGPoint(x: center.x, y: center.y - curveAmt * 0.3))
        }

        let glowPulse = 0.9 + 0.2 * life.breathPhase
        var glow2 = ctx
        glow2.addFilter(.blur(radius: 12))
        glow2.opacity = eyeGlowMultiplier * 0.4 * glowPulse
        glow2.fill(p, with: .color(eyeBaseColor))

        var glow1 = ctx
        glow1.addFilter(.blur(radius: 5))
        glow1.opacity = eyeGlowMultiplier * 0.75 * glowPulse
        glow1.fill(p, with: .color(eyeBaseColor))

        ctx.fill(p, with: .color(.white))
    }

    // MARK: - Mouth

    private func drawMouth(ctx: inout GraphicsContext, cx: CGFloat, cy: CGFloat, t: Double) {
        var mCtx = ctx
        mCtx.opacity = mouthOpacity

        switch mouthType {
        case 1: // Speaking — stroked lip outline with a dark cavity between,
                // shaped by a layered phoneme-like cadence. The outlined form
                // reads as "mouth with teeth" instead of "glowing blob".
            // Three layered sines at different frequencies + phases model the
            // alternation between vowel opens and consonant closes, giving a
            // much more natural speech rhythm than a single amplitude pulse.
            let vowel     = abs(sin(t * 7.2))                       // syllable beat
            let consonant = abs(sin(t * 12.6 + 1.4))                // faster closes
            let shape     = sin(t * 3.1 + 0.4) * 0.5 + 0.5          // slow width shift
            // Hold the mouth at least barely open so she's never "closed" mid-word.
            let openness: CGFloat = CGFloat(vowel * 0.65 + consonant * 0.3 + 0.05)

            // Width drifts between round "o" and wide "ee" shapes over time.
            let halfW: CGFloat = 10 + CGFloat(shape) * 2.5           // 10 → 12.5
            let h: CGFloat = openness * 6.5 + 1.2                    // 1.2 → ~7.7

            let rect = CGRect(x: cx - halfW, y: cy - h/2, width: halfW * 2, height: h)
            let lipPath = Ellipse().path(in: rect)

            // 1. Dark mouth cavity — the darker interior is what sells the
            //    "open mouth" read. Without it a stroked oval just looks like
            //    a ring, not a mouth.
            let cavity = Color(hue: 0, saturation: 0.0, brightness: 0.08)
            mCtx.fill(lipPath, with: .color(cavity))

            // 2. Outer glow around the lips, matched to current state color.
            var glow = mCtx
            glow.addFilter(.blur(radius: 4))
            glow.opacity = 0.55
            glow.stroke(lipPath, with: .color(eyeBaseColor),
                        style: StrokeStyle(lineWidth: 3.0, lineCap: .round))

            // 3. Crisp white lip outline on top.
            mCtx.stroke(lipPath, with: .color(.white.opacity(0.95)),
                        style: StrokeStyle(lineWidth: 1.8, lineCap: .round))

            // 4. Subtle highlight on the upper lip — catches light like a real lip.
            var highlight = Path()
            highlight.move(to: CGPoint(x: cx - halfW * 0.55, y: cy - h/2 + 0.4))
            highlight.addQuadCurve(
                to: CGPoint(x: cx + halfW * 0.55, y: cy - h/2 + 0.4),
                control: CGPoint(x: cx, y: cy - h/2 - 0.4)
            )
            var highlightCtx = mCtx
            highlightCtx.opacity = 0.55
            highlightCtx.stroke(highlight, with: .color(.white),
                                style: StrokeStyle(lineWidth: 0.9, lineCap: .round))

        case 2: // Warm smile
            let halfW: CGFloat = 13
            let depth: CGFloat = 7
            var p = Path()
            p.move(to: CGPoint(x: cx - halfW, y: cy - 1))
            p.addQuadCurve(to: CGPoint(x: cx + halfW, y: cy - 1),
                           control: CGPoint(x: cx, y: cy + depth))

            var g = mCtx; g.addFilter(.blur(radius: 5)); g.opacity = 0.5
            g.stroke(p, with: .color(eyeBaseColor),
                     style: StrokeStyle(lineWidth: 3.2, lineCap: .round))
            mCtx.stroke(p, with: .color(.white.opacity(0.95)),
                        style: StrokeStyle(lineWidth: 2.2, lineCap: .round))

        case 3: // Frown
            var p = Path()
            p.move(to: CGPoint(x: cx - 10, y: cy + 2))
            p.addQuadCurve(to: CGPoint(x: cx + 10, y: cy + 2), control: CGPoint(x: cx, y: cy - 4))

            var g = mCtx; g.addFilter(.blur(radius: 4)); g.opacity = 0.6
            g.stroke(p, with: .color(eyeBaseColor), style: StrokeStyle(lineWidth: 3, lineCap: .round))
            mCtx.stroke(p, with: .color(.white.opacity(0.9)), style: StrokeStyle(lineWidth: 2, lineCap: .round))

        case 4: // Slow breathing oval (needsApproval — calm waiting)
            let h = 5 + 3 * CGFloat(abs(sin(t * 3)))
            let rect = CGRect(x: cx - 6, y: cy - h/2, width: 12, height: h)
            let p = Ellipse().path(in: rect)

            var g = mCtx; g.addFilter(.blur(radius: 4)); g.opacity = 0.6
            g.fill(p, with: .color(eyeBaseColor))
            mCtx.fill(p, with: .color(.white.opacity(0.9)))

        default: break
        }
    }

    // MARK: - Blush

    private func drawBlush(ctx: inout GraphicsContext, leftCenter: CGPoint, rightCenter: CGPoint, t: Double) {
        let breath = CGFloat(1.0 + 0.06 * sin(t * 1.2))
        for c in [leftCenter, rightCenter] {
            let rw: CGFloat = 4.2 * breath
            let rect = CGRect(x: c.x - rw, y: c.y - rw*0.6, width: rw*2, height: rw*1.2)
            let path = Ellipse().path(in: rect)
            var g = ctx
            g.opacity = blushOpacity
            g.addFilter(.blur(radius: 3.5))
            g.fill(path, with: .color(blushColor))
        }
    }

    // MARK: - Thought bubbles

    private func drawThoughtBubbles(ctx: inout GraphicsContext, cx: CGFloat, cy: CGFloat, t: Double) {
        let dots: [(dx: CGFloat, dy: CGFloat, baseR: CGFloat, phase: Double)] = [
            (-9,  4, 2.2, 0.0),
            ( 2,  0, 3.0, 0.33),
            (13, -2, 3.8, 0.66)
        ]
        for d in dots {
            let pulse = 0.6 + 0.4 * abs(sin(t * 2 + d.phase * .pi * 2))
            let r = d.baseR * CGFloat(pulse)
            let center = CGPoint(x: cx + d.dx, y: cy + d.dy)
            let rect = CGRect(x: center.x - r, y: center.y - r, width: r*2, height: r*2)
            let path = Ellipse().path(in: rect)

            var glow = ctx
            glow.addFilter(.blur(radius: 3.5))
            glow.opacity = thoughtBubbleOpacity * 0.7
            glow.fill(path, with: .color(eyeBaseColor))

            var core = ctx
            core.opacity = thoughtBubbleOpacity
            core.fill(path, with: .color(.white.opacity(0.92)))
        }
    }

    // MARK: - Exclamation (search)

    private func drawExclamation(ctx: inout GraphicsContext, cx: CGFloat, cy: CGFloat, opacity: Double) {
        let warm = Color(hue: 0.12, saturation: 0.85, brightness: 1.0)  // warm amber
        // Stem
        let stemRect = CGRect(x: cx - 1.4, y: cy - 10, width: 2.8, height: 8)
        let stemPath = RoundedRectangle(cornerRadius: 1.4).path(in: stemRect)
        // Dot
        let dotRect = CGRect(x: cx - 1.6, y: cy - 0.5, width: 3.2, height: 3.2)
        let dotPath = Ellipse().path(in: dotRect)

        var glow = ctx
        glow.addFilter(.blur(radius: 3))
        glow.opacity = opacity * 0.8
        glow.fill(stemPath, with: .color(warm))
        glow.fill(dotPath, with: .color(warm))

        var core = ctx
        core.opacity = opacity
        core.fill(stemPath, with: .color(.white))
        core.fill(dotPath, with: .color(.white))
    }

    // MARK: - Eye life helper

    fileprivate struct EyeLife {
        let blinkScaleY: CGFloat
        let breathScale: CGFloat
        let breathPhase: Double
        let verticalBreath: CGFloat

        init(at t: Double, state: CompanionState) {
            let breathSpeed: Double = state == .listening ? 1.3 : 0.8
            let phase = sin(t * breathSpeed)
            self.breathPhase = phase
            self.breathScale = 1.0 + CGFloat(phase) * 0.035
            self.verticalBreath = CGFloat(phase) * 0.6

            let suppressBlink: Bool = {
                switch state {
                case .success, .error, .speaking, .greeting: return true
                default: return false
                }
            }()

            if suppressBlink {
                self.blinkScaleY = 1.0
            } else {
                let cycle: Double = 5.2
                let jitter = (floor(t / cycle).truncatingRemainder(dividingBy: 7.0)) * 0.35
                let phaseT = (t - jitter).truncatingRemainder(dividingBy: cycle)
                if phaseT >= 0 && phaseT < 0.07 {
                    let u = phaseT / 0.07
                    self.blinkScaleY = CGFloat(1.0 - u * 0.95)
                } else if phaseT >= 0.07 && phaseT < 0.18 {
                    let u = (phaseT - 0.07) / 0.11
                    self.blinkScaleY = CGFloat(0.05 + u * 0.95)
                } else {
                    self.blinkScaleY = 1.0
                }
            }
        }
    }
}

```