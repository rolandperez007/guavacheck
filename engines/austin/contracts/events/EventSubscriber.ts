/**
 * ============================================================
 * EVENT SUBSCRIBER
 * ============================================================
 *
 * Constitutional References
 * ACAS Vol.2
 */

import { Event } from "./Event";

export interface EventSubscriber {
  subscribe(
    event: string,

    handler: (event: Event) => Promise<void>,
  ): Promise<void>;

  unsubscribe(event: string): Promise<void>;
}
