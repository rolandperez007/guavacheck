"use client";

const actions = [
  "Verify Ownership",
  "Generate Valuation",
  "Estimate Construction Cost",
  "Create Investment Report",
  "Compare Similar Properties",
  "Export PDF"
];

export default function SuggestedActions() {
  return (
    <section className="p-6">

      <h3 className="text-xl font-semibold">
        Suggested Actions
      </h3>

      <div className="mt-6 space-y-3">

        {actions.map((action) => (

          <button
            key={action}
            className="w-full rounded-xl border border-neutral-800 p-4 text-left hover:border-emerald-500 hover:bg-neutral-900 transition"
          >

            {action}

          </button>

        ))}

      </div>

    </section>
  );
}