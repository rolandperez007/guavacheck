/**
 * RuntimeRegistry
 *
 * Maintains every runtime component.
 */

export class RuntimeRegistry {
  private readonly components = new Map<string, unknown>();

  public async initialize(): Promise<void> {
    this.components.clear();
  }

  public register(name: string, component: unknown): void {
    this.components.set(name, component);
  }

  public resolve<T>(name: string): T | undefined {
    return this.components.get(name) as T;
  }
}
