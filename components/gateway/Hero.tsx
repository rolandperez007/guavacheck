"use client";

import Image from "next/image";
import Link from "next/link";

export default function Hero() {
  return (
    <section className="relative min-h-screen w-full overflow-hidden bg-black">
      {/* Background Image */}

      <Image
        src="/images/launch/hero.png"
        alt="Guava City"
        fill
        priority
        quality={100}
        sizes="100vw"
        className="object-cover object-center"
      />

      {/* Readability Overlay */}

      <div className="absolute inset-0 bg-black/35" />

      <div
        className="
          absolute
          inset-0
          bg-gradient-to-r
          from-black/80
          via-black/45
          to-transparent
        "
      />

      <div
        className="
          absolute
          inset-x-0
          bottom-0
          h-60
          bg-gradient-to-t
          from-[#08120E]
          to-transparent
        "
      />

      {/* Navigation */}

      <header className="absolute inset-x-0 top-0 z-30">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-8">
          <Link href="/" className="text-2xl font-semibold tracking-tight text-white">
            guavacheck
          </Link>

          <div
            className="
              rounded-full
              border
              border-white/20
              bg-white/10
              px-5
              py-2
              backdrop-blur-md
            "
          >
            <span className="text-xs uppercase tracking-[0.25em] text-white">
              Powered by Austin
            </span>
          </div>
        </div>
      </header>

      {/* Hero */}

      <div className="relative z-20 flex min-h-screen items-center">
        <div className="mx-auto w-full max-w-7xl px-6">
          <div className="max-w-3xl">
            <div
              className="
                inline-flex
                items-center
                rounded-full
                border
                border-[#72BF44]/40
                bg-[#72BF44]/10
                px-5
                py-2
                backdrop-blur-md
              "
            >
              <span className="text-xs uppercase tracking-[0.28em] text-[#C9F8B2]">
                AI PROPERTY INTELLIGENCE
              </span>
            </div>

            <h1
              className="
                mt-10
                text-5xl
                font-semibold
                leading-[0.95]
                tracking-tight
                text-white

                md:text-7xl
                xl:text-8xl
              "
            >
              Building the
              <br />
              Future of the
              <br />
              <span className="text-[#72BF44]">Built Environment</span>
            </h1>

            <p
              className="
                mt-8
                max-w-xl
                text-lg
                leading-8
                text-white/80

                md:text-xl
              "
            >
              AI-powered property intelligence connecting verification, construction, finance,
              valuation and global investment into one intelligent platform.
            </p>

            <div className="mt-10">
              <h2 className="text-2xl font-semibold text-white">The Gates Open Soon.</h2>

              <p className="mt-3 text-white/70">Join the first builders shaping tomorrow.</p>
            </div>

            <div className="mt-12 flex flex-col gap-5 sm:flex-row">
              <a
                href="#early-access"
                className="
                  inline-flex
                  items-center
                  justify-center
                  rounded-full
                  bg-[#72BF44]
                  px-8
                  py-4
                  text-lg
                  font-semibold
                  text-black
                  transition
                  hover:scale-105
                "
              >
                Request Early Access
              </a>

              <a
                href="#vision"
                className="
    inline-flex
    items-center
    justify-center
    rounded-full
    border
    border-white/20
    bg-white/10
    px-8
    py-4
    text-lg
    text-white
    backdrop-blur-md
  "
              >
                Discover the Vision
              </a>
            </div>

            {/* Platform Features */}

            <div className="mt-14 flex flex-wrap gap-3">
              {[
                "AI First",
                "Global",
                "Property Verification",
                "Construction",
                "Investment",
                "Finance",
                "Multi-Currency",
                "Multi-Language",
              ].map((item) => (
                <span
                  key={item}
                  className="
                    rounded-full
                    border
                    border-white/20
                    bg-white/10
                    px-4
                    py-2
                    text-sm
                    text-white/80
                    backdrop-blur-md
                  "
                >
                  {item}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Scroll Indicator */}

      <div
        className="
          absolute
          bottom-8
          left-1/2
          -translate-x-1/2
          animate-bounce
        "
      >
        <div
          className="
            flex
            h-12
            w-7
            justify-center
            rounded-full
            border
            border-white/30
          "
        >
          <div
            className="
              mt-2
              h-2
              w-2
              rounded-full
              bg-[#72BF44]
            "
          />
        </div>
      </div>
    </section>
  );
}
