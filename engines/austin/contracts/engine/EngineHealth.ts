/**
 * Engine Health
 */

export interface EngineHealth {

    healthy: boolean;

    score: number;

    uptime: number;

    startedAt: Date;

    lastHeartbeat: Date;

    memoryUsage: number;

    cpuUsage: number;

    activeWorkers: number;

    queuedJobs: number;

    activeRequests: number;

    failedRequests: number;

    warnings: string[];

    errors: string[];

}