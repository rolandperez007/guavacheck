"use client";

export default function RevenueChart() {

return(

<section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

<h2 className="text-3xl font-semibold">

Revenue Streams

</h2>

<div className="mt-10 space-y-6">

<div>

<div className="flex justify-between">

<span>Subscriptions</span>

<span>$0</span>

</div>

<div className="mt-2 h-3 rounded-full bg-neutral-800">

<div className="h-3 w-0 rounded-full bg-emerald-500"/>

</div>

</div>

<div>

<div className="flex justify-between">

<span>AI Credits</span>

<span>$0</span>

</div>

<div className="mt-2 h-3 rounded-full bg-neutral-800">

<div className="h-3 w-0 rounded-full bg-sky-500"/>

</div>

</div>

</div>

<div>

<div className="flex justify-between">

<span>Marketplace</span>

<span>$0</span>

</div>

<div className="mt-2 h-3 rounded-full bg-neutral-800">

<div className="h-3 w-0 rounded-full bg-orange-500"/>

</div>

</div>

</div>

</div>

</section>

)

}