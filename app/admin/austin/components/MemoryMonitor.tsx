"use client";

import { useLiveMetrics } from "../hooks/useLiveMetrics";
import MetricCard from "../widgets/MetricCard";
import SectionTitle from "../widgets/SectionTitle";

export default function MemoryMonitor() {
  const { metrics, loading } = useLiveMetrics();

  const memory = metrics?.memoryStats;

  if (loading && !memory) {
    return <div>Loading memory statistics...</div>;
  }

  return (
    <section>
      <SectionTitle title="Memory Monitor" subtitle="Austin cache and memory intelligence" />

      <div className="grid gap-4 md:grid-cols-3">
        <MetricCard title="Total Memory" value={memory?.total ?? 0} />

        <MetricCard title="Used Memory" value={memory?.used ?? 0} />

        <MetricCard title="Cache Size" value={memory?.cacheSize ?? 0} />
      </div>
    </section>
  );
}
