"use client";

import Image from "next/image";
import Link from "next/link";
import { useState } from "react";

const navItems = [
  { label: "AI Architect", href: "/ai/architect" },
  { label: "Marketplace", href: "/marketplace" },
  { label: "Investor", href: "/investor" },
  { label: "Dashboard", href: "/dashboard" },
];

export default function Navigation() {
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 w-full border-b border-white/10 bg-slate-950/70 backdrop-blur-xl">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-3 transition hover:opacity-90">
          <Image src="/images/guava-logo.png" alt="GuavaCheck" width={46} height={46} priority />

          <div>
            <div className="text-lg font-bold tracking-wide text-white">GUAVACHECK</div>

            <div className="text-xs tracking-[0.3em] text-emerald-400 uppercase">
              Austin Intelligence
            </div>
          </div>
        </Link>

        {/* Desktop Navigation */}
        <nav className="hidden items-center gap-8 lg:flex">
          {navItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="text-sm font-medium text-slate-300 transition hover:text-emerald-400"
            >
              {item.label}
            </Link>
          ))}
        </nav>

        {/* Status + CTA */}
        <div className="hidden items-center gap-4 lg:flex">
          <div className="flex items-center gap-2 rounded-full border border-emerald-500/30 bg-emerald-500/10 px-4 py-2">
            <span className="h-2.5 w-2.5 rounded-full bg-emerald-400 animate-pulse" />
            <span className="text-xs font-medium text-emerald-300">Austin Online</span>
          </div>

          <Link
            href="/dashboard"
            className="rounded-xl bg-emerald-500 px-5 py-2.5 text-sm font-semibold text-slate-950 transition hover:bg-emerald-400"
          >
            Launch Platform
          </Link>
        </div>

        {/* Mobile Button */}
        <button
          onClick={() => setMobileOpen(!mobileOpen)}
          className="rounded-lg border border-white/10 p-2 text-white lg:hidden"
          aria-label="Toggle navigation"
        >
          ☰
        </button>
      </div>

      {/* Mobile Menu */}
      {mobileOpen && (
        <div className="border-t border-white/10 bg-slate-950 lg:hidden">
          <nav className="flex flex-col p-5">
            {navItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                onClick={() => setMobileOpen(false)}
                className="rounded-lg px-3 py-3 text-slate-300 transition hover:bg-white/5 hover:text-emerald-400"
              >
                {item.label}
              </Link>
            ))}

            <Link
              href="/dashboard"
              className="mt-4 rounded-xl bg-emerald-500 px-4 py-3 text-center font-semibold text-slate-950"
            >
              Launch Platform
            </Link>
          </nav>
        </div>
      )}
    </header>
  );
}
