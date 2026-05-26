# Mô tả yêu cầu màn hình đăng nhập thanh toán (Checkout Login Brief)

## Mục đích

Cho phép người dùng lựa chọn đăng nhập tài khoản hoặc tiếp tục thanh toán không cần tài khoản (guest checkout) trước khi chuyển tiếp sang luồng nhập thông tin giao nhận và thanh toán.

## Yêu cầu chính (Key requirements)

- Địa chỉ email là bắt buộc nếu người dùng chọn phương thức thanh toán không cần tài khoản.
- Người dùng đã có tài khoản trên hệ thống có thể thực hiện đăng nhập nhanh.
- Giao diện phải bố trí lối đi rõ ràng, trực quan sang chế độ thanh toán không cần tài khoản.
- Phải hiển thị thông báo lỗi rõ ràng nếu thông tin đăng nhập tài khoản bị sai.
