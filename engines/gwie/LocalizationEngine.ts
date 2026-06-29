import { CountryProfile } from "./types";

export class LocalizationEngine {

    constructor(private readonly profile: CountryProfile){}

    public language(){

        return this.profile.language;

    }

    public currency(){

        return this.profile.currency;

    }

    public timezone(){

        return this.profile.timezone;

    }

    public measurement(){

        return this.profile.measurementSystem;

    }

}