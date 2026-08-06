import AustinCard from "../shared/AustinCard";
export default function Hero() {
  return (
    <section
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg,#050907 0%,#07130C 35%,#0F2417 70%,#173927 100%)",
        color: "white",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: "80px 40px",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "1300px",
          display: "grid",
          gridTemplateColumns: "1.1fr 0.9fr",
          gap: "70px",
          alignItems: "center",
        }}
      >
        {/* LEFT */}

        <div>
          <div
            style={{
              color: "#6EE7B7",
              letterSpacing: 3,
              fontWeight: 700,
              marginBottom: 18,
            }}
          >
            DESIGN • ESTIMATE • VERIFY • BUILD
          </div>

          <h1
            style={{
              fontSize: "84px",
              lineHeight: 1,
              marginBottom: 24,
            }}
          >
            guavacheck
          </h1>

          <h2
            style={{
              fontSize: "38px",
              marginBottom: 30,
              fontWeight: 500,
            }}
          >
            The Future of AI Property Intelligence
          </h2>

          <p
            style={{
              fontSize: 21,
              lineHeight: 1.8,
              opacity: 0.9,
              maxWidth: 650,
            }}
          >
            Design smarter. Estimate accurately. Verify confidently.
            <br />
            <br />
            Powered by Austin™ — your AI construction and property intelligence partner.
          </p>

          <div
            style={{
              display: "flex",
              gap: 18,
              marginTop: 40,
              flexWrap: "wrap",
            }}
          >
            <a
              href="/design"
              style={{
                background: "#4CAF50",
                color: "white",
                padding: "18px 34px",
                borderRadius: 14,
                textDecoration: "none",
                fontWeight: 700,
              }}
            >
              Start Designing
            </a>

            <a
              href="#austin"
              style={{
                border: "1px solid #6EE7B7",
                color: "#6EE7B7",
                padding: "18px 34px",
                borderRadius: 14,
                textDecoration: "none",
                fontWeight: 700,
              }}
            >
              Talk to Austin™
            </a>
          </div>
        </div>

        {/* RIGHT */}

        <AustinCard />
      </div>
    </section>
  );
}
