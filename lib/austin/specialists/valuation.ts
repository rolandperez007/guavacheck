import { PropertyContext, SpecialistResponse } from "../types";

export function valuationSpecialist(
  context: PropertyContext
): SpecialistResponse {
  const p = context.property;

  let basePrice = 0;

  // simple heuristic model (we improve later with real data)
  if (p?.buildingSize) {
    basePrice += p.buildingSize * 500; // per sqm baseline
  }

  if (p?.bedrooms) {
    basePrice += p.bedrooms * 20000;
  }

  if (p?.location?.city === "Lekki") {
    basePrice *= 1.4;
  }

  return {
    specialist: "valuation",
    summary: "Property valuation completed using heuristic model",

    findings: [
      `Estimated base value calculated from size and rooms`,
      `Location adjustment applied`,
    ],

    opportunities: [
      "Property may be optimized for higher listing price",
    ],

    data: {
      estimatedValue: Math.round(basePrice),
    },
  };
}