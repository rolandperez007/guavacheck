/**
 * RuntimeCapabilities
 */

export interface RuntimeCapabilities {

    supportsParallelExecution: boolean;

    supportsBackgroundWorkers: boolean;

    supportsScheduling: boolean;

    supportsTracing: boolean;

    supportsSnapshots: boolean;

    supportsPipelines: boolean;

}