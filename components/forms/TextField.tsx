"use client";

interface TextFieldProps {
  label: string;
  value: string;
  placeholder?: string;
  required?: boolean;

  onChange: (value: string) => void;
}

export default function TextField({
  label,
  value,
  placeholder,
  required = false,
  onChange,
}: TextFieldProps) {
  return (
    <div className="space-y-2">
      <label className="font-medium">
        {label}

        {required && <span className="ml-1 text-red-500">*</span>}
      </label>

      <input
        type="text"
        value={value}
        placeholder={placeholder}
        onChange={(e) => onChange(e.target.value)}
        className="w-full rounded-xl border border-gray-300 p-3 transition focus:border-green-600 focus:outline-none focus:ring-2 focus:ring-green-200"
      />
    </div>
  );
}
