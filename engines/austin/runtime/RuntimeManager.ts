/**
 * RuntimeManager
 *
 * Controls the operational lifecycle of the Runtime.
 */

export class RuntimeManager {
  private running = false;

  public async initialize(): Promise<void> {
    this.running = false;
  }

  public async start(): Promise<void> {
    this.running = true;
  }

  public async shutdown(): Promise<void> {
    this.running = false;
  }

  public isRunning(): boolean {
    return this.running;
  }
}
