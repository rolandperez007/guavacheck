/**
 * ============================================================
 * HEALTH STATUS
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 1 - Health Monitoring
 * ACAS Volume 4 - Engine Lifecycle
 * AIAS Volume 2 - Infrastructure Reliability
 */

export enum HealthStatus {
  UNKNOWN = "UNKNOWN",

  INITIALIZING = "INITIALIZING",

  HEALTHY = "HEALTHY",

  DEGRADED = "DEGRADED",

  WARNING = "WARNING",

  RECOVERING = "RECOVERING",

  UNHEALTHY = "UNHEALTHY",

  FAILED = "FAILED",

  SHUTDOWN = "SHUTDOWN",
}
