import React from "react";

export default function AustinCard() {
  return (
    <div
      style={{
        background: "rgba(255,255,255,0.04)",
        border: "1px solid rgba(110,231,183,.15)",
        borderRadius: 28,
        padding: 50,
        backdropFilter: "blur(18px)",
        boxShadow: "0 30px 80px rgba(0,0,0,.35)",
        textAlign: "center",
      }}
    >
      {/* Avatar */}

      <div style={avatarContainer}>
        <div style={orbGlow}></div>

        <img src="/images/austin-core.png" alt="Austin" style={avatarImage} />
      </div>

      {/* Online */}

      <div style={statusStyle}>
        <span style={statusDot}></span>
        Austin Online
      </div>

      <h2
        style={{
          fontSize: 40,
          marginBottom: 10,
        }}
      >
        Austin™
      </h2>

      <p
        style={{
          color: "#A7F3D0",
          letterSpacing: 1,
          marginBottom: 30,
        }}
      >
        AI Construction Intelligence
      </p>

      <div style={systemBox}>
        <SystemRow title="Construction Brain" />
        <SystemRow title="3D Engine" />
        <SystemRow title="Cost Intelligence" />
        <SystemRow title="Verification Engine" />
      </div>

      <p
        style={{
          lineHeight: 1.8,
          marginTop: 30,
          marginBottom: 35,
          opacity: 0.92,
        }}
      >
        <strong>Good afternoon.</strong>
        <br />
        <br />
        I'm ready to help design, estimate, analyse, verify and supervise your next construction
        project.
        <br />
        <br />
        <strong>What shall we build today?</strong>
      </p>

      <div
        style={{
          display: "grid",
          gap: 14,
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

function SystemRow({ title }: { title: string }) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        padding: "10px 0",
        borderBottom: "1px solid rgba(255,255,255,.05)",
      }}
    >
      <span>{title}</span>

      <span
        style={{
          color: "#6EE7B7",
          fontWeight: 700,
        }}
      >
        READY
      </span>
    </div>
  );
}

const avatarContainer: React.CSSProperties = {
  position: "relative",
  width: 210,
  height: 210,
  margin: "0 auto 30px",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

const orbGlow: React.CSSProperties = {
  position: "absolute",
  width: 180,
  height: 180,
  borderRadius: "50%",
  background: "radial-gradient(circle, rgba(110,231,183,.25), rgba(110,231,183,.05), transparent)",
  filter: "blur(16px)",
};

const avatarImage: React.CSSProperties = {
  position: "relative",
  width: 190,
  height: 190,
  objectFit: "contain",
  filter: "drop-shadow(0 0 18px rgba(110,231,183,.35)) drop-shadow(0 0 60px rgba(110,231,183,.18))",
};

const statusStyle: React.CSSProperties = {
  display: "inline-flex",
  alignItems: "center",
  gap: 10,
  background: "rgba(76,175,80,.15)",
  color: "#6EE7B7",
  padding: "8px 18px",
  borderRadius: 999,
  fontWeight: 700,
  marginBottom: 25,
};

const statusDot: React.CSSProperties = {
  width: 10,
  height: 10,
  borderRadius: "50%",
  background: "#4CAF50",
};

const systemBox: React.CSSProperties = {
  background: "rgba(255,255,255,.03)",
  border: "1px solid rgba(255,255,255,.05)",
  borderRadius: 18,
  padding: 20,
  textAlign: "left",
};

const buttonStyle: React.CSSProperties = {
  width: "100%",
  padding: "16px",
  borderRadius: "14px",
  border: "1px solid rgba(110,231,183,.2)",
  background: "rgba(255,255,255,.03)",
  color: "white",
  fontWeight: 600,
  fontSize: "16px",
  cursor: "pointer",
};
