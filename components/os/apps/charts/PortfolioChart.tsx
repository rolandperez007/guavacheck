"use client";

export default function PortfolioChart() {

    return(

<section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

<h2 className="text-3xl font-semibold">

Portfolio Growth

</h2>

<div className="mt-10 h-80 rounded-2xl border border-neutral-800 flex items-end gap-4 p-8">

{

[20,40,35,60,55,75,88].map((height,index)=>(

<div

key={index}

style={{

height:`${height}%`

}}

className="flex-1 rounded-t-xl bg-emerald-500"

>

</div>

))

}

</div>

</section>

)

}