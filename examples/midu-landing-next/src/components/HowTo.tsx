import Image from "next/image";
import { SectionHeading } from "./SectionHeading";

const STEPS = [
  {
    title: "Mỗi ngày một ống",
    body: "Sau bữa sáng, vị dễ uống, không cần pha. Bé từ 2 tuổi trở lên*.",
  },
  {
    title: "Vận động & ngủ đủ",
    body: "Nhảy dây, bơi, ngủ trước 22h — hormone tăng trưởng làm việc mạnh nhất khi bé ngủ sâu.",
  },
  {
    title: "Đo chiều cao mỗi tháng",
    body: "Đánh dấu lên tường, nhìn vạch nhích dần — động lực tốt nhất của cả mẹ và bé.",
  },
] as const;

function RulerProgress() {
  return (
    <div aria-hidden className="mt-2.5 max-w-[420px]">
      <div className="relative h-3 overflow-hidden rounded-pill bg-surface-soft">
        <div
          className="absolute inset-0"
          style={{
            background:
              "repeating-linear-gradient(90deg, transparent 0 calc(10% - 1px), var(--color-hairline) calc(10% - 1px) 10%)",
          }}
        />
        <div className="bg-grad-sun relative h-full w-[58%] rounded-pill" />
      </div>
    </div>
  );
}

export function HowTo() {
  return (
    <section id="cachdung" className="mx-auto max-w-[1200px] px-6 py-20">
      <SectionHeading
        eyebrow="Cách dùng"
        eyebrowTone="onCanvas"
        title="Ba bước, một thói quen"
        subtitle="Đơn giản đến mức MIGI cũng làm được — và bé sẽ muốn tự làm."
      />
      <div className="grid items-center gap-12 md:grid-cols-[.8fr_1.2fr]">
        <div className="text-center">
          <Image
            src="/images/migi-medicine.png"
            alt="MIGI uống một ống MIDU"
            width={300}
            height={300}
            className="mx-auto w-[min(300px,80%)]"
          />
          <div className="font-sticker mt-2 text-2xl">Đến giờ rồi!</div>
        </div>
        <div>
          {STEPS.map((step, index) => (
            <div
              key={step.title}
              className="flex gap-4 border-b border-hairline py-4.5 last:border-b-0"
            >
              <div className="flex size-10 flex-none items-center justify-center rounded-full bg-primary font-black text-white">
                {index + 1}
              </div>
              <div className="w-full">
                <h3 className="mb-1 text-lg font-bold">{step.title}</h3>
                <p className="text-[15px] text-ink-soft">{step.body}</p>
                {index === STEPS.length - 1 ? <RulerProgress /> : null}
              </div>
            </div>
          ))}
          <p className="mt-3.5 text-xs text-ink-soft">
            *Thông tin minh họa — thay bằng hướng dẫn sử dụng công bố của sản phẩm.
          </p>
        </div>
      </div>
    </section>
  );
}
