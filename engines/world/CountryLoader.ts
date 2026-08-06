import countries from "@/knowledge/countries/countries.json";
import { CountryProfile } from "./types";

export class CountryLoader {
  static load(): CountryProfile[] {
    return countries as CountryProfile[];
  }

  static count(): number {
    return this.load().length;
  }
}
