/**
 * ============================================================
 * ENGINE CONFIGURATION CONTRACT
 * ============================================================
 */

export interface EngineConfiguration {

    enabled: boolean;

    autoStart: boolean;

    autoRecover: boolean;

    debug: boolean;

    maintenanceMode: boolean;

    timeout: number;

    retryAttempts: number;

    retryDelay: number;

    maxConcurrency: number;

    maxQueueSize: number;

    cacheEnabled: boolean;

    metricsEnabled: boolean;

    tracingEnabled: boolean;

    loggingEnabled: boolean;

    healthCheckInterval: number;

    heartbeatInterval: number;

    custom?: Record<string, unknown>;

}