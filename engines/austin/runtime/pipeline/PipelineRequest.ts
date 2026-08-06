/**
 * ============================================================================
 * Austin Cognitive Operating System (ACOS)
 * ----------------------------------------------------------------------------
 * PipelineRequest
 *
 * A PipelineRequest represents a single command sent into the Austin
 * Execution Pipeline.
 *
 * Every feature of Austin begins here.
 *
 * Examples:
 *
 * • Estimate building cost
 * • Verify contractor
 * • Run fraud detection
 * • Generate recommendation
 * • Predict market trend
 * • Execute simulation
 * • Search knowledge
 * • Build workflow
 *
 * ============================================================================
 */

export type PipelinePriority = "Low" | "Normal" | "High" | "Critical";

export interface PipelineRequest {
  /**
   * Unique request identifier.
   */
  requestId: string;

  /**
   * Service responsible for execution.
   *
   * Examples:
   *  verification
   *  simulation
   *  knowledge
   *  recommendation
   *  construction
   */
  service: string;

  /**
   * Action to perform.
   *
   * Examples:
   * estimateCost
   * verifyCompany
   * searchMaterials
   */
  action: string;

  /**
   * User payload.
   */
  payload: unknown;

  /**
   * User initiating request.
   */
  userId?: string;

  /**
   * Optional session.
   */
  sessionId?: string;

  /**
   * Optional project.
   */
  projectId?: string;

  /**
   * Geographic region.
   */
  location?: string;

  /**
   * Preferred language.
   */
  language?: string;

  /**
   * Request priority.
   */
  priority?: PipelinePriority;

  /**
   * Tags for routing,
   * analytics,
   * search,
   * logging.
   */
  tags?: string[];

  /**
   * Arbitrary metadata.
   */
  metadata?: Record<string, unknown>;

  /**
   * Creation timestamp.
   */
  createdAt: Date;
}
