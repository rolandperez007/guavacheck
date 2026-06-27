export default function Home() {
  return (
    <main style={{
      minHeight: "100vh",
      background: "black",
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}>
      <img
        src="/404.png"
        alt="GuavaCheck"
        style={{
          width: "100%",
          maxHeight: "100vh",
          objectFit: "contain"
        }}
      />
    </main>
  );
}