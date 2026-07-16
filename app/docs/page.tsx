import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Developer Documentation",
};

export default function DocsPage() {
  return (
    <main
      style={{
        maxWidth: 1100,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>Developer Documentation</h1>

      <p>
        Documentation for APIs, SDKs and integrations
        powering guavacheck.
      </p>
    </main>
  );
}