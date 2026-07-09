/**
 * GuavaCheck Engineering Engine
 * HVAC Engineering Module
 * ----------------------------
 * Handles cooling load estimation,
 * airflow, and ventilation system design.
 */

import {
  EngineeringInput,
  EngineeringResult,
  IEngineeringModule,
} from "./EngineeringTypes";

import { EngineeringCalculator } from "./EngineeringCalculator";
import { EngineeringValidator } from "./EngineeringValidator";

export interface HVACInput {
  areaSqm: number;
  occupants: number;
  ceilingHeight?: number;
}

export interface HVACOutput {
  coolingLoadBTU: number;
  airflowRequirement: number;
  systemSizeRecommendation: string;
  efficiencyRating: "low" | "medium" | "high";
}

export class HVACEngineering
  implements IEngineeringModule<HVACInput, HVACOutput>
{
  discipline = "hvac" as const;

  async validate(input: EngineeringInput<HVACInput>): Promise<void> {
    EngineeringValidator.validateProjectContext(input);

    if (input.data.areaSqm <= 0) {
      throw new Error("Invalid area");
    }
  }

  async compute(
    input: EngineeringInput<HVACInput>
  ): Promise<EngineeringResult<HVACOutput>> {
    const {
      areaSqm,
      occupants,
      ceilingHeight = 3,
    } = input.data;

    const coolingLoadBTU =
      EngineeringCalculator.estimateCoolingLoad(areaSqm, ceilingHeight);

    const airflowRequirement =
      (occupants * 6) + (areaSqm * 0.3); // simplified ventilation model

    const systemSizeRecommendation =
      coolingLoadBTU > 60000
        ? "Central HVAC system recommended"
        : coolingLoadBTU > 30000
        ? "Split unit system recommended"
        : "Single unit AC system sufficient";

    const efficiencyRating =
      coolingLoadBTU > 80000
        ? "low"
        : coolingLoadBTU > 50000
        ? "medium"
        : "high";

    return {
      discipline: this.discipline,
      success: true,
      summary: "HVAC analysis completed",

      data: {
        coolingLoadBTU,
        airflowRequirement,
        systemSizeRecommendation,
        efficiencyRating,
      },

      metrics: {
        areaSqm,
        occupants,
        ceilingHeight,
      },

      warnings:
        efficiencyRating === "low"
          ? ["High cooling demand detected"]
          : [],

      errors: [],

      generatedAt: new Date(),
    };
  }
}