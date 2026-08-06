import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Security",
};

export default function SecurityPage() {
  return (
    <main
      style={{
        maxWidth: 1000,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>Security</h1>

      <p>guavacheck is designed with security, responsible AI and privacy-first principles.</p>
    </main>
  );
}
