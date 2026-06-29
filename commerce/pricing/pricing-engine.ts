/**
 * ===========================================================
 * GUAVA COMMERCE ENGINE
 * Pricing Engine
 *
 * Guava Networks Inc.
 * ===========================================================
 */

import { Plans } from "./plans";

import {

    PricingRequest,

    PricingResult

} from "./pricing-types";

import {

    calculateLocalizedPrice,

    getMultiplier

} from "./pricing-rules";

import {

    getPreferredProvider,

    getPreferredCurrency

} from "../providers/provider-selector";

export class PricingEngine {

    calculate(request: PricingRequest): PricingResult {

        const plan = Plans.find(

            p => p.id === request.plan

        );

        if (!plan) {

            throw new Error("Unknown plan.");

        }

        const localizedPrice = calculateLocalizedPrice(

            plan.basePriceUSD,

            request.country

        );

        return {

            success: true,

            originalPriceUSD: plan.basePriceUSD,

            localizedPrice,

            currency:

                request.currency ??

                getPreferredCurrency(request.country),

            country: request.country,

            provider:

                getPreferredProvider(request.country),

            multiplier:

                getMultiplier(request.country),

            savings:

                plan.basePriceUSD - localizedPrice

        };

    }

}

export const pricingEngine = new PricingEngine();