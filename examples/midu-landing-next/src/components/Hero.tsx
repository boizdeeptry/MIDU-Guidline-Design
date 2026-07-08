import Image from "next/image";
import { Bubble } from "./Bubble";
import { Eyebrow } from "./Eyebrow";

const BUBBLES = [
  { label: "K2", size: 52, orange: false, delay: "0s", style: { top: "10%", right: "6%" } },
  { label: "D3", size: 40, orange: false, delay: "-2s", style: { top: "16%", right: "38%" } },
  { label: "Ca+", size: 46, orange: false, delay: "-4s", style: { bottom: "16%", right: "40%" } },
  { label: "Arg", size: 36, orange: true, delay: "-5s", style: { bottom: "36%", right: "4%" } },
] as const;

export function Hero() {
  return (
    <header id="top" className="mx-auto max-w-[1200px] px-6 pb-20 pt-12">
      <div className="relative grid items-center gap-8 rounded-[28px] bg-grad-brand p-12 text-white max-md:p-7 md:grid-cols-[1.2fr_.8fr]">
        <div aria-hidden className="pointer-events-none absolute inset-0 max-md:hidden">
          {BUBBLES.map((b) => (
            <span
              key={b.label}
              className="absolute"
              style={{ ...b.style, animation: "bubble-float 7s ease-in-out infinite", animationDelay: b.delay }}
            >
              <Bubble label={b.label} size={b.size} orange={b.orange} />
            </span>
          ))}
        </div>
        <div>
          <Eyebrow tone="onGradient">Chuyên gia chiều cao</Eyebrow>
          <h1 className="mb-4 text-[clamp(40px,6vw,64px)] font-black leading-[1.05] tracking-[-0.5px] text-balance">
            Cao lớn mỗi ngày cùng MIGI
          </h1>
          <p className="mb-7 max-w-[48ch] text-lg font-medium leading-relaxed opacity-90">
            MIDU MenaQ7 kết hợp Canxi, D3 và K2 MenaQ7® chuẩn Âu — đưa canxi vào đúng xương, để mỗi
            tháng đo lại là một lần &ldquo;wow&rdquo; của cả nhà.
          </p>
          <div className="flex flex-wrap gap-3.5">
            <a href="#dangky" className="btn-primary">
              Nhận tư vấn miễn phí
            </a>
            <a
              href="#visao"
              className="font-display rounded-pill border-2 border-white px-6 py-3 font-bold text-white hover:bg-white/10"
            >
              Tìm hiểu thêm
            </a>
          </div>
        </div>
        <div className="flex min-h-[260px] items-end justify-center self-end max-md:min-h-0 max-md:mt-2">
          <Image
            src="/images/migi-hello.png"
            alt="MIGI — chú hươu cao cổ bác sĩ vẫy tay chào"
            width={320}
            height={320}
            priority
            className="-mb-[76px] w-[min(320px,100%)] drop-shadow-[0_20px_30px_rgba(34,31,31,.3)] max-md:-mb-14 max-md:w-[min(240px,70%)]"
          />
        </div>
      </div>
    </header>
  );
}
