export default function Features() {
  const cardStyle = {
    background: "rgba(255,255,255,0.04)",
    border: "1px solid rgba(110,231,183,.12)",
    borderRadius: "22px",
    padding: "32px",
    transition: "0.3s",
  };

  return (
    <section
      style={{
        background: "#07130C",
        color: "white",
        padding: "110px 40px",
      }}
    >
      <div
        style={{
          maxWidth: "1300px",
          margin: "0 auto",
        }}
      >
        <div
          style={{
            textAlign: "center",
            marginBottom: "70px",
          }}
        >
          <div
            style={{
              color: "#6EE7B7",
              letterSpacing: 2,
              fontWeight: 700,
              marginBottom: 16,
            }}
          >
            EVERYTHING YOU NEED
          </div>

          <h2
            style={{
              fontSize: "54px",
              marginBottom: "20px",
            }}
          >
            One Platform.
            <br />
            Complete Property Intelligence.
          </h2>

          <p
            style={{
              maxWidth: "700px",
              margin: "0 auto",
              opacity: .8,
              lineHeight: 1.8,
              fontSize: "19px",
            }}
          >
            From your first sketch to final construction,
            guavacheck helps you design, estimate,
            verify and build with confidence.
          </p>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(2,1fr)",
            gap: "28px",
          }}
        >
          <div style={cardStyle}>
            <h3>🏠 AI Property Design</h3>
            <p>Create intelligent floor plans and architectural concepts in minutes.</p>
          </div>

          <div style={cardStyle}>
            <h3>💰 Cost Estimation</h3>
            <p>Generate accurate construction budgets with AI-powered pricing.</p>
          </div>

          <div style={cardStyle}>
            <h3>🛡 Property Verification</h3>
            <p>Verify ownership records and property authenticity before purchase.</p>
          </div>

          <div style={cardStyle}>
            <h3>📈 Investment Intelligence</h3>
            <p>Discover opportunities and evaluate real estate investments with confidence.</p>
          </div>
        </div>
      </div>
    </section>
  );
}