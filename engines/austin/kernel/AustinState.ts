/**
 * ============================================================
 * guavacheck
 * Austin Operating System
 * ------------------------------------------------------------
 * File: AustinState.ts
 * Description:
 * Defines every lifecycle state of the Austin Kernel.
 *
 * All Austin components should reference this enum instead of
 * using hardcoded strings.
 * ============================================================
 */

export enum AustinState {

    /**
     * Austin has not yet started.
     */
    STOPPED = "STOPPED",

    /**
     * Austin is initializing internal systems.
     */
    INITIALIZING = "INITIALIZING",

    /**
     * Core services are loading.
     */
    BOOTSTRAPPING = "BOOTSTRAPPING",

    /**
     * Engines are registering.
     */
    REGISTERING = "REGISTERING",

    /**
     * Knowledge and memory are loading.
     */
    LOADING = "LOADING",

    /**
     * Austin is operational and ready to receive requests.
     */
    READY = "READY",

    /**
     * Austin is actively processing requests.
     */
    RUNNING = "RUNNING",

    /**
     * Austin is temporarily paused.
     */
    PAUSED = "PAUSED",

    /**
     * Austin is restarting.
     */
    RESTARTING = "RESTARTING",

    /**
     * Austin is shutting down.
     */
    SHUTTING_DOWN = "SHUTTING_DOWN",

    /**
     * Austin encountered a fatal error.
     */
    FAILED = "FAILED",

    /**
     * Austin has completely shut down.
     */
    TERMINATED = "TERMINATED"

}