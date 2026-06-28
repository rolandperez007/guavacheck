"use client";

interface TextAreaFieldProps {
  label: string;
  value: string;
  rows?: number;

  placeholder?: string;

  onChange: (value: string) => void;
}

export default function TextAreaField({
  label,
  value,
  rows = 5,
  placeholder,
  onChange,
}: TextAreaFieldProps) {
  return (
    <div className="space-y-2">

      <label className="font-medium">
        {label}
      </label>

      <textarea
        rows={rows}
        value={value}
        placeholder={placeholder}
        onChange={(e) =>
          onChange(e.target.value)
        }
        className="w-full rounded-xl border border-gray-300 p-3 transition focus:border-green-600 focus:outline-none focus:ring-2 focus:ring-green-200"
      />

    </div>
  );
}