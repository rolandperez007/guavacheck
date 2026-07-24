"use client";

const notifications = [

"Welcome to guavacheck.",

"No active property verifications.",

"Austin AI is online.",

"Your dashboard is ready.",

"Market intelligence initialized."

];

export default function NotificationCenter(){

return(

<section className="rounded-3xl border border-neutral-800 bg-neutral-950 p-8">

<h2 className="text-3xl font-semibold">

Notifications

</h2>

<div className="mt-8 space-y-4">

{

notifications.map((item,index)=>(

<div

key={index}

className="rounded-xl border border-neutral-800 p-4 hover:bg-neutral-900 transition"

>

{item}

</div>

))

}

</div>

</section>

)

}