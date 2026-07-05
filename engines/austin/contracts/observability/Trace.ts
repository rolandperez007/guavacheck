/**
 * ============================================================
 * TRACE
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 2
 */

import { Span } from "./Span";

export interface Trace {

    traceId: string;

    requestId: string;

    sessionId?: string;

    userId?: string;

    engine: string;

    operation: string;

    startTime: Date;

    endTime?: Date;

    durationMs?: number;

    status:

        | "RUNNING"

        | "SUCCESS"

        | "FAILED"

        | "CANCELLED";

    spans: Span[];

}