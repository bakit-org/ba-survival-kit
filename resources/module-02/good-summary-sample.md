# Ví dụ kết quả tóm tắt đạt yêu cầu (Good Summary Sample)

## Bối cảnh (Context)

- **Tính năng (Feature):** Luồng thanh toán đơn hàng (E-commerce checkout)
- **Tài liệu đầu vào (Source Input):** Project brief mẫu
- **Mục tiêu tài liệu:** Bản tóm tắt dự thảo có cấu trúc và có thể sử dụng ngay dành cho BA

## Các nội dung chính (Main Points)

- Quy trình thanh toán phải hỗ trợ cả người dùng đã đăng nhập và khách vãng lai (guest user).
- Người dùng bắt buộc phải nhìn thấy phí vận chuyển hiển thị rõ ràng trước khi bấm xác nhận thanh toán.
- Khi thanh toán thất bại, hệ thống không được bắt người dùng thực hiện lại từ đầu mà phải hỗ trợ cơ chế thử lại (retry).
- Áp dụng mã giảm giá: Giới hạn tối đa một mã trên một đơn hàng.
- Thanh toán COD: Có giới hạn về hạn mức giá trị đơn hàng tối đa (dưới 3 triệu).

## Các giả định liên quan (Assumptions)

- Phí vận chuyển được tính toán tự động thông qua việc kết nối API với dịch vụ vận chuyển riêng của đối tác.
- Bảng tóm tắt đơn hàng (Order summary) có giao diện hiển thị khác nhau để tối ưu hóa trên Desktop và Mobile.

## Các câu hỏi cần làm rõ (Open Questions)

- Đơn hàng chờ thanh toán (Pending payment) sẽ được lưu lại để cho phép người dùng thử lại (retry) trong khoảng thời gian bao lâu?
- Trường hợp cổng thanh toán phản hồi chậm (payment timeout) thì giao diện sẽ hiển thị thông báo lỗi dưới dạng nào (inline, modal hay toast)?
- Quy trình thanh toán không tài khoản (guest checkout) có yêu cầu xác thực email (OTP/link kích hoạt) ngay lập tức hay không?

## Đề xuất các bước tiếp theo (Next Steps)

- Thiết kế wireframe cho bước xem lại giỏ hàng (cart review) và bước thanh toán (payment step).
- Viết tài liệu đặc tả màn hình (screen spec) chi tiết cho form nhập thông tin thanh toán.
- Vẽ sơ đồ luồng (activity flow) xử lý trường hợp thử lại thanh toán khi gặp lỗi.
