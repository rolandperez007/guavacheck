import Link from "next/link";

export default function LoginButton() {
  return (
    <Link
      href="/login"
      style={{
        textDecoration: "none",
      }}
    >
      Sign In
    </Link>
  );
}