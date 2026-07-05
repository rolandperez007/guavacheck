/**
 * RuntimeConfiguration
 */

export interface RuntimeConfiguration {

    workerThreads: number;

    enableTracing: boolean;

    enableProfiling: boolean;

    maximumQueueSize: number;

    taskTimeoutMs: number;

    retryAttempts: number;

}