"use client";

export function AustinTimeline({ events }: any) {
  if (!events?.length) return null;

  const labelMap: any = {
    intent: "Understanding request",
    planning: "Designing execution plan",
    execution: "Running intelligence engine",
    step: "Processing step",
    step_complete: "Completed step",
    complete: "Finalizing result"
  };

  return (
    <div className="bg-white border rounded-xl p-4 shadow-sm space-y-2">

      <div className="text-sm font-semibold text-gray-800">
        Austin Processing
      </div>

      <div className="space-y-1 text-sm text-gray-600">
        {events.map((e: any, i: number) => (
          <div key={i} className="flex items-center gap-2">

            {/* dot indicator */}
            <div className="w-2 h-2 rounded-full bg-black animate-pulse" />

            <span className="font-medium text-gray-800">
              {labelMap[e.stage] || e.stage}
            </span>

            {e.step && (
              <span className="text-gray-500">
                → {e.step}
              </span>
            )}

          </div>
        ))}
      </div>
    </div>
  );
}


