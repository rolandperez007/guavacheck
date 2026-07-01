import countries from "@/knowledge/countries/countries.json";

import {
    CountryProfile,
    SupportLevel,
    CapabilitySet
} from "./types";

export class CountryRegistry {

    private static registry = new Map<string, CountryProfile>();

    static initialize(): void {

        if (this.registry.size > 0) return;

        countries.forEach((country: any) => {

            this.register({

                ...country,

                measurementSystem: country.measurement,

                supportLevel: SupportLevel.GLOBAL_AI,

                paymentProviders: [],

                capabilities: {

                    construction: "none",
                    valuation: "none",
                    mortgage: "none",
                    insurance: "none",
                    distress: "none",
                    buildingPassport: "none",
                    regulations: "none",
                    materials: "none",
                    climate: "none",
                    taxation: "none",
                    subscriptions: "standard",
                    payments: "standard"

                } satisfies CapabilitySet

            });

        });

    }

    static register(profile: CountryProfile): void {

        this.registry.set(profile.code.toUpperCase(), profile);

    }

    static byCode(code: string): CountryProfile | undefined {

        return this.registry.get(code.toUpperCase());

    }

    static all(): CountryProfile[] {

        return [...this.registry.values()];

    }

    static count(): number {

        return this.registry.size;

    }

}