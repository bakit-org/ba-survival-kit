# Bộ hồ sơ tài liệu BA thu nhỏ mẫu (Sample Mini BA Pack)

## 1. Bản tóm tắt yêu cầu sơ bộ (Brief summary)

Luồng thanh toán (Checkout flow) cần bắt buộc hỗ trợ tính năng mua hàng không cần tài khoản (guest checkout), hiển thị phí vận chuyển minh bạch ngay trước bước thanh toán và hỗ trợ cơ chế cho phép thử lại (retry) khi thanh toán gặp lỗi.

## 2. Giao diện phác thảo & ghi chú (Wireframe notes)

- Màn hình lựa chọn Đăng nhập hoặc Thanh toán nhanh (Login / Guest checkout entry).
- Màn hình xem lại giỏ hàng (Cart review screen).
- Màn hình nhập thông tin thanh toán (Checkout payment step screen).

## 3. Đặc tả chi tiết màn hình (Screen description)

- Đặc tả chi tiết màn hình thanh toán (CHK-PAY-01): bao gồm ô nhập mã giảm giá, bộ chọn phương thức thanh toán, bảng tóm tắt đơn hàng và nút xác nhận hoàn tất đặt hàng.

## 4. Các sơ đồ quy trình (Diagrams)

- Sơ đồ hoạt động (Activity flow) mô tả toàn bộ quy trình đặt hàng từ giỏ hàng đến hoàn tất đơn.
- Sơ đồ trình tự (Sequence diagram) mô tả tương tác kỹ thuật chi tiết khi thực hiện thử lại thanh toán.
- Sơ đồ vẽ nhanh bằng ký tự (ASCII flow) dùng trong biên bản họp thảo luận logic.

## 5. Ca sử dụng nghiệp vụ (Use case)

- Ca sử dụng: Hoàn tất thanh toán đơn hàng (Complete checkout).

## 6. Câu chuyện người dùng & tiêu chí nghiệm thu (User stories and AC)

- Câu chuyện: Mua hàng nhanh không cần tài khoản (Guest checkout).
- Câu chuyện: Lựa chọn phương thức thanh toán (Payment selection).
- Câu chuyện: Thử lại thanh toán khi gặp lỗi (Retry payment).

## 7. Checklist kiểm duyệt chất lượng (Review checklist)

- Đảm bảo phạm vi nghiệp vụ nằm trong Phase 1.
- Quy tắc giới hạn thanh toán COD dưới 3 triệu đã được thể hiện chính xác.
- Đầy đủ các trạng thái lỗi giao diện và lỗi kết nối.

## 8. Kịch bản kiểm thử (Test cases)

- Kịch bản: Khách hàng mua hàng và thanh toán thành công (Happy path checkout).
- Kịch bản: Hệ thống báo lỗi khi nhập mã giảm giá không hợp lệ (Invalid discount code).
- Kịch bản: Vô hiệu hóa phương thức COD khi đơn hàng có giá trị lớn (COD unavailable).
- Kịch bản: Xử lý khi cổng thanh toán bị nghẽn và người dùng thực hiện thử lại (Payment timeout & retry).
