"use client";

import Link from "next/link";

const navigation = [
  {
    name: "Vision",
    href: "#vision",
  },
  {
    name: "Platform",
    href: "#platform",
  },
  {
    name: "Austin",
    href: "#austin",
  },
  {
    name: "Early Access",
    href: "#early-access",
  },
];

export default function Navigation() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6 lg:px-10">

        {/* Logo */}
        <Link
          href="/"
          className="text-2xl font-semibold tracking-tight text-white transition hover:text-[#72BF44]"
        >
          guavacheck
        </Link>

        {/* Desktop Navigation */}
        <nav className="hidden items-center gap-10 md:flex">
          {navigation.map((item) => (
            <a
              key={item.name}
              href={item.href}
              className="text-sm font-medium text-white/80 transition duration-300 hover:text-white"
            >
              {item.name}
            </a>
          ))}
        </nav>

        {/* CTA */}
        <a
          href="#early-access"
          className="hidden rounded-full border border-[#72BF44]/40 bg-[#72BF44]/15 px-5 py-2 text-sm font-semibold text-[#72BF44] backdrop-blur-xl transition-all duration-300 hover:border-[#72BF44] hover:bg-[#72BF44] hover:text-white hover:shadow-[0_0_25px_rgba(114,191,68,.45)] md:inline-flex"
        >
          Request Early Access
        </a>

      </div>
    </header>
  );
}