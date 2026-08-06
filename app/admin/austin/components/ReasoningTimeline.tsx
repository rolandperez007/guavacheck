"use client";

import SectionTitle from "../widgets/SectionTitle";

const reasoningSteps = [
  {
    title: "Input Received",
    description: "Austin received and classified user request.",
  },

  {
    title: "Context Analysis",
    description: "Global context and intelligence layers activated.",
  },

  {
    title: "Engine Routing",
    description: "Relevant AI engines selected for execution.",
  },

  {
    title: "Response Generation",
    description: "Final intelligence response prepared.",
  },
];

export default function ReasoningTimeline() {
  return (
    <section>
      <SectionTitle title="Reasoning Timeline" subtitle="Austin cognitive execution flow" />

      <div className="space-y-4">
        {reasoningSteps.map((step, index) => (
          <div
            key={index}
            className="
              rounded-xl
              border
              bg-white
              p-5
              shadow-sm
            "
          >
            <div className="font-semibold">
              {index + 1}. {step.title}
            </div>

            <p className="mt-2 text-sm text-gray-500">{step.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
