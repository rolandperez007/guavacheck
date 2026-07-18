import Image from "next/image";

export default function HomePage() {
  return (
    <main className="relative min-h-screen w-screen overflow-hidden bg-black">

      <Image
        src="/images/launch/hero.png"
        alt="guavacheck — AI-powered global property intelligence platform"
        fill
        priority
        sizes="100vw"
        className="object-cover"
      />

      <section className="absolute inset-0 flex items-center justify-center">

        <div className="max-w-3xl px-6 text-center text-white">

          <h1 className="text-4xl font-semibold tracking-tight md:text-6xl">
            guavacheck
          </h1>

          <p className="mt-6 text-lg md:text-xl">
            AI-powered global property intelligence platform
            connecting property discovery, valuation,
            construction intelligence and investment analytics.
          </p>

          <p className="mt-4 text-sm opacity-80">
            Guava City is opening soon.
          </p>

        </div>

      </section>

    </main>
  );
}