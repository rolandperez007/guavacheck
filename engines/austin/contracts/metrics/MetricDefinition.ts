/**
 * ============================================================
 * METRIC DEFINITION
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 5
 */

export interface MetricDefinition {
  id: string;

  name: string;

  description: string;

  unit: string;

  aggregation: "SUM" | "AVG" | "MAX" | "MIN" | "COUNT" | "RATE" | "PERCENTILE";

  retentionDays: number;
}
