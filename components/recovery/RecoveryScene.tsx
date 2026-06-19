"use client";

import Image from "next/image";
import AIAssistant from "./AIAssistant";
import RecoveryActions from "./RecoveryActions";

export default function RecoveryScene() {
  return (
    <div className="relative h-screen w-full bg-[#070b14] overflow-hidden text-white">

      {/* BACKGROUND GLOW */}
      <div className="absolute inset-0 bg-gradient-to-br from-black via-[#0b1a2e] to-black opacity-90" />

      {/* YOUR IMAGE (UNCHANGED) */}
      <div className="absolute inset-0 flex items-center justify-center">
        <div className="animate-bounce">
          <Image
            src="/404.png"
            alt="GuavaCheck 404"
            width={520}
            height={520}
          />
        </div>
      </div>

      {/* AI LAYER */}
      <div className="absolute bottom-28 w-full">
        <AIAssistant />
      </div>

      {/* ACTION LAYER */}
      <div className="absolute bottom-6 w-full">
        <RecoveryActions />
      </div>

    </div>
  );
}