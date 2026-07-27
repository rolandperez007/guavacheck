"use client";

import Sky from "./Sky";
import Clouds from "./Clouds";
import AmbientLife from "./AmbientLife";

import Shell from "./Shell";

export default function GuavaOS({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <main
      className="
      relative
      min-h-screen
      overflow-hidden
      bg-black
      "
    >

      <Sky />

      <Clouds />

      <AmbientLife />

      <div className="relative z-10">
        <Shell>
          {children}
        </Shell>
      </div>

    </main>
  );
}