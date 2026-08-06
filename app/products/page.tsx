import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Products",
};

export default function ProductsPage() {
  return (
    <main
      style={{
        maxWidth: 1200,
        margin: "80px auto",
        padding: 24,
      }}
    >
      <h1>Products</h1>

      <p>Explore AI-powered products developed by Guava Networks Limited.</p>
    </main>
  );
}
