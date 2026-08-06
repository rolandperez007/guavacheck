import { CountryProfile } from "./types";

export class PPPEngine {
  constructor(private readonly profile: CountryProfile) {}

  public multiplier(): number {
    return 1;
  }

  public adjust(priceUSD: number): number {
    return Number((priceUSD * this.multiplier()).toFixed(2));
  }
}
