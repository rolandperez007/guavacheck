import { PropertyContext, SpecialistResponse } from "../types";

export function legalSpecialist(
  context: PropertyContext
): SpecialistResponse {
  const docs = context.documents;

  const missing: string[] = [];

  if (!docs?.certificateOfOccupancy?.length)
    missing.push("Certificate of Occupancy");

  if (!docs?.deedOfAssignment?.length)
    missing.push("Deed of Assignment");

  return {
    specialist: "legal",

    summary: "Legal verification assessment completed",

    findings: [
      missing.length === 0
        ? "All key legal documents present"
        : "Some legal documents are missing",
    ],

    risks:
      missing.length > 0
        ? missing.map((m) => `Missing: ${m}`)
        : [],

    opportunities: [
      missing.length === 0
        ? "Property is ready for secure transaction"
        : "Complete documentation to increase buyer trust",
    ],
  };
}