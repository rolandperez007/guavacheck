"use client";

interface NavigationButtonsProps {
  currentIndex: number;
  totalSteps: number;

  onPrevious: () => void;
  onNext: () => void;
}

export default function NavigationButtons({
  currentIndex,
  totalSteps,
  onPrevious,
  onNext,
}: NavigationButtonsProps) {
  const isFirst = currentIndex === 0;
  const isLast = currentIndex === totalSteps - 1;

  return (
    <div className="flex items-center justify-between">
      <button
        type="button"
        onClick={onPrevious}
        disabled={isFirst}
        className="rounded-lg border border-gray-300 px-5 py-2 font-medium transition hover:bg-gray-100 disabled:cursor-not-allowed disabled:opacity-50"
      >
        Previous
      </button>

      <div className="text-sm text-gray-500">
        Step {currentIndex + 1} of {totalSteps}
      </div>

      <button
        type="button"
        onClick={onNext}
        className="rounded-lg bg-green-600 px-6 py-2 font-semibold text-white transition hover:bg-green-700"
      >
        {isLast ? "Finish" : "Next"}
      </button>
    </div>
  );
}
