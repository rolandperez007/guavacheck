import { buildAustinContext } from "./context";
import { reasonAboutRequest } from "./reasoning";
import { buildAustinResponse } from "./response";

import {
  AustinResponse,
  WizardAustinInput,
} from "./types";

/**
 * Austin Brain (CEO Layer)
 * Orchestrates the entire intelligence pipeline
 *
 * Flow:
 * Wizard Input
 *   → Context
 *   → Reasoning
 *   → (Specialists later)
 *   → Response
 */

export async function runAustin(
  input: WizardAustinInput
): Promise<AustinResponse> {
  try {
    /**
     * 1. PERCEPTION LAYER
     * Convert raw wizard data into structured context
     */
    const context = buildAustinContext(input);

    /**
     * 2. THINKING LAYER
     * Austin analyzes context and decides what to do
     */
    const decision = reasonAboutRequest(context);

    /**
     * 3. SPECIALISTS LAYER (placeholder for now)
     * Later we will plug in real AI/agents here
     */
    const specialistResults = await runSpecialists(decision, context);

    /**
     * 4. RESPONSE LAYER
     * Convert intelligence into structured output
     */
    const response = buildAustinResponse({
      decision,
      specialistResults,
    });

    return response;
  } catch (error: any) {
    return {
      title: "Austin Error Report",

      summary:
        "Austin encountered an issue while processing this request.",

      insights: [],

      warnings: [
        error?.message || "Unknown error occurred",
      ],

      recommendations: [
        "Retry analysis",
        "Check input data completeness",
      ],

      confidence: {
        value: 0,
        factors: ["system_failure"],
      },

      nextActions: ["Restart Austin pipeline"],

      raw: error,
    };
  }
}

/* -----------------------------
   SPECIALIST ENGINE (PLACEHOLDER)
------------------------------*/

import {
  valuationSpecialist,
  marketSpecialist,
  legalSpecialist,
  mediaSpecialist,
  distressSpecialist,
} from "./specialists";

/**
 * SPECIALIST ENGINE
 * Real execution layer (NO MOCKS)
 */

export async function runSpecialists(
  decision: any,
  context: any
) {
  const results = [];

  for (const specialist of decision.specialistsUsed) {
    switch (specialist) {
      case "valuation":
        results.push(valuationSpecialist(context));
        break;

      case "market":
        results.push(marketSpecialist(context));
        break;

      case "legal":
        results.push(legalSpecialist(context));
        break;

      case "media":
        results.push(mediaSpecialist(context));
        break;

      case "distress":
        results.push(distressSpecialist(context));
        break;
    }
  }

  return results;
}