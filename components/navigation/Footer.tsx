import Link from "next/link";

export default function Footer() {
  return (
    <footer
      style={{
        marginTop: 100,
        borderTop: "1px solid #ddd",
        padding: 40,
      }}
    >
      <p>
        © {new Date().getFullYear()} Guava Networks Limited
      </p>

      <div
        style={{
          display: "flex",
          gap: 24,
          marginTop: 20,
        }}
      >
        <Link href="/privacy">Privacy</Link>

        <Link href="/security">Security</Link>

        <Link href="/terms">Terms</Link>

        <Link href="/company">Company</Link>
      </div>
    </footer>
  );
}