"use client";

import Shell from "./Shell";

export default function Desktop() {

    return (

        <main className="relative h-screen overflow-hidden">

            <div className="absolute inset-0 bg-black" />

            <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,#16312d,transparent_55%)] opacity-40" />

            <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,.03)_1px,transparent_1px)] bg-[size:60px_60px]" />

            <Shell />

        </main>

    );

}