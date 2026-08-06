/**
 * ============================================================
 * ENGINE STATISTICS
 * ============================================================
 */

export interface EngineStatistics {
  totalRequests: number;

  successfulRequests: number;

  failedRequests: number;

  activeRequests: number;

  queuedRequests: number;

  averageLatency: number;

  peakLatency: number;

  throughputPerSecond: number;

  uptimeSeconds: number;

  restarts: number;

  crashes: number;

  warnings: number;

  errors: number;

  memoryUsageMB: number;

  cpuUsagePercent: number;
}
