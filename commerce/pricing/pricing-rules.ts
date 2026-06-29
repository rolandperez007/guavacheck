/**
 * ===========================================================
 * GUAVA COMMERCE ENGINE
 * Pricing Rules
 *
 * Guava Networks Inc.
 * ===========================================================
 */

import { PurchasingPower } from "./purchasing-power";
import { Tier1, Tier2, Tier3 } from "./country-tiers";

export function getCountryTier(country: string): number {

    const code = country.toUpperCase();

    if (Tier1.includes(code)) return 1;

    if (Tier2.includes(code)) return 2;

    if (Tier3.includes(code)) return 3;

    return 1;
}

export function getMultiplier(country: string): number {

    const tier = getCountryTier(country);

    switch (tier) {

        case 1:
            return PurchasingPower.tier1;

        case 2:
            return PurchasingPower.tier2;

        case 3:
            return PurchasingPower.tier3;

        default:
            return 1;
    }
}

export function calculateLocalizedPrice(

    basePrice: number,

    country: string

): number {

    const multiplier = getMultiplier(country);

    return Math.round(basePrice * multiplier);

}