import { CountryProfile } from "../../types";

export class CountryRegistry {
  private static countries: Record<string, CountryProfile> = {};

  static register(profile: CountryProfile) {
    this.countries[profile.code] = profile;
  }

  static byCode(code: string): CountryProfile | undefined {
    return this.countries[code];
  }

  static getAll(): CountryProfile[] {
    return Object.values(this.countries);
  }
}
