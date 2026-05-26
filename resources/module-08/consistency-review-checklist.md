# Checklist rà soát tính nhất quán của Tài liệu (Consistency Review Checklist)

## 1. Thống nhất thuật ngữ (Terminology)

- Tên các màn hình (Screen names) có đồng nhất giữa bản vẽ giao diện, biểu đồ luồng và tài liệu đặc tả không?
- Tên các nút hành động (Action names - ví dụ: Xác nhận đặt hàng / Đặt hàng) có bị gọi khác nhau ở các tài liệu khác nhau không?
- Tên của tác nhân (Actor names) thực hiện quy trình có nhất quán không?

## 2. Thống nhất luồng nghiệp vụ (Flow)

- Các khu vực thông tin và nút bấm trên giao diện (Wireframe) có khớp hoàn toàn với mô tả trong đặc tả màn hình (Screen Spec) không?
- Các quy tắc nghiệp vụ trong đặc tả màn hình có ăn khớp với kịch bản các ca sử dụng (Use Case) không?
- Các câu chuyện người dùng (User Stories) có phản ánh chính xác các luồng hoạt động đã vẽ trên biểu đồ (Diagrams) không?

## 3. Tính khả thi kiểm thử & Truy vết (Testability)

- Mọi kịch bản kiểm thử (Test Cases) có liên kết (trace) ngược lại được về từng tiêu chí nghiệm thu (Acceptance Criteria) cụ thể không?
- Nội dung thông báo lỗi và cảnh báo (Messages) có trùng khớp hoàn toàn giữa tài liệu đặc tả màn hình và kịch bản kiểm thử không?

## 4. Thống nhất phạm vi (Scope)

- Có tài liệu hoặc kịch bản nào bị viết thừa, mô tả các tính năng đã bị loại trừ trong giai đoạn 1 (Phase 1 Scope Exclusions) không?
