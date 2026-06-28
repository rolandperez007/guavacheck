"use client";

interface Option {
  label: string;
  value: string;
}

interface SelectFieldProps {
  label: string;
  value: string;

  options: Option[];

  onChange: (value: string) => void;
}

export default function SelectField({
  label,
  value,
  options,
  onChange,
}: SelectFieldProps) {
  return (
    <div className="space-y-2">

      <label className="font-medium">
        {label}
      </label>

      <select
        value={value}
        onChange={(e) =>
          onChange(e.target.value)
        }
        className="w-full rounded-xl border border-gray-300 p-3 transition focus:border-green-600 focus:outline-none focus:ring-2 focus:ring-green-200"
      >
        <option value="">
          Select...
        </option>

        {options.map((option) => (
          <option
            key={option.value}
            value={option.value}
          >
            {option.label}
          </option>
        ))}

      </select>

    </div>
  );
}