"use client";

import PropertySearch from "./PropertySearch";
import PropertyFilters from "./PropertyFilters";
import PropertyMap from "./PropertyMap";
import PropertyPreview from "./PropertyPreview";

export default function PropertyWorkspace() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">
      <div className="mb-8">
        <h2 className="text-4xl font-bold">Property Intelligence</h2>

        <p className="mt-3 text-neutral-400">
          Search, verify and analyse property anywhere in the world.
        </p>
      </div>

      <PropertySearch />

      <div className="mt-8 grid gap-8 xl:grid-cols-4">
        <div>
          <PropertyFilters />
        </div>

        <div className="xl:col-span-2">
          <PropertyMap />
        </div>

        <div>
          <PropertyPreview />
        </div>
      </div>
    </section>
  );
}
