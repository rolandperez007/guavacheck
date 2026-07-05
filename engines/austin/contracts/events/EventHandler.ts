/**
 * ============================================================
 * EVENT HANDLER CONTRACT
 * ============================================================
 *
 * Constitutional References
 * ACAS Vol.2
 * AIAS Vol.3
 */

import { Event } from "./Event";

export interface EventHandler {

    readonly event: string;

    handle(event: Event): Promise<void>;

}