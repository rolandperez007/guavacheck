export default function NotFound() {
  return (
    <div style={{
      minHeight: "100vh",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      flexDirection: "column",
      textAlign: "center",
      padding: "40px",
      background: "#0b0f17",
      color: "white"
    }}>
      
      <h1 style={{ fontSize: "48px", marginBottom: "10px" }}>
        404
      </h1>

      <h2 style={{ marginBottom: "20px", opacity: 0.9 }}>
        Oops! This space isn’t built yet inside GuavaCheck.
      </h2>

      <img
        src="/404.png"
        alt="GuavaCheck Construction"
        style={{
          width: "100%",
          maxWidth: "700px",
          borderRadius: "16px",
          marginBottom: "25px",
          boxShadow: "0 20px 60px rgba(0,0,0,0.4)"
        }}
      />

      <p style={{ fontStyle: "italic", opacity: 0.8, maxWidth: "600px" }}>
        🤖 Austin AI: “I can see the blueprint… but this room hasn’t been constructed yet.”
      </p>

      <div style={{ marginTop: "30px", display: "flex", gap: "15px" }}>
        <a href="/" style={btnStyle}>Back to Home</a>
        <a href="/search" style={btnStyle}>Search</a>
        <a href="/contact" style={btnStyle}>Contact Us</a>
      </div>
    </div>
  );
}

const btnStyle = {
  padding: "12px 18px",
  borderRadius: "10px",
  background: "#1f2937",
  color: "white",
  textDecoration: "none",
  fontSize: "14px"
};


