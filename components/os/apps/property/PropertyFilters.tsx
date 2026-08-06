"use client";

const filters = [
  "Residential",
  "Commercial",
  "Industrial",
  "Land",
  "Verified",
  "Distressed",
  "Mortgage",
  "Investment Grade",
];

export default function PropertyFilters() {
  return (
    <div className="rounded-2xl border border-neutral-800 bg-black p-6">
      <h3 className="text-xl font-semibold">Filters</h3>

      <div className="mt-6 space-y-3">
        {filters.map((filter) => (
          <button
            key={filter}
            className="w-full rounded-xl border border-neutral-800 px-4 py-3 text-left hover:border-emerald-500"
          >
            {filter}
          </button>
        ))}
      </div>
    </div>
  );
}
