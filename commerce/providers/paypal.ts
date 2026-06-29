/**
 * PayPal Adapter
 *
 * Guava Networks Inc.
 */

export class PaypalProvider {

    async createOrder(data: unknown) {

        console.log("PayPal checkout");

        return {

            success: true,

            provider: "paypal",

            order: null,

            data

        };

    }

}

export const paypalProvider =

new PaypalProvider();