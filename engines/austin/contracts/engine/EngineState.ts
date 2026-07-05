/**
 * Engine Runtime State
 */

export enum EngineState {

    CREATED = "CREATED",

    INITIALIZING = "INITIALIZING",

    READY = "READY",

    STARTING = "STARTING",

    RUNNING = "RUNNING",

    PAUSED = "PAUSED",

    DEGRADED = "DEGRADED",

    RECOVERING = "RECOVERING",

    STOPPING = "STOPPING",

    STOPPED = "STOPPED",

    FAILED = "FAILED",

    SHUTDOWN = "SHUTDOWN"

}