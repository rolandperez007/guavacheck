import Link from "next/link";

export default function HeaderLogo() {
  return (
    <Link
      href="/"
      style={{
        fontSize: 26,
        fontWeight: 700,
        color: "#0f766e",
      }}
    >
      guavacheck
    </Link>
  );
}