"use client";

const missions=[

"Verify 12 Ikoyi properties",

"Analyse Lagos luxury market",

"Generate investor report",

"Prepare valuation",

"Monitor exchange rates",

"Scan new planning approvals",

];

export default function MissionQueue(){

return(

<div className="rounded-2xl border border-neutral-800 bg-neutral-950 p-6">

<h2 className="mb-6 text-lg font-semibold text-white">

Austin Mission Queue

</h2>

<div className="space-y-3">

{missions.map((mission,index)=>(

<div

key={index}

className="rounded-xl border border-neutral-800 bg-black p-4"

>

{mission}

</div>

))}

</div>

</div>

);

}