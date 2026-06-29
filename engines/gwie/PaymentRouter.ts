import { CountryProfile } from "./types";

export class PaymentRouter {

    constructor(private readonly profile: CountryProfile) {}

    public providers() {

        return this.profile.paymentProviders;

    }

    public primary() {

        return this.profile.paymentProviders.find(p => p.supported);

    }

    public supports(id: string) {

        return this.profile.paymentProviders.some(

            p => p.id === id && p.supported

        );

    }

}