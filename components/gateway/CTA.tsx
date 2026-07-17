export default function CTA() {
  return (
    <div className="relative z-10 mx-auto max-w-3xl text-center">

      <h2 className="text-4xl font-semibold tracking-tight text-white md:text-5xl">
        The gates are opening soon.
      </h2>

      <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-white/60">
        guavacheck is building the intelligence layer for the future of the
        built environment. Join the early access list and be among the first
        to experience what comes next.
      </p>

      <form
        className="mx-auto mt-10 flex max-w-xl flex-col gap-4 sm:flex-row"
        action="#"
      >
        <input
          type="email"
          placeholder="Enter your email address"
          className="
            h-14 flex-1 rounded-full border border-white/10
            bg-white/5 px-6 text-white
            placeholder:text-white/40
            outline-none
            backdrop-blur-md
            focus:border-white/30
          "
        />

        <button
          type="submit"
          className="
            h-14 rounded-full
            bg-[#8BC34A]
            px-8
            font-medium
            text-black
            transition
            hover:opacity-90
          "
        >
          Request Early Access
        </button>
      </form>

    </div>
  );
}