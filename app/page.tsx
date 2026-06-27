import Image from "next/image";

export default function Home() {
  return (
    <main
      style={{
        width: "100vw",
        height: "100vh",
        margin: 0,
        padding: 0,
        overflow: "hidden",
      }}
    >
      <Image
        src="/404.png"
        alt="GuavaCheck"
        fill
        priority
        style={{
          objectFit: "cover",
        }}
      />
    </main>
  );
}