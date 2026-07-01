import { CountryRegistry } from "./CountryRegistry";

export class CountryLoader {

    static initialize(): void {

        CountryRegistry.initialize();

        console.log(
            `GWIE loaded ${CountryRegistry.count()} countries.`
        );

    }

}