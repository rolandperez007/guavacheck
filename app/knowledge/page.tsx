import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Knowledge Center",
};

export default function KnowledgePage() {
  return (
    <main
      style={{
        maxWidth: 1100,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>Knowledge Center</h1>

      <p>
        Guides, AI insights and educational resources on property intelligence, valuation,
        investment and construction.
      </p>
    </main>
  );
}
