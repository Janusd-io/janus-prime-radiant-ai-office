---
type: source
source_type: laptop
title: Toast
slug: toast
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/Toast.tsx
original_size: 2016
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# Toast

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/Toast.tsx` on 2026-05-14._

```tsx
'use client';

import { useEffect, useState } from 'react';
import { X, AlertCircle, CheckCircle2, Info } from 'lucide-react';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface ToastProps {
  message: string;
  type?: 'error' | 'success' | 'info';
  duration?: number;
  onClose: () => void;
}

export default function Toast({ message, type = 'info', duration = 5000, onClose }: ToastProps) {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
    const timer = setTimeout(() => {
      setIsVisible(false);
      setTimeout(onClose, 300); // Wait for fade-out animation
    }, duration);

    return () => clearTimeout(timer);
  }, [duration, onClose]);

  const icons = {
    error: <AlertCircle className="w-5 h-5 text-red-500" />,
    success: <CheckCircle2 className="w-5 h-5 text-green-500" />,
    info: <Info className="w-5 h-5 text-blue-500" />,
  };

  const styles = {
    error: 'border-red-100 bg-red-50 text-red-900',
    success: 'border-green-100 bg-green-50 text-green-900',
    info: 'border-blue-100 bg-blue-50 text-blue-900',
  };

  return (
    <div className={cn(
      'fixed bottom-8 right-8 z-[100] transition-all duration-300 transform',
      isVisible ? 'translate-y-0 opacity-100' : 'translate-y-4 opacity-0'
    )}>
      <div className={cn(
        'flex items-center gap-3 px-4 py-3 rounded-xl border shadow-lg max-w-md min-w-[320px]',
        styles[type]
      )}>
        <div className="flex-shrink-0">{icons[type]}</div>
        <p className="text-sm font-medium flex-grow">{message}</p>
        <button 
          onClick={() => {
            setIsVisible(false);
            setTimeout(onClose, 300);
          }}
          className="flex-shrink-0 p-1 rounded-lg hover:bg-black/5 transition-colors"
        >
          <X className="w-4 h-4 opacity-50" />
        </button>
      </div>
    </div>
  );
}

```