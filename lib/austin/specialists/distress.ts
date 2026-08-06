import { PropertyContext, SpecialistResponse } from "../types";

export function distressSpecialist(context: PropertyContext): SpecialistResponse {
  const pricePressure = Math.random() * 100;

  return {
    specialist: "distress",

    summary: "Distress analysis completed",

    findings: [pricePressure > 70 ? "High urgency property detected" : "Normal listing pressure"],

    opportunities: [
      pricePressure > 70
        ? "Fast-sale opportunity available"
        : "Standard market listing recommended",
    ],

    risks: pricePressure > 80 ? ["High discount pressure expected"] : [],
  };
}
