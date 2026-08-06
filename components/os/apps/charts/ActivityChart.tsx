"use client";

export default function ActivityChart() {
  const values = [45, 52, 60, 72, 65, 84, 90];

  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">
      <h2 className="text-3xl font-semibold">Platform Activity</h2>

      <div className="mt-10 flex h-72 items-end gap-4">
        {values.map((value, index) => (
          <div
            key={index}

            style={{
              height: `${value}%`,
            }}

            className="flex-1 rounded-t-xl bg-sky-500"
          ></div>
        ))}
      </div>
    </section>
  );
}
