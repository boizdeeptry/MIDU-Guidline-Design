import { SectionHeading } from "./SectionHeading";

const FAQS = [
  {
    q: "Bé mấy tuổi dùng được MIDU MenaQ7?",
    a: "Theo khuyến nghị in trên bao bì của sản phẩm — vui lòng đọc kỹ hướng dẫn sử dụng và tham khảo ý kiến chuyên gia y tế.",
  },
  {
    q: "K2 MenaQ7® khác gì K2 thông thường?",
    a: "MenaQ7® là dạng MK-7 tự nhiên có nghiên cứu lâm sàng về sinh khả dụng — thông tin chi tiết theo tài liệu công bố của nhà sản xuất.",
  },
  {
    q: "Dùng bao lâu thì thấy khác biệt?",
    a: "Chiều cao là hành trình dài — hãy đo mỗi tháng và duy trì đủ dinh dưỡng, vận động, giấc ngủ. Không có sản phẩm nào thay thế được cả ba yếu tố đó.",
  },
] as const;

export function Faq() {
  return (
    <section className="mx-auto max-w-[1200px] px-6 py-20">
      <SectionHeading
        eyebrow="Câu hỏi thường gặp"
        eyebrowTone="onCanvas"
        title="Mẹ hỏi — MIGI trả lời"
        subtitle={<>Nội dung minh họa — thay bằng Q&amp;A đã duyệt y khoa trước khi công bố.</>}
        center
      />
      <div className="mx-auto max-w-[760px]">
        {FAQS.map((faq) => (
          <details
            key={faq.q}
            className="mb-3 rounded-lg border border-hairline bg-canvas px-6 py-4.5 open:shadow-card"
          >
            <summary className="cursor-pointer font-bold focus-visible:outline-3 focus-visible:outline-sun">
              {faq.q}
            </summary>
            <p className="mt-2.5 text-[15px] text-ink-soft">{faq.a}</p>
          </details>
        ))}
      </div>
    </section>
  );
}
