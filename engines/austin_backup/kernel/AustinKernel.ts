import { AustinConfiguration } from "./AustinConfiguration";
import { AustinState } from "./AustinState";

/**
 * Austin Operating System Kernel
 */
export class AustinKernel {
  /**
   * Current kernel state.
   */
  private state: AustinState = AustinState.STOPPED;

  /**
   * Global Austin configuration.
   */
  private readonly configuration: AustinConfiguration;

  /**
   * Timestamp when Austin started.
   */
  private startedAt?: Date;

  /**
   * Number of processed requests.
   */
  private requestsProcessed = 0;

  /**
   * Current uptime.
   */
  private uptime = 0;

  constructor(configuration: AustinConfiguration) {
    this.configuration = configuration;
  }

  /**
   * Initializes Austin.
   */
  public async initialize(): Promise<void> {
    this.transition(AustinState.INITIALIZING);

    /**
     * Future
     *
     * Logger
     * Metrics
     * Registry
     * Plugins
     * Security
     * Knowledge
     */
  }

  /**
   * Starts Austin.
   */
  public async start(): Promise<void> {
    this.transition(AustinState.BOOTSTRAPPING);

    this.startedAt = new Date();

    this.transition(AustinState.READY);

    this.transition(AustinState.RUNNING);
  }

  /**
   * Executes one Austin request.
   */
  public async execute<TRequest, TResponse>(request: TRequest): Promise<TResponse> {
    if (this.state !== AustinState.RUNNING) {
      throw new Error(`Austin is currently ${this.state}.`);
    }

    this.requestsProcessed++;

    /**
     * Future pipeline
     *
     * Planner
     *
     * Context
     *
     * Knowledge
     *
     * Registry
     *
     * Simulation
     *
     * Prediction
     *
     * Decision
     *
     * Recommendation
     *
     * Explanation
     *
     * Execution
     */

    return {} as TResponse;
  }

  /**
   * Gracefully shuts Austin down.
   */
  public async shutdown(): Promise<void> {
    this.transition(AustinState.SHUTTING_DOWN);

    /**
     * Future
     *
     * Save memory
     * Flush logs
     * Finish workflows
     * Disconnect services
     */

    this.transition(AustinState.TERMINATED);
  }

  /**
   * Current kernel state.
   */
  public getState(): AustinState {
    return this.state;
  }

  /**
   * Austin uptime.
   */
  public getUptime(): number {
    if (!this.startedAt) {
      return 0;
    }

    return Date.now() - this.startedAt.getTime();
  }

  /**
   * Number of processed requests.
   */
  public getProcessedRequests(): number {
    return this.requestsProcessed;
  }

  /**
   * Kernel status.
   */
  public status() {
    return {
      state: this.state,

      version: this.configuration.version,

      environment: this.configuration.environment,

      startedAt: this.startedAt,

      uptime: this.getUptime(),

      requestsProcessed: this.requestsProcessed,
    };
  }

  /**
   * Changes kernel state.
   */
  private transition(state: AustinState): void {
    this.state = state;
  }
}
