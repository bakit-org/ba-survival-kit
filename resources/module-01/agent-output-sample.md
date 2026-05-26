# Kết quả mẫu từ Agent (Agent Output Sample)

## Tính năng

Luồng thanh toán (Checkout flow) cho website thương mại điện tử.

## Mục tiêu nghiệp vụ

- Giảm tỷ lệ bỏ sót đơn hàng (drop-off) ở bước thanh toán.
- Hiển thị tổng chi phí minh bạch cho người dùng trước khi xác nhận đơn hàng.
- Hỗ trợ xử lý thanh toán thất bại theo hướng cho phép thử lại (retry) thay vì bắt người dùng phải làm lại từ đầu.

## Yêu cầu dự thảo (Draft requirements)

### Yêu cầu chức năng (Functional)

- Hệ thống phải hỗ trợ cả hai hình thức: thanh toán bằng tài khoản đã đăng nhập và thanh toán không cần tài khoản (guest checkout).
- Đối với hình thức thanh toán không cần tài khoản, người dùng bắt buộc phải nhập email để nhận xác nhận đơn hàng.
- Hệ thống phải hiển thị rõ ràng phí vận chuyển trước khi người dùng bấm xác nhận thanh toán.
- Hệ thống phải hỗ trợ áp dụng mã giảm giá (tối đa một mã cho mỗi đơn hàng).
- Hệ thống phải kiểm tra tính hợp lệ của mã giảm giá trước khi áp dụng vào tổng tiền thanh toán.
- Hệ thống phải hỗ trợ các phương thức thanh toán phổ biến: thẻ ATM nội địa, ví điện tử, và thanh toán khi nhận hàng (COD).
- Phương thức COD chỉ áp dụng cho các đơn hàng có tổng trị giá dưới 3.000.000 VND.
- Nếu thanh toán thất bại hoặc quá thời gian phản hồi (timeout), hệ thống phải hỗ trợ cơ chế cho phép thử lại (retry payment).
- Nếu địa chỉ giao hàng của người dùng nằm ngoài vùng hỗ trợ của đối tác vận chuyển, hệ thống phải chặn không cho thực hiện checkout.

### Phạm vi loại trừ (Scope exclusions)

- Trong giai đoạn 1 (Phase 1), chưa hỗ trợ tính năng chia một đơn hàng để giao đến nhiều địa chỉ khác nhau.

## Giả định (Assumptions)

- Phí vận chuyển sẽ được tính toán tự động qua API kết nối với dịch vụ vận chuyển riêng.
- Bảng tóm tắt đơn hàng (Order summary) trên Desktop sẽ được hiển thị cố định ở thanh bên phải (right panel).
- Trên giao diện Mobile, bảng tóm tắt đơn hàng có thể thu gọn/mở rộng linh hoạt để tối ưu không gian hiển thị.

## Các câu hỏi cần làm rõ (Open questions)

- Nội dung thông báo lỗi cụ thể khi người dùng áp dụng mã giảm giá hết hạn hoặc không hợp lệ là gì?
- Khi cổng thanh toán phản hồi chậm (gateway timeout), hệ thống nên hiển thị thông báo lỗi ngay trên dòng (inline message), dạng hộp thoại (modal popup), hay thông báo trượt (toast message)?
- Đơn hàng ở trạng thái "Chờ thanh toán" (Pending payment) sẽ được hệ thống giữ lại trong bao lâu để người dùng thực hiện thử lại (retry)?

## Đề xuất các sản phẩm tiếp theo (Suggested next outputs)

- Thiết kế wireframe cho các màn hình: kiểm tra giỏ hàng (cart review), form nhập thông tin giao hàng/thanh toán (shipping/payment form), và bảng tóm tắt đơn hàng (order summary).
- Tài liệu mô tả màn hình chi tiết (screen description) cho form thanh toán.
- Biểu đồ trình tự (sequence diagram) mô tả luồng thử lại thanh toán khi gặp lỗi.
