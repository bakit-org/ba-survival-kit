# Cấu trúc Bộ tài liệu BA thu nhỏ (Mini BA Pack Structure)

## Yêu cầu tài liệu hợp nhất

`mini-ba-pack.md` là một tài liệu bàn giao duy nhất chứa nội dung đầy đủ, không chỉ là trang index hoặc danh sách liên kết.

## Thứ tự nội dung bắt buộc

1. **Bản tóm tắt yêu cầu sơ bộ** (Brief summary).
2. **Giao diện phác thảo & ghi chú** (Wireframe notes).
3. **Đặc tả chi tiết màn hình** (Screen description / Screen spec).
4. **Các sơ đồ quy trình** (Diagrams - Activity / Sequence / ASCII).
5. **Đặc tả các ca sử dụng** (Use cases).
6. **Câu chuyện người dùng & tiêu chí nghiệm thu** (User stories & AC).
7. **Checklist kiểm duyệt chất lượng** (Review checklist).
8. **Kịch bản kiểm thử mẫu** (Test cases).

## Lưu ý khi đóng gói

Mỗi phần phải chứa nội dung đã duyệt từ artifact nguồn, ghi nguồn và giữ nguyên ID. Chuỗi truy vết tối thiểu phải nhìn thấy trực tiếp trong tài liệu:

`CHK-{DOMAIN}-{NN} -> UC-{FLOW}-{NN} -> US-{FLOW}-{NN} -> AC-{FLOW}-{NN} -> TC-{FLOW}-{NN}`, cùng các `MSG-{TYPE}-{NN}` được tái sử dụng nguyên văn.
