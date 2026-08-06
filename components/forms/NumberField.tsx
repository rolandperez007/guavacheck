"use client";

interface NumberFieldProps {
  label: string;
  value: number;
  min?: number;
  max?: number;

  onChange: (value: number) => void;
}

export default function NumberField({ label, value, min = 0, max, onChange }: NumberFieldProps) {
  return (
    <div className="space-y-2">
      <label className="font-medium">{label}</label>

      <input
        type="number"
        value={value}
        min={min}
        max={max}
        onChange={(e) => onChange(Number(e.target.value))}
        className="w-full rounded-xl border border-gray-300 p-3 transition focus:border-green-600 focus:outline-none focus:ring-2 focus:ring-green-200"
      />
    </div>
  );
}
