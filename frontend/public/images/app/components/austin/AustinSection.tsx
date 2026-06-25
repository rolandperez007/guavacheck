export default function AustinSection() {
  return (
    <section
      style={{
        background: "#07130C",
        color: "white",
        padding: "120px 60px",
      }}
    >
      <div
        style={{
          maxWidth: "1200px",
          margin: "0 auto",
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "60px",
          alignItems: "center",
        }}
      >
        <div>
          <div
            style={{
              color: "#6EE7B7",
              fontWeight: 700,
              letterSpacing: 2,
              marginBottom: 18,
            }}
          >
            MEET AUSTIN™
          </div>

          <h2
            style={{
              fontSize: "54px",
              marginBottom: "24px",
            }}
          >
            The Intelligence Behind guavacheck
          </h2>

          <p
            style={{
              fontSize: "20px",
              lineHeight: 1.8,
              opacity: .9,
            }}
          >
            Austin™ is your AI construction partner.
            From the first sketch to the final block,
            Austin helps you design smarter,
            estimate accurately, verify property records,
            and guide your project from concept to completion.
          </p>

          <div
            style={{
              marginTop: "35px",
              display: "grid",
              gap: "16px",
            }}
          >
            <div>✅ AI Property Design</div>
            <div>✅ Intelligent Cost Estimation</div>
            <div>✅ Property Verification</div>
            <div>✅ Construction Guidance</div>
            <div>✅ Investment Insights</div>
          </div>

          <button
            style={{
              marginTop: "45px",
              padding: "16px 32px",
              background: "#4CAF50",
              color: "white",
              border: "none",
              borderRadius: "12px",
              fontWeight: 700,
              cursor: "pointer",
            }}
          >
            Talk to Austin™
          </button>
        </div>

        <div
          style={{
            background:
              "linear-gradient(135deg,#163522,#0C1D14)",
            borderRadius: "30px",
            padding: "60px",
            border: "1px solid rgba(255,255,255,.08)",
            textAlign: "center",
          }}
        >
          <div
            style={{
              fontSize: "120px",
            }}
          >
            🤖
          </div>

          <h3
            style={{
              fontSize: "34px",
            }}
          >
            Austin™
          </h3>

          <p
            style={{
              opacity: .75,
              lineHeight: 1.8,
            }}
          >
            "Every great building starts with a great decision.
            I'm here to help you make it."
          </p>
        </div>
      </div>
    </section>
  );
}