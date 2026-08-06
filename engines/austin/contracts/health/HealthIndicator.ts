/**
 * ============================================================
 * HEALTH INDICATOR
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 2
 * ACAS Volume 5
 */

import { HealthStatus } from "./HealthStatus";

export interface HealthIndicator {
  id: string;

  name: string;

  status: HealthStatus;

  score: number;

  value: unknown;

  threshold?: number;

  message?: string;

  timestamp: Date;
}
