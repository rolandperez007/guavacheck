import { Verification } from "./Verification";

export class VerificationEngine {
  private static registry = new Map<string, Verification>();

  static register(record: Verification): void {
    this.registry.set(record.id, record);
  }

  static find(id: string): Verification | undefined {
    return this.registry.get(id);
  }

  static all(): Verification[] {
    return [...this.registry.values()];
  }
}
