"use client";

import Image from "next/image";
import { useState } from "react";
import type { FormEvent } from "react";
import { LEAD_SUBMIT_FAILED, leadResponseSchema, leadSchema } from "@/lib/leads";

const inputClass =
  "rounded-xl border border-hairline px-4 py-3 text-base font-normal focus:border-primary focus:outline-none focus:ring-[3px] focus:ring-primary/15";

type Status =
  | { kind: "idle" }
  | { kind: "submitting" }
  | { kind: "success" }
  | { kind: "error"; message: string };

export function LeadForm() {
  const [status, setStatus] = useState<Status>({ kind: "idle" });

  async function handleSubmit(event: FormEvent<HTMLFormElement>): Promise<void> {
    event.preventDefault();
    const form = event.currentTarget;
    const data = new FormData(form);

    const parsed = leadSchema.safeParse({
      parentName: data.get("parentName"),
      phone: data.get("phone"),
      childAge: data.get("childAge") === "" ? undefined : data.get("childAge"),
      note: data.get("note") === "" ? undefined : data.get("note"),
    });
    if (!parsed.success) {
      setStatus({ kind: "error", message: parsed.error.issues[0]?.message ?? "Dữ liệu chưa hợp lệ." });
      return;
    }

    setStatus({ kind: "submitting" });
    try {
      const response = await fetch("/api/leads", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(parsed.data),
      });
      const parsedResponse = leadResponseSchema.safeParse(await response.json());
      if (!parsedResponse.success || !parsedResponse.data.success) {
        const message = (parsedResponse.success ? parsedResponse.data.error : null) ?? LEAD_SUBMIT_FAILED;
        setStatus({ kind: "error", message });
        return;
      }
      form.reset();
      setStatus({ kind: "success" });
    } catch {
      setStatus({ kind: "error", message: "Mất kết nối — kiểm tra mạng và thử lại giúp mẹ nhé." });
    }
  }

  if (status.kind === "success") {
    return (
      <div className="rounded-lg bg-canvas p-8 text-center shadow-card">
        <Image
          src="/images/migi-love.png"
          alt="MIGI bắn tim cảm ơn"
          width={160}
          height={160}
          className="mx-auto"
        />
        <h3 className="mt-3 text-[22px] font-bold">Đã nhận thông tin!</h3>
        <p className="mt-1.5 text-[15px] text-ink-soft">
          Chuyên gia của MIDU sẽ gọi lại cho mẹ trong 24h. Cảm ơn mẹ đã tin MIGI!
        </p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} noValidate className="rounded-lg bg-canvas p-8 shadow-card">
      <div className="grid gap-4 md:grid-cols-2">
        <label className="flex flex-col gap-1.5 text-sm font-medium">
          Tên của mẹ/bố *
          <input
            name="parentName"
            required
            maxLength={120}
            autoComplete="name"
            className={inputClass}
          />
        </label>
        <label className="flex flex-col gap-1.5 text-sm font-medium">
          Số điện thoại *
          <input
            name="phone"
            required
            inputMode="tel"
            autoComplete="tel"
            placeholder="VD: 0912 345 678"
            className={inputClass}
          />
        </label>
        <label className="flex flex-col gap-1.5 text-sm font-medium">
          Tuổi của bé
          <input
            name="childAge"
            inputMode="numeric"
            placeholder="VD: 5"
            className={inputClass}
          />
        </label>
        <label className="flex flex-col gap-1.5 text-sm font-medium">
          Mẹ muốn hỏi thêm
          <input
            name="note"
            maxLength={1000}
            placeholder="VD: bé biếng ăn, ngủ muộn…"
            className={inputClass}
          />
        </label>
      </div>
      {status.kind === "error" ? (
        <p role="alert" className="mt-3 text-sm text-error">
          {status.message}
        </p>
      ) : null}
      <button
        type="submit"
        disabled={status.kind === "submitting"}
        className="btn-primary mt-5 w-full disabled:opacity-60 md:w-auto"
      >
        {status.kind === "submitting" ? "Đang gửi…" : "Nhận tư vấn miễn phí"}
      </button>
      <p className="mt-3 text-xs text-ink-soft">
        Thông tin chỉ dùng để tư vấn, không chia sẻ cho bên thứ ba.
      </p>
    </form>
  );
}
