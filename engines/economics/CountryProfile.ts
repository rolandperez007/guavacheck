import countries from "@/knowledge/economics/countries.json";
import { CountryProfile } from "./EconomicTypes";

export function getCountryProfile(countryCode: string): CountryProfile | undefined {
  return (countries as CountryProfile[]).find(
    (country) => country.country === countryCode.toUpperCase(),
  );
}
