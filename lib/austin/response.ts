import { AustinResponse, AustinDecision, SpecialistResponse } from "./types";

/**
 * Austin Response Engine
 * Converts reasoning + specialist output → final human-readable intelligence
 */

export function buildAustinResponse(params: {
  decision: AustinDecision;
  specialistResults?: SpecialistResponse[];
}): AustinResponse {
  const { decision, specialistResults = [] } = params;

  const insights = extractInsights(specialistResults);
  const warnings = extractWarnings(specialistResults);
  const recommendations = extractRecommendations(specialistResults);

  return {
    title: generateTitle(decision),

    summary: generateSummary(decision, insights),

    insights,

    warnings,

    recommendations,

    confidence: decision.confidence,

    nextActions: generateNextActions(decision),

    raw: {
      decision,
      specialistResults,
    },
  };
}

/* -----------------------------
   TITLE GENERATION
------------------------------*/

function generateTitle(decision: AustinDecision): string {
  switch (decision.intent) {
    case "price_estimate":
      return "Property Valuation Analysis";

    case "construction_analysis":
      return "Construction Assessment Report";

    case "distress_analysis":
      return "Distress Property Evaluation";

    case "verification":
      return "Property Verification Review";

    case "market_insight":
      return "Market Intelligence Report";

    default:
      return "Property Intelligence Report";
  }
}

/* -----------------------------
   SUMMARY
------------------------------*/

function generateSummary(decision: AustinDecision, insights: string[]): string {
  const base = "Austin has completed an analysis of the provided property data.";

  const confidenceNote = `Confidence level: ${decision.confidence.value}%.`;

  const insightPreview = insights.length > 0 ? ` Key insight: ${insights[0]}` : "";

  return `${base} ${confidenceNote}${insightPreview}`;
}

/* -----------------------------
   INSIGHTS EXTRACTION
------------------------------*/

function extractInsights(results: SpecialistResponse[]): string[] {
  const insights: string[] = [];

  for (const r of results) {
    if (r.findings?.length) {
      insights.push(...r.findings);
    }
  }

  return insights.slice(0, 5);
}

/* -----------------------------
   WARNINGS
------------------------------*/

function extractWarnings(results: SpecialistResponse[]): string[] {
  const warnings: string[] = [];

  for (const r of results) {
    if (r.risks?.length) {
      warnings.push(...r.risks);
    }
  }

  return warnings.slice(0, 5);
}

/* -----------------------------
   RECOMMENDATIONS
------------------------------*/

function extractRecommendations(results: SpecialistResponse[]): string[] {
  const recs: string[] = [];

  for (const r of results) {
    if (r.opportunities?.length) {
      recs.push(...r.opportunities);
    }
  }

  return recs.slice(0, 5);
}

/* -----------------------------
   NEXT ACTIONS
------------------------------*/

function generateNextActions(decision: AustinDecision): string[] {
  const actions: string[] = [];

  if (decision.confidence.value < 60) {
    actions.push("Request additional property information");
  }

  if (decision.specialistsUsed.includes("media")) {
    actions.push("Improve property media quality");
  }

  if (decision.specialistsUsed.includes("legal")) {
    actions.push("Complete document verification");
  }

  if (decision.specialistsUsed.includes("valuation")) {
    actions.push("Refine market pricing strategy");
  }

  actions.push("Generate updated Austin report");

  return actions;
}
