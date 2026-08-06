/**
 * ============================================================
 * HEALTH CHECK CONTRACT
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 3
 * AIAS Volume 4
 */

import { HealthReport } from "./HealthReport";

export interface HealthCheck {
  execute(): Promise<HealthReport>;
}
