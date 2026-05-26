# Ví dụ nhận xét giao diện đạt yêu cầu (Good Wireframe Notes)

## Đánh giá tổng quan (Overall)

Bản phác thảo wireframe đã thể hiện trực quan bước thanh toán (payment step), bảng tóm tắt đơn hàng (order summary) và nút kêu gọi hành động (CTA) chính để xác nhận đơn hàng.

## Các điểm đã làm tốt (What works)

- Các phương thức thanh toán (Payment methods) được nhóm và phân loại rõ ràng, dễ lựa chọn.
- Bảng tóm tắt đơn hàng (Order summary) được đặt ở vị trí thuận mắt, dễ theo dõi tổng số tiền.
- Ô nhập mã giảm giá (Discount code) được bố trí riêng biệt, trực quan.

## Các điểm cần cải thiện (What to improve)

- **Thiếu trạng thái giới hạn COD:** Cần thể hiện rõ trạng thái vô hiệu hóa (disabled/unavailable) của phương thức COD khi đơn hàng vượt quá 3.000.000 VND.
- **Thiếu thông báo lỗi mã giảm giá:** Chưa hiển thị vị trí và cách thức hiển thị thông báo lỗi khi người dùng nhập mã không hợp lệ (invalid discount code).
- **Thiếu luồng xử lý lỗi thanh toán:** Chưa thấy nút bấm hoặc hướng dẫn cho phép người dùng thanh toán lại (retry) khi gặp lỗi quá thời gian (timeout).
- **Thiếu logic ràng buộc nút bấm:** Cần ghi chú rõ quy tắc vô hiệu hóa nút "Xác nhận đơn hàng" khi người dùng chưa hoàn tất việc chọn phương thức thanh toán.

## Đề xuất chỉnh sửa (Recommendation)

- Bổ sung 3 trạng thái màn hình còn thiếu (COD unavailable, invalid discount code, và payment timeout retry).
- Ghi chú trực tiếp các quy tắc kiểm tra dữ liệu (validation) và nội dung thông báo (messages) đi kèm vào bản vẽ wireframe hoặc file tài liệu đính kèm.
