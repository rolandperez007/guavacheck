import Link from "next/link";

export default function SignupButton() {
  return (
    <Link
      href="/auth"
      style={{
        padding: "10px 18px",
        borderRadius: 10,
        background: "#0f766e",
        color: "#fff",
        textDecoration: "none",
      }}
    >
      Get Started
    </Link>
  );
}
