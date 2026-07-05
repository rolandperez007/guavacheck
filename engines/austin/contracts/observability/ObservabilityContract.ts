/**
 * ============================================================
 * OBSERVABILITY CONTRACT
 * ============================================================
 *
 * Constitutional References
 * -------------------------
 * AOBS Volume 1 - Unified Observability
 * AOBS Volume 2 - Distributed Tracing
 * ACAS Volume 7 - Cognitive Visibility
 *
 * Every Austin engine must expose complete observability.
 */

import { CorrelationContext } from "./CorrelationContext";
import { RequestContext } from "./RequestContext";
import { Span } from "./Span";
import { Trace } from "./Trace";

export interface ObservabilityContract {

    startTrace(context: RequestContext): Promise<Trace>;

    endTrace(traceId: string): Promise<void>;

    startSpan(
        traceId: string,
        name: string
    ): Promise<Span>;

    finishSpan(spanId: string): Promise<void>;

    currentContext(): CorrelationContext;

}