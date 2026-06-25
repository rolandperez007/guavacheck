export default function AustinCard() {
  return (
    <div
      style={{
        background: "rgba(255,255,255,0.04)",
        border: "1px solid rgba(110,231,183,0.15)",
        borderRadius: "28px",
        padding: "50px",
        backdropFilter: "blur(18px)",
        boxShadow: "0 30px 80px rgba(0,0,0,0.35)",
        textAlign: "center",
      }}
    >
      {/* Austin Icon */}
      <img
        src="/images/austin-core.png"
        alt="Austin™"
        style={{
          width: "190px",
          height: "190px",
          objectFit: "contain",
          display: "block",
          margin: "0 auto 30px",
          filter:
            "drop-shadow(0 0 18px rgba(110,231,183,.35)) drop-shadow(0 0 50px rgba(110,231,183,.18))",
        }}
      />

      {/* Status */}
      <div
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: "10px",
          background: "rgba(76,175,80,.15)",
          color: "#6EE7B7",
          padding: "8px 18px",
          borderRadius: "999px",
          fontWeight: 700,
          marginBottom: "24px",
        }}
      >
        <span
          style={{
            width: 10,
            height: 10,
            borderRadius: "50%",
            background: "#4CAF50",
          }}
        />
        Austin Online
      </div>

      <h2
        style={{
          fontSize: "38px",
          marginBottom: "8px",
        }}
      >
        Austin™
      </h2>

      <p
        style={{
          color: "#A7F3D0",
          letterSpacing: "1px",
          marginBottom: "28px",
        }}
      >
        AI Property Intelligence
      </p>

      <p
        style={{
          lineHeight: 1.8,
          opacity: 0.9,
          marginBottom: "32px",
        }}
      >
        <strong>Good afternoon.</strong>
        <br />
        <br />
        What would you like to accomplish today?
      </p>

      <div
        style={{
          display: "grid",
          gap: "14px",
        }}
      >
        <button style={buttonStyle}>Design Property</button>
        <button style={buttonStyle}>Estimate Cost</button>
        <button style={buttonStyle}>Verify Property</button>
        <button style={buttonStyle}>Investment Intelligence</button>
      </div>
    </div>
  );
}

const buttonStyle: React.CSSProperties = {
  width: "100%",
  padding: "16px",
  borderRadius: "14px",
  border: "1px solid rgba(110,231,183,.20)",
  background: "rgba(255,255,255,.03)",
  color: "white",
  fontWeight: 600,
  fontSize: "16px",
  cursor: "pointer",
};