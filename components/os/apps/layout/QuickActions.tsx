"use client";

const actions = [

"Verify Property",

"AI Valuation",

"Generate Report",

"Mortgage Calculator",

"Upload Document",

"Construction Estimate"

];

export default function QuickActions(){

return(

<section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

<h2 className="text-2xl font-semibold">

Quick Actions

</h2>

<div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">

{

actions.map((action)=>(

<button

key={action}

className="rounded-2xl border border-neutral-800 p-6 text-left hover:border-emerald-500 hover:bg-neutral-900 transition"

>

{action}

</button>

))

}

</div>

</section>

)

}