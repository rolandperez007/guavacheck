import Navbar from "./components/layout/Navbar";
import Hero from "./components/hero/Hero";
import AustinSection from "./components/austin/AustinSection";

export default function Home() {
  return (
    <>
      <Navbar />
      <Hero />
      <AustinSection />
    </>
  );
}