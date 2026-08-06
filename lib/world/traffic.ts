import { getWorldClock } from "./clock";

export interface TrafficFlow {
  cars: number;
  buses: number;
  trucks: number;
  pedestrians: number;
}

export function getTraffic(): TrafficFlow {
  const hour = getWorldClock().hour;

  if (hour >= 7 && hour <= 9) {
    return {
      cars: 95,
      buses: 42,
      trucks: 12,
      pedestrians: 90,
    };
  }

  if (hour >= 16 && hour <= 19) {
    return {
      cars: 100,
      buses: 48,
      trucks: 15,
      pedestrians: 95,
    };
  }

  if (hour >= 0 && hour <= 5) {
    return {
      cars: 10,
      buses: 2,
      trucks: 6,
      pedestrians: 4,
    };
  }

  return {
    cars: 55,
    buses: 15,
    trucks: 8,
    pedestrians: 35,
  };
}
