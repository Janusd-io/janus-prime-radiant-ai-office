---
type: source
source_type: laptop
title: App
slug: app-2
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/App.jsx
original_size: 1802
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# App

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/App.jsx` on 2026-05-14._

```jsx
import React from 'react';
import { Header } from './components/layout/Header';
import { Footer } from './components/layout/Footer';
import { Container } from './components/layout/Container';
import { RequestForm } from './components/form/RequestForm';

function App() {
  return (
    <div className="min-h-screen bg-slate-50 flex flex-col font-sans text-psi-blue-900 overflow-x-hidden selection:bg-psi-orange-100 selection:text-psi-orange-900">
      <Header />

      <main className="flex-grow relative">
        {/* Modern animated gradient background */}
        <div className="fixed inset-0 z-0 pointer-events-none overflow-hidden">
          <div className="absolute top-[-20%] left-[-10%] w-[60vw] h-[60vw] bg-janus-blue-100/40 rounded-full blur-[100px] animate-pulse-slow"></div>
          <div className="absolute bottom-[-20%] right-[-10%] w-[50vw] h-[50vw] bg-janus-orange-100/30 rounded-full blur-[100px] animate-pulse-slow delay-1000"></div>
          <div className="absolute top-[40%] left-[30%] w-[30vh] h-[30vh] bg-indigo-50/50 rounded-full blur-[80px] animate-pulse-slow delay-2000"></div>
        </div>

        <Container className="relative z-10 py-12">
          <div className="mb-12 text-center max-w-2xl mx-auto">
            <h2 className="text-4xl sm:text-5xl font-extrabold tracking-tight text-janus-blue-900 mb-6 drop-shadow-sm">
              HR Request Portal.
            </h2>
            <p className="text-lg text-slate-500 leading-relaxed font-light">
              Submit your HR information quickly and easily. Fields marked with <span className="text-janus-orange-500 font-semibold">*</span> are required.
            </p>
          </div>

          <RequestForm />
        </Container>
      </main>

      <Footer />
    </div>
  );
}

export default App;

```