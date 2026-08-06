"use client";

import HeroMap from "./HeroMap";
import MetricsGrid from "./MetricsGrid";
import LiveActivity from "./LiveActivity";
import MissionQueue from "./MissionQueue";

export default function MissionControl() {
  return (
    <main className="grid h-full grid-cols-12 gap-6 p-6">
      <section className="col-span-8">
        <HeroMap />
      </section>

      <section className="col-span-4 flex flex-col gap-6">
        <MetricsGrid />

        <MissionQueue />

        <LiveActivity />
      </section>
    </main>
  );
}
