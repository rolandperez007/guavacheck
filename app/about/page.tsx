import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About",
  description: "Learn about guavacheck and Guava Networks Limited.",
};

export default function AboutPage() {
  return (
    <main
      style={{
        maxWidth: 1100,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>About guavacheck</h1>

      <p>
        guavacheck is the flagship AI-powered global property intelligence platform developed and
        operated by Guava Networks Limited.
      </p>

      <p>
        The platform combines property intelligence, valuation, construction intelligence,
        investment analytics, verification, multilingual support and AI into one unified ecosystem.
      </p>
    </main>
  );
}
