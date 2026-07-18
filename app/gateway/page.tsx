import Hero from "@/components/gateway/Hero";
import CTA from "@/components/gateway/CTA";
import Footer from "@/components/gateway/Footer";

export default function GatewayPage() {
  return (
    <>
      <Hero />

      <div className="bg-black">
        <CTA />
        <Footer />
      </div>
    </>
  );
}