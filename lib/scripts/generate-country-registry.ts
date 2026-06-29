import fs from "fs";
import path from "path";

const ROOT = process.cwd();

const OUTPUT = path.join(
    ROOT,
    "knowledge",
    "countries"
);

const PROFILE_DIR = path.join(
    OUTPUT,
    "profiles"
);

fs.mkdirSync(PROFILE_DIR, { recursive: true });

const countries = [

{
code:"NG",
iso3:"NGA",
name:"Nigeria",
continent:"Africa",
capital:"Abuja",
currency:"NGN",
languages:["English"],
timezone:["Africa/Lagos"],
measurementSystem:"metric"
},

{
code:"US",
iso3:"USA",
name:"United States",
continent:"North America",
capital:"Washington DC",
currency:"USD",
languages:["English"],
timezone:["America/New_York"],
measurementSystem:"imperial"
},

{
code:"GB",
iso3:"GBR",
name:"United Kingdom",
continent:"Europe",
capital:"London",
currency:"GBP",
languages:["English"],
timezone:["Europe/London"],
measurementSystem:"metric"
},

{
code:"ZA",
iso3:"ZAF",
name:"South Africa",
continent:"Africa",
capital:"Pretoria",
currency:"ZAR",
languages:["English"],
timezone:["Africa/Johannesburg"],
measurementSystem:"metric"
},

{
code:"BR",
iso3:"BRA",
name:"Brazil",
continent:"South America",
capital:"Brasilia",
currency:"BRL",
languages:["Portuguese"],
timezone:["America/Sao_Paulo"],
measurementSystem:"metric"
},

{
code:"IN",
iso3:"IND",
name:"India",
continent:"Asia",
capital:"New Delhi",
currency:"INR",
languages:["Hindi","English"],
timezone:["Asia/Kolkata"],
measurementSystem:"metric"
},

{
code:"JP",
iso3:"JPN",
name:"Japan",
continent:"Asia",
capital:"Tokyo",
currency:"JPY",
languages:["Japanese"],
timezone:["Asia/Tokyo"],
measurementSystem:"metric"
},

{
code:"KR",
iso3:"KOR",
name:"South Korea",
continent:"Asia",
capital:"Seoul",
currency:"KRW",
languages:["Korean"],
timezone:["Asia/Seoul"],
measurementSystem:"metric"
},

{
code:"AU",
iso3:"AUS",
name:"Australia",
continent:"Oceania",
capital:"Canberra",
currency:"AUD",
languages:["English"],
timezone:["Australia/Sydney"],
measurementSystem:"metric"
},

{
code:"CA",
iso3:"CAN",
name:"Canada",
continent:"North America",
capital:"Ottawa",
currency:"CAD",
languages:["English","French"],
timezone:["America/Toronto"],
measurementSystem:"metric"
}

];

fs.writeFileSync(

path.join(OUTPUT,"countries.json"),

JSON.stringify(countries,null,2)

);

for(const country of countries){

const profile={

...country,

supportLevel:1,

capabilities:{

construction:false,

valuation:false,

mortgage:false,

insurance:false,

distress:false,

buildingPassport:false,

regulations:false,

materials:false,

climate:false,

taxation:false,

subscriptions:true,

payments:true

},

paymentProviders:[]

};

fs.writeFileSync(

path.join(PROFILE_DIR,`${country.code}.json`),

JSON.stringify(profile,null,2)

);

}

console.log("GWIE Registry Generated.");