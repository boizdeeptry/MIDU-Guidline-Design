import { createClient } from "@supabase/supabase-js";
import { NextResponse } from "next/server";
import { LEAD_SUBMIT_FAILED, leadSchema } from "@/lib/leads";

const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
// Module-level singleton: reused across warm invocations instead of rebuilt per request.
const supabase = url !== undefined && anonKey !== undefined ? createClient(url, anonKey) : null;

export async function POST(request: Request): Promise<NextResponse> {
  if (supabase === null) {
    console.error("leads: missing Supabase env (NEXT_PUBLIC_SUPABASE_URL / NEXT_PUBLIC_SUPABASE_ANON_KEY)");
    return NextResponse.json(
      { success: false, error: "Hệ thống đang bảo trì, vui lòng thử lại sau." },
      { status: 503 },
    );
  }

  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json(
      { success: false, error: "Dữ liệu gửi lên không hợp lệ." },
      { status: 400 },
    );
  }

  const parsed = leadSchema.safeParse(body);
  if (!parsed.success) {
    const message = parsed.error.issues[0]?.message ?? "Dữ liệu chưa hợp lệ.";
    return NextResponse.json({ success: false, error: message }, { status: 400 });
  }

  const { error } = await supabase.from("leads").insert({
    parent_name: parsed.data.parentName,
    phone: parsed.data.phone,
    child_age: parsed.data.childAge ?? null,
    note: parsed.data.note ?? null,
  });

  if (error !== null) {
    console.error("leads: insert failed", { code: error.code, message: error.message });
    return NextResponse.json({ success: false, error: LEAD_SUBMIT_FAILED }, { status: 502 });
  }

  return NextResponse.json({ success: true, error: null }, { status: 201 });
}
