/**
 * ============================================================
 * HEALTH POLICY
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 4
 * AIAS Volume 5
 */

export interface HealthPolicy {
  enabled: boolean;

  heartbeatInterval: number;

  timeout: number;

  warningThreshold: number;

  criticalThreshold: number;

  autoRecovery: boolean;

  restartOnFailure: boolean;

  notifyOnFailure: boolean;

  maxRecoveryAttempts: number;
}
