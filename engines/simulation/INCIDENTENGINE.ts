import { Incident } from "./INCIDENT";

export class IncidentEngine {

    static evaluate(incident: Incident): string {

        if (incident.severity === "critical")
            return "Immediate Response";

        if (incident.severity === "high")
            return "Priority Investigation";

        return "Monitor";

    }

}