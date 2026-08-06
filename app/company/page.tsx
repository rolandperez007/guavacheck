import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Company",
  description: "Corporate information about Guava Networks Limited, the company behind guavacheck.",
};

export default function CompanyPage() {
  return (
    <main
      style={{
        maxWidth: 1100,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>Guava Networks Limited</h1>

      <p>
        Guava Networks Limited is a technology company building AI-powered software for global
        property intelligence.
      </p>

      <p>
        Its flagship platform, <strong>guavacheck</strong>, combines valuation, construction
        intelligence, investment analytics, verification and multilingual AI into a unified
        platform.
      </p>
    </main>
  );
}
