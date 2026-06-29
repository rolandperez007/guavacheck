/**
 * Flutterwave Adapter
 *
 * Guava Networks Inc.
 */

export class FlutterwaveProvider {

    async initializeTransaction(data: unknown) {

        console.log("Flutterwave checkout");

        return {

            success: true,

            provider: "flutterwave",

            transaction: null,

            data

        };

    }

}

export const flutterwaveProvider =

new FlutterwaveProvider();