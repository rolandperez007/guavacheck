import Background from "@/components/gateway/Background";
import Navigation from "@/components/gateway/Navigation";
import Hero from "@/components/gateway/Hero";
import CTA from "@/components/gateway/CTA";
import Footer from "@/components/gateway/Footer";
import AustinOrb from "@/components/gateway/AustinOrb";
export const metadata = {
  title: "guavacheck | The Gates Open Soon",
  description:
    "Building the Future of the Built Environment. Powered by Austin.",
};

export default function GatewayPage() {
  return (
    <main className="relative min-h-screen overflow-hidden bg-[#07110E] text-white">
      <Background />

      <AustinOrb />

      <Navigation />

      <Hero />

      <section
        id="early-access"
        className="relative z-10 mx-auto max-w-7xl px-6 py-32 lg:px-10"
      >
        <CTA />
      </section>

      <Footer />
    </main>
  );
}