/**
 * ============================================================
 * EVENT METADATA
 * ============================================================
 *
 * Constitutional References
 * ACAS Vol.2
 * AOBS Vol.2
 */

export interface EventMetadata {
  environment: string;

  runtime: string;

  region: string;

  engine: string;

  version: string;

  hostname?: string;

  ipAddress?: string;

  traceId?: string;
}
