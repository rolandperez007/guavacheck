/**
 * Engine Capability Declaration
 */

export interface EngineCapabilities {

    enabled: boolean;

    supportsRealtime: boolean;

    supportsPersistence: boolean;

    supportsRecovery: boolean;

    supportsScaling: boolean;

    supportsObservability: boolean;

    supportsTelemetry: boolean;

    supportsCaching: boolean;

    supportsLearning: boolean;

    supportsSimulation: boolean;

    supportsPrediction: boolean;

    supportsDistributedExecution: boolean;

    supportsBackgroundJobs: boolean;

    supportsEncryption: boolean;

    supportsCompression: boolean;

    supportsVersioning: boolean;

    maxConcurrency?: number;

    maxWorkers?: number;

}