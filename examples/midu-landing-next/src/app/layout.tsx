import type { Metadata } from "next";
import { Lexend, Patrick_Hand, Quicksand } from "next/font/google";
import localFont from "next/font/local";
import type { ReactNode } from "react";
import "./globals.css";

const fzRubik = localFont({
  src: [
    { path: "../fonts/fzrubik-400.woff2", weight: "400", style: "normal" },
    { path: "../fonts/fzrubik-500.woff2", weight: "500", style: "normal" },
    { path: "../fonts/fzrubik-700.woff2", weight: "700", style: "normal" },
    { path: "../fonts/fzrubik-900.woff2", weight: "900", style: "normal" },
  ],
  variable: "--font-fz-rubik",
  display: "swap",
});

const lexend = Lexend({
  subsets: ["vietnamese", "latin"],
  weight: ["400", "500", "700"],
  variable: "--font-lexend",
  display: "swap",
});

const quicksand = Quicksand({
  subsets: ["latin", "vietnamese"],
  weight: "400",
  variable: "--font-quicksand",
  display: "swap",
});

const patrickHand = Patrick_Hand({
  subsets: ["latin", "vietnamese"],
  weight: "400",
  variable: "--font-patrick-hand",
  display: "swap",
});

export const metadata: Metadata = {
  title: "MIDU MenaQ7 — Chuyên gia chiều cao",
  description:
    "MIDU MenaQ7 kết hợp Canxi, D3 và K2 MenaQ7® chuẩn Âu — đồng hành cùng con cao lớn mỗi ngày cùng MIGI.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html
      lang="vi"
      className={`${fzRubik.variable} ${lexend.variable} ${quicksand.variable} ${patrickHand.variable}`}
    >
      <body>{children}</body>
    </html>
  );
}
