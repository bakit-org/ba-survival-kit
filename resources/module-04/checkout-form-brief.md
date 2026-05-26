# Mô tả yêu cầu form nhập thông tin thanh toán (Checkout Form Brief)

## Mục đích

Thu thập thông tin địa chỉ nhận hàng và lựa chọn phương thức thanh toán của người dùng.

## Các phần nội dung bắt buộc (Required sections)

- Họ và tên người nhận (Recipient name).
- Số điện thoại liên hệ (Phone number).
- Địa chỉ chi tiết - Số nhà, tên đường (Address).
- Tỉnh/Thành phố - Quận/Huyện - Phường/Xã (Province / District / Ward).
- Hình thức vận chuyển (Shipping option).
- Phương thức thanh toán (Payment method).

## Quy tắc nghiệp vụ (Rules)

- Hệ thống không được cho phép người dùng xác nhận đơn hàng khi còn thiếu bất kỳ trường thông tin bắt buộc nào.
- Nếu địa chỉ nhận hàng nằm ngoài vùng hỗ trợ của đối tác vận chuyển, hệ thống phải hiển thị thông báo cảnh báo và chặn không cho tiếp tục thanh toán.
