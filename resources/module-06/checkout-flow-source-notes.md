# Tài liệu ghi chú luồng nghiệp vụ thanh toán (Checkout Flow Source Notes)

## Luồng đi thuận lợi (Happy Path)

1. Người dùng truy cập màn hình xem lại giỏ hàng (cart review).
2. Người dùng kiểm tra danh sách sản phẩm, số lượng và tổng tiền hàng.
3. Người dùng bấm chuyển tiếp sang bước thanh toán (checkout).
4. Người dùng nhập đầy đủ thông tin địa chỉ giao nhận hàng.
5. Hệ thống tự động tính toán và hiển thị phí vận chuyển.
6. Người dùng lựa chọn phương thức thanh toán mong muốn.
7. Người dùng bấm xác nhận đơn hàng để thực hiện thanh toán.
8. Giao dịch thanh toán thành công.
9. Hệ thống ghi nhận đơn hàng thành công và chuyển sang màn hình hoàn tất.

## Các luồng thay thế và luồng xử lý lỗi (Alternate / Error Paths)

- **Lỗi áp dụng mã giảm giá:** Mã giảm giá nhập vào không hợp lệ hoặc hết hạn -> Hệ thống báo lỗi, người dùng có thể nhập mã khác hoặc bỏ qua.
- **Lỗi địa chỉ ngoài vùng phục vụ:** Địa chỉ giao hàng nằm ngoài vùng hỗ trợ vận chuyển -> Hệ thống hiển thị cảnh báo và chặn không cho tiến hành thanh toán.
- **Phương thức COD không khả dụng:** Đơn hàng có giá trị từ 3 triệu trở lên -> Hệ thống làm mờ tùy chọn COD kèm dòng giải thích.
- **Lỗi nghẽn cổng thanh toán (Payment timeout):** Cổng thanh toán phản hồi chậm -> Hệ thống báo lỗi và hiển thị tùy chọn cho phép thử lại.
- **Lỗi thanh toán thất bại:** Giao dịch bị từ chối -> Hệ thống giữ đơn ở trạng thái chờ thanh toán và cho phép thử lại trực tiếp tại giao diện.
