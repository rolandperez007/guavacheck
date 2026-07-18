export default function Footer() {
  return (
    <footer className="border-t border-white/10 bg-black/90">
      <div className="mx-auto flex h-12 items-center justify-center gap-4 text-xs text-white/50">
        <a href="/privacy" className="transition hover:text-white">
          Privacy
        </a>

        <span>•</span>

        <a href="/terms" className="transition hover:text-white">
          Terms
        </a>

        <span>•</span>

        <span>© {new Date().getFullYear()} Guava</span>
      </div>
    </footer>
  );
}