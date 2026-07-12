export interface PPPInfo {
  country: string;
  index: number;
}

export class PPPRegistry {
  private static registry = new Map<string, PPPInfo>();

  /**
   * Initializes the PPP registry.
   * Placeholder until a global PPP dataset is loaded.
   */
  static initialize(): void {
    // Future:
    // Load PPP data from JSON/database/API.
    // Safe to call multiple times.
  }

  static register(item: PPPInfo): void {
    this.registry.set(item.country, item);
  }

  static byCountry(code: string): PPPInfo | undefined {
    return this.registry.get(code);
  }

  static all(): PPPInfo[] {
    return [...this.registry.values()];
  }

  static count(): number {
    return this.registry.size;
  }

  static clear(): void {
    this.registry.clear();
  }
}