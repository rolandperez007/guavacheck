import { CountryProfile } from "./types";

export class ContextBuilder {
  constructor(private readonly profile: CountryProfile) {}

  public build() {
    return {
      country: this.profile,

      localization: {
        language: this.profile.language,

        currency: this.profile.currency,

        timezone: this.profile.timezone,
      },
    };
  }
}
