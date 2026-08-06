"use client";

import { useRef } from "react";

export interface FileUploadProps {
  label: string;

  accept?: string;

  multiple?: boolean;

  files?: File[];

  helperText?: string;

  disabled?: boolean;

  onChange: (files: File[]) => void;
}

export default function FileUpload({
  label,
  accept = "*/*",
  multiple = true,
  files = [],
  helperText,
  disabled = false,
  onChange,
}: FileUploadProps) {
  const inputRef = useRef<HTMLInputElement>(null);

  function openPicker() {
    if (!disabled) {
      inputRef.current?.click();
    }
  }

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    const selectedFiles = event.target.files;

    if (!selectedFiles) return;

    onChange(Array.from(selectedFiles));

    // Allow selecting the same file again
    event.target.value = "";
  }

  return (
    <div className="space-y-3">
      <label className="block text-sm font-semibold text-gray-700">{label}</label>

      <div
        onClick={openPicker}
        className={`rounded-2xl border-2 border-dashed p-8 text-center transition ${
          disabled
            ? "cursor-not-allowed border-gray-200 bg-gray-100 opacity-60"
            : "cursor-pointer border-gray-300 bg-gray-50 hover:border-green-500 hover:bg-green-50"
        }`}
      >
        <div className="mb-4 text-5xl">📂</div>

        <h3 className="text-lg font-semibold">Upload Files</h3>

        <p className="mt-2 text-sm text-gray-500">Click here to browse your device</p>

        {helperText && <p className="mt-3 text-xs text-gray-400">{helperText}</p>}
      </div>

      <input
        ref={inputRef}
        type="file"
        hidden
        accept={accept}
        multiple={multiple}
        disabled={disabled}
        onChange={handleChange}
      />

      {files.length > 0 && (
        <div className="space-y-2">
          <p className="text-sm font-semibold text-gray-700">Selected Files ({files.length})</p>

          {files.map((file, index) => (
            <div
              key={`${file.name}-${index}`}
              className="flex items-center justify-between rounded-xl border border-gray-200 bg-white p-3"
            >
              <div>
                <p className="font-medium">{file.name}</p>

                <p className="text-xs text-gray-500">{(file.size / 1024 / 1024).toFixed(2)} MB</p>
              </div>

              <span className="rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700">
                Ready
              </span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
