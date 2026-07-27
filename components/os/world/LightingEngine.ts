import { WorldPhase } from "./WorldState";

export function backgroundForPhase(
  phase: WorldPhase
) {

  switch (phase) {

    case "dawn":

      return
        "from-orange-200 via-sky-200 to-blue-200";

    case "morning":

      return
        "from-sky-300 via-blue-300 to-white";

    case "day":

      return
        "from-blue-400 via-sky-300 to-cyan-200";

    case "golden-hour":

      return
        "from-yellow-300 via-orange-300 to-pink-300";

    case "sunset":

      return
        "from-orange-600 via-purple-700 to-slate-900";

    default:

      return
        "from-slate-950 via-black to-black";

  }

}