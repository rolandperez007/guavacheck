"use client";

export default function PropertySearch() {
  return (
    <div className="flex gap-4">
      <input
        placeholder="Search address, title number, owner, coordinates..."
        className="flex-1 rounded-xl border border-neutral-700 bg-black px-5 py-4 outline-none"
      />

      <button className="rounded-xl bg-emerald-500 px-8 font-semibold text-black">Search</button>
    </div>
  );
}
