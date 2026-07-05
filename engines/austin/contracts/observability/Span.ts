/**
 * ============================================================
 * SPAN
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 3
 */

export interface Span {

    spanId: string;

    parentSpanId?: string;

    traceId: string;

    engine: string;

    name: string;

    operation: string;

    startTime: Date;

    endTime?: Date;

    durationMs?: number;

    success: boolean;

    metadata?: Record<string, unknown>;

}