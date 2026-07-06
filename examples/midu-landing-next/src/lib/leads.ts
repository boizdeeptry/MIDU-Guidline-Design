import { z } from "zod";

export const leadSchema = z.object({
  parentName: z.string().trim().min(1, "Vui lòng nhập tên").max(120, "Tên quá dài"),
  phone: z
    .string()
    .trim()
    .regex(/^[0-9+ ().-]{8,20}$/, "Số điện thoại chưa đúng định dạng"),
  childAge: z.coerce
    .number()
    .int("Tuổi phải là số nguyên")
    .min(0, "Tuổi không hợp lệ")
    .max(18, "Sản phẩm dành cho trẻ 0–18 tuổi")
    .optional(),
  note: z.string().trim().max(1000, "Ghi chú tối đa 1000 ký tự").optional(),
});

export type LeadInput = z.infer<typeof leadSchema>;

export const leadResponseSchema = z.object({
  success: z.boolean(),
  error: z.string().nullable(),
});

export const LEAD_SUBMIT_FAILED = "Chưa gửi được thông tin, vui lòng thử lại.";
