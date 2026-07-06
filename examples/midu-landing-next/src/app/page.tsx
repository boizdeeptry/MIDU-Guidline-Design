import { Benefits } from "@/components/Benefits";
import { Faq } from "@/components/Faq";
import { Footer } from "@/components/Footer";
import { Hero } from "@/components/Hero";
import { HowTo } from "@/components/HowTo";
import { LeadSection } from "@/components/LeadSection";
import { Nav } from "@/components/Nav";
import { Stats } from "@/components/Stats";
import { Testimonials } from "@/components/Testimonials";

export default function Home() {
  return (
    <>
      <Nav />
      <main>
        <Hero />
        <Stats />
        <Benefits />
        <HowTo />
        <Testimonials />
        <Faq />
        <LeadSection />
      </main>
      <Footer />
    </>
  );
}
