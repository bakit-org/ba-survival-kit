# Yêu cầu sơ bộ màn hình mẫu (Screen Brief Sample)

## Màn hình

Thanh toán đơn hàng (Checkout - Payment Step)

## Mục đích

Cho phép người dùng lựa chọn phương thức thanh toán và bấm xác nhận đơn hàng để hoàn tất mua sắm.

## Các phần nội dung bắt buộc (Required sections)

- Bảng tóm tắt thông tin giao hàng (Shipping address summary).
- Bảng tóm tắt hình thức vận chuyển (Delivery option summary).
- Khu vực nhập mã giảm giá (Discount code area).
- Bộ chọn phương thức thanh toán (Payment method selector).
- Bảng tóm tắt đơn hàng (Order summary).
- Nút xác nhận đơn hàng (Confirm order button).

## Quy tắc nghiệp vụ chính (Key rules)

- Phương thức thanh toán khi nhận hàng (COD) chỉ hiển thị khi tổng giá trị đơn hàng dưới 3.000.000 VND.
- Nếu mã giảm giá không hợp lệ, hệ thống phải hiển thị thông báo lỗi rõ ràng ngay dưới trường nhập.
- Nếu cổng thanh toán bị quá thời gian phản hồi (payment gateway timeout), hệ thống phải hiển thị nút cho phép người dùng thanh toán lại (retry).

## Các trạng thái màn hình (States)

- Trạng thái mặc định (Default state).
- Trạng thái mã giảm giá không hợp lệ (Invalid discount code state).
- Trạng thái lỗi/quá thời gian thanh toán (Payment timeout/error state).
- Trạng thái không hỗ trợ COD do đơn hàng vượt hạn mức (COD unavailable state).

## Ghi chú thiết kế (Notes)

- Trên giao diện Desktop: bảng tóm tắt đơn hàng hiển thị cố định ở thanh bên phải (right panel).
- Trên giao diện Mobile: bảng tóm tắt đơn hàng có thể thu gọn/mở rộng linh hoạt.
