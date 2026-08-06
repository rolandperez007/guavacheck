"use client";

import { useRouter } from "next/navigation";

export default function NotFound() {
  const router = useRouter();

  return (
    <div style={styles.wrapper}>
      <div style={styles.overlay} />

      {/* BACKGROUND IMAGE */}
      <div style={styles.imageLayer} />

      {/* FLOATING PARTICLES */}
      <div style={styles.particles} />

      {/* CONTENT */}
      <div style={styles.content}>
        <h1 style={styles.title}>404</h1>

        <p style={styles.subtitle}>Oops! This space isn’t built yet inside GuavaCheck.</p>

        <div style={styles.aiBox}>
          🤖 Austin AI
          <br />
          “I can see the blueprint… but this room hasn’t been constructed yet.”
        </div>

        <div style={styles.buttons}>
          <button onClick={() => router.push("/")} style={styles.primary}>
            Back to Home
          </button>

          <button onClick={() => router.push("/search")} style={styles.secondary}>
            Search
          </button>

          <button onClick={() => router.push("/contact")} style={styles.secondary}>
            Contact Us
          </button>
        </div>
      </div>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  wrapper: {
    height: "100vh",
    overflow: "hidden",
    position: "relative",
    background: "#050814",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    color: "white",
  },

  /* dark cinematic overlay */
  overlay: {
    position: "absolute",
    inset: 0,
    background:
      "radial-gradient(circle at 30% 30%, rgba(16,185,129,0.08), transparent 50%), radial-gradient(circle at 70% 70%, rgba(59,130,246,0.08), transparent 50%)",
    zIndex: 1,
  },

  /* your image as background with slow zoom */
  imageLayer: {
    position: "absolute",
    inset: 0,
    backgroundImage: "url('/assets/guava-404.png')",
    backgroundSize: "cover",
    backgroundPosition: "center",
    animation: "slowZoom 12s ease-in-out infinite alternate",
    filter: "brightness(0.9) contrast(1.05)",
    zIndex: 0,
  },

  /* subtle particles */
  particles: {
    position: "absolute",
    inset: 0,
    background: "radial-gradient(circle, rgba(255,255,255,0.06) 1px, transparent 1px)",
    backgroundSize: "60px 60px",
    animation: "floatParticles 20s linear infinite",
    zIndex: 2,
    opacity: 0.4,
  },

  content: {
    position: "relative",
    zIndex: 3,
    textAlign: "center",
    maxWidth: "700px",
    padding: "20px",
  },

  title: {
    fontSize: "4rem",
    fontWeight: 700,
    marginBottom: "10px",
    textShadow: "0 0 30px rgba(16,185,129,0.4)",
  },

  subtitle: {
    opacity: 0.8,
    marginBottom: "20px",
  },

  aiBox: {
    background: "rgba(0,0,0,0.4)",
    border: "1px solid rgba(255,255,255,0.1)",
    padding: "16px",
    borderRadius: "12px",
    marginBottom: "25px",
    backdropFilter: "blur(10px)",
  },

  buttons: {
    display: "flex",
    gap: "10px",
    justifyContent: "center",
    flexWrap: "wrap",
  },

  primary: {
    padding: "10px 16px",
    background: "#10b981",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: 600,
    color: "black",
  },

  secondary: {
    padding: "10px 16px",
    background: "rgba(255,255,255,0.05)",
    border: "1px solid rgba(255,255,255,0.15)",
    borderRadius: "8px",
    cursor: "pointer",
    color: "white",
  },
};

/* inject animations */
if (typeof window !== "undefined") {
  const style = document.createElement("style");
  style.innerHTML = `
    @keyframes slowZoom {
      from { transform: scale(1); }
      to { transform: scale(1.08); }
    }

    @keyframes floatParticles {
      from { transform: translateY(0px); }
      to { transform: translateY(-80px); }
    }
  `;
  document.head.appendChild(style);
}
