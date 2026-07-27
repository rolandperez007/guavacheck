import { WorldPhase } from "./WorldState";

export function getWorldPhase(date: Date): WorldPhase {

  const hour = date.getHours();

  if (hour >= 5 && hour < 7)
    return "dawn";

  if (hour >= 7 && hour < 11)
    return "morning";

  if (hour >= 11 && hour < 17)
    return "day";

  if (hour >= 17 && hour < 18)
    return "golden-hour";

  if (hour >= 18 && hour < 20)
    return "sunset";

  return "night";

}