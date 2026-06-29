import { getCountryProfile } from "./CountryProfile";

export class EconomicsEngine {
  getCountryProfile(countryCode: string) {
    return getCountryProfile(countryCode);
  }
}

export const economicsEngine = new EconomicsEngine();