import fs from "fs";
import path from "path";

interface CountrySeed {
    code: string;
    iso3: string;
    name: string;
    continent: string;
    capital: string;
    currency: string;
    language: string[];
    timezone: string[];
    measurement: "metric" | "imperial";
}

const registryPath = path.join(
    process.cwd(),
    "knowledge",
    "countries",
    "registry.json"
);

const outputPath = path.join(
    process.cwd(),
    "knowledge",
    "countries",
    "countries.json"
);

if (!fs.existsSync(registryPath)) {

    console.error("registry.json not found.");

    process.exit(1);

}

const registry: CountrySeed[] = JSON.parse(
    fs.readFileSync(registryPath, "utf8")
);

registry.sort((a, b) => a.name.localeCompare(b.name));

fs.writeFileSync(
    outputPath,
    JSON.stringify(registry, null, 2)
);

console.log(`GWIE Registry Built.`);
console.log(`Countries: ${registry.length}`);
console.log(`Output: ${outputPath}`);
const countries = registry.map(country => ({

    ...country,

    measurementSystem: country.measurement

}));

fs.writeFileSync(
    outputPath,
    JSON.stringify(countries, null, 2)
);

console.log("=================================");
console.log("GWIE Registry Built Successfully");
console.log("Countries:", countries.length);
console.log("=================================");