"use client";

import Image from "next/image";
import { useEffect, useState } from "react";

export default function NotFound() {
  const messages = [
    "System alert: page not found…",
    "Activating Guava recovery protocol…",
    "Scanning property network…",
    "Recovery routes ready."
  ];

  const [index, setIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setIndex((prev) => (prev + 1) % messages.length);
    }, 2500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="relative h-screen w-full bg-[#070b14] text-white overflow-hidden">

      <div className="absolute inset-0 bg-gradient-to-br from-black via-[#0b1a2e] to-black opacity-90" />

      {/* YOUR IMAGE (UNCHANGED) */}
      <div className="absolute inset-0 flex items-center justify-center">
        <Image
          src="/404.png"
          alt="GuavaCheck 404"
          width={520}
          height={520}
        />
      </div>

      {/* AI TEXT */}
      <div className="absolute bottom-28 w-full text-center">
        <p className="text-lg">
          🤖 {messages[index]}
        </p>
      </div>

      {/* NAVIGATION */}
      <div className="absolute bottom-6 w-full flex justify-center gap-4 flex-wrap">

        <a href="/" className="px-5 py-2 bg-green-600 rounded">
          🏠 Home
        </a>

        <a href="/properties" className="px-5 py-2 bg-blue-600 rounded">
          🏡 Properties
        </a>

        <a href="/dashboard" className="px-5 py-2 bg-purple-600 rounded">
          📊 Dashboard
        </a>

      </div>

    </div>
  );
}