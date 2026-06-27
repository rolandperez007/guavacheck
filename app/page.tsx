export default function Home() {
  return (
    <main
      style={{
        minHeight: "100vh",
        display: "grid",
        placeItems: "center",
        background: "#08120d",
        color: "white",
        textAlign: "center",
        padding: "2rem",
      }}
    >
      <div>
        <img
          src="/images/guava-logo.png"
          alt="GuavaCheck"
          style={{ width: 120, marginBottom: 24 }}
        />

        <h1>GuavaCheck V2 is Under Construction</h1>

        <p style={{ maxWidth: 600, margin: "20px auto" }}>
          Austin is preparing the next generation of AI-powered property
          intelligence. We'll be back shortly with a completely redesigned
          experience.
        </p>

        <p>
          Thank you for your patience.
        </p>
      </div>
    </main>
  );
}