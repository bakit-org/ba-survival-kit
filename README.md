# BA Personal Survival Kit - Bộ Đồ Nghề Sinh Tồn Cho Business Analyst

Dành cho các BA bận rộn, học viên của khóa học **"AI Agent for IT Business Analyst with Antigravity"**. Bộ công cụ này kết hợp sức mạnh của **Antigravity AI** và **Figma MCP** để tự động hóa toàn bộ công việc viết tài liệu đặc tả, vẽ sơ đồ và dựng wireframe chỉ với vài dòng lệnh.

---

## 1. Danh sách đồ nghề (Skills Catalog)

Bộ công cụ gồm 20 skills được đóng gói sẵn và chia thành các nhóm tương ứng với lộ trình học tập thực tế:

```text
                        [ NGUYÊN LIỆU THÔ ]
                   (Bản ghi họp, Brief thô, Email)
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
  ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
  │ NHÓM SETUP  │         │  NHÓM SINH  │         │ NHÓM REVIEW │
  │ & GHI CHÚ   │         │  TÀI LIỆU   │         │ & HOÀN THIỆN│
  │ (Summary,   │         │ (Spec, UC,  │         │ (Checklist, │
  │  Intake)    │         │ US, Diagram)│         │ Test Cases) │
  └─────────────┘         └─────────────┘         └─────────────┘
```

### Nhóm 1: Tóm tắt & Cấu hình (Notes/Brief Setup)
*   **`brief-to-structured-notes`:** Tóm tắt brief dự án thô thành ghi chú làm việc có cấu trúc (Context, assumptions, open questions, risks).
*   **`meeting-notes-summary`:** Đọc transcript họp thô và chắt lọc các quyết định (decisions), action items và các điểm cần làm rõ.
*   **`requirements-intake-summary`:** Phân tích tài liệu intake thô để bóc tách yêu cầu, phạm vi và những lỗ hổng nghiệp vụ ban đầu.

### Nhóm 2: Thiết kế giao diện (Wireframing & Prototyping)
*   **`wireframe-request-prep`:** Chuẩn bị brief đặc tả chi tiết màn hình (fields, actions, constraints) để làm input vẽ wireframe.
*   **`wireframe-review-note-generator`:** Rà soát và ghi chú lỗi nghiệp vụ, thiếu sót layout trên các bản thiết kế/wireframe thô.
*   **`wireframe-from-requirement`:** Chuyển yêu cầu nghiệp vụ thành mô tả khung xương màn hình (UI widgets, layout blocks) theo guideline.
*   **`screen-layout-draft`:** Phác thảo nhanh lưới bố cục (sections, grid) của màn hình dạng text hoặc block.
*   **`prototype-note-generator`:** Ghi chú các luồng tương tác, liên kết điều hướng và hiệu ứng chuyển cảnh giữa các màn hình.

### Nhóm 3: Đặc tả màn hình (Screen Specifications)
*   **`screen-spec-from-wireframe`:** Tạo tài liệu đặc tả màn hình chi tiết (fields list, display, behavior, validation rules và error codes).
*   **`field-rules-generator`:** Tạo bảng đặc tả chi tiết cho từng trường nhập liệu (kiểu dữ liệu, validation, default values).
*   **`screen-state-drafter`:** Thiết lập quy tắc hoạt động của màn hình theo các trạng thái (loading, default, empty, error, success).

### Nhóm 4: Vẽ biểu đồ (Diagramming)
*   **`activity-flow-generator`:** Vẽ quy trình nghiệp vụ (Activity flow) bằng mã Mermaid TD/LR.
*   **`sequence-diagram-generator`:** Vẽ trình tự tương tác hệ thống (Sequence diagram) bằng mã Mermaid.
*   **`ascii-flow-generator`:** Vẽ sơ đồ nhanh dạng chữ ASCII để nhúng trực tiếp vào ghi chú hoặc email.

### Nhóm 5: Ca sử dụng & Câu chuyện người dùng (Backlog/Stories)
*   **`use-case-generator`:** Đặc tả các kịch bản sử dụng hệ thống (Main flow, alternate flows, exception flows).
*   **`user-story-generator`:** Chia nhỏ yêu cầu thành danh sách User Stories dạng "As a..., I want..., So that...".
*   **`acceptance-criteria-generator`:** Viết tiêu chí nghiệm thu (Acceptance Criteria) chuẩn Gherkin (Given-When-Then).

### Nhóm 6: Kiểm thử & Đóng gói (QA & Documentation Pack)
*   **`review-checklist-generator`:** Sinh danh sách kiểm duyệt chất lượng tài liệu đặc tả để chuẩn bị gửi stakeholders.
*   **`test-case-generator`:** Tự động tạo bảng kịch bản kiểm thử (Test cases) từ User Stories và Acceptance Criteria.
*   **`mini-doc-pack-generator`:** Đóng gói và liên kết chéo các file tài liệu BA đơn lẻ thành một bộ hồ sơ bàn giao (Mini BA Pack) hoàn chỉnh.

---

## 2. Hướng dẫn cài đặt

Mở Terminal tại thư mục dự án và chạy các script sau để Antigravity IDE nhận diện bộ công cụ:

*   **Cài đặt cho không gian làm việc này (Workspace level):**
    ```bash
    ./scripts/install-antigravity-workspace.sh
    ```
*   **Cài đặt toàn cục trên máy của bạn (Global level):**
    ```bash
    ./scripts/install-antigravity-global.sh
    ```

---

## 3. Lộ trình thực hành theo Module (Step-by-Step Course Workflow)

Mỗi thư mục con trong `resources/` chứa đầy đủ nguyên liệu thô (inputs), templates, và outputs tham khảo để bạn luyện tập:

```text
resources/
  ├── module-01-ai-agent-foundation/           (Mindset review, chatbot vs agent)
  ├── module-02-antigravity-markdown-workflow/  (Làm quen Markdown-first, intake)
  ├── module-03-figma-mcp-for-ba/               (Figma MCP, wireframe review)
  ├── module-04-wireframe-prototype-with-skills/(Phác thảo wireframe login/form/cart)
  ├── module-05-screen-description-in-markdown/ (Viết spec màn hình & validation rules)
  ├── module-06-diagrams-in-markdown/          (Mermaid & ASCII flows)
  ├── module-07-use-cases-and-user-stories/     (Backlog: UC, US & AC)
  └── module-08-checklists-test-cases-mini-pack/(QA & Đóng gói hồ sơ bàn giao)
```

### Cách thực hành một Lab bài học:
1.  Tru cập vào thư mục `resources/module-XX/` tương ứng.
2.  Đọc đề bài và lấy thông tin thô trong thư mục `inputs` (hoặc các file brief mẫu).
3.  Mở Antigravity và gọi skill phù hợp của module (ví dụ: gõ `"Chạy skill user-story-generator cho file checkout-business-flow.md"`).
4.  Rà soát kết quả đầu ra Markdown, sửa lỗi logic và đối chiếu với checklist chất lượng.
5.  Nộp bài bằng file Markdown hoàn thiện.
