import { getWorldClock } from "./clock";

export interface CloudState {
  coverage: number;
  opacity: number;
  speed: number;
  direction: number;
}

export function getCloudState(): CloudState {
  const clock = getWorldClock();

  switch (clock.phase) {
    case "dawn":
      return {
        coverage: 0.45,
        opacity: 0.55,
        speed: 0.22,
        direction: 1,
      };

    case "morning":
      return {
        coverage: 0.35,
        opacity: 0.5,
        speed: 0.3,
        direction: 1,
      };

    case "afternoon":
      return {
        coverage: 0.25,
        opacity: 0.4,
        speed: 0.45,
        direction: 1,
      };

    case "sunset":
      return {
        coverage: 0.4,
        opacity: 0.6,
        speed: 0.28,
        direction: 1,
      };

    default:
      return {
        coverage: 0.18,
        opacity: 0.22,
        speed: 0.12,
        direction: 1,
      };
  }
}
