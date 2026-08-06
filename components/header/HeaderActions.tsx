import Link from "next/link";

export default function HeaderActions() {
  return (
    <div
      style={{
        display: "flex",
        gap: 18,
        alignItems: "center",
      }}
    >
      <Link href="/login">Sign In</Link>

      <Link
        href="/auth"
        style={{
          background: "#0f766e",
          color: "#fff",
          padding: "10px 18px",
          borderRadius: 8,
        }}
      >
        Get Started
      </Link>
    </div>
  );
}
