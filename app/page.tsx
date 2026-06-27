import Image from "next/image";

export default function Home() {
  return (
    <main
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#000",
      }}
    >
      <Image
        src="/404.png"
        alt="GuavaCheck Under Construction"
        width={1920}
        height={1080}
        priority
        style={{
          width: "100%",
          height: "auto",
          maxHeight: "100vh",
          objectFit: "contain",
        }}
      />
    </main>
  );
}