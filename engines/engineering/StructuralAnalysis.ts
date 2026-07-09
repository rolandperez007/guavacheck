/**
 * GuavaCheck Engineering Engine
 * Structural Analysis Module
 * ----------------------------
 * Core structural computation engine:
 * - Load analysis
 * - Beam stress estimation
 * - Safety evaluation
 */

import {
  EngineeringInput,
  EngineeringResult,
  IEngineeringModule,
} from "./EngineeringTypes";

import { EngineeringCalculator } from "./EngineeringCalculator";
import { EngineeringValidator } from "./EngineeringValidator";

export interface StructuralInput {
  span: number; // meters
  load: number; // kN
  materialStrength: number; // MPa
  safetyFactor?: number;
}

export interface StructuralOutput {
  stress: number;
  safe: boolean;
  recommendation: string;
}

export class StructuralAnalysis
  implements IEngineeringModule<StructuralInput, StructuralOutput>
{
  discipline = "structural" as const;

  async validate(input: EngineeringInput<StructuralInput>): Promise<void> {
    EngineeringValidator.validateProjectContext(input);
    EngineeringValidator.validateStructuralSafety(input.data);
  }

  async compute(
    input: EngineeringInput<StructuralInput>
  ): Promise<EngineeringResult<StructuralOutput>> {
    const { span, load, materialStrength, safetyFactor = 1.5 } =
      input.data;

    // Step 1: distributed load
    const distributedLoad =
      EngineeringCalculator.distributeLoad(load, span);

    // Step 2: simplified bending moment
    const moment = (load * span) / 8;

    // Step 3: stress calculation
    const stress = EngineeringCalculator.bendingStress(
      moment,
      materialStrength
    );

    // Step 4: apply safety factor
    const safeStress =
      EngineeringCalculator.applySafetyFactor(stress, safetyFactor);

    const safe = safeStress < materialStrength;

    return {
      discipline: this.discipline,
      success: true,
      summary: safe
        ? "Structure is within safe limits"
        : "Structure exceeds safe stress limits",

      data: {
        stress: safeStress,
        safe,
        recommendation: safe
          ? "Design is acceptable with current parameters"
          : "Increase beam size or reduce span/load",
      },

      metrics: {
        distributedLoad,
        moment,
        stress,
        safetyFactor,
      },

      warnings: safe ? [] : ["Structural risk detected"],

      errors: [],

      generatedAt: new Date(),
    };
  }
}