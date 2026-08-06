"use client";

interface CheckboxFieldProps {
  label: string;
  checked: boolean;

  onChange: (checked: boolean) => void;
}

export default function CheckboxField({ label, checked, onChange }: CheckboxFieldProps) {
  return (
    <label className="flex items-center gap-3">
      <input type="checkbox" checked={checked} onChange={(e) => onChange(e.target.checked)} />

      <span>{label}</span>
    </label>
  );
}
