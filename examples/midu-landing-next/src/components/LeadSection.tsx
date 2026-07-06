import { LeadForm } from "./LeadForm";
import { SectionHeading } from "./SectionHeading";

export function LeadSection() {
  return (
    <section id="dangky" className="bg-surface-tint py-20">
      <div className="mx-auto max-w-[760px] px-6">
        <SectionHeading
          eyebrow="Nhận tư vấn"
          title="Để chuyên gia gọi lại cho mẹ"
          subtitle="Điền thông tin, chuyên gia dinh dưỡng của MIDU sẽ tư vấn lộ trình chiều cao phù hợp với bé — hoàn toàn miễn phí."
          center
          maxWidthClass="max-w-[52ch]"
        />
        <LeadForm />
      </div>
    </section>
  );
}
