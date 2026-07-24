"use client";

const markets = [

["Lagos","+18%"],

["Abuja","+11%"],

["London","+6%"],

["Dubai","+15%"],

["Nairobi","+9%"]

];

export default function MarketPulse(){

return(

<section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

<h2 className="text-3xl font-semibold">

Market Pulse

</h2>

<p className="mt-2 text-neutral-400">

Live global activity

</p>

<div className="mt-8 space-y-4">

{

markets.map(([city,growth])=>(

<div
key={city}
className="flex items-center justify-between rounded-xl border border-neutral-800 p-4"
>

<span>{city}</span>

<span className="font-semibold text-emerald-400">

{growth}

</span>

</div>

))

}

</div>

</section>

)

}