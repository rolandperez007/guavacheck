import { buildCity } from "./city";
import { getEconomy } from "./economy";
import { randomEvent } from "./events";

export function runSimulation() {
  return {
    world: buildCity(),

    economy: getEconomy(),

    event: randomEvent(),
  };
}
