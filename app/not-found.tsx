"use client";

import { useRouter } from "next/navigation";

export default function NotFound() {
  const router = useRouter();

  return (
    <div style={styles.wrapper}>
      {/* Background grid effect */}
      <div style={styles.gridOverlay} />

      {/* Main content */}
      <div style={styles.center}>
        
        {/* Construction icon */}
        <div style={styles.icon}>👷🏽‍♂️🏗️</div>

        <h1 style={styles.title}>
          Building Something Powerful
        </h1>

        <p style={styles.subtitle}>
          This section of GuavaCheck is still under construction.
        </p>

        {/* AI message */}
        <div style={styles.aiBox}>
          🤖 Austin AI:
          <br />
          "I searched the blueprints… this page isn’t ready yet.
          But I can still help you find what you need."
        </div>

        {/* Feature preview */}
        <div style={styles.features}>
          <div>🏠 AI Property Design</div>
          <div>💰 Cost Estimation Engine</div>
          <div>📊 Investor Dashboard</div>
          <div>🧱 Construction Calculator</div>
          <div>🌍 Marketplace</div>
          <div>🤖 Austin AI Assistant</div>
        </div>

        {/* Buttons */}
        <div style={styles.buttons}>
          <button onClick={() => router.push("/")} style={styles.primaryBtn}>
            Return Home
          </button>

          <button onClick={() => router.push("/contact")} style={styles.secondaryBtn}>
            Contact Us
          </button>

          <button onClick={() => router.push("/onboarding")} style={styles.secondaryBtn}>
            Join Beta
          </button>
        </div>

        {/* Footer */}
        <p style={styles.footer}>
          GuavaCheck • Building the Future of African Real Estate
        </p>
      </div>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  wrapper: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "#070b14",
    color: "white",
    textAlign: "center",
    position: "relative",
    overflow: "hidden"
  },

  gridOverlay: {
    position: "absolute",
    width: "200%",
    height: "200%",
    backgroundImage:
      "linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px)",
    backgroundSize: "40px 40px",
    transform: "rotate(10deg)",
    opacity: 0.4
  },

  center: {
    zIndex: 2,
    maxWidth: "800px",
    padding: "20px"
  },

  icon: {
    fontSize: "3rem",
    marginBottom: "10px"
  },

  title: {
    fontSize: "2.2rem",
    marginBottom: "10px"
  },

  subtitle: {
    opacity: 0.7,
    marginBottom: "20px"
  },

  aiBox: {
    background: "rgba(255,255,255,0.05)",
    padding: "15px",
    borderRadius: "10px",
    marginBottom: "20px",
    border: "1px solid rgba(255,255,255,0.1)"
  },

  features: {
    display: "grid",
    gridTemplateColumns: "repeat(2, minmax(0, 1fr))",
    gap: "10px",
    marginBottom: "20px",
    fontSize: "0.9rem",
    opacity: 0.85
  },

  buttons: {
    display: "flex",
    gap: "10px",
    justifyContent: "center",
    flexWrap: "wrap",
    marginBottom: "20px"
  },

  primaryBtn: {
    padding: "10px 16px",
    background: "#10b981",
    border: "none",
    color: "black",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: 600
  },

  secondaryBtn: {
    padding: "10px 16px",
    background: "transparent",
    border: "1px solid #374151",
    color: "white",
    borderRadius: "8px",
    cursor: "pointer"
  },

  footer: {
    opacity: 0.5,
    fontSize: "0.8rem"
  }
};