export default function Footer() {
  return (
    <footer className="relative z-10 border-t border-white/10 bg-black">
      <div className="mx-auto flex max-w-7xl flex-col items-center justify-between gap-6 px-6 py-10 text-center text-sm text-white/50 lg:flex-row lg:px-10">
        <div>
          <p className="font-medium text-white/80">
            guavacheck
          </p>

          <p className="mt-1">
            Building the Future of the Built Environment.
          </p>
        </div>

        <div className="flex items-center gap-6">
          <a
            href="/privacy"
            className="transition hover:text-white"
          >
            Privacy
          </a>

          <a
            href="/terms"
            className="transition hover:text-white"
          >
            Terms
          </a>

          <a
            href="#early-access"
            className="transition hover:text-white"
          >
            Early Access
          </a>
        </div>

        <div>
          © {new Date().getFullYear()} Guava Networks Limited
        </div>
      </div>
    </footer>
  );
}