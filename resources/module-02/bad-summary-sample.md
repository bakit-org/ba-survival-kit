# Ví dụ kết quả tóm tắt chưa đạt (Bad Summary Sample)

Thanh toán (Checkout) là một tính năng cực kỳ quan trọng giúp người dùng hoàn tất việc mua sắm. Tính năng này cần mang lại trải nghiệm thuận tiện và nhanh chóng cho khách hàng. Có nhiều điểm cần chú ý trong quá trình triển khai như xử lý mã giảm giá, phí vận chuyển và tích hợp thanh toán.

Một số việc cần làm tiếp theo:
- Vẽ giao diện (wireframe)
- Viết tài liệu nghiệp vụ
- Kiểm tra các luồng logic

## Các vấn đề khiến kết quả này chưa đạt (Nhận xét từ Giảng viên)

- **Thông tin quá chung chung:** Không chỉ ra được các quy tắc nghiệp vụ cốt lõi (ví dụ: hạn mức COD dưới 3 triệu, bắt buộc nhập email đối với guest checkout).
- **Thiếu phần Giả định (Assumptions):** Không nêu được các giả định làm nền tảng phát triển (ví dụ: cách tính phí ship qua bên thứ ba).
- **Thiếu các Câu hỏi chưa rõ (Open Questions):** Bỏ qua các vấn đề cốt lõi cần làm rõ với PO hoặc Dev (ví dụ: thời gian giữ đơn hàng để chờ retry).
- **Đầu việc tiếp theo mơ hồ:** Các bước tiếp theo viết rất chung chung, không chỉ rõ sản phẩm bàn giao (artifact) cụ thể nào cần tạo ra.
