/**
 * ============================================================
 * AUSTIN EVENT CONTRACT
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * ACAS Vol. 2 - Engine Communication
 * AOBS Vol. 1 - Observability
 * AIAS Vol. 3 - Distributed Runtime
 *
 * Every Austin event MUST implement this interface.
 */

export interface Event {

    id: string;

    type: string;

    source: string;

    timestamp: Date;

    correlationId: string;

    requestId?: string;

    sessionId?: string;

    userId?: string;

    priority: "LOW" | "NORMAL" | "HIGH" | "CRITICAL";

    payload: Record<string, unknown>;

    metadata?: Record<string, unknown>;

}