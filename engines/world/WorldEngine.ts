import { CountryRegistry } from "./CountryRegistry";
import { CurrencyRegistry } from "./CurrencyRegistry";
import { PPPRegistry } from "./PPPRegistry";
import { PaymentRegistry } from "./PaymentRegistry";
import { RegionRegistry } from "./RegionRegistry";
import { MeasurementRegistry } from "./MeasurementRegistry";
import { TimezoneRegistry } from "./TimezoneRegistry";
import { LanguageRegistry } from "./LanguageRegistry";

export class WorldEngine {
  static initialize(): void {
    CountryRegistry.initialize();
    PPPRegistry.initialize();
    PaymentRegistry.initialize();
  }

  static ready(): boolean {
    return CountryRegistry.count() > 0;
  }

  static countries() {
    return CountryRegistry.all();
  }
}