/**
 * ============================================================
 * EVENT BUS CONTRACT
 * ============================================================
 *
 * Constitutional References
 * ACAS Vol.2
 * AOBS Vol.3
 * AIAS Vol.4
 *
 * Austin's central nervous system.
 */

import { Event } from "./Event";

export interface EventBus {

    publish(event: Event): Promise<void>;

    subscribe(

        event: string,

        handler: (event: Event) => Promise<void>

    ): Promise<void>;

    unsubscribe(event: string): Promise<void>;

    clear(): Promise<void>;

}