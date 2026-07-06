const STATS = [
  { value: "5", label: "dưỡng chất vàng", source: "Ca+ · D3 · K2 · Mg · Arg" },
  { value: "K2", label: "MenaQ7® chuẩn Âu", source: "Nguyên liệu nhập khẩu Na Uy*" },
  { value: "1.000", label: "ngày vàng phát triển", source: "*Thông tin minh họa — thay bằng số liệu công bố" },
] as const;

export function Stats() {
  return (
    <section className="mx-auto max-w-[1200px] px-6 pb-20">
      <div className="grid gap-5 md:grid-cols-3">
        {STATS.map((stat) => (
          <div key={stat.label} className="rounded-lg bg-canvas p-6 text-center shadow-card">
            <div className="text-grad-brand text-[44px] font-black leading-[1.1] tracking-[-0.25px]">
              {stat.value}
            </div>
            <div className="mt-1.5 text-[13px] font-bold uppercase tracking-[1.5px] text-magenta">
              {stat.label}
            </div>
            <div className="mt-2.5 text-xs text-ink-soft">{stat.source}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
