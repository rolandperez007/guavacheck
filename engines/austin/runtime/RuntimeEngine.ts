/**
 * ==============================================================
 * RuntimeEngine
 * --------------------------------------------------------------
 * The central execution coordinator for Austin.
 *
 * Responsibilities
 * - Start the runtime
 * - Stop the runtime
 * - Coordinate workers
 * - Coordinate schedulers
 * - Dispatch execution pipelines
 * - Report runtime health
 * ==============================================================
 */

import { RuntimeManager } from "./RuntimeManager";
import { RuntimeRegistry } from "./RuntimeRegistry";
import { RuntimeHealth } from "./RuntimeHealth";

export class RuntimeEngine {

    private readonly manager = new RuntimeManager();

    private readonly registry = new RuntimeRegistry();

    private readonly health = new RuntimeHealth();

    public async initialize(): Promise<void> {

        await this.registry.initialize();

        await this.manager.initialize();

    }

    public async start(): Promise<void> {

        await this.manager.start();

    }

    public async shutdown(): Promise<void> {

        await this.manager.shutdown();

    }

    public getHealth(): RuntimeHealth {

        return this.health;

    }

}