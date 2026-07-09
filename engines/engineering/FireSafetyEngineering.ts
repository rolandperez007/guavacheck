/**
 * GuavaCheck Engineering Engine
 * Fire Safety Engineering Module
 * ----------------------------
 * Handles fire risk assessment,
 * evacuation logic, and safety classification.
 */

import {
  EngineeringInput,
  EngineeringResult,
  IEngineeringModule,
} from "./EngineeringTypes";

import { EngineeringValidator } from "./EngineeringValidator";

export interface FireSafetyInput {
  areaSqm: number;
  floors: number;
  occupancy: number;
}

export interface FireSafetyOutput {
  fireRiskScore: number;
  evacuationTime: number;
  safetyLevel: "safe" | "moderate" | "critical";
  recommendation: string;
}

export class FireSafetyEngineering
  implements IEngineeringModule<FireSafetyInput, FireSafetyOutput>
{
  discipline = "fire_safety" as const;

  async validate(input: EngineeringInput<FireSafetyInput>): Promise<void> {
    EngineeringValidator.validateProjectContext(input);

    if (input.data.occupancy <= 0) {
      throw new Error("Occupancy must be greater than 0");
    }
  }

  async compute(
    input: EngineeringInput<FireSafetyInput>
  ): Promise<EngineeringResult<FireSafetyOutput>> {
    const { areaSqm, floors, occupancy } = input.data;

    // Fire risk model (simplified composite score)
    const fireRiskScore =
      (areaSqm * 0.3) + (floors * 10) + (occupancy * 2);

    // Evacuation time model (seconds)
    const evacuationTime =
      (areaSqm / 10) + (occupancy * 0.5) + (floors * 15);

    const safetyLevel =
      fireRiskScore > 200
        ? "critical"
        : fireRiskScore > 120
        ? "moderate"
        : "safe";

    const recommendation =
      safetyLevel === "critical"
        ? "Install advanced fire suppression and increase exits"
        : safetyLevel === "moderate"
        ? "Improve evacuation routes and fire systems"
        : "Meets basic fire safety standards";

    return {
      discipline: this.discipline,
      success: true,
      summary: "Fire safety analysis completed",

      data: {
        fireRiskScore,
        evacuationTime,
        safetyLevel,
        recommendation,
      },

      metrics: {
        areaSqm,
        floors,
        occupancy,
      },

      warnings:
        safetyLevel !== "safe"
          ? ["Fire safety attention required"]
          : [],

      errors: [],

      generatedAt: new Date(),
    };
  }
}