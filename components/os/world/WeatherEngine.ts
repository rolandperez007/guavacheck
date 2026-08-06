import { WorldState } from "./WorldState";

export function simulateWeather(state: WorldState): WorldState {
  return {
    ...state,

    cloudCoverage: Math.random(),

    humidity: 0.45 + Math.random() * 0.45,

    windSpeed: Math.round(Math.random() * 14),

    visibility: 0.8 + Math.random() * 0.2,

    precipitation: Math.random(),

    raining: Math.random() > 0.82,

    storm: Math.random() > 0.96,
  };
}
