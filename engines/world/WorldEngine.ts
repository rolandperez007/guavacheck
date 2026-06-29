import { CountryRegistry } from "./CountryRegistry";
import { CapabilityEngine } from "./CapabilityEngine";
import { KnowledgeLoader } from "./KnowledgeLoader";
import { LocalizationEngine } from "./LocalizationEngine";
import { PaymentRouter } from "./PaymentRouter";
import { PPPEngine } from "./PPPEngine";
import { ContextBuilder } from "./ContextBuilder";

export class WorldEngine {

    static forCountry(code:string){

        const profile=CountryRegistry.byCode(code);

        if(!profile){

            throw new Error(`Unknown country: ${code}`);

        }

        return{

            profile,

            capabilities:new CapabilityEngine(profile),

            localization:new LocalizationEngine(profile),

            knowledge:new KnowledgeLoader(profile),

            payments:new PaymentRouter(profile),

            ppp:new PPPEngine(profile),

            context:new ContextBuilder(profile)

        };

    }

}