"use client";

const materials=[

["Cement","+2%"],

["Steel","-4%"],

["Granite","+1%"],

["Blocks","+3%"],

["Labour","+6%"]

];

export default function ConstructionMonitor(){

return(

<section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

<h2 className="text-3xl font-semibold">

Construction Monitor

</h2>

<div className="mt-8 space-y-4">

{

materials.map(([name,change])=>(

<div
key={name}
className="flex justify-between rounded-xl border border-neutral-800 p-5"
>

{name}

<span className="font-semibold">

{change}

</span>

</div>

))

}

</div>

</section>

)

}