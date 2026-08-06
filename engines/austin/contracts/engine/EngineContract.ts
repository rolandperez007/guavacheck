/**
 * ============================================================
 * AUSTIN ENGINE CONTRACT
 * ============================================================
 *
 * Every Austin Engine MUST implement this contract.
 * This is the constitutional foundation of the Austin OS.
 *
 * Constitutional References:
 * - ACAS
 * - AOBS
 * - AIAS
 *
 * Version: 1.0
 */

export interface EngineContract {
  readonly id: string;

  readonly name: string;

  readonly version: string;

  readonly description: string;

  readonly author: string;

  readonly constitutionalReferences: string[];

  readonly dependencies: string[];

  readonly capabilities: string[];

  readonly publishes: string[];

  readonly subscribes: string[];

  initialize(): Promise<void>;

  start(): Promise<void>;

  stop(): Promise<void>;

  restart(): Promise<void>;

  shutdown(): Promise<void>;

  health(): Promise<boolean>;

  metrics(): Promise<Record<string, unknown>>;
}
