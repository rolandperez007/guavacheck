/**
 * ============================================================
 * CORRELATION CONTEXT
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 4
 */

export interface CorrelationContext {
  correlationId: string;

  traceId: string;

  requestId: string;

  sessionId?: string;

  userId?: string;

  workflowId?: string;

  pipelineId?: string;
}
