"use client";

import { useWorld } from "./WorldProvider";

import { backgroundForPhase } from "./LightingEngine";

export default function SkyRenderer() {

  const world = useWorld();

  return (

    <div

      className={`
        absolute
        inset-0
        bg-gradient-to-b
        ${backgroundForPhase(world.phase)}
        transition-all
        duration-[4000ms]
      `}

    />

  );

}