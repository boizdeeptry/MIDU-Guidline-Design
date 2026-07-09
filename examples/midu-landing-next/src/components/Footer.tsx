import Image from "next/image";

export function Footer() {
  return (
    <footer className="bg-grad-brand-rev on-brand-gradient mt-20 py-12 text-white">
      <div className="mx-auto flex max-w-[1200px] flex-wrap items-center justify-between gap-6 px-6">
        <div>
          <Image src="/images/logo-midu-white.png" alt="MIDU" width={116} height={44} />
          <div className="font-tagline mt-2 text-lg tracking-[1px] opacity-90">
            Chuyên gia chiều cao
          </div>
        </div>
        <p className="max-w-[44ch] text-[13px] opacity-85">
          Trang minh họa dựng bằng MIDU Vibecoder Kit. Thực phẩm này không phải là thuốc và không có
          tác dụng thay thế thuốc chữa bệnh.
        </p>
      </div>
    </footer>
  );
}
