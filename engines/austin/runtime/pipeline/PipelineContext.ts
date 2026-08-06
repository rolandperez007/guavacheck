/**
 * ============================================================================
 * Austin Cognitive Operating System (ACOS)
 * ----------------------------------------------------------------------------
 * PipelineContext
 *
 * The PipelineContext is the shared execution state for a single request.
 *
 * Every stage in the Austin Execution Pipeline receives the same context.
 *
 * Stages MUST NOT communicate directly with one another.
 * They exchange information only through this object.
 *
 * Lifetime:
 *
 * Request Received
 *        │
 *        ▼
 * PipelineContext Created
 *        │
 * Validation
 *        │
 * Context
 *        │
 * Memory
 *        │
 * Knowledge
 *        │
 * Decision
 *        │
 * Planning
 *        │
 * Simulation
 *        │
 * Recommendation
 *        │
 * Execution
 *        │
 * Storage
 *        │
 * Metrics
 *        │
 * Audit
 *        │
 * Learning
 *        │
 * Response
 *        ▼
 * Context Destroyed
 * ============================================================================
 */

import { PipelineRequest } from "./PipelineRequest";
import { PipelineResponse } from "./PipelineResponse";

export class PipelineContext {
  /**
   * Unique execution identifier.
   */
  public readonly executionId: string;

  /**
   * Time request entered Austin.
   */
  public readonly startedAt: Date;

  /**
   * Time execution completed.
   */
  public completedAt?: Date;

  /**
   * Original request.
   */
  public request: PipelineRequest;

  /**
   * Final response.
   */
  public response?: PipelineResponse;

  /**
   * Current pipeline stage.
   */
  public currentStage: string = "Initialization";

  /**
   * Execution status.
   */
  public status: "Pending" | "Running" | "Completed" | "Failed" = "Pending";

  /**
   * Working data shared between stages.
   */
  public readonly data = new Map<string, unknown>();

  /**
   * Runtime metadata.
   */
  public readonly metadata = new Map<string, unknown>();

  /**
   * Warnings generated during execution.
   */
  public readonly warnings: string[] = [];

  /**
   * Errors generated during execution.
   */
  public readonly errors: Error[] = [];

  /**
   * Pipeline execution history.
   */
  public readonly history: string[] = [];

  /**
   * Performance metrics.
   */
  public readonly metrics = {
    stagesExecuted: 0,

    executionTimeMs: 0,

    startedAt: Date.now(),
  };

  constructor(request: PipelineRequest) {
    this.executionId = crypto.randomUUID();

    this.startedAt = new Date();

    this.request = request;
  }

  /**
   * Store shared data.
   */
  public set<T>(key: string, value: T): void {
    this.data.set(key, value);
  }

  /**
   * Retrieve shared data.
   */
  public get<T>(key: string): T | undefined {
    return this.data.get(key) as T | undefined;
  }

  /**
   * Record stage transition.
   */
  public moveTo(stage: string): void {
    this.currentStage = stage;

    this.history.push(stage);

    this.metrics.stagesExecuted++;
  }

  /**
   * Record warning.
   */
  public warn(message: string): void {
    this.warnings.push(message);
  }

  /**
   * Record error.
   */
  public fail(error: Error): void {
    this.errors.push(error);

    this.status = "Failed";
  }

  /**
   * Mark execution as started.
   */
  public start(): void {
    this.status = "Running";
  }

  /**
   * Mark execution as complete.
   */
  public complete(response: PipelineResponse): void {
    this.status = "Completed";

    this.completedAt = new Date();

    this.response = response;

    this.metrics.executionTimeMs = Date.now() - this.metrics.startedAt;
  }
}
