# Luồng nghiệp vụ thanh toán mẫu (Checkout Business Flow)

## Tóm tắt luồng nghiệp vụ (Flow summary)

Người dùng kiểm tra giỏ hàng, chuyển sang bước thanh toán, nhập địa chỉ nhận hàng, chọn phương thức thanh toán phù hợp, bấm xác nhận đặt hàng và nhận phản hồi kết quả giao dịch thanh toán từ hệ thống.

## Quy tắc nghiệp vụ cốt lõi (Core rules)

- Thanh toán không đăng nhập (guest checkout) bắt buộc phải cung cấp địa chỉ email hợp lệ để nhận hóa đơn điện tử.
- Hệ thống bắt buộc phải hiển thị phí vận chuyển trước khi người dùng thực hiện bấm nút xác nhận thanh toán.
- Phương thức thanh toán khi nhận hàng (COD) chỉ áp dụng cho đơn hàng có tổng trị giá dưới 3.000.000 VND.
- Khi giao dịch thanh toán bị lỗi hoặc quá thời gian phản hồi (timeout), hệ thống phải hỗ trợ luồng cho phép người dùng thanh toán lại (retry).

## Các trường hợp biên đáng chú ý (Notable edge cases)

- Mã giảm giá người dùng áp dụng đã hết hạn hoặc không hợp lệ.
- Địa chỉ nhận hàng nằm ngoài vùng hỗ trợ vận chuyển của đối tác logistics.
- Cổng thanh toán bị nghẽn kết nối (payment gateway timeout).
- Giá trị đơn hàng vượt quá hạn mức thanh toán COD.
