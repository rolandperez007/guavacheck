import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Privacy Policy",
};

export default function PrivacyPage() {
  return (
    <main
      style={{
        maxWidth: 1000,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>Privacy Policy</h1>

      <p>Your privacy and data protection are fundamental to Guava Networks Limited.</p>
    </main>
  );
}
