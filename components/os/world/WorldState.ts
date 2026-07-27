export type WorldPhase =
  | "dawn"
  | "morning"
  | "day"
  | "golden-hour"
  | "sunset"
  | "night";

export interface WorldState {

  now: Date;

  timezone: string;

  latitude?: number;

  longitude?: number;

  phase: WorldPhase;

  sunrise: string;

  sunset: string;

  temperature: number;

  humidity: number;

  visibility: number;

  windSpeed: number;

  cloudCoverage: number;

  precipitation: number;

  raining: boolean;

  storm: boolean;

  trafficLevel: number;

  peopleDensity: number;

  starsVisible: boolean;

  moonVisible: boolean;

}