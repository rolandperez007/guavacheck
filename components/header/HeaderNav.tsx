import Link from "next/link";

export default function HeaderNav() {
  return (
    <nav
      style={{
        display: "flex",
        gap: 28,
      }}
    >
      <Link href="/products">Products</Link>

      <Link href="/knowledge">Knowledge</Link>

      <Link href="/docs">Docs</Link>

      <Link href="/company">Company</Link>

      <Link href="/contact">Contact</Link>
    </nav>
  );
}
