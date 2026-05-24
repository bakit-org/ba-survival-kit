# BA Personal Survival Kit - Bộ Đồ Nghề Sinh Tồn Cho Business Analyst

Dành cho các BA bận rộn, thường xuyên phải đối mặt với các bản ghi họp (meeting transcript) lộn xộn, ghi chú viết vội của khách hàng hoặc các tài liệu cũ nát. Bộ công cụ này kết hợp sức mạnh của **Antigravity AI** và **Figma Make** để tự động hóa toàn bộ công việc viết tài liệu và dựng wireframe chỉ với vài dòng lệnh.

---

## 1. Danh sách đồ nghề (Skills Catalog)

Bộ công cụ được chia làm 3 nhóm chính theo đúng quy trình làm việc thực tế:

```text
                       [ NGUYÊN LIỆU THÔ ]
                  (Bản ghi họp, Brandbook, Email)
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
 ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
 │ NHÓM SETUP  │         │  NHÓM SINH  │         │ NHÓM REVIEW │
 │ (Styleguide,│         │  TÀI LIỆU   │         │ & HOÀN THIỆN│
 │   Intake)   │         │ (BRD, SRS,  │         │ (Gap-check, │
 │             │         │  Stories...)│         │   Polish)   │
 └─────────────┘         └─────────────┘         └─────────────┘
```

### Nhóm 1: Chuẩn bị & Cấu hình (Setup Helpers)
*   **[ba-generate-ui-styleguide](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-ui-styleguide/SKILL.md):** Bóc tách tài liệu thương hiệu của khách hàng (logo, màu sắc) để sinh file cấu hình giao diện `figma-make-guidelines.md`. Đảm bảo các màn hình vẽ ra sau này đồng bộ về màu sắc và phong cách.
*   **[ba-parse-intake](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-parse-intake/SKILL.md):** (Không bắt buộc) Dùng khi bản ghi họp quá dài (>5000 từ). AI sẽ lọc bớt rác và tóm tắt thành một bản brief cô đọng trước khi viết tài liệu chi tiết.

### Nhóm 2: Sinh tài liệu tự động (Primary Generators)
*   **[ba-generate-srs](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-srs/SKILL.md):** (Mỳ ăn liền nhất) Sinh file đặc tả hệ thống `srs.md` và thư mục `srs-screens/` chứa đặc tả chi tiết từng màn hình (tách bạch Display, Behaviour, và Validation Rules cho từng field). Tài liệu sử dụng các mã lỗi code hóa (ví dụ: `[MSG-001]`) trỏ đến registry tập trung tại `srs-screens/message-registry.md`. Bản nháp phân mảnh có thể gộp nhanh bằng script gộp file [scripts/merge-srs.sh](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/scripts/merge-srs.sh).
*   **[ba-generate-brd](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-brd/SKILL.md):** Viết nhanh tài liệu yêu cầu nghiệp vụ tập trung vào bài toán kinh doanh, mục tiêu và phạm vi (Scope).
*   **[ba-generate-user-stories](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-user-stories/SKILL.md):** Chia nhỏ yêu cầu thành danh sách User Stories kèm Acceptance Criteria (AC) chuẩn Agile cho đội phát triển.
*   **[ba-generate-urd](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-urd/SKILL.md):** Sinh tài liệu yêu cầu người dùng (tập trung vào pain points của user).
*   **[ba-generate-prd](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-prd/SKILL.md):** Sinh tài liệu yêu cầu sản phẩm (Product vision, metrics, roadmap).
*   **[ba-generate-frd](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-frd/SKILL.md):** Sinh tài liệu mô tả chi tiết logic tính toán và validate của hệ thống.
*   **[ba-generate-use-cases](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-use-cases/SKILL.md):** Đặc tả các kịch bản sử dụng hệ thống (Main flow, Alternative flow).
*   **[ba-generate-raci](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-generate-raci/SKILL.md):** Phân vai trách nhiệm dự án và vẽ sơ đồ quy trình nghiệp vụ bằng mã Mermaid.

### Nhóm 3: Kiểm định & Đánh bóng (Reviewers & Polishers)
*   **[ba-gap-check](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-gap-check/SKILL.md):** So khớp bản nháp tài liệu với bản ghi họp gốc để tìm ra các lỗi logic, mâu thuẫn thông tin hoặc những giả định chưa được làm rõ.
*   **[ba-polish-doc](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/skills/ba-polish-doc/SKILL.md):** Sửa câu từ chuyên nghiệp. Hỗ trợ chế độ `--internal` (cho nội bộ, giữ nguyên câu hỏi thô) và `--client-ready` (làm mượt câu chữ, gom câu hỏi thành lịch họp để gửi khách hàng).

---

## 2. Hướng dẫn sử dụng step-by-step (Cho người mới bắt đầu)

Dưới đây là quy trình thực tế từ lúc nhận yêu cầu thô đến khi bàn giao sản phẩm:

