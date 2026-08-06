/**
 * ============================================================
 * EVENT PUBLISHER
 * ============================================================
 *
 * Constitutional References
 * ACAS Vol.2
 * AOBS Vol.2
 */

import { Event } from "./Event";

export interface EventPublisher {
  publish(event: Event): Promise<void>;
}
