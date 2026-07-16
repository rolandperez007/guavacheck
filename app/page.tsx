import Link from "next/link";

const districts = [
  {
    title: "Residential District",
    description:
      "Discover verified residential properties, neighborhoods, pricing insights, and AI-powered recommendations.",
    href: "/properties",
  },
  {
    title: "Construction District",
    description:
      "Estimate building costs, generate BOQs, and plan construction projects with AI assistance.",
    href: "/products/construction-cost-estimator",
  },
  {
    title: "Investor District",
    description:
      "Access market intelligence, investment analytics, ROI tools, and institutional-grade insights.",
    href: "/investor",
  },
  {
    title: "Community District",
    description:
      "Connect with buyers, sellers, developers, professionals, and trusted service providers.",
    href: "/community",
  },
  {
    title: "Austin AI District",
    description:
      "Work alongside Austin, your AI property intelligence assistant for research, valuation, and decision support.",
    href: "/austin",
  },
];

const engines = [
  "Property Intelligence",
  "Property Valuation",
  "AI Architect",
  "Construction Cost Estimator",
  "Mortgage Calculator",
  "Market Intelligence",
  "Geo Engine",
  "Currency Engine",
];

export default function Home() {
  return (
    <main>
      {/* Hero */}
      <section
        style={{
          padding: "96px 24px",
          maxWidth: "1200px",
          margin: "0 auto",
        }}
      >
        <p
          style={{
            color: "#16a34a",
            fontWeight: 600,
            marginBottom: 12,
            letterSpacing: "0.08em",
            textTransform: "uppercase",
          }}
        >
          Global Property Intelligence Engine
        </p>

        <h1
          style={{
            fontSize: "3rem",
            lineHeight: 1.1,
            marginBottom: 24,
          }}
        >
          Welcome to guavacheck
        </h1>

        <p
          style={{
            maxWidth: "760px",
            fontSize: "1.2rem",
            lineHeight: 1.8,
            color: "#555",
          }}
        >
          guavacheck brings together property discovery, valuation,
          construction intelligence, investment analytics, AI assistance,
          verification, and market insights into one unified platform for
          property professionals, investors, developers, and home buyers.
        </p>

        <div
          style={{
            display: "flex",
            gap: "16px",
            flexWrap: "wrap",
            marginTop: "40px",
          }}
        >
          <Link href="/properties">Explore Properties</Link>
          <Link href="/austin">Launch Austin AI</Link>
        </div>
      </section>

      {/* Platform */}
      <section
        style={{
          padding: "48px 24px",
          background: "#f8fafc",
        }}
      >
        <div
          style={{
            maxWidth: "1200px",
            margin: "0 auto",
          }}
        >
          <h2>One Platform. Multiple Intelligence Engines.</h2>

          <p
            style={{
              marginTop: 20,
              maxWidth: "760px",
              lineHeight: 1.8,
            }}
          >
            Every tool inside guavacheck is designed to work together,
            transforming fragmented property workflows into one intelligent
            ecosystem powered by AI and real-world market data.
          </p>

          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
              gap: "16px",
              marginTop: "36px",
            }}
          >
            {engines.map((engine) => (
              <div
                key={engine}
                style={{
                  padding: "18px",
                  border: "1px solid #ddd",
                  borderRadius: 12,
                  background: "#fff",
                }}
              >
                {engine}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Districts */}
      <section
        style={{
          padding: "80px 24px",
          maxWidth: "1200px",
          margin: "0 auto",
        }}
      >
        <h2>Explore Guava City</h2>

        <p
          style={{
            marginTop: 16,
            marginBottom: 40,
            maxWidth: "760px",
            lineHeight: 1.8,
          }}
        >
          Guava City is the digital ecosystem that powers every experience
          across the platform. Each district focuses on a different stage of
          the property journey while remaining connected through shared AI,
          market intelligence, and verification systems.
        </p>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit,minmax(300px,1fr))",
            gap: "24px",
          }}
        >
          {districts.map((district) => (
            <div
              key={district.title}
              style={{
                border: "1px solid #ddd",
                borderRadius: 16,
                padding: "28px",
              }}
            >
              <h3>{district.title}</h3>

              <p
                style={{
                  margin: "16px 0 24px",
                  lineHeight: 1.7,
                  color: "#555",
                }}
              >
                {district.description}
              </p>

              <Link href={district.href}>Explore →</Link>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section
        style={{
          padding: "80px 24px",
          background: "#0f172a",
          color: "#fff",
          textAlign: "center",
        }}
      >
        <h2>Building the Future of Property Intelligence</h2>

        <p
          style={{
            maxWidth: "720px",
            margin: "24px auto",
            lineHeight: 1.8,
          }}
        >
          Whether you're buying, building, investing, valuing, or researching,
          guavacheck provides the intelligence needed to make better property
          decisions.
        </p>

        <Link
          href="/properties"
          style={{
            color: "#4ade80",
            fontWeight: 600,
          }}
        >
          Start Exploring →
        </Link>
      </section>
    </main>
  );
}