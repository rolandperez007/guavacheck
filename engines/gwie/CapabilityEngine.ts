import { CountryProfile } from "./types";

export class CapabilityEngine {
  constructor(private readonly profile: CountryProfile) {}

  public has(capability: keyof CountryProfile["capabilities"]): boolean {
    return Boolean(this.profile.capabilities[capability]);
  }

  public all() {
    return this.profile.capabilities;
  }

  public enabled(): string[] {
    return Object.entries(this.profile.capabilities)

      .filter(([_, value]) => value)

      .map(([key]) => key);
  }
}
