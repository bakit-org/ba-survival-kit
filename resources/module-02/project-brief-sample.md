# Tài liệu mô tả yêu cầu sơ bộ mẫu (Project Brief Sample)

## Tên tính năng

Luồng thanh toán đơn hàng (E-commerce checkout flow)

## Mục tiêu kinh doanh / nghiệp vụ

Tăng tỷ lệ hoàn tất đơn hàng bằng cách rút ngắn quy trình thanh toán, hiển thị thông tin rõ ràng và giảm thiểu tối đa các lỗi giao diện gây ức chế cho người dùng.

## Đối tượng người dùng mục tiêu

- Khách hàng đã đăng nhập tài khoản.
- Khách hàng vãng lai mua nhanh không cần đăng nhập (guest checkout).

## Phạm vi thực hiện (In Scope)

- Kiểm tra lại giỏ hàng (Cart review).
- Nhập thông tin địa chỉ giao hàng (Shipping address).
- Hiển thị phí vận chuyển (Shipping fee display).
- Áp dụng mã giảm giá (Discount code).
- Lựa chọn phương thức thanh toán (Payment method selection).
- Tóm tắt đơn hàng (Order summary).
- Xác nhận và hoàn tất đơn hàng (Order confirmation).

## Phạm vi loại trừ (Out of Scope)

- Tách đơn hàng để vận chuyển thành nhiều đợt (Split shipment).
- Giao một đơn hàng đến nhiều địa chỉ khác nhau.
- Thanh toán trả góp (Installment payment).

## Các quy tắc nghiệp vụ đã xác định (Known rules)

- Khách thanh toán không cần tài khoản bắt buộc phải cung cấp địa chỉ email hợp lệ để nhận thông tin đơn hàng.
- Mỗi đơn hàng chỉ được phép áp dụng tối đa một mã giảm giá.
- Phương thức thanh toán khi nhận hàng (COD) chỉ khả dụng với các đơn hàng có tổng giá trị dưới 3.000.000 VND.
- Hệ thống sẽ chặn không cho thanh toán nếu địa chỉ giao hàng nằm ngoài vùng phục vụ của đối tác vận chuyển.

## Các vấn đề cần lưu ý hiện tại (Current concerns)

- Tỷ lệ người dùng thoát trang ở bước thanh toán hiện tại rất cao.
- Phí vận chuyển hiển thị quá muộn trong quy trình khiến khách hàng bất ngờ và hủy đơn.
- Khi thanh toán gặp lỗi, hệ thống bắt người dùng nhập lại quá nhiều thông tin từ đầu.

## Yêu cầu kết quả đầu ra (Needed output)

- Bản tóm tắt tính năng (Brief summary).
- Danh sách các giả định cần kiểm chứng (Assumptions).
- Danh sách các câu hỏi cần làm rõ thêm (Open questions).
- Danh sách các đầu việc tiếp theo dành cho BA (Action list).
