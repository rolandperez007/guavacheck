/**
 * ============================================================
 * AUSTIN METRIC
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 5 - Metrics
 * ACAS Volume 6 - Engine Intelligence
 * ARGS Volume 2 - Resource Accounting
 *
 * Every measurable value inside Austin is represented
 * by this contract.
 */

export interface Metric {
  id: string;

  name: string;

  category: string;

  description?: string;

  value: number;

  unit: string;

  source: string;

  timestamp: Date;

  tags?: Record<string, string>;
}
