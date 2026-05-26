# Biên bản cuộc họp mẫu (Meeting Notes Sample)

## Thông tin cuộc họp

- Chủ đề: Luồng thanh toán (Checkout flow) cho website thương mại điện tử
- Thời lượng: 45 phút
- Người tham gia:
  - Product Owner (PO)
  - Business Analyst (BA)
  - Tech Lead
  - QA Lead

## Nội dung ghi chú thô

- Khách mua hàng có thể thanh toán bằng tài khoản đã đăng nhập hoặc chọn thanh toán không cần tài khoản (guest checkout).
- Nếu thanh toán không cần tài khoản thì vẫn bắt buộc nhập email để nhận thông tin xác nhận đơn hàng.
- Mục tiêu của team: giảm tỷ lệ bỏ sót đơn hàng (drop-off) ở bước thanh toán.
- Cần hiển thị rõ ràng phí vận chuyển cho người dùng thấy trước khi họ bấm xác nhận thanh toán.
- Có hỗ trợ áp dụng mã giảm giá, nhưng mỗi đơn hàng chỉ được sử dụng tối đa một mã.
- Hệ thống phải kiểm tra tính hợp lệ của mã giảm giá trước khi trừ vào tổng tiền.
- Nếu thanh toán thất bại, đơn hàng sẽ không được chuyển sang trạng thái hoàn tất.
- Có thể tạo đơn hàng ở trạng thái "Chờ thanh toán" (Pending payment) để cho phép người dùng thanh toán lại (retry) khi cần.
- Các phương thức thanh toán hỗ trợ trong giai đoạn đầu:
  - Thẻ ATM nội địa
  - Ví điện tử
  - Thanh toán khi nhận hàng (COD)
- Phương thức COD chỉ áp dụng cho đơn hàng có tổng trị giá dưới 3 triệu đồng.
- Nếu địa chỉ nhận hàng của người dùng nằm ngoài vùng hỗ trợ giao hàng thì hệ thống phải chặn không cho thanh toán.
- Người dùng có thể quay lại giỏ hàng để cập nhật số lượng sản phẩm.
- Thiết kế trên Desktop: hiển thị bảng tóm tắt đơn hàng (Order summary) cố định ở thanh bên phải (right panel).
- Thiết kế trên Mobile: bảng tóm tắt đơn hàng có thể thu gọn lại cho thoáng màn hình.
- Ý kiến của QA Lead:
  - Nếu mã giảm giá hết hạn thì hiển thị thông báo lỗi cụ thể như thế nào?
  - Nếu cổng thanh toán bị nghẽn (gateway timeout) thì giao diện sẽ hiển thị gì cho người dùng?
- Ý kiến của Tech Lead: Phí vận chuyển sẽ được tính toán thông qua một dịch vụ riêng (shipping service API).
- Ý kiến của Product Owner: Trong giai đoạn đầu, chưa hỗ trợ việc chia một đơn hàng để giao đến nhiều địa chỉ khác nhau.

## Các trao đổi và quyết định quan trọng

- "Bắt buộc phải có chức năng thanh toán không cần đăng nhập (guest checkout) ngay trong giai đoạn 1."
- "Không được để người dùng nhập thông tin thanh toán xong xuôi rồi mới hiển thị phí vận chuyển. Phải minh bạch ngay từ đầu."
- "Nếu thanh toán lỗi, phải cho người dùng thử lại ngay tại màn hình đó, đừng bắt họ phải nhập lại thông tin từ đầu."
