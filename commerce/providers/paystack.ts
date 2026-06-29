/**
 * Paystack Adapter
 *
 * Guava Networks Inc.
 */

export class PaystackProvider {

    async initializeTransaction(data: unknown) {

        console.log("Paystack checkout");

        return {

            success: true,

            provider: "paystack",

            transaction: null,

            data

        };

    }

}

export const paystackProvider =

new PaystackProvider();