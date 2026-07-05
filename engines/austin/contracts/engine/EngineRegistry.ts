/**
 * ============================================================
 * ENGINE REGISTRY CONTRACT
 * ============================================================
 */

import { EngineContract } from "./EngineContract";

export interface EngineRegistry {

    register(engine: EngineContract): Promise<void>;

    unregister(id: string): Promise<void>;

    get(id: string): EngineContract | undefined;

    getAll(): EngineContract[];

    exists(id: string): boolean;

    clear(): Promise<void>;

}