/**
 * ==============================================================
 * guavacheck
 * Austin Construction Intelligence Platform
 * --------------------------------------------------------------
 * Module:
 * AustinConstants
 *
 * Responsibility:
 * Defines immutable system-wide constants used throughout the
 * Austin Operating System.
 *
 * Design Goals:
 * - Eliminate magic numbers
 * - Promote consistency
 * - Centralize platform defaults
 * - Improve maintainability
 *
 * Dependencies:
 * None
 *
 * Thread Safety:
 * Immutable
 *
 * Future Extensions:
 * - Distributed runtime limits
 * - Cluster configuration constants
 * - AI execution defaults
 * ==============================================================
 */

export class AustinConstants {

    /**
     * Platform
     */
    public static readonly PLATFORM_NAME = "guavacheck";

    public static readonly PLATFORM_CODE = "AUSTIN";

    /**
     * Versioning
     */
    public static readonly API_VERSION = "1.0";

    public static readonly BUILD_VERSION = "1.0.0";

    /**
     * Pipeline
     */
    public static readonly MAX_PIPELINE_STAGES = 64;

    public static readonly DEFAULT_PIPELINE_TIMEOUT_MS = 30000;

    /**
     * Execution
     */
    public static readonly MAX_RETRIES = 3;

    public static readonly MAX_CONCURRENT_REQUESTS = 100;

    /**
     * AI
     */
    public static readonly MIN_CONFIDENCE_SCORE = 0.75;

    public static readonly DEFAULT_CONFIDENCE_SCORE = 0.90;

    /**
     * Knowledge
     */
    public static readonly MAX_KNOWLEDGE_RESULTS = 50;

    /**
     * Memory
     */
    public static readonly MAX_MEMORY_RESULTS = 100;

    /**
     * Runtime
     */
    public static readonly HEARTBEAT_INTERVAL_MS = 5000;

    public static readonly HEALTH_CHECK_INTERVAL_MS = 30000;

    /**
     * Logging
     */
    public static readonly MAX_LOG_BATCH = 500;

    /**
     * Plugins
     */
    public static readonly MAX_PLUGINS = 500;

    /**
     * Registry
     */
    public static readonly MAX_REGISTERED_ENGINES = 1000;

    /**
     * Identity
     */
    public static readonly UUID_LENGTH = 36;

    /**
     * Security
     */
    public static readonly MAX_FAILED_ATTEMPTS = 5;

    /**
     * Time
     */
    public static readonly MILLISECONDS_PER_SECOND = 1000;

    public static readonly SECONDS_PER_MINUTE = 60;

    public static readonly MINUTES_PER_HOUR = 60;

    public static readonly HOURS_PER_DAY = 24;

}