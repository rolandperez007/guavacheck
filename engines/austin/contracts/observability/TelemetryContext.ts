/**
 * ============================================================
 * TELEMETRY CONTEXT
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 5
 */

export interface TelemetryContext {

    cpuUsage: number;

    memoryUsage: number;

    activeWorkers: number;

    queuedTasks: number;

    activeRequests: number;

    latencyMs: number;

    throughput: number;

    errorRate: number;

    cacheHitRate: number;

    networkLatency: number;

    storageLatency: number;

    aiLatency?: number;

}