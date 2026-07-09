/**
 * GuavaCheck Engineering Engine
 * Mechanical Engineering Module
 * ----------------------------
 * Handles mechanical systems, load transfer,
 * efficiency and equipment estimation.
 */

import {
  EngineeringInput,
  EngineeringResult,
  IEngineeringModule,
} from "./EngineeringTypes";

import { EngineeringCalculator } from "./EngineeringCalculator";
import { EngineeringValidator } from "./EngineeringValidator";

export interface MechanicalInput {
  systemLoad: number; // kW
  efficiency?: number; // %
  operatingHours?: number;
}

export interface MechanicalOutput {
  effectivePower: number;
  energyConsumption: number;
  recommendation: string;
}

export class MechanicalEngineering
  implements IEngineeringModule<MechanicalInput, MechanicalOutput>
{
  discipline = "mechanical" as const;

  async validate(input: EngineeringInput<MechanicalInput>): Promise<void> {
    EngineeringValidator.validateProjectContext(input);

    if (input.data.systemLoad < 0) {
      throw new Error("System load cannot be negative");
    }
  }

  async compute(
    input: EngineeringInput<MechanicalInput>
  ): Promise<EngineeringResult<MechanicalOutput>> {
    const {
      systemLoad,
      efficiency = 85,
      operatingHours = 8,
    } = input.data;

    const efficiencyFactor = efficiency / 100;

    const effectivePower = systemLoad * efficiencyFactor;

    const energyConsumption = effectivePower * operatingHours;

    const recommendation =
      efficiency < 70
        ? "System efficiency is low — upgrade recommended"
        : "System operating within acceptable efficiency range";

    return {
      discipline: this.discipline,
      success: true,
      summary: "Mechanical system analysis complete",

      data: {
        effectivePower,
        energyConsumption,
        recommendation,
      },

      metrics: {
        efficiency,
        operatingHours,
      },

      warnings: efficiency < 70 ? ["Low mechanical efficiency"] : [],

      errors: [],

      generatedAt: new Date(),
    };
  }
}