import Header from "@/components/navigation/Header";
import Footer from "@/components/navigation/Footer";

interface Props {
  children: React.ReactNode;
}

export default function SiteLayout({
  children,
}: Props) {
  return (
    <>
      <Header />

      <main>{children}</main>

      <Footer />
    </>
  );
}