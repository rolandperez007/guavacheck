"use client";

import { useLiveMetrics } from "../hooks/useLiveMetrics";
import MetricCard from "../widgets/MetricCard";
import SectionTitle from "../widgets/SectionTitle";

export default function JobQueue() {
  const { metrics, loading } = useLiveMetrics();

  const queue = metrics?.queue;

  if (loading && !queue) {
    return <div>Loading queue statistics...</div>;
  }

  return (
    <section>
      <SectionTitle title="Job Queue" subtitle="Background workers and processing pipeline" />

      <div className="grid gap-4 md:grid-cols-4">
        <MetricCard title="Pending" value={queue?.pending ?? 0} />

        <MetricCard title="Processing" value={queue?.processing ?? 0} />

        <MetricCard title="Completed" value={queue?.completed ?? 0} />

        <MetricCard title="Failed" value={queue?.failed ?? 0} status="danger" />
      </div>

      {queue?.workers !== undefined && (
        <div className="mt-4 rounded-xl border bg-white p-4">
          Active Workers:
          <strong className="ml-2">{queue.workers}</strong>
        </div>
      )}
    </section>
  );
}
