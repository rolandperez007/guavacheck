"use client";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-neutral-950 text-white">
      <Sidebar />

      <div className="flex flex-1 flex-col">
        <Topbar />

        <div className="flex-1 p-8 overflow-y-auto">{children}</div>
      </div>
    </div>
  );
}
