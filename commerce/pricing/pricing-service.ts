/**
 * ===========================================================
 * GUAVA COMMERCE SERVICE
 *
 * Guava Networks Inc.
 * ===========================================================
 */

import {

    PricingRequest,

    PricingResult

} from "./pricing-types";

import {

    pricingEngine

} from "./pricing-engine";

class PricingService {

    async getPricing(

        request: PricingRequest

    ): Promise<PricingResult> {

        return pricingEngine.calculate(request);

    }

}

export const pricingService =

    new PricingService();