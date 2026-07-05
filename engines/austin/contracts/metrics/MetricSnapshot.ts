/**
 * ============================================================
 * METRIC SNAPSHOT
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 7
 */

import { Metric } from "./Metric";

export interface MetricSnapshot {

    generatedAt: Date;

    engine: string;

    metrics: Metric[];

    totalMetrics: number;

    durationMs: number;

}