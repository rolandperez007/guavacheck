export interface PaymentProvider {

    id: string;

    name: string;

    regions: string[];

    currencies: string[];

}

export class PaymentRegistry {

    private static providers: PaymentProvider[] = [];

    static register(provider: PaymentProvider): void {

        this.providers.push(provider);

    }

    static all(): PaymentProvider[] {

        return this.providers;

    }

}