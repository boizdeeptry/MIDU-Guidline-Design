import type { ReactNode } from "react";
import { Eyebrow } from "./Eyebrow";

type SectionHeadingProps = {
  eyebrow: string;
  eyebrowTone?: "onCanvas" | "onTint";
  title: ReactNode;
  subtitle: ReactNode;
  center?: boolean;
  maxWidthClass?: string;
  balance?: boolean;
};

export function SectionHeading({
  eyebrow,
  eyebrowTone = "onTint",
  title,
  subtitle,
  center = false,
  maxWidthClass = "max-w-[62ch]",
  balance = false,
}: SectionHeadingProps) {
  return (
    <div className={center ? "text-center" : undefined}>
      <Eyebrow tone={eyebrowTone}>{eyebrow}</Eyebrow>
      <h2 className={`text-[30px] font-bold leading-tight ${balance ? "text-balance" : ""}`}>{title}</h2>
      <p className={`mt-2 mb-9 text-ink-soft ${maxWidthClass} ${center ? "mx-auto" : ""}`}>{subtitle}</p>
    </div>
  );
}
