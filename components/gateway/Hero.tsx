"use client";

import Image from "next/image";
import Link from "next/link";

export default function Hero() {
  return (
    <section className="relative h-[100svh] min-h-[700px] w-full overflow-hidden bg-black">
      {/* Background */}
      <div className="absolute inset-0 scale-110 md:scale-100 transition-transform duration-700">
        <Image
          src="/images/launch/hero.png"
          alt="Guava City"
          fill
          priority
          quality={100}
          sizes="100vw"
          className="object-cover object-[55%_center] md:object-center"
        />
      </div>

      {/* Dark Overlay */}
      <div className="absolute inset-0 bg-black/40" />

      {/* Hero Content */}
      <div className="relative z-10 flex h-full items-end justify-center pb-24 md:items-center md:pb-0">
        <div className="mx-auto max-w-4xl px-6 text-center">
          <h1 className="text-4xl font-semibold tracking-tight text-white md:text-7xl">
            Welcome to
            <br />
            Guava City
          </h1>

          <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-white/80 md:text-xl">
            The future home of global property intelligence, AI-powered real estate, construction
            technology, and smarter investment decisions.
          </p>

          <div className="mt-10">
            <Link
              href="#early-access"
              className="inline-flex rounded-full border border-white/20 bg-white/10 px-8 py-4 text-white backdrop-blur transition hover:bg-white/20"
            >
              Request Early Access
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
