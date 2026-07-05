/**
 * ============================================================
 * guavacheck
 * Austin Operating System
 * ------------------------------------------------------------
 * File: AustinConfiguration.ts
 *
 * Description:
 * Defines the global configuration used by the Austin Kernel.
 *
 * Austin reads this configuration during boot before any engine
 * is initialized.
 *
 * Think of this as Austin's DNA.
 * ============================================================
 /**
 * Default Austin Configuration
 */
 export const DefaultAustinConfiguration: AustinConfiguration = {

    name: "Austin",

    version: "1.0.0",

    environment: "development",

    debug: true,

    simulationEnabled: true,

    predictionEnabled: true,

    learningEnabled: true,

    maxConcurrentWorkflows: 100,

    maxConcurrentSimulations: 50,

    memoryCacheLimit: 10000,

    autoRegisterEngines: true,

    pluginsEnabled: true,

    auditEnabled: true,

    healthMonitoring: true,

    language: "en",

    timezone: "UTC"

};

export interface AustinConfiguration {

    /**
     * Name of the AI platform.
     */
    readonly name: string;

    /**
     * Austin version.
     */
    readonly version: string;

    /**
     * Current environment.
     */
    readonly environment:
        | "development"
        | "staging"
        | "production";

    /**
     * Enable verbose logging.
     */
    readonly debug: boolean;

    /**
     * Enable simulation engine.
     */
    readonly simulationEnabled: boolean;

    /**
     * Enable prediction engine.
     */
    readonly predictionEnabled: boolean;

    /**
     * Enable learning engine.
     */
    readonly learningEnabled: boolean;

    /**
     * Maximum concurrent workflows.
     */
    readonly maxConcurrentWorkflows: number;

    /**
     * Maximum concurrent simulations.
     */
    readonly maxConcurrentSimulations: number;

    /**
     * Maximum memory cache entries.
     */
    readonly memoryCacheLimit: number;

    /**
     * Auto-register all engines during startup.
     */
    readonly autoRegisterEngines: boolean;

    /**
     * Enable plugin discovery.
     */
    readonly pluginsEnabled: boolean;

    /**
     * Enable audit logging.
     */
    readonly auditEnabled: boolean;

    /**
     * Enable health monitoring.
     */
    readonly healthMonitoring: boolean;

    /**
     * Default language.
     */
    readonly language: string;

    /**
     * Default timezone.
     */
    readonly timezone: string;

}