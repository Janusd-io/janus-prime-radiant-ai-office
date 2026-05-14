---
type: source
source_type: laptop
title: FileUpload
slug: fileupload
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/components/form/FileUpload.jsx
original_size: 5536
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# FileUpload

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/components/form/FileUpload.jsx` on 2026-05-14._

```jsx
import React, { useRef, useState } from 'react';
import { cn } from '../../lib/utils';
import { UploadCloud, X, File as FileIcon } from 'lucide-react';

export const FileUpload = ({ label, onChange, error, value, multiple = false, required }) => {
    const inputRef = useRef(null);
    const [dragActive, setDragActive] = useState(false);

    const handleDrag = (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (e.type === 'dragenter' || e.type === 'dragover') {
            setDragActive(true);
        } else if (e.type === 'dragleave') {
            setDragActive(false);
        }
    };

    const handleDrop = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setDragActive(false);
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            handleFiles(e.dataTransfer.files);
        }
    };

    const handleChange = (e) => {
        e.preventDefault();
        if (e.target.files && e.target.files[0]) {
            handleFiles(e.target.files);
        }
    };

    const handleFiles = (files) => {
        const fileArray = Array.from(files);
        
        const validFiles = fileArray.filter(file => {
            if (file.size > 1024 * 1024) {
                alert(`File size exceeds 1MB limit for: ${file.name}`);
                return false;
            }
            if (file.type !== 'image/jpeg' && file.type !== 'image/jpg') {
                alert(`Only JPEG format is allowed. Invalid file: ${file.name}`);
                return false;
            }
            return true;
        });

        if (validFiles.length === 0) return;

        if (multiple) {
            const currentFiles = value ? (Array.isArray(value) ? value : [value]) : [];
            onChange([...currentFiles, ...validFiles]);
        } else {
            onChange(validFiles[0]);
        }
    };

    const removeFile = (index) => {
        if (multiple) {
            const newFiles = [...value];
            newFiles.splice(index, 1);
            onChange(newFiles.length > 0 ? newFiles : null);
        } else {
            onChange(null);
            if (inputRef.current) inputRef.current.value = '';
        }
    };

    const displayFiles = multiple ? (Array.isArray(value) ? value : []) : (value ? [value] : []);

    return (
        <div className="w-full">
            {label && (
                <label className="block text-sm font-medium text-janus-blue-900 mb-2">
                    {label} {required && <span className="text-janus-orange-500">*</span>}
                </label>
            )}

            <div
                className={cn(
                    'relative flex flex-col items-center justify-center w-full min-h-[120px] rounded-lg border-2 border-dashed transition-colors',
                    dragActive ? 'border-janus-orange-500 bg-janus-orange-50' : 'border-gray-300 bg-gray-50',
                    error ? 'border-red-500' : 'hover:bg-gray-100',
                )}
                onDragEnter={handleDrag}
                onDragLeave={handleDrag}
                onDragOver={handleDrag}
                onDrop={handleDrop}
            >
                <div className="flex flex-col items-center justify-center pt-5 pb-6 text-center px-4">
                    <UploadCloud className="w-8 h-8 text-gray-400 mb-2" />
                    <p className="mb-2 text-sm text-gray-500">
                        <span className="font-semibold text-janus-orange-500">Click to upload</span> or drag and drop
                    </p>
                    <p className="text-xs text-gray-400">JPEG format only (max 1MB per file)</p>
                </div>
                <input
                    ref={inputRef}
                    type="file"
                    className="hidden"
                    accept="image/jpeg,image/jpg"
                    multiple={multiple}
                    onChange={handleChange}
                />
                <div
                    className="absolute inset-0 cursor-pointer"
                    onClick={() => inputRef.current?.click()}
                />
            </div>

            {/* File List */}
            {displayFiles.length > 0 && (
                <ul className="mt-3 space-y-2">
                    {displayFiles.map((file, index) => (
                        <li key={index} className="flex items-center justify-between p-3 bg-white border border-gray-200 rounded-lg shadow-sm">
                            <div className="flex items-center overflow-hidden">
                                <FileIcon className="w-5 h-5 text-janus-blue-500 mr-2 flex-shrink-0" />
                                <span className="text-sm text-gray-700 truncate max-w-[200px] sm:max-w-xs">{file.name}</span>
                                <span className="text-xs text-gray-400 ml-2 flex-shrink-0">({(file.size / 1024 / 1024).toFixed(2)} MB)</span>
                            </div>
                            <button
                                type="button"
                                onClick={() => removeFile(index)}
                                className="text-gray-400 hover:text-red-500 transition-colors"
                            >
                                <X className="w-5 h-5" />
                            </button>
                        </li>
                    ))}
                </ul>
            )}

            {error && (
                <span className="text-xs text-red-500 mt-1 block">{error}</span>
            )}
        </div>
    );
};

```