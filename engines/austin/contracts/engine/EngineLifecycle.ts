/**
 * ============================================================
 * ENGINE LIFECYCLE CONTRACT
 * ============================================================
 */

import { EngineState } from "./EngineState";

export interface EngineLifecycle {

    readonly state: EngineState;

    initialize(): Promise<void>;

    configure(): Promise<void>;

    start(): Promise<void>;

    pause(): Promise<void>;

    resume(): Promise<void>;

    reload(): Promise<void>;

    recover(): Promise<void>;

    stop(): Promise<void>;

    shutdown(): Promise<void>;

}