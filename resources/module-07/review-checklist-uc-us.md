# Checklist rà soát Use Case / User Story (Review Checklist)

## 1. Đối với Ca sử dụng (Use Case)

- **Tác nhân (Actor):** Đã làm rõ ai là người thực hiện hành động chính và các hệ thống hỗ trợ chưa?
- **Luồng chính (Main flow):** Đã mô tả đầy đủ, chi tiết các bước cốt lõi để đạt mục tiêu chưa?
- **Luồng thay thế (Alternate flow):** Các trường hợp rẽ nhánh nghiệp vụ (ví dụ: áp mã giảm giá thành công) đã được thể hiện đầy đủ chưa?
- **Luồng ngoại lệ (Exception flow):** Các trường hợp xảy ra sự cố lỗi (ví dụ: lỗi thanh toán) đã có luồng xử lý tương ứng chưa?
- **Sơ đồ:** Mỗi use case chi tiết đã có sequence diagram hoặc process flow thể hiện cùng luồng chưa?
- **Màn hình:** Hành động trong UC có trùng wording với hành động của Screen ID liên quan chưa?

## 2. Đối với Câu chuyện người dùng (User Story)

- **Vai trò (Role):** Đối tượng người dùng trong câu chuyện đã được định nghĩa cụ thể chưa (tránh viết chung chung kiểu 'người dùng')?
- **Mục tiêu (Goal):** Hành động mong muốn của người dùng có rõ ràng và khả thi không?
- **Lợi ích (Benefit):** Giá trị nghiệp vụ nhận lại có thực tế và hợp lý không?

## 3. Đối với Tiêu chí nghiệm thu (Acceptance Criteria)

- **Khả năng kiểm thử (Testability):** Tiêu chí nghiệm thu có thể đo lường và viết thành kịch bản kiểm thử (test case) được không?
- **Độ chi tiết:** Tiêu chí có bị viết quá chung chung, mơ hồ không?
- **Độ chính xác:** Nội dung tiêu chí có phản ánh đúng các quy tắc nghiệp vụ (business rules) của dự án không?
- **Truy vết:** Mỗi AC có mã ổn định và liên kết tới story/test case tương ứng chưa?
