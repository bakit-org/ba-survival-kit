# Checklist đánh giá chất lượng Wireframe (Wireframe Quality Checklist)

## 1. Tính Logic & Luồng đi (Logic)

- Bản vẽ có thể hiện đúng mục đích cốt lõi của màn hình không?
- Người dùng khi nhìn vào giao diện có biết ngay bước tiếp theo cần làm gì không?
- Luồng di chuyển giữa các khu vực thông tin trên màn hình có mạch lạc không?

## 2. Dữ liệu & Thông tin hiển thị (Data)

- Đã hiển thị đầy đủ các trường thông tin (fields) cần thiết chưa?
- Có bị thiếu thông tin quan trọng nào khiến người dùng phân vân, không thể đưa ra quyết định (ví dụ: thiếu phí vận chuyển ở bước thanh toán) không?

## 3. Các nút Hành động (Actions)

- Nút hành động chính (Primary Action - ví dụ: Xác nhận đặt hàng) có nổi bật không?
- Các nút hành động phụ (Secondary Actions - ví dụ: Quay lại, Áp dụng mã giảm giá, Hủy) đã được bố trí đầy đủ và hợp lý chưa?

## 4. Các trạng thái giao diện (States)

- Trạng thái mặc định (Default state) khi người dùng mới truy cập.
- Trạng thái lỗi (Error state) khi có sự cố hệ thống hoặc thanh toán lỗi.
- Trạng thái trống (Empty/Unavailable state) ví dụ như khi giỏ hàng trống hoặc phương thức thanh toán COD không khả dụng.
- Trạng thái thành công hoặc thông báo xác nhận (Success/Confirmation state).

## 5. Kiểm tra tính hợp lệ dữ liệu (Validation)

- Những trường nhập liệu nào cần có cơ chế kiểm tra lỗi trực quan ngay trên giao diện?
- Có quy tắc vô hiệu hóa/kích hoạt nút bấm (disable/enable button logic) dựa trên việc nhập thông tin hợp lệ của người dùng không?
