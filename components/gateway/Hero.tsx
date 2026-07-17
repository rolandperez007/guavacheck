"use client";

export default function Hero() {
  return (
    <section className="relative flex min-h-screen items-center">
      <div className="mx-auto flex w-full max-w-7xl px-6 pt-24 pb-16 lg:px-10">
        <div className="max-w-3xl">

          {/* Badge */}
          <div className="mb-8 inline-flex items-center rounded-full border border-[#72BF44]/30 bg-white/5 px-5 py-2 backdrop-blur-xl">
            <span className="mr-2 h-2 w-2 rounded-full bg-[#72BF44]" />
            <span className="text-sm font-medium tracking-wide text-white/80">
              Powered by Austin
            </span>
          </div>

          {/* Headline */}
          <h1 className="text-5xl font-bold leading-[1.05] tracking-tight text-white md:text-7xl xl:text-8xl">
            Building the
            <br />
            Future of the
            <br />
            <span className="text-[#72BF44]">
              Built Environment
            </span>
          </h1>

          {/* Description */}
          <p className="mt-8 max-w-2xl text-lg leading-8 text-white/75 md:text-xl">
            A next-generation intelligence platform bringing together
            property, construction, verification, finance, planning,
            and AI into one seamless ecosystem.
          </p>

          {/* Status */}
          <p className="mt-6 text-lg font-medium text-[#72BF44]">
            The gates open soon.
          </p>

          {/* CTA */}
          <div className="mt-12 flex flex-col gap-4 sm:flex-row">

            <a
              href="#early-access"
              className="inline-flex items-center justify-center rounded-full bg-[#72BF44] px-8 py-4 text-base font-semibold text-black transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_0_35px_rgba(114,191,68,.55)]"
            >
              Request Early Access
            </a>

            <a
              href="#vision"
              className="inline-flex items-center justify-center rounded-full border border-white/20 bg-white/5 px-8 py-4 text-base font-medium text-white backdrop-blur-xl transition-all duration-300 hover:border-white/40 hover:bg-white/10"
            >
              Discover the Vision
            </a>

          </div>

          {/* Bottom note */}
          <div className="mt-16 flex items-center gap-3 text-sm text-white/60">
            <span className="h-2 w-2 rounded-full bg-[#72BF44]" />
            Global • AI-First • Multi-Currency • Multi-Language
          </div>

        </div>
      </div>
    </section>
  );
}