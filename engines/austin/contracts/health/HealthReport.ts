/**
 * ============================================================
 * HEALTH REPORT
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 3
 * ACAS Volume 5
 */

import { HealthIndicator } from "./HealthIndicator";
import { HealthStatus } from "./HealthStatus";

export interface HealthReport {

    engine: string;

    status: HealthStatus;

    overallScore: number;

    indicators: HealthIndicator[];

    warnings: string[];

    recommendations: string[];

    generatedAt: Date;

    nextCheck: Date;

}