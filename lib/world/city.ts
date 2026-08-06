import { getWorldClock } from "./clock";
import { getWeather } from "./weather";
import { getLighting } from "./lighting";
import { getCloudState } from "./clouds";
import { getTraffic } from "./traffic";
import { getPopulation } from "./people";
import { getConstruction } from "./construction";

export function buildCity() {
  return {
    generatedAt: new Date().toISOString(),

    clock: getWorldClock(),

    weather: getWeather(),

    lighting: getLighting(),

    clouds: getCloudState(),

    traffic: getTraffic(),

    population: getPopulation(),

    construction: getConstruction(),
  };
}
