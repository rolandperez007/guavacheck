import { getWorldClock } from "./clock";

export interface ConstructionActivity {
  cranesActive: boolean;
  workers: number;
  deliveries: number;
}

export function getConstruction(): ConstructionActivity {
  const hour = getWorldClock().hour;

  if (hour >= 7 && hour <= 18) {
    return {
      cranesActive: true,
      workers: 220,
      deliveries: 38,
    };
  }

  return {
    cranesActive: false,
    workers: 12,
    deliveries: 2,
  };
}