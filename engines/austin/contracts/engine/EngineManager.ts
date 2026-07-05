/**
 * ============================================================
 * ENGINE MANAGER CONTRACT
 * ============================================================
 */

import { EngineContract } from "./EngineContract";

export interface EngineManager {

    load(engine: EngineContract): Promise<void>;

    unload(id: string): Promise<void>;

    initializeAll(): Promise<void>;

    startAll(): Promise<void>;

    stopAll(): Promise<void>;

    restartAll(): Promise<void>;

    shutdownAll(): Promise<void>;

    healthCheck(): Promise<void>;

}