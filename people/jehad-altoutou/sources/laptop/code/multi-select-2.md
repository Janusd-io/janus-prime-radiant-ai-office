---
type: source
source_type: laptop
title: multi-select
slug: multi-select-2
created: 2026-02-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request copy/src/components/ui/multi-select.jsx
original_size: 5211
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# multi-select

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request copy/src/components/ui/multi-select.jsx` on 2026-05-14._

```jsx
import React, { useState, useRef, useEffect } from 'react';
import { cn } from '../../lib/utils';
import { ChevronDown, X, Check } from 'lucide-react';

export const MultiSelect = ({ options = [], value = [], onChange, placeholder, error, className }) => {
    const [isOpen, setIsOpen] = useState(false);
    const containerRef = useRef(null);

    // Close when clicking outside
    useEffect(() => {
        const handleClickOutside = (event) => {
            if (containerRef.current && !containerRef.current.contains(event.target)) {
                setIsOpen(false);
            }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    const handleSelect = (optionValue) => {
        if (value.includes(optionValue)) {
            onChange(value.filter((v) => v !== optionValue));
        } else {
            onChange([...value, optionValue]);
        }
    };

    const removeValue = (e, val) => {
        e.stopPropagation();
        onChange(value.filter((v) => v !== val));
    };

    return (
        <div className="relative group" ref={containerRef}>
            <div
                className={cn(
                    'flex min-h-[48px] w-full rounded-xl border border-transparent bg-white/60 px-3 py-2 text-sm shadow-sm ring-1 ring-gray-200/50 backdrop-blur-sm transition-all duration-300 cursor-pointer',
                    'hover:bg-white/80 hover:ring-gray-300',
                    isOpen && 'ring-2 ring-psi-orange-500/50 bg-white shadow-md',
                    error && 'ring-red-500 bg-red-50/10',
                    className
                )}
                onClick={() => setIsOpen(!isOpen)}
            >
                <div className="flex flex-wrap gap-1.5 flex-1 items-center">
                    {value.length === 0 && (
                        <span className="text-gray-400 px-1">{placeholder || 'Select options...'}</span>
                    )}
                    {value.map((val) => (
                        <span
                            key={val}
                            className="inline-flex items-center rounded-md bg-psi-blue-50 px-2 py-1 text-xs font-medium text-psi-blue-700 ring-1 ring-inset ring-psi-blue-700/10 animate-fade-in"
                        >
                            {val}
                            <button
                                type="button"
                                className="ml-1 inline-flex h-3 w-3 flex-shrink-0 items-center justify-center rounded-full text-psi-blue-400 hover:bg-psi-blue-200 hover:text-psi-blue-600 focus:outline-none"
                                onClick={(e) => removeValue(e, val)}
                            >
                                <X className="h-2.5 w-2.5" />
                            </button>
                        </span>
                    ))}
                </div>
                <div className="flex items-center pl-2">
                    <ChevronDown className={cn("h-5 w-5 text-gray-400 transition-transform duration-200", isOpen && "rotate-180")} />
                </div>
            </div>

            {/* Dropdown Menu */}
            {isOpen && (
                <div className="absolute z-50 mt-2 max-h-60 w-full overflow-auto rounded-xl bg-white/90 backdrop-blur-xl py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm animate-fade-in custom-scrollbar border border-white/50">
                    {options.map((option) => {
                        const isSelected = value.includes(option.value || option);
                        const label = option.label || option;
                        const val = option.value || option;

                        return (
                            <div
                                key={val}
                                className={cn(
                                    'relative cursor-pointer select-none py-2.5 pl-10 pr-4 transition-colors',
                                    isSelected ? 'bg-psi-blue-50 text-psi-blue-900' : 'text-gray-900 hover:bg-gray-50'
                                )}
                                onClick={() => handleSelect(val)}
                            >
                                <>
                                    <span className={cn('block truncate', isSelected ? 'font-medium' : 'font-normal')}>
                                        {label}
                                    </span>
                                    {isSelected ? (
                                        <span className="absolute inset-y-0 left-0 flex items-center pl-3 text-psi-orange-600">
                                            <Check className="h-4 w-4" aria-hidden="true" />
                                        </span>
                                    ) : null}
                                </>
                            </div>
                        );
                    })}
                </div>
            )}

            {error && (
                <span className="text-xs text-red-500 mt-1.5 block font-medium animate-fade-in">{error}</span>
            )}
        </div>
    );
};

```