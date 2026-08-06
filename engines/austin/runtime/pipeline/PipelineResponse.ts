/**
 * ============================================================================
 * Austin Cognitive Operating System (ACOS)
 * ----------------------------------------------------------------------------
 * PipelineResponse
 * ----------------------------------------------------------------------------
 * Standard response returned by every Austin pipeline execution.
 *
 * Every request entering Austin MUST produce exactly one PipelineResponse.
 *
 * The response is intentionally generic so that all Austin services share
 * one unified execution contract.
 *
 * Examples:
 *
 * • Construction estimate
 * • Verification report
 * • Knowledge search
 * • Recommendation
 * • Simulation
 * • Escrow
 * • Fraud detection
 * • Marketplace
 * • Banking
 *
 * ============================================================================
 */

export type PipelineStatus = "SUCCESS" | "PARTIAL_SUCCESS" | "FAILED" | "CANCELLED" | "TIMEOUT";

export interface PipelineResponse<T = unknown> {
  /**
   * Original request identifier.
   */
  requestId: string;

  /**
   * Pipeline execution identifier.
   */
  executionId: string;

  /**
   * Final execution status.
   */
  status: PipelineStatus;

  /**
   * Whether execution completed successfully.
   */
  success: boolean;

  /**
   * Service that generated the response.
   */
  service: string;

  /**
   * Action that was executed.
   */
  action: string;

  /**
   * Returned data.
   */
  result?: T;

  /**
   * Optional human-readable summary.
   */
  message?: string;

  /**
   * Warnings produced during execution.
   */
  warnings: string[];

  /**
   * Recoverable issues.
   */
  notices: string[];

  /**
   * Execution errors.
   */
  errors: string[];

  /**
   * Current pipeline stage when execution finished.
   */
  completedStage: string;

  /**
   * Number of stages executed.
   */
  stagesExecuted: number;

  /**
   * Total execution duration.
   */
  executionTimeMs: number;

  /**
   * CPU time consumed (optional).
   */
  cpuTimeMs?: number;

  /**
   * Peak memory usage (optional).
   */
  memoryUsageMb?: number;

  /**
   * Pipeline start time.
   */
  startedAt: Date;

  /**
   * Pipeline completion time.
   */
  completedAt: Date;

  /**
   * Correlation identifier for distributed tracing.
   */
  correlationId?: string;

  /**
   * Trace identifier.
   */
  traceId?: string;

  /**
   * Version of Austin producing this response.
   */
  runtimeVersion?: string;

  /**
   * Arbitrary metadata.
   */
  metadata: Record<string, unknown>;
}
