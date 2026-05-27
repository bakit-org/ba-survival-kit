# Hướng dẫn nhanh về Figma MCP (Figma MCP Quick Guide)

## Figma MCP trong khóa học này dùng để làm gì?

- Tạo bản phác thảo cấu trúc màn hình (wireframe draft) một cách tự động.
- Hỗ trợ hình dung bố cục (layout) màn hình nhanh hơn.
- Hỗ trợ BA rà soát luồng chuyển đổi giữa các màn hình (screen flow).
- Trả về tham chiếu frame/node để BA ghi nhận bằng chứng review trong Markdown.

## Flow thực hành

1. Chạy `wireframe-request-prep` để tạo request có Screen ID, trường, hành động và trạng thái.
2. Gửi request qua kết nối Figma MCP đã cấu hình trong Antigravity.
3. Ghi lại frame/node reference của bản nháp trả về.
4. Chạy `wireframe-review-note-generator` để đối chiếu frame với request nguồn.

## Khi nào nên sử dụng?

- Khi các thông tin mô tả màn hình (brief) đã tương đối rõ ràng.
- Khi cần có giao diện trực quan để thảo luận nhanh về bố cục và các nút hành động (actions) với team.
- Khi chuẩn bị viết tài liệu đặc tả màn hình chi tiết (screen spec) ở bước sau.

## Khi nào chưa cần sử dụng?

- Khi mới chỉ ở bước thu thập yêu cầu sơ bộ (requirements intake).
- Khi các quy tắc nghiệp vụ cốt lõi (business logic) còn quá mơ hồ.
- Khi chưa xác định rõ các hành động chính của người dùng (user actions).

## BA cần rà soát (review) gì sau khi có bản vẽ wireframe từ AI?

- **Mục đích màn hình (Screen purpose):** Bản vẽ có thể hiện đúng vai trò cốt lõi của màn hình không?
- **Danh sách trường dữ liệu (Field coverage):** Có bị thiếu hay thừa các ô nhập liệu, thông tin hiển thị không?
- **Các nút hành động (Action coverage):** Đã có đủ các nút bấm cần thiết (nhập mã, hủy đơn, xác nhận, quay lại) chưa?
- **Các trạng thái màn hình (State coverage):** Đã hiển thị đủ trạng thái thành công, thất bại, đang tải (loading) hay chưa?
- **Quy tắc kiểm tra dữ liệu (Validation coverage):** Bản vẽ có gợi ý các thông báo lỗi hoặc vô hiệu hóa nút bấm khi người dùng nhập sai không?
- **Bằng chứng MCP:** Ghi rõ Screen ID và frame/node reference nào đã được review.
