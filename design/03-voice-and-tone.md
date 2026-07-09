## Voice and Tone

MIDU speaks with two voices layered on one personality: a **trusted pediatric expert** (the credibility layer) who travels with a **cheerful giraffe sidekick** (the warmth layer). Copy should never fully commit to either — pure clinical copy reads cold for a kids' brand; pure mascot-cute copy undermines a supplement claim.

1. **Address the parent as "bạn," the child as "con" or "bé" — never "em" or "cháu" for the parent.** The reader is an adult customer, not a subordinate. Reserve exclamation-heavy, mascot-voiced lines ("Wow!", "Cố lên nào!") for MIGI's own speech bubbles and micro-copy (empty states, celebrations) — never for headlines making a health claim.
2. **Every measurable claim needs a number and a source caption.** "Hỗ trợ phát triển chiều cao" is fine as a headline; "+3–5cm/năm" needs a `{typography.caption}` footnote citing the study/condition — see `{components.stat-tile}`. This is a trust and regulatory requirement, not a style preference.
3. **No fear, no guilt, no scarcity pressure.** Avoid "Con bạn đang thấp hơn bạn bè?" framing, countdown timers, or "chỉ còn X suất" copy. Pair any shortfall message with an encouraging MIGI pose (`migi-cheer`) — never `migi-cry`/`migi-sulk` used to shame the reader into buying.
4. **Mascot exclamations stay short, singular, and read like real speech — not shouty body copy.** "Wow!", "Cố lên!", "Tuyệt vời!" are one-line `{typography.sticker}` captions beside a MIGI pose. They never appear in `{typography.body}` paragraphs or on button labels.
5. **Never fabricate data.** Product names, ingredient dosages, prices, customer counts, satisfaction %, ratings, doctor names, and citations must come from a real Midu source — never invented, not even as "*illustrative" placeholder. If a real figure isn't available: omit the number, use a clearly-labelled structural placeholder (e.g. "[nội dung minh họa — chưa có đánh giá thật]"), or drop the element. Specific danger zones: **ingredient dosages** (Midu MenaQ7 K2 comes only in 45 / 180 / 360 mcg — never invent a mg value the packaging doesn't state), **expert endorsements** (attribute only to real advisory-board doctors, with a real cited source; rank-and-file staff may not self-style as "bác sĩ"), and **testimonials/social proof** (Midu's own rule: "hỏi hiện trạng, không bịa social proof"). Real company figures to reach for instead of invented ones: ~20.000 chuyên gia đã đào tạo, 91+ khóa học, ~300.000 phác đồ (source: midu.vn).

| | Copy |
|---|---|
| ❌ Don't | "CON BẠN ĐANG THUA KÉM BẠN BÈ VỀ CHIỀU CAO?? Đặt hàng NGAY để không bỏ lỡ ưu đãi cuối cùng!!!" |
| ✅ Do | "Hỗ trợ con phát triển chiều cao mỗi ngày, cùng MIGI." — button: `{components.button-primary}` "Bắt đầu đo" |

