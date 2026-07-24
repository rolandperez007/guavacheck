import { getWorldClock } from "./clock";

export interface LightingState {
  brightness: number;
  cityLights: boolean;
  windowLights: boolean;
  streetLights: boolean;
  stars: boolean;
  moon: boolean;
}

export function getLighting(): LightingState {
  const phase = getWorldClock().phase;

  switch (phase) {
    case "dawn":
      return {
        brightness: 0.55,
        cityLights: true,
        windowLights: true,
        streetLights: true,
        stars: false,
        moon: false,
      };

    case "morning":
      return {
        brightness: 0.90,
        cityLights: false,
        windowLights: false,
        streetLights: false,
        stars: false,
        moon: false,
      };

    case "afternoon":
      return {
        brightness: 1,
        cityLights: false,
        windowLights: false,
        streetLights: false,
        stars: false,
        moon: false,
      };

    case "sunset":
      return {
        brightness: 0.55,
        cityLights: true,
        windowLights: true,
        streetLights: true,
        stars: false,
        moon: true,
      };

    default:
      return {
        brightness: 0.18,
        cityLights: true,
        windowLights: true,
        streetLights: true,
        stars: true,
        moon: true,
      };
  }
}