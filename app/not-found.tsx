"use client";

import Image from "next/image";

export default function NotFound() {
  return (
    <div className="relative h-screen w-full bg-[#0b0f19] text-white overflow-hidden">

      {/* YOUR IMAGE (UNCHANGED) */}
      <div className="absolute inset-0 flex items-center justify-center opacity-90">
        <Image
          src="/Updated 404.png"
          alt="GuavaCheck 404"
          width={500}
          height={500}
        />
      </div>

      {/* AI TEXT LAYER */}
      <div className="absolute bottom-20 w-full text-center px-6">
        <p className="text-lg animate-pulse">
          🤖 I couldn’t find that page… but I can help you recover it.
        </p>
      </div>

      {/* NAVIGATION LAYER */}
      <div className="absolute bottom-6 w-full flex justify-center gap-4 flex-wrap">
        <button className="px-4 py-2 bg-green-600 rounded">
          Take me Home
        </button>

        <button className="px-4 py-2 bg-blue-600 rounded">
          Search Property
        </button>

        <button className="px-4 py-2 bg-purple-600 rounded">
          Open Dashboard
        </button>
      </div>

    </div>
  );
}