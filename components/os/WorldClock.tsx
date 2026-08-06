"use client";

import { useEffect, useState } from "react";

export type WorldPhase = "dawn" | "morning" | "day" | "sunset" | "night";

export default function WorldClock() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
    }, 60000);

    return () => clearInterval(timer);
  }, []);

  const hour = time.getHours();

  const phase: WorldPhase =
    hour >= 5 && hour < 8
      ? "dawn"
      : hour >= 8 && hour < 17
        ? "day"
        : hour >= 17 && hour < 20
          ? "sunset"
          : hour >= 20 || hour < 5
            ? "night"
            : "morning";

  return <div data-phase={phase} className="absolute inset-0 pointer-events-none" />;
}
