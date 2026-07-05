export interface PPPInfo {
  country: string;
  index: number;
}

export class PPPRegistry {
  private static registry = new Map<string, PPPInfo>();

  static register(item: PPPInfo) {
    this.registry.set(item.country, item);
  }

  static byCountry(code: string) {
    return this.registry.get(code);
  }

  static all() {
    return [...this.registry.values()];
  }
}