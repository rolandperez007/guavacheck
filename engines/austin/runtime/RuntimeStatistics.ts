/**
 * RuntimeStatistics
 */

export interface RuntimeStatistics {

    totalTasksExecuted: number;

    totalFailures: number;

    totalWorkerStarts: number;

    averageExecutionTimeMs: number;

    averageQueueTimeMs: number;

    peakWorkers: number;

    runtimeStarted: string;

}