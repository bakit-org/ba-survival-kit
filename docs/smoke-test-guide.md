# Smoke Testing and Routing Guide

Since Antigravity routes requests dynamically based on skill descriptions, use this test matrix to verify that the skills trigger correctly.

---

## 1. Routing Verification Matrix

| Target Skill | Sample User Prompt | Expected Output |
| :--- | :--- | :--- |
| **`ba-generate-ui-styleguide`** | *"Đọc file brand-guidelines.txt và sinh bộ quy chuẩn thiết kế Figma Make cho tôi"* | Generates `figma-make-guidelines.md` in the workspace |
| **`ba-generate-srs`** | *"Dịch bản ghi họp examples/meeting-transcript.txt thành tài liệu SRS và tạo đặc tả các màn hình để chạy Figma"* | Generates `srs.md` and screen specs under `srs-screens/` |
| **`ba-generate-brd`** | *"Tạo tài liệu BRD cho dự án checkout mới từ meeting-transcript.txt"* | Generates a clean business requirement draft `brd.md` |
| **`ba-generate-user-stories`** | *"Sinh danh sách User Stories kèm Acceptance Criteria cho cổng thanh toán mới"* | Generates `user-stories.md` |
| **`ba-generate-raci`** | *"Phân chia nhiệm vụ các vai trò và vẽ quy trình luồng thanh toán"* | Generates RACI tables and a Mermaid flowchart |
| **`ba-gap-check`** | *"Quét lỗi logic và kẽ hở giữa bản nháp srs.md với transcript gốc"* | Outputs a gap analysis report |
| **`ba-polish-doc`** | *"Đánh bóng tài liệu srs.md này sang chế độ client-ready"* | Rewrites document for clients |

---

## 2. Running a Manual Smoke Test

1. Open Antigravity in this workspace.
2. Run the first prompt in the matrix.
3. Check that Antigravity selects the correct skill and generates the expected output file.
4. Verify that the generated file contains all structural sections from the templates.
