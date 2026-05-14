---
type: source
source_type: laptop
title: tailwind.config
slug: tailwind-config-3
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/tailwind.config.js
original_size: 2677
original_ext: .js
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# tailwind.config

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/tailwind.config.js` on 2026-05-14._

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        psi: {
          blue: {
            DEFAULT: '#2C2D65',
            50: '#EAEAFA',
            100: '#D5D5F5',
            200: '#ABACEB',
            300: '#8182E0',
            400: '#5759D6',
            500: '#2C2D65', // Primary Dark Blue
            600: '#232451',
            700: '#1A1B3D',
            800: '#121229',
            900: '#090914',
          },
          orange: {
            DEFAULT: '#E0592A',
            50: '#FCECE8',
            100: '#F9D9D1',
            200: '#F3B3A3',
            300: '#ED8D75',
            400: '#E66747',
            500: '#E0592A', // Primary Orange
            600: '#B34722',
            700: '#863519',
            800: '#5A2411',
            900: '#2D1208',
          },
        },
        janus: {
          blue: {
            DEFAULT: '#2C2D65',
            50: '#EAEAFA',
            100: '#D5D5F5',
            200: '#ABACEB',
            300: '#8182E0',
            400: '#5759D6',
            500: '#2C2D65',
            600: '#232451',
            700: '#1A1B3D',
            800: '#121229',
            900: '#090914',
          },
          orange: {
            DEFAULT: '#E0592A',
            50: '#FCECE8',
            100: '#F9D9D1',
            200: '#F3B3A3',
            300: '#ED8D75',
            400: '#E66747',
            500: '#E0592A',
            600: '#B34722',
            700: '#863519',
            800: '#5A2411',
            900: '#2D1208',
          },
        },
      },
      fontFamily: {
        sans: ['Alexandria', 'system-ui', 'sans-serif'],
      },
      container: {
        center: true,
        padding: '1rem',
        screens: {
          lg: '1024px',
          xl: '1024px', // Limit max width for form readability
        },
      },
      animation: {
        'fade-in': 'fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1)',
        'slide-up': 'slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1)',
        'pulse-slow': 'pulseSlow 8s infinite ease-in-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        pulseSlow: {
          '0%, 100%': { opacity: '0.4', transform: 'scale(1)' },
          '50%': { opacity: '0.6', transform: 'scale(1.1)' },
        },
      },
    },
  },
  plugins: [],
}

```