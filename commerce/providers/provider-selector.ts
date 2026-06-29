/**
 * ===========================================================
 * GUAVA COMMERCE ENGINE
 * Provider Selector
 *
 * Guava Networks Inc.
 * ===========================================================
 */
import { ProviderRegistry } from "./provider-registry";

export function getProvider(id: string) {

    return ProviderRegistry.find(

        p => p.id === id

    );

}

export function getSupportedProviders(country: string) {

    const code = country.toUpperCase();

    return ProviderRegistry.filter(

        provider =>

            provider.supportedCountries.includes("*") ||

            provider.supportedCountries.includes(code)

    );

}
export function getPreferredProvider(country: string): string {

    const code = country.toUpperCase();

    switch (code) {

        // Africa
        case "NG":
        case "GH":
            return "paystack";

        case "KE":
        case "UG":
        case "TZ":
        case "RW":
        case "ZM":
        case "ZW":
        case "ZA":
            return "flutterwave";

        // Default
        default:
            return "stripe";
    }
}

export function getPreferredCurrency(country: string): string {

    const code = country.toUpperCase();

    switch (code) {

        case "NG":
            return "NGN";

        case "GH":
            return "GHS";

        case "KE":
            return "KES";

        case "ZA":
            return "ZAR";

        case "JP":
            return "JPY";

        case "KR":
            return "KRW";

        case "AU":
            return "AUD";

        case "GB":
            return "GBP";

        case "BR":
            return "BRL";

        case "CA":
            return "CAD";

        case "DE":
        case "FR":
        case "IT":
        case "ES":
        case "NL":
        case "PT":
            return "EUR";

        default:
            return "USD";
    }
}