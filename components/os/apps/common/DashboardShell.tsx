"use client";

export default function DashboardShell({ children }: { children: React.ReactNode }) {
  return (
    <main className="min-h-screen bg-neutral-950">
      <div className="mx-auto max-w-[1800px] px-8 py-8">{children}</div>
    </main>
  );
}
