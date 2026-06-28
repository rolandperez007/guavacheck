import {
  AustinSpecialist,
  AustinThinkingStep,
  PropertyContext,
  AustinDecision,
  UserIntent,
} from "./types";

/**
 * Austin Reasoning Engine
 * Converts context → structured thinking → decision path
 */

export function reasonAboutRequest(
  context: PropertyContext
): AustinDecision {
  const steps: AustinThinkingStep[] = [];

  // 1. Understand intent
  steps.push({
    step: "intent_analysis",
    description: "Determining user intent from context",
    result: context.intent,
    confidenceImpact: 5,
  });

  // 2. Identify missing data
  const missingData = detectMissingData(context);

  steps.push({
    step: "data_check",
    description: "Checking completeness of property data",
    result:
      missingData.length > 0
        ? `Missing: ${missingData.join(", ")}`
        : "Data complete",
    confidenceImpact: missingData.length > 0 ? -10 : 10,
  });

  // 3. Select specialists
  const specialists = selectSpecialists(context.intent);

  steps.push({
    step: "specialist_selection",
    description: "Selecting required expert systems",
    result: specialists.join(", "),
    confidenceImpact: 10,
  });

  // 4. Risk evaluation
  const risks = evaluateRisks(context);

  steps.push({
    step: "risk_assessment",
    description: "Evaluating potential risks in property data",
    result:
      risks.length > 0 ? risks.join(", ") : "No major risks detected",
    confidenceImpact: risks.length > 0 ? -15 : 5,
  });

  // 5. Compute confidence
  const confidence = computeConfidence(steps);

  return {
    intent: context.intent || "general_query",
    specialistsUsed: specialists,
    reasoning: steps.map((s) => s.description),
    confidence,
  };
}

/* -----------------------------
   SPECIALIST SELECTION
------------------------------*/

function selectSpecialists(
  intent?: UserIntent
): AustinSpecialist[] {
  switch (intent) {
    case "price_estimate":
    case "valuation":
      return ["valuation", "market"];

    case "construction_analysis":
      return ["construction", "inspection"];

    case "media_review":
      return ["media"];
    
    case "verification":
      return ["legal"];
    
      case "distress_analysis":
      return ["distress", "valuation", "legal"];

    case "design_advice":
      return ["design", "construction"];

    case "market_insight":
      return ["market"];

    default:
      return ["market"];
  }
}

/* -----------------------------
   MISSING DATA DETECTION
------------------------------*/

function detectMissingData(context: PropertyContext): string[] {
  const missing: string[] = [];

  if (!context.property?.bedrooms) missing.push("bedrooms");
  if (!context.location?.city) missing.push("location");
  if (!context.media?.photos?.length) missing.push("photos");

  return missing;
}

/* -----------------------------
   RISK EVALUATION
------------------------------*/

function evaluateRisks(context: PropertyContext): string[] {
  const risks: string[] = [];

  if (!context.documents?.certificateOfOccupancy) {
    risks.push("Missing Certificate of Occupancy");
  }

  if (!context.location?.latitude) {
    risks.push("Unverified geolocation");
  }

  return risks;
}

/* -----------------------------
   CONFIDENCE ENGINE
------------------------------*/

function computeConfidence(
  steps: AustinThinkingStep[]
) {
  let score = 70; // base confidence

  for (const step of steps) {
    score += step.confidenceImpact || 0;
  }

  // clamp between 0–100
  score = Math.max(0, Math.min(100, score));

  const factors = steps.map((s) => s.step);

  return {
    value: score,
    factors,
  };
}