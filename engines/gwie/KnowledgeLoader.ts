import { CountryProfile } from "./types";

export class KnowledgeLoader {

    constructor(private readonly profile: CountryProfile) {}

    public load() {

        return {

            country: this.profile.code,

            profile: this.profile,

            climate: `knowledge/climates/${this.profile.code}`,

            regulations: `knowledge/regulations/${this.profile.code}`,

            materials: `knowledge/materials/${this.profile.code}`,

            economics: `knowledge/economics/${this.profile.code}`

        };

    }

}