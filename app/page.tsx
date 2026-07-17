import Image from "next/image";

export default function HomePage() {
  return (
    <main className="relative h-screen w-screen overflow-hidden bg-black">
      <Image
        src="/images/guava-city-coming-soon.png"
        alt="Guava City — The Gates Open Soon"
        fill
        priority
        className="object-cover"
      />
    </main>
  );
}