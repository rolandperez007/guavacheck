/**
 * ==============================================================
 * guavacheck
 * Austin Construction Intelligence Platform
 * --------------------------------------------------------------
 * Module:
 * AustinClock
 *
 * Responsibility:
 * Centralized system clock for the Austin Operating System.
 *
 * All kernel services must obtain time through AustinClock
 * instead of directly calling Date.now() or new Date().
 *
 * Design Goals:
 * • Single source of time
 * • Consistent timestamps
 * • Testability
 * • Future distributed synchronization
 *
 * Dependencies:
 * None
 *
 * Thread Safety:
 * Stateless
 *
 * Future Extensions:
 * • NTP synchronization
 * • Cluster time
 * • Virtual simulation clocks
 * • Time acceleration
 * ==============================================================
 */

export class AustinClock {
  /**
   * Current timestamp in milliseconds.
   */
  public static now(): number {
    return Date.now();
  }

  /**
   * Current Date object.
   */
  public static date(): Date {
    return new Date();
  }

  /**
   * Current UTC ISO-8601 timestamp.
   */
  public static utc(): string {
    return new Date().toISOString();
  }

  /**
   * Unix timestamp (seconds).
   */
  public static unix(): number {
    return Math.floor(Date.now() / 1000);
  }

  /**
   * Measures elapsed milliseconds.
   */
  public static elapsed(startTime: number): number {
    return this.now() - startTime;
  }

  /**
   * High precision timer.
   *
   * Uses performance.now() when available.
   */
  public static highResolution(): number {
    if (typeof performance !== "undefined" && typeof performance.now === "function") {
      return performance.now();
    }

    return Date.now();
  }

  /**
   * Sleep helper.
   */
  public static sleep(milliseconds: number): Promise<void> {
    return new Promise((resolve) => {
      setTimeout(resolve, milliseconds);
    });
  }

  /**
   * Generates an ISO timestamp.
   */
  public static timestamp(): string {
    return this.utc();
  }

  /**
   * Measures execution time of an async task.
   */
  public static async measure<T>(operation: () => Promise<T>): Promise<{
    result: T;
    duration: number;
  }> {
    const start = this.highResolution();

    const result = await operation();

    const end = this.highResolution();

    return {
      result,

      duration: end - start,
    };
  }
}
