export default function NotFound() {
  return (
    <div style={{ 
      height: "100vh",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      background: "#0b0f19",
      color: "white"
    }}>
      <img src="/guavacheck-icon.png" width="120" />

      <h1>I couldn't find that page</h1>
      <p>But I can help you navigate.</p>

      <video autoPlay loop muted width="300">
        <source src="/construction-worker.mp4" type="video/mp4" />
      </video>
    </div>
  );
}