import fs from "fs";
import path from "path";

const ROOT = process.cwd();

const KNOWLEDGE = path.join(ROOT, "knowledge", "countries");

const PROFILES = path.join(KNOWLEDGE, "profiles");

fs.mkdirSync(PROFILES, { recursive: true });

const registry = JSON.parse(

fs.readFileSync(

path.join(KNOWLEDGE, "registry.json"),

"utf8"

)

);

fs.writeFileSync(

path.join(KNOWLEDGE, "countries.json"),

JSON.stringify(registry, null, 2)

);

for (const country of registry) {

const profile = {

...country,

supportLevel: 1,

pppMultiplier: 1,

paymentProviders: [],

capabilities: {

construction: false,

valuation: false,

mortgage: false,

insurance: false,

distress: false,

buildingPassport: false,

regulations: false,

materials: false,

climate: false,

subscriptions: true,

payments: true

}

};

fs.writeFileSync(

path.join(PROFILES, `${country.code}.json`),

JSON.stringify(profile, null, 2)

);

}

console.log(

`Generated ${registry.length} country profiles.`

);