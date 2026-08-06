/**
 * GuavaCheck Engineering Engine
 * Core Orchestrator
 * ----------------------------
 * This is the execution layer that:
 * - Validates input
 * - Routes to correct module
 * - Executes computation
 * - Normalizes output
 * - Prepares AI-ready response layer
 */

import {
  EngineeringInput,
  EngineeringResult,
  EngineeringDiscipline,
  IEngineeringModule,
} from "./EngineeringTypes";

import { EngineeringRegistry } from "./EngineeringRegistry";

export class EngineeringEngine {
  private registry: EngineeringRegistry;

  constructor(registry: EngineeringRegistry) {
    this.registry = registry;
  }

  /**
   * Main execution entry point
   */
  async run<TInput, TOutput>(input: EngineeringInput<TInput>): Promise<EngineeringResult<TOutput>> {
    const module = this.registry.get(input.discipline) as IEngineeringModule<TInput, TOutput>;

    await this.safeValidate(module, input);

    const result = await module.compute(input);

    return this.enrichResult(result, input.discipline);
  }

  /**
   * Safe validation layer (prevents module crashes from breaking engine)
   */
  private async safeValidate<TInput>(
    module: IEngineeringModule<TInput>,
    input: EngineeringInput<TInput>,
  ): Promise<void> {
    try {
      await module.validate(input);
    } catch (error: any) {
      throw new Error(`Validation failed for ${input.discipline}: ${error.message}`);
    }
  }

  /**
   * Standardized output enrichment layer
   */
  private enrichResult<T>(
    result: EngineeringResult<T>,
    discipline: EngineeringDiscipline,
  ): EngineeringResult<T> {
    return {
      ...result,
      discipline,
      generatedAt: new Date(),
    };
  }

  /**
   * Health check for system readiness
   */
  health(): {
    status: "ok" | "degraded";
    modules: number;
  } {
    return {
      status: "ok",
      modules: this.registry.list().length,
    };
  }
}
