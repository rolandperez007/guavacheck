export default function AustinSection() {
  return (
    <section
      style={{
        background: "red",
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
            THIS IS AUSTIN™ SECTION
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
              opacity: 0.9,
            }}
          >
            Austin™ is your AI construction partner. From the first sketch to the final block,
            Austin helps you design smarter, estimate accurately, verify property records, and guide
            your project from concept to completion.
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
            background: "linear-gradient(135deg,#163522,#0C1D14)",
            borderRadius: "30px",
            padding: "60px",
            border: "1px solid rgba(255,255,255,.08)",
            textAlign: "center",
          }}
        >
          <div
            style={{
              width: 170,
              height: 170,
              margin: "0 auto 30px",
              borderRadius: "50%",
              background:
                "radial-gradient(circle at 30% 30%, #1A1A1A 0%, #0B0B0B 45%, #000000 100%)",
              border: "2px solid rgba(110,231,183,.35)",
              boxShadow: "0 0 80px rgba(110,231,183,.30), inset 0 0 40px rgba(255,255,255,.04)",
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <div
              style={{
                width: 22,
                height: 22,
                borderRadius: "50%",
                background: "#6EE7B7",
                boxShadow: "0 0 25px #6EE7B7",
              }}
            />
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
              opacity: 0.75,
              lineHeight: 1.8,
            }}
          >
            "Every great building starts with a great decision. I'm here to help you make it."
          </p>
        </div>
      </div>
    </section>
  );
}
