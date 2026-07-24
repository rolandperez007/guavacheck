"use client";

const feed = [
  "Austin initialized successfully.",
  "Knowledge engine synchronized.",
  "Market feeds connected.",
  "No pending verifications.",
  "Portfolio monitoring started.",
  "AI waiting for instructions."
];

export default function ActivityFeed() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

      <h2 className="text-3xl font-semibold">
        Live Activity
      </h2>

      <div className="mt-8 space-y-4">

        {feed.map((item, index) => (

          <div
            key={index}
            className="flex items-center gap-4 rounded-xl border border-neutral-800 p-4"
          >

            <div className="h-3 w-3 rounded-full bg-emerald-400" />

            <span>{item}</span>

          </div>

        ))}

      </div>

    </section>
  );
}