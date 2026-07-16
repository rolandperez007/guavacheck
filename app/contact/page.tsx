import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact",
};

export default function ContactPage() {
  return (
    <main
      style={{
        maxWidth: 900,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>Contact</h1>

      <p>
        Contact Guava Networks Limited regarding guavacheck,
        partnerships, enterprise services and support.
      </p>
    </main>
  );
}