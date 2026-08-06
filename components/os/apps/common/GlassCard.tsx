"use client";

export default function GlassCard({
  title,

  children,
}: {
  title: string;

  children: React.ReactNode;
}) {
  return (
    <section className="rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl p-8 shadow-2xl">
      <h2 className="mb-8 text-2xl font-semibold">{title}</h2>

      {children}
    </section>
  );
}
