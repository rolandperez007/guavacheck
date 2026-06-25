import Image from "next/image";

export default function Navbar() {
  return (
    <nav
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        right: 0,
        height: "80px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 60px",
        background: "rgba(7,19,12,.72)",
        backdropFilter: "blur(18px)",
        borderBottom: "1px solid rgba(255,255,255,.08)",
        zIndex: 1000,
      }}
    >
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 14,
        }}
      >
        <Image
          src="/images/guava-logo.png"
          alt="guavacheck"
          width={46}
          height={46}
          priority
        />

        <div>
          <div
            style={{
              fontSize: 28,
              fontWeight: 800,
            }}
          >
            guavacheck
          </div>

          <div
            style={{
              color: "#6EE7B7",
              fontSize: 12,
            }}
          >
            AI Property Intelligence
          </div>
        </div>
      </div>

      <div
        style={{
          display: "flex",
          gap: 28,
          alignItems: "center",
        }}
      >
        <a href="/">Home</a>
        <a href="/design">Design</a>
        <a href="/estimate">Estimate</a>
        <a href="/verify">Verify</a>
        <a href="/austin">Austin™</a>

        <a
          href="#"
          style={{
            background: "#4CAF50",
            color: "white",
            textDecoration: "none",
            padding: "12px 22px",
            borderRadius: 10,
            fontWeight: 700,
          }}
        >
          Get Started
        </a>
      </div>
    </nav>
  );
}