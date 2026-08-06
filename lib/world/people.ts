import { getWorldClock } from "./clock";

export interface PopulationState {
  offices: number;
  parks: number;
  shopping: number;
  restaurants: number;
}

export function getPopulation(): PopulationState {
  const hour = getWorldClock().hour;

  return {
    offices: hour >= 8 && hour <= 17 ? 100 : 20,
    parks: hour >= 17 && hour <= 20 ? 85 : 35,
    shopping: hour >= 10 && hour <= 21 ? 90 : 25,
    restaurants: hour >= 18 ? 95 : 30,
  };
}