```text
               BẢN GHI HỌP THÔ & BRANDBOOK KHÁCH HÀNG
                                │
                                ▼
  BƯỚC 1: Chạy script cài đặt (Chỉ cần làm một lần duy nhất)
                                │
                                ▼
  BƯỚC 2: Cấu hình giao diện thương hiệu (ba-generate-ui-styleguide)
                                │
                                ▼
  BƯỚC 3: Sinh tài liệu SRS & Prompt Figma (ba-generate-srs)
                                │
                                ├────────────────────────┐
                                ▼                        ▼
                    [ Tài liệu srs.md ]        [ srs-screens/ ]
                                                 (Mô tả & Prompts)
                                                         │
                                                         ▼
                                       BƯỚC 4: Vẽ UI tự động trên Figma
                                                         │
                                                         ▼
                                       BƯỚC 5: Check lỗi logic (ba-gap-check)
                                                         │
                                                         ▼
                                       BƯỚC 6: Đánh bóng gửi khách (ba-polish-doc)
```

### Bước 1: Cài đặt bộ skill vào máy
Mở Terminal tại thư mục dự án và chạy lệnh sau để Antigravity nhận diện bộ công cụ:

*   **Nếu chỉ muốn dùng cho dự án này (Workspace level):**
    ```bash
    ./scripts/install-antigravity-workspace.sh
    ```
*   **Nếu muốn dùng ở bất kỳ thư mục nào trên máy (Global level):**
    ```bash
    ./scripts/install-antigravity-global.sh
    ```

### Bước 2: Thiết lập quy chuẩn giao diện (Màu sắc, Bo góc)
Nếu khách hàng gửi brand guidelines hoặc có yêu cầu thiết kế cụ thể, hãy yêu cầu Antigravity phân tích và lưu lại style guide:
*   *Lệnh gõ:* `"Đọc file brand-book.pdf này và sinh bộ quy chuẩn thiết kế Figma Make"`
*   *Kết quả:* AI sẽ tự tạo ra file [shared/figma-make-guidelines.md](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/shared/figma-layout-guidelines.md) để các bước sau dùng chung.

### Bước 3: Sinh tài liệu SRS và Prompt vẽ màn hình
Đưa bản ghi cuộc họp hoặc ghi chú yêu cầu vào dự án và gõ lệnh:
*   *Lệnh gõ:* `"Dịch file meeting-notes.txt thành tài liệu SRS và tạo đặc tả màn hình Figma Make"`
*   *Kết quả:* 
    *   File [srs.md](file:///Users/damtuana/Projects/BA-kit-allrepos/BA-skills/templates/srs.md) (Dự thảo SRS tổng quan).
    *   Thư mục `srs-screens/` chứa các file đặc tả chi tiết từng màn hình (tách bạch Display, Behaviour, và Validation Rules cho mỗi field).
    *   File `srs-screens/message-registry.md` chứa toàn bộ câu chữ thông báo lỗi của hệ thống tương ứng với các mã lỗi (ví dụ: `[MSG-001]`).

### Bước 3.5: Gộp tài liệu màn hình thành một file SRS tổng hợp (Tùy chọn)
Nếu bạn cần gửi một file tài liệu SRS duy nhất cho khách hàng thay vì các file màn hình phân mảnh, hãy chạy script gộp file:
```bash
./scripts/merge-srs.sh
```
Script này sẽ tự động gộp nội dung của `srs.md`, tất cả các màn hình trong `srs-screens/` và bảng thông báo `message-registry.md` vào một file duy nhất mang tên `srs-compiled.md`.

### Bước 4: Vẽ giao diện tự động trên Figma
1. Mở file thiết kế của bạn trong Figma.
2. Click biểu tượng **Actions** (hình ngôi sao trên thanh công cụ) -> Chọn **First Draft**.
3. Mở các file trong thư mục `srs-screens/` vừa sinh, tìm phần **Figma Make Prompt**, copy toàn bộ nội dung trong ô và paste vào Figma First Draft -> Bấm **Generate**.
4. Chờ 30 giây để Figma tự động dựng khung xương wireframe hoàn chỉnh.

### Bước 5: Kiểm tra hạt sạn nghiệp vụ
Trước khi đóng gói, hãy nhờ AI đối soát chéo xem tài liệu đã viết có bị sót ý hoặc mâu thuẫn với lời khách hàng nói trong buổi họp hay không:
*   *Lệnh gõ:* `"Quét lỗi logic nghiệp vụ và kẽ hở thông tin của file srs.md so với meeting-notes.txt"`
*   *Kết quả:* Một file báo cáo chỉ rõ chỗ nào viết sai logic, chỗ nào khách nói A nhưng tài liệu viết B để bạn sửa.

### Bước 6: Đánh bóng và xuất bản gửi khách hàng
Sau khi đã sửa các lỗi logic, tiến hành làm đẹp câu từ để sẵn sàng gửi cho khách hàng duyệt:
*   *Lệnh gõ:* `"Đánh bóng tài liệu srs.md sang chế độ client-ready"`
*   *Kết quả:* AI sẽ tự động viết lại các phần giả định một cách lịch sự, xóa các câu hỏi lập trình thô và chuyển các câu hỏi chưa rõ thành một chương trình họp (Agenda) gọn gàng ở cuối trang.
