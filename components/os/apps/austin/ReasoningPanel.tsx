"use client";

const tasks = [
  "Scanning market data...",
  "Checking ownership records...",
  "Comparing historical prices...",
  "Evaluating ROI...",
  "Computing confidence score..."
];

export default function ReasoningPanel() {
  return (
    <section className="border-b border-neutral-800 p-6">

      <h3 className="text-xl font-semibold">
        Austin Thinking
      </h3>

      <div className="mt-6 space-y-4">

        {tasks.map((task) => (

          <div
            key={task}
            className="flex items-center gap-3 rounded-xl bg-neutral-900 p-4"
          >

            <div className="h-3 w-3 rounded-full bg-emerald-400 animate-pulse" />

            {task}

          </div>

        ))}

      </div>

    </section>
  );
}