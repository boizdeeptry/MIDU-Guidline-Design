type BubbleProps = {
  label: string;
  size: number;
  orange?: boolean;
};

export function Bubble({ label, size, orange = false }: BubbleProps) {
  return (
    <span
      className={`relative inline-flex items-center justify-center rounded-full font-bold text-white ${
        orange ? "bg-grad-bubble-orange" : "bg-grad-bubble"
      }`}
      style={{ width: size, height: size, fontSize: size < 44 ? 11 : 13, letterSpacing: "0.5px" }}
    >
      {label}
      <span
        aria-hidden
        className="absolute rounded-full bg-white/80"
        style={{ top: "14%", right: "18%", width: "22%", height: "14%", transform: "rotate(-28deg)" }}
      />
    </span>
  );
}
