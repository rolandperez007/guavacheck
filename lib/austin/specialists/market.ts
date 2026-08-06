import { PropertyContext, SpecialistResponse } from "../types";

export function marketSpecialist(context: PropertyContext): SpecialistResponse {
  const city = context.location?.city;

  const trends: Record<string, number> = {
    Lagos: 8.2,
    Lekki: 10.5,
    Abuja: 6.8,
  };

  const growth = trends[city || ""] || 5;

  return {
    specialist: "market",

    summary: "Market conditions analyzed",

    findings: [`Average market growth: ${growth}%`, "Demand trending upward in selected region"],

    opportunities: ["Strong appreciation potential", "Good time to list property"],

    risks: growth < 6 ? ["Slow market conditions"] : [],
  };
}
