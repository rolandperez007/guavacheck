import Image from "next/image";

export default function Background() {
  return (
    <div className="fixed inset-0 -z-10">

      <Image
        src="/images/launch/hero.png"
        alt="Guava City"
        fill
        priority
        sizes="100vw"
        className="object-cover object-center"
      />

      {/* Cinematic Overlay */}
      <div className="absolute inset-0 bg-black/35" />

      {/* Soft Gradient */}
      <div className="absolute inset-0 bg-gradient-to-b from-black/10 via-transparent to-[#07110E]/80" />

    </div>
  );
}