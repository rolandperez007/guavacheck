"use client";

import {
  Home,
  Building2,
  ShieldCheck,
  LineChart,
  Hammer,
  FileText,
  Users,
  Brain,
  Globe,
  Settings,
} from "lucide-react";

const apps = [
  { icon: Home, label: "Mission" },

  { icon: Building2, label: "Properties" },

  { icon: ShieldCheck, label: "Verification" },

  { icon: Hammer, label: "Construction" },

  { icon: LineChart, label: "Investor" },

  { icon: FileText, label: "Documents" },

  { icon: Users, label: "Community" },

  { icon: Brain, label: "Austin" },

  { icon: Globe, label: "World" },

  { icon: Settings, label: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="flex w-20 flex-col items-center border-r border-white/10 bg-black/30 py-6 backdrop-blur-xl">
      <div className="mb-10">
        <div className="h-12 w-12 rounded-2xl bg-emerald-500" />
      </div>

      <div className="flex flex-col gap-4">
        {apps.map(({ icon: Icon, label }) => (
          <button
            key={label}

            className="group flex h-12 w-12 items-center justify-center rounded-xl transition hover:bg-white/10"

            title={label}
          >
            <Icon className="h-5 w-5 text-neutral-400 group-hover:text-white" />
          </button>
        ))}
      </div>
    </aside>
  );
}
