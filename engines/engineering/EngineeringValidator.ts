/**
 * GuavaCheck Engineering Engine
 * Engineering Validator
 * ----------------------------
 * Ensures engineering inputs are safe, realistic, and consistent
 * before computation occurs.
 */

import { EngineeringInput } from "./EngineeringTypes";

export class EngineeringValidator {
  /**
   * Validate project context
   */
  static validateProjectContext(input: EngineeringInput): void {
    const ctx = input.context;

    if (!ctx.id) throw new Error("Project ID is required");
    if (!ctx.name) throw new Error("Project name is required");

    if (!ctx.location?.country) {
      throw new Error("Project location country is required");
    }

    if (ctx.plotArea && ctx.plotArea <= 0) {
      throw new Error("Plot area must be greater than 0");
    }

    if (ctx.floors && ctx.floors < 1) {
      throw new Error("Floors must be at least 1");
    }
  }

  /**
   * Validate numerical ranges for engineering safety
   */
  static validateEngineeringLimits(data: any): void {
    if (data?.height && data.height > 1000) {
      throw new Error("Building height exceeds safe engineering limits");
    }

    if (data?.load && data.load < 0) {
      throw new Error("Load cannot be negative");
    }
  }

  /**
   * Validate structural safety constraints
   */
  static validateStructuralSafety(params: {
    span?: number;
    load?: number;
    materialStrength?: number;
  }): void {
    if (params.span && params.span > 50) {
      throw new Error("Span exceeds standard structural limits");
    }

    if (params.load && params.load > 100000) {
      throw new Error("Load exceeds safety threshold");
    }

    if (params.materialStrength && params.materialStrength <= 0) {
      throw new Error("Invalid material strength");
    }
  }

  /**
   * General purpose sanitizer
   */
  static sanitizeInput<T>(input: T): T {
    // In future: AI-based sanitization layer can plug here
    return input;
  }
}
