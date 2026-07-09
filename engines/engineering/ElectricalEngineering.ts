/**
 * GuavaCheck Engineering Engine
 * Electrical Engineering Module
 * ----------------------------
 * Handles electrical load estimation,
 * power distribution, and system sizing.
 */

import {
  EngineeringInput,
  EngineeringResult,
  IEngineeringModule,
} from "./EngineeringTypes";

import { EngineeringCalculator } from "./EngineeringCalculator";
import { EngineeringValidator } from "./EngineeringValidator";

export interface ElectricalInput {
  areaSqm: number;
  applianceLoad?: number; // kW optional override
  backupSystem?: "solar" | "generator" | "hybrid" | "none";
}

export interface ElectricalOutput {
  totalLoad: number;
  recommendedCapacity: number;
  backupSuggestion: string;
  riskLevel: "low" | "medium" | "high";
}

export class ElectricalEngineering
  implements IEngineeringModule<ElectricalInput, ElectricalOutput>
{
  discipline = "electrical" as const;

  async validate(input: EngineeringInput<ElectricalInput>): Promise<void> {
    EngineeringValidator.validateProjectContext(input);

    if (input.data.areaSqm <= 0) {
      throw new Error("Area must be greater than 0");
    }
  }

  async compute(
    input: EngineeringInput<ElectricalInput>
  ): Promise<EngineeringResult<ElectricalOutput>> {
    const { areaSqm, applianceLoad, backupSystem = "solar" } = input.data;

    const estimatedLoad =
      applianceLoad ??
      EngineeringCalculator.estimateElectricalLoad(areaSqm) / 1000; // convert W → kW

    const recommendedCapacity = estimatedLoad * 1.25;

    const riskLevel =
      estimatedLoad > 20
        ? "high"
        : estimatedLoad > 10
        ? "medium"
        : "low";

    const backupSuggestion = this.getBackupAdvice(
      backupSystem,
      estimatedLoad
    );

    return {
      discipline: this.discipline,
      success: true,
      summary: "Electrical load analysis completed",

      data: {
        totalLoad: estimatedLoad,
        recommendedCapacity,
        backupSuggestion,
        riskLevel,
      },

      metrics: {
        areaSqm,
        loadFactor: estimatedLoad / areaSqm,
      },

      warnings:
        riskLevel === "high"
          ? ["High electrical load detected"]
          : [],

      errors: [],

      generatedAt: new Date(),
    };
  }

  private getBackupAdvice(
    system: ElectricalInput["backupSystem"],
    load: number
  ): string {
    switch (system) {
      case "solar":
        return load > 15
          ? "Hybrid solar system recommended"
          : "Standard solar system sufficient";
      case "generator":
        return "Diesel generator backup recommended";
      case "hybrid":
        return "Hybrid solar + generator system ideal";
      default:
        return "No backup system configured";
    }
  }
}