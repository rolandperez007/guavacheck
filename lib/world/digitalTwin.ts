import { runSimulation } from "./simulation";

export function getDigitalTwin() {
  return {
    city: runSimulation(),

    version: "1.0",

    syncedAt: new Date().toISOString(),
  };
}
