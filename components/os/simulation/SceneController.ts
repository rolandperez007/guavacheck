"use client";

import { useEffect } from "react";
import { worldClock } from "./WorldClock";
import { eventBus } from "./EventBus";

export default function SceneController() {
  useEffect(() => {
    const interval = setInterval(() => {
      eventBus.emit({
        id: crypto.randomUUID(),

        type: "world.tick",

        timestamp: Date.now(),

        payload: {
          progress: worldClock.getDayProgress(),
        },
      });
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return null;
}
