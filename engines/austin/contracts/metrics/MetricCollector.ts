/**
 * ============================================================
 * METRIC COLLECTOR
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 6
 */

import { Metric } from "./Metric";

export interface MetricCollector {
  collect(metric: Metric): Promise<void>;

  flush(): Promise<void>;

  clear(): Promise<void>;
}
