/**
 * GuavaCheck Engineering Engine
 * Plumbing Engineering Module
 * ----------------------------
 * Handles water distribution, drainage systems,
 * pipe flow estimation, and consumption modeling.
 */

import {
  EngineeringInput,
  EngineeringResult,
  IEngineeringModule,
} from "./EngineeringTypes";

import { EngineeringCalculator } from "./EngineeringCalculator";
import { EngineeringValidator } from "./EngineeringValidator";

export interface PlumbingInput {
  occupants: number;
  buildingArea: number;
  waterPressure?: number;
}

export interface PlumbingOutput {
  dailyWaterDemand: number;
  pipeFlowRate: number;
  storageTankRecommendation: number;
  riskLevel: "low" | "medium" | "high";
}

export class PlumbingEngineering
  implements IEngineeringModule<PlumbingInput, PlumbingOutput>
{
  discipline = "plumbing" as const;

  async validate(input: EngineeringInput<PlumbingInput>): Promise<void> {
    EngineeringValidator.validateProjectContext(input);

    if (input.data.occupants <= 0) {
      throw new Error("Occupants must be greater than 0");
    }
  }

  async compute(
    input: EngineeringInput<PlumbingInput>
  ): Promise<EngineeringResult<PlumbingOutput>> {
    const { occupants, buildingArea, waterPressure = 3 } = input.data;

    // Average water demand per person (liters/day)
    const dailyWaterDemand = occupants * 150;

    // Pipe flow estimation
    const pipeFlowRate = EngineeringCalculator.pipeFlowRate(
      25,
      waterPressure
    );

    // Storage sizing (3-day backup)
    const storageTankRecommendation = dailyWaterDemand * 3;

    const riskLevel =
      waterPressure < 2
        ? "high"
        : waterPressure < 3
        ? "medium"
        : "low";

    return {
      discipline: this.discipline,
      success: true,
      summary: "Plumbing system analysis completed",

      data: {
        dailyWaterDemand,
        pipeFlowRate,
        storageTankRecommendation,
        riskLevel,
      },

      metrics: {
        occupants,
        buildingArea,
      },

      warnings:
        riskLevel === "high"
          ? ["Low water pressure detected"]
          : [],

      errors: [],

      generatedAt: new Date(),
    };
  }
}