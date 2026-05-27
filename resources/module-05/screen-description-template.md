# Mẫu đặc tả chi tiết màn hình (Screen Description Template)

## Thông tin màn hình (Screen info)

- **Tên màn hình (Screen name):**
- **Mã màn hình (Screen ID):** [CHK-{SCREEN}-01]
- **Mục đích (Purpose):**
- **Luồng quy trình liên quan (Related flow):**
- **Ca sử dụng liên quan (Related Use Case ID):** [UC-{FLOW}-01]
- **Tham chiếu Figma MCP (Frame/Node reference):**

## Hành động của người dùng (User actions)

| Hành động (Action) | Điều kiện kích hoạt (Trigger) | Kết quả xử lý (Result) | Bước UC liên quan |
|---|---|---|---|
| [Tên hành động nghiệp vụ] | [Điều kiện kích hoạt] | [Kết quả xử lý] | [UC-{FLOW}-01 / bước] |

## Danh sách trường dữ liệu (Fields)

| Trường dữ liệu (Field) | Kiểu dữ liệu / Hiển thị | Bắt buộc | Mặc định | Ghi chú (Notes) |
|---|---|---|---|---|
| [Ví dụ: Họ và tên] | [Text box, tối đa 100 ký tự] | [Có] | [Trống] | [Không nhập ký tự đặc biệt] |

## Quy tắc hiển thị (Display rules)

- [Quy định về bố cục, ẩn/hiển các khối thông tin dựa trên giao diện hoặc thiết bị]

## Quy tắc tương tác và hành vi (Behavior rules)

- [Hệ thống phản hồi thế nào khi người dùng thao tác, ví dụ: tự động tính phí ship, enable/disable nút bấm]

## Quy tắc kiểm tra tính hợp lệ dữ liệu (Validation rules)

- [Các ràng buộc về dữ liệu nhập vào và xử lý lỗi]

## Các trạng thái màn hình (States)

- **Trạng thái mặc định (Default state):**
- **Trạng thái lỗi (Error state):**
- **Trạng thái thành công (Success state):**
- **Trạng thái không khả dụng (Unavailable state):**

## Thông báo hệ thống (Message list)

| Mã thông báo | Loại | Nội dung chính xác |
|---|---|---|
| MSG-ERR-01 | Lỗi | [Nội dung thông báo hiển thị trên giao diện] |
