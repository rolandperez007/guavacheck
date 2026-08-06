import { CountryRegistry } from "./CountryRegistry";

export class CountryResolver {
  static resolve(country: string) {
    return CountryRegistry.byCode(country);
  }
}
