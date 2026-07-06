import { Bubble } from "./Bubble";
import { SectionHeading } from "./SectionHeading";

const BENEFITS = [
  {
    chip: "Ca+",
    title: "Canxi — nguyên liệu xây xương",
    body: "Khối vật liệu chính của khung xương đang lớn. Thiếu canxi, mọi thứ khác đều vô nghĩa.",
  },
  {
    chip: "D3",
    title: "Vitamin D3 — mở cửa hấp thu",
    body: "Giúp ruột hấp thu canxi từ thức ăn vào máu. Không có D3, canxi đi qua rồi… đi luôn.",
  },
  {
    chip: "K2",
    title: "K2 MenaQ7® — dẫn canxi vào xương",
    body: "Kích hoạt osteocalcin, “chở” canxi từ máu gắn vào xương — đúng chỗ cần, không lạc đường.",
  },
] as const;

export function Benefits() {
  return (
    <section id="visao" className="bg-surface-soft py-20">
      <div className="mx-auto max-w-[1200px] px-6 text-center">
        <SectionHeading
          eyebrow="Vì sao MIDU"
          title="Canxi chỉ là nguyên liệu — K2 mới là người dẫn đường"
          subtitle="Uống nhiều canxi không đồng nghĩa xương nhận đủ. Bộ ba dưỡng chất của MIDU làm việc như một đội: mỗi chất một nhiệm vụ, đủ mặt thì canxi mới về đúng đích."
          center
          balance
        />
        <div className="grid gap-5 text-left md:grid-cols-3">
          {BENEFITS.map((benefit) => (
            <div key={benefit.chip} className="rounded-lg bg-canvas p-6 shadow-card">
              <Bubble label={benefit.chip} size={48} />
              <h3 className="mt-3.5 mb-2 text-[22px] font-bold leading-snug">{benefit.title}</h3>
              <p className="text-[15px] text-ink-soft">{benefit.body}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
