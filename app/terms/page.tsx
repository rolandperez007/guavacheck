import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Terms of Service",
};

export default function TermsPage() {
  return (
    <main
      style={{
        maxWidth: 1000,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>Terms of Service</h1>

      <p>Terms governing the use of guavacheck and services provided by Guava Networks Limited.</p>
    </main>
  );
}
