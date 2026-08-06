export type TimeOfDay = "dawn" | "morning" | "afternoon" | "sunset" | "night";

export interface WorldClock {
  hour: number;
  minute: number;
  timezone: string;
  phase: TimeOfDay;
  isDay: boolean;
}

export interface WeatherState {
  condition: "clear" | "cloudy" | "rain" | "storm" | "fog";

  temperature: number;
  humidity: number;
  windSpeed: number;
}

export interface TrafficState {
  density: number;
  movingVehicles: number;
  parkedVehicles: number;
}

export interface ConstructionState {
  activeProjects: number;
  cranes: number;
  workers: number;
}

export interface EconomyState {
  marketIndex: number;
  investorConfidence: number;
}

export interface CityState {
  clock: WorldClock;
  weather: WeatherState;
  traffic: TrafficState;
  construction: ConstructionState;
  economy: EconomyState;
}
