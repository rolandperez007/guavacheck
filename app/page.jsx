export default function Home() {
  return (
    <main style={{ fontFamily: "sans-serif" }}>

      {/* HERO */}
      <section style={{
        padding: "100px 20px",
        textAlign: "center",
        background: "#0f172a",
        color: "white"
      }}>

        <video
          autoPlay
          loop
          muted
          style={{
            width: "90%",
            borderRadius: 20,
            marginBottom: 30
          }}
        >
          <source src="/hero.mp4" />
        </video>

        <h1 style={{ fontSize: 48 }}>
          Global Real Estate Intelligence System
        </h1>

        <p style={{ fontSize: 18, opacity: 0.8 }}>
          Analyze. Build. Invest. Manage property ecosystems worldwide.
        </p>

        <div style={{ marginTop: 30 }}>
          <a href="/auth">
            <button style={{
              padding: "12px 24px",
              marginRight: 10,
              cursor: "pointer"
            }}>
              Get Started
            </button>
          </a>

          <a href="/properties">
            <button style={{
              padding: "12px 24px",
              cursor: "pointer"
            }}>
              Explore Listings
            </button>
          </a>
        </div>

      </section>

      {/* FEATURES */}
<div>
  <h3>📰 Blog & Insights</h3>
  <p>AI generated property intelligence and market news.</p>
</div>

<div>
  <h3>🌍 Community</h3>
  <p>Connect with investors, buyers and professionals.</p>
</div>

<div>
  <h3>💰 Mortgage Center</h3>
  <p>Calculate affordability and financing options.</p>
</div>

<div>
  <h3>📊 Investor Dashboard</h3>
  <p>Track ROI, forecasts and opportunities.</p>
</div>

<div>
  <h3>🚨 Distressed Deals</h3>
  <p>Discover undervalued investment opportunities.</p>
</div>

<div>
  <h3>👷 Contractor Marketplace</h3>
  <p>Find trusted contractors and request bids.</p>
</div>
      <section style={{
        padding: "80px 20px",
        textAlign: "center"
      }}>

        <h2>Everything in one ecosystem</h2>

        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
          gap: 20,
          marginTop: 40
        }}>

          <div>
            <h3>🌍 Global Marketplace</h3>
            <p>Buy and list properties across regions and markets.</p>
          </div>

          <div>
            <h3>💱 Multi-Currency Engine</h3>
            <p>Real-time valuation across global currencies & crypto.</p>
          </div>

          <div>
            <h3>🏗 Construction Intelligence</h3>
            <p>Estimate, plan, and simulate building costs instantly.</p>
          </div>

          <div>
            <h3>🤖 AI Property Insights</h3>
            <p>Smart analysis for investment and valuation decisions.</p>
          </div>

        </div>

      </section>

      {/* CTA */}
      <section style={{
        padding: "80px 20px",
        textAlign: "center",
        background: "#f8fafc"
      }}>

        <h2>Start building your real estate system today</h2>

        <a href="/auth">
          <button style={{
            padding: "14px 28px",
            marginTop: 20,
            cursor: "pointer"
          }}>
            Create Account
          </button>
        </a>

      </section>

    </main>
  )
}
