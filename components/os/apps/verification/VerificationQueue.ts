"use client";

const queue = [

["Land Title","Pending"],

["Survey Plan","Processing"],

["Governor Consent","Queued"],

["Ownership","Verified"]

];

export default function VerificationQueue(){

return(

<section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

<h2 className="text-3xl font-semibold">

Verification Queue

</h2>

<div className="mt-8 space-y-4">

{

queue.map(([title,status])=>(

<div
key={title}
className="flex justify-between rounded-xl border border-neutral-800 p-5"
>

<div>{title}</div>

<div className="text-emerald-400">

{status}

</div>

</div>

))

}

</div>

</section>

)

}