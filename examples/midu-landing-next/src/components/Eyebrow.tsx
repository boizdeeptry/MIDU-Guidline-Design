type Tone = "onCanvas" | "onTint" | "onGradient";

// Matches DESIGN.md components: eyebrow-badge (onCanvas, for plain sections),
// eyebrow-badge-on-tint (onTint, for surface-soft/-tint sections — magenta-on-tint
// fails AA at 4.45:1), plus the on-gradient look Hero needs that the spec doesn't name.
const TONE_CLASS: Record<Tone, string> = {
  onCanvas: "border border-hairline bg-surface-soft text-magenta",
  onTint: "border border-hairline bg-canvas text-magenta",
  onGradient: "bg-white/15 text-white",
};

export function Eyebrow({ tone = "onTint", children }: { tone?: Tone; children: string }) {
  return (
    <span
      className={`font-display mb-4 inline-flex rounded-pill px-3.5 py-1.5 text-[13px] font-bold uppercase tracking-[1.5px] ${TONE_CLASS[tone]}`}
    >
      {children}
    </span>
  );
}
