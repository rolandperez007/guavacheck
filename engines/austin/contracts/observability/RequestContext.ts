/**
 * ============================================================
 * REQUEST CONTEXT
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 4
 * ACAS Volume 8
 */

export interface RequestContext {
  requestId: string;

  sessionId?: string;

  userId?: string;

  ipAddress?: string;

  country?: string;

  city?: string;

  userAgent?: string;

  engine: string;

  endpoint?: string;

  method?: string;

  timestamp: Date;
}
