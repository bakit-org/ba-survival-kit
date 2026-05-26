# Mô tả yêu cầu màn hình xem lại giỏ hàng (Cart Review Brief)

## Mục đích

Cho phép người dùng kiểm tra lại danh sách sản phẩm, số lượng, đơn giá, phí vận chuyển ước tính và áp dụng mã giảm giá trước khi chuyển tiếp sang bước thanh toán.

## Các phần nội dung bắt buộc (Required sections)

- Danh sách các sản phẩm đã chọn (Product line items).
- Bộ điều chỉnh số lượng sản phẩm - tăng/giảm (Quantity control).
- Nút xóa sản phẩm khỏi giỏ hàng (Remove action).
- Ô nhập mã giảm giá (Discount code input).
- Tổng tiền hàng tạm tính (Subtotal).
- Phí vận chuyển ước tính (Estimated shipping fee).
- Nút chuyển tiếp sang thanh toán (Proceed to checkout CTA).

## Quy tắc nghiệp vụ (Rules)

- Nếu giỏ hàng trống (cart rỗng), hệ thống phải hiển thị trạng thái giỏ hàng trống (empty state) kèm nút dẫn người dùng quay lại trang chủ mua sắm.
- Nếu mã giảm giá người dùng nhập không hợp lệ, hệ thống phải hiển thị thông báo lỗi chi tiết.
