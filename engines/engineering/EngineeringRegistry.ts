/**
 * GuavaCheck Engineering Engine
 * Module Registry
 * ----------------------------
 * Central registry for all engineering modules.
 * Enables dynamic injection, swapping, scaling, and AI routing.
 */

import {
  EngineeringDiscipline,
  IEngineeringModule,
  RegisteredModule,
} from "./EngineeringTypes";

export class EngineeringRegistry {
  private modules: Map<EngineeringDiscipline, RegisteredModule>;

  constructor() {
    this.modules = new Map();
  }

  /**
   * Register a new engineering module
   */
  register(module: IEngineeringModule, version = "1.0.0"): void {
    const entry: RegisteredModule = {
      discipline: module.discipline,
      module,
      version,
    };

    this.modules.set(module.discipline, entry);
  }

  /**
   * Get a registered module
   */
  get(discipline: EngineeringDiscipline): IEngineeringModule {
    const entry = this.modules.get(discipline);

    if (!entry) {
      throw new Error(
        `Engineering module not found for discipline: ${discipline}`
      );
    }

    return entry.module;
  }

  /**
   * Check if module exists
   */
  has(discipline: EngineeringDiscipline): boolean {
    return this.modules.has(discipline);
  }

  /**
   * List all registered modules
   */
  list(): RegisteredModule[] {
    return Array.from(this.modules.values());
  }

  /**
   * Clear registry (useful for testing or hot reload)
   */
  clear(): void {
    this.modules.clear();
  }
}