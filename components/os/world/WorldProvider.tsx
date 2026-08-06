"use client";

import { createContext, useContext, useEffect, useState } from "react";

import { WorldState } from "./WorldState";

import { getWorldPhase } from "./TimeEngine";

import { simulateWeather } from "./WeatherEngine";

const WorldContext = createContext<WorldState | null>(null);

export function WorldProvider({ children }: { children: React.ReactNode }) {
  const [world, setWorld] = useState<WorldState>(() => {
    const now = new Date();

    return {
      now,

      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,

      phase: getWorldPhase(now),

      sunrise: "06:25",

      sunset: "18:48",

      temperature: 27,

      humidity: 0.52,

      visibility: 1,

      windSpeed: 5,

      cloudCoverage: 0.35,

      precipitation: 0,

      raining: false,

      storm: false,

      trafficLevel: 0.55,

      peopleDensity: 0.62,

      starsVisible: false,

      moonVisible: false,
    };
  });

  useEffect(() => {
    const timer = setInterval(() => {
      setWorld((previous) => {
        const now = new Date();

        return simulateWeather({
          ...previous,

          now,

          phase: getWorldPhase(now),

          starsVisible: now.getHours() >= 20,

          moonVisible: now.getHours() >= 18,
        });
      });
    }, 60000);

    return () => clearInterval(timer);
  }, []);

  return <WorldContext.Provider value={world}>{children}</WorldContext.Provider>;
}

export function useWorld() {
  const context = useContext(WorldContext);

  if (!context) throw new Error("useWorld must be used inside WorldProvider");

  return context;
}
