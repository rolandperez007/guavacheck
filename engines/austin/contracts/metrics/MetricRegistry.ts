/**
 * ============================================================
 * METRIC REGISTRY
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 6
 */

import { MetricDefinition } from "./MetricDefinition";

export interface MetricRegistry {
  register(metric: MetricDefinition): Promise<void>;

  unregister(id: string): Promise<void>;

  exists(id: string): boolean;

  get(id: string): MetricDefinition | undefined;

  getAll(): MetricDefinition[];
}
