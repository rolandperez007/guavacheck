"use client";

export default function MissionControl() {
  return (
    <section className="rounded-3xl border border-neutral-800 bg-gradient-to-br from-neutral-950 via-black to-neutral-900 p-8">
      <div className="flex items-center justify-between">
        <div>
          <div className="text-sm uppercase tracking-[0.35em] text-emerald-400">
            Mission Control
          </div>

          <h2 className="mt-3 text-4xl font-bold">Austin Command Center</h2>
        </div>

        <div className="rounded-full bg-emerald-500/20 px-5 py-2 text-emerald-400">● Online</div>
      </div>

      <div className="mt-10 grid gap-6 md:grid-cols-4">
        <div className="rounded-2xl bg-neutral-900 p-6">
          <div className="text-neutral-400">AI Requests</div>
          <div className="mt-2 text-4xl font-bold">0</div>
        </div>

        <div className="rounded-2xl bg-neutral-900 p-6">
          <div className="text-neutral-400">Properties</div>
          <div className="mt-2 text-4xl font-bold">0</div>
        </div>

        <div className="rounded-2xl bg-neutral-900 p-6">
          <div className="text-neutral-400">Verifications</div>
          <div className="mt-2 text-4xl font-bold">0</div>
        </div>

        <div className="rounded-2xl bg-neutral-900 p-6">
          <div className="text-neutral-400">Opportunities</div>
          <div className="mt-2 text-4xl font-bold">0</div>
        </div>
      </div>
    </section>
  );
}
