"use client";

import Link from "next/link";

const navigation = [
  "Dashboard",
  "Properties",
  "Verification",
  "Construction",
  "Portfolio",
  "Finance",
  "Marketplace",
  "Knowledge",
  "Austin AI",
  "Community",
  "Analytics",
  "Settings",
];

export default function Sidebar() {
  return (
    <aside className="w-80 border-r border-neutral-800 bg-black">
      <div className="border-b border-neutral-800 p-8">
        <h1 className="text-3xl font-bold">guavacheck</h1>

        <p className="mt-2 text-neutral-500">Global Property Intelligence</p>
      </div>

      <nav className="space-y-2 p-5">
        {navigation.map((item) => (
          <Link
            key={item}

            href="#"

            className="block rounded-xl px-5 py-4 text-neutral-300 transition hover:bg-neutral-900 hover:text-white"
          >
            {item}
          </Link>
        ))}
      </nav>

      <div className="m-5 rounded-2xl bg-neutral-900 p-6">
        <div className="text-sm text-neutral-500">Austin Status</div>

        <div className="mt-3 flex items-center gap-3">
          <div className="h-3 w-3 rounded-full bg-emerald-400 animate-pulse" />

          <span>Online</span>
        </div>
      </div>
    </aside>
  );
}
