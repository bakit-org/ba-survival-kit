# Tài liệu đặc tả chi tiết màn hình mẫu - Bước thanh toán (Sample Screen Spec)

## Thông tin màn hình (Screen info)

- **Tên màn hình (Screen name):** Bước thanh toán đơn hàng (Checkout Payment Step)
- **Mã màn hình (Screen ID):** CHK-PAY-01
- **Mục đích (Purpose):** Cho phép người dùng lựa chọn phương thức thanh toán và bấm xác nhận đơn hàng.
- **Luồng quy trình liên quan (Related flow):** Quy trình đặt hàng và thanh toán (Checkout flow).

## Hành động của người dùng (User actions)

| Hành động (Action) | Điều kiện kích hoạt (Trigger) | Kết quả xử lý (Result) |
|---|---|---|
| Chọn phương thức thanh toán | Người dùng click chọn một tùy chọn (COD, thẻ, ví) | Hệ thống cập nhật phương thức thanh toán được chọn và kiểm tra tính hợp lệ |
| Áp dụng mã giảm giá | Người dùng nhập mã và click nút `Áp dụng` | Hệ thống kiểm tra mã, cập nhật tổng số tiền đơn hàng hoặc báo lỗi |
| Xác nhận đặt hàng | Người dùng click nút `Xác nhận đơn hàng` | Hệ thống tạo đơn hàng hoặc gọi luồng xử lý thanh toán |
| Thử lại thanh toán | Người dùng click nút `Thử lại` sau khi lỗi thanh toán | Hệ thống gọi lại luồng thanh toán cho đơn hàng đang chờ (pending payment) |

## Danh sách trường dữ liệu (Fields)

| Trường dữ liệu (Field) | Kiểu dữ liệu / Hiển thị | Bắt buộc | Mặc định | Ghi chú (Notes) |
|---|---|---|---|---|
| Mã giảm giá (Discount code) | Ô nhập văn bản (Text input) | Không | Trống | Chỉ hỗ trợ áp dụng tối đa một mã trên một đơn hàng |
| Phương thức thanh toán (Payment method) | Nhóm nút chọn duy nhất (Radio group) | Có | Không | Tùy chọn COD chỉ hiển thị khi tổng tiền hàng < 3.000.000 VND |
| Tóm tắt đơn hàng (Order summary) | Bảng hiển thị thông tin (Read-only panel) | Có | Tự động | Hiển thị: Tiền hàng tạm tính, phí ship, số tiền giảm, tổng thanh toán |

## Quy tắc hiển thị (Display rules)

- Trên giao diện Desktop: bảng tóm tắt đơn hàng hiển thị cố định ở thanh bên phải (right panel).
- Trên giao diện Mobile: bảng tóm tắt đơn hàng có thể thu gọn lại để tối ưu hóa không gian.
- Nếu phương thức COD không khả dụng do đơn hàng vượt hạn mức, tùy chọn COD sẽ hiển thị ở trạng thái bị vô hiệu hóa (disabled) kèm dòng ghi chú giải thích lý do bên dưới.

## Quy tắc tương tác và hành vi (Behavior rules)

- Nút `Xác nhận đơn hàng` chỉ được kích hoạt (enabled) sau khi người dùng đã lựa chọn một phương thức thanh toán hợp lệ.
- Nếu cổng thanh toán phản hồi chậm (gateway timeout), người dùng sẽ được giữ lại màn hình hiện tại và giao diện hiển thị nút cho phép bấm thử lại (retry).
- Nếu mã giảm giá được áp dụng thành công, hệ thống phải cập nhật lại ngay số tiền giảm và tổng thanh toán trên bảng tóm tắt đơn hàng.

## Quy tắc kiểm tra tính hợp lệ dữ liệu (Validation rules)

- Nếu mã giảm giá nhập vào không tồn tại hoặc đã hết hạn, hệ thống hiển thị thông báo lỗi tương ứng bên dưới ô nhập.
- Nếu người dùng bấm xác nhận đơn hàng khi chưa chọn phương thức thanh toán, hệ thống chặn thao tác và hiển thị cảnh báo lỗi.
- Nếu giá trị đơn hàng vượt quá 3 triệu đồng, hệ thống không cho phép người dùng chọn phương thức COD.

## Các trạng thái màn hình (States)

- **Trạng thái mặc định (Default state):** Hiển thị đầy đủ các phần thông tin và phương thức thanh toán để người dùng thao tác.
- **Trạng thái lỗi (Error state):** Hiển thị thông báo cảnh báo khi mã giảm giá sai hoặc thanh toán gặp sự cố gián đoạn.
- **Trạng thái thành công (Success state):** Đơn hàng được ghi nhận thành công, hệ thống chuyển tiếp người dùng sang màn hình cảm ơn (Thank you screen).
- **Trạng thái COD không khả dụng (COD unavailable state):** Nút chọn COD bị mờ (disabled) do đơn hàng vượt giới hạn giá trị.

## Thông báo hệ thống (Messages)

- `Mã giảm giá không hợp lệ hoặc đã hết hạn sử dụng.`
- `Vui lòng lựa chọn phương thức thanh toán.`
- `COD không áp dụng cho đơn hàng có giá trị từ 3.000.000 VND trở lên.`
- `Giao dịch thanh toán bị gián đoạn. Vui lòng thử lại.`
