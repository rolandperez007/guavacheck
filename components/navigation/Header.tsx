import Link from "next/link";

import SearchBar from "@/components/search/SearchBar";

import LoginButton from "@/components/auth/LoginButton";

import SignupButton from "@/components/auth/SignupButton";

export default function Header() {
  return (
    <header
      style={{
        borderBottom: "1px solid #e5e7eb",
        padding: "16px 40px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        gap: 24,
      }}
    >
      <Link
        href="/"
        style={{
          fontSize: 26,
          fontWeight: 700,
          textDecoration: "none",
          color: "#111827",
        }}
      >
        guavacheck
      </Link>

      <SearchBar />

      <nav
        style={{
          display: "flex",
          gap: 18,
          alignItems: "center",
        }}
      >
        <Link href="/products">Products</Link>

        <Link href="/knowledge">Knowledge</Link>

        <Link href="/about">About</Link>

        <Link href="/contact">Contact</Link>

        <LoginButton />

        <SignupButton />
      </nav>
    </header>
  );
}