/**
 * GuavaCheck Engineering Engine
 * Public API Entry Point
 * ----------------------------
 * This file exposes the entire engineering system
 * as a clean, consumable module.
 */

export * from "./EngineeringTypes";
export * from "./EngineeringRegistry";
export * from "./EngineeringEngine";

/**
 * Factory helper for quick bootstrapping
 */
import { EngineeringRegistry } from "./EngineeringRegistry";
import { EngineeringEngine } from "./EngineeringEngine";

export function createEngineeringEngine() {
  const registry = new EngineeringRegistry();
  const engine = new EngineeringEngine(registry);

  return {
    registry,
    engine,
  };
}