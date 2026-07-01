export interface PPPProfile {

    country: string;

    multiplier: number;

    updated: string;

}

export class PPPRegistry {

    private static profiles = new Map<string, PPPProfile>();

    static register(profile: PPPProfile): void {

        this.profiles.set(profile.country, profile);

    }

    static byCountry(country: string): PPPProfile | undefined {

        return this.profiles.get(country);

    }

}