"use client";

interface ProgressBarProps {
  percentage: number;
}

export default function ProgressBar({ percentage }: ProgressBarProps) {
  const value = Math.max(0, Math.min(100, percentage));

  return (
    <div className="w-full">
      <div className="mb-2 flex items-center justify-between">
        <span className="text-sm font-medium text-gray-600">Progress</span>

        <span className="text-sm font-semibold text-green-600">{value}%</span>
      </div>

      <div className="h-3 w-full overflow-hidden rounded-full bg-gray-200">
        <div
          className="h-full rounded-full bg-green-600 transition-all duration-500"
          style={{
            width: `${value}%`,
          }}
        />
      </div>
    </div>
  );
}
