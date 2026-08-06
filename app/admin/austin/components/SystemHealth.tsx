"use client";

import { useSystemHealth } from "../hooks/useSystemHealth";
import StatusBadge from "../widgets/StatusBadge";
import SectionTitle from "../widgets/SectionTitle";

export default function SystemHealth() {
  const { health, loading } = useSystemHealth();

  if (loading && !health) {
    return <div className="rounded-xl border p-5">Checking system health...</div>;
  }

  if (!health) {
    return <div className="rounded-xl border p-5">No health data available.</div>;
  }

  const services = [health.fastapi, health.redis, health.postgres, health.websocket];

  return (
    <section>
      <SectionTitle title="System Health" subtitle="Core Austin infrastructure monitoring" />

      <div className="grid gap-4 md:grid-cols-2">
        {services.map((service) => (
          <div key={service.name} className="rounded-xl border bg-white p-5 shadow-sm">
            <div className="flex items-center justify-between">
              <h3 className="font-semibold">{service.name}</h3>

              <StatusBadge status={service.status} />
            </div>

            {service.latency && (
              <p className="mt-3 text-sm text-gray-500">Latency: {service.latency}ms</p>
            )}
          </div>
        ))}
      </div>
    </section>
  );
}
