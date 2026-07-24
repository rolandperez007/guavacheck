"use client";

import AustinOrb from "@/components/icons/AustinOrb";

export default function HeroMap(){

return(

<div className="relative h-full min-h-[720px] overflow-hidden rounded-3xl border border-neutral-800 bg-gradient-to-br from-neutral-950 via-neutral-900 to-black">

<div className="absolute inset-0 opacity-10">

<div className="h-full w-full bg-[radial-gradient(circle_at_center,#10b981_1px,transparent_1px)] bg-[length:28px_28px]" />

</div>

<div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">

<AustinOrb

size={150}

state="processing"

/>

</div>

<div className="absolute left-10 top-10">

<h1 className="text-4xl font-bold text-white">

Mission Control

</h1>

<p className="mt-3 max-w-lg text-neutral-400">

Global property intelligence operating system.

</p>

</div>

</div>

);

}