import Image from "next/image";
import { SectionHeading } from "./SectionHeading";

const QUOTES = [
  {
    text: "“Bé nhà mình tự nhắc 'đến giờ MIGI rồi mẹ ơi'. Sáu tháng, vạch trên tường nhích thấy rõ.”",
    who: "Chị Ngọc Anh",
    meta: "Mẹ bé 5 tuổi · Hà Nội",
  },
  {
    text: "“Mình chọn vì có K2 MenaQ7 chuẩn Âu — đọc kỹ mới biết canxi không tự vào xương được.”",
    who: "Chị Thu Hằng",
    meta: "Mẹ bé 7 tuổi · TP.HCM",
  },
] as const;

export function Testimonials() {
  return (
    <section className="bg-surface-soft py-20">
      <div className="mx-auto max-w-[1200px] px-6">
        <SectionHeading
          eyebrow="Mẹ kể lại"
          title={<>Cả nhà cùng &ldquo;wow&rdquo;</>}
          subtitle="Trích lời minh họa cho bản demo — thay bằng đánh giá thật khi công bố."
        />
        <div className="grid items-start gap-5 md:grid-cols-3">
          {QUOTES.map((quote) => (
            <figure key={quote.who} className="rounded-lg bg-canvas p-6 shadow-card">
              <blockquote className="text-[15px] leading-relaxed">{quote.text}</blockquote>
              <figcaption>
                <div className="mt-3.5 text-sm font-bold">{quote.who}</div>
                <div className="text-xs text-ink-soft">{quote.meta}</div>
              </figcaption>
            </figure>
          ))}
          <div className="text-center">
            <Image
              src="/images/migi-love.png"
              alt="MIGI bắn tim cảm ơn"
              width={240}
              height={240}
              className="mx-auto w-[min(240px,70%)]"
            />
          </div>
        </div>
      </div>
    </section>
  );
}
