import Image from "next/image";
import Link from "next/link";

const LINKS = [
  { href: "#visao", label: "Vì sao MIDU" },
  { href: "#cachdung", label: "Cách dùng" },
  { href: "#dangky", label: "Nhận tư vấn" },
] as const;

export function Nav() {
  return (
    <nav aria-label="Điều hướng chính" className="sticky top-0 z-50 h-16 bg-canvas shadow-card">
      <div className="mx-auto flex h-16 max-w-[1200px] items-center gap-7 px-6">
        <Link href="#top" aria-label="MIDU — về đầu trang">
          <Image src="/images/logo-midu.png" alt="MIDU" width={90} height={34} priority />
        </Link>
        <div className="ml-auto hidden gap-6 text-sm font-medium text-ink-soft md:flex">
          {LINKS.map((link) => (
            <a key={link.href} href={link.href} className="hover:text-magenta focus-visible:text-magenta">
              {link.label}
            </a>
          ))}
        </div>
        {/* Nav CTA stays secondary — the hero owns the one gradient pill per viewport */}
        <a
          href="#dangky"
          className="rounded-pill border-2 border-primary px-5 py-2 text-sm font-bold text-primary hover:bg-surface-soft"
        >
          Mua ngay
        </a>
      </div>
    </nav>
  );
}
