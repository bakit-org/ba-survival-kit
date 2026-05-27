# Smoke Testing and Skill Usage Guide

This guide contains the verification matrix for all 20 skills defined in the repository. Antigravity routes prompts dynamically using the `description` header inside each skill folder's `SKILL.md`; `name` identifies the selected skill.

---

## 1. Skill Verification Matrix

| Target Skill | Sample User Prompt (Vietnamese) | Expected Deliverable / Outcome |
| :--- | :--- | :--- |
| **`brief-to-structured-notes`** | *"Tóm tắt bản brief dự án thô này thành ghi chú công việc có cấu trúc"* | Generates `brief-summary.md` and `working-notes.md` |
| **`meeting-notes-summary`** | *"Đọc transcript cuộc họp này và rút ra các quyết định, action items"* | Generates `meeting-notes-summary.md` |
| **`requirements-intake-summary`** | *"Phân tích intake brief này và chỉ ra các rủi ro, kẽ hở nghiệp vụ"* | Generates `requirements-intake-summary.md` |
| **`wireframe-request-prep`** | *"Chuẩn bị request Figma MCP cho màn hình thanh toán"* | Generates `wireframe-request.md` with Screen ID |
| **`wireframe-review-note-generator`**| *"Rà soát frame Figma MCP này theo wireframe request"* | Generates `wireframe-review-notes.md` with frame reference |
| **`wireframe-from-requirement`** | *"Dựng khung xương wireframe từ mô tả yêu cầu chức năng này"* | Generates `wireframe-pack.md` |
| **`screen-layout-draft`** | *"Phác thảo bố cục layout màn hình Checkout Checkout Step 2"* | Generates `screen-layout-draft.md` |
| **`prototype-note-generator`** | *"Ghi nhận các luồng tương tác và chuyển động màn hình giữa Login và Cart"*| Generates `prototype-notes.md` |
| **`screen-spec-from-wireframe`** | *"Viết tài liệu đặc tả màn hình chi tiết từ bản vẽ layout này"* | Generates `screen-description.md` |
| **`field-rules-generator`** | *"Tạo các quy tắc kiểm tra logic dữ liệu (validation rules) cho các trường"* | Generates `field-rules.md` |
| **`screen-state-drafter`** | *"Đặc tả các trạng thái màn hình: loading, error, empty, offline"* | Generates `screen-states.md` |
| **`activity-flow-generator`** | *"Vẽ sơ đồ quy trình Activity Flow bằng Mermaid cho luồng Checkout"* | Generates `activity-flow.md` |
| **`sequence-diagram-generator`** | *"Vẽ sơ đồ Sequence Diagram Mermaid mô tả cuộc gọi API thanh toán"* | Generates `sequence-diagram.md` |
| **`ascii-flow-generator`** | *"Vẽ sơ đồ ASCII nhanh cho luồng tương tác Checkout"* | Generates `ascii-flow.md` |
| **`use-case-generator`** | *"Viết ca sử dụng Use Case chi tiết cho tính năng nhập mã coupon"* | Generates `use-cases.md` |
| **`user-story-generator`** | *"Tạo danh sách các User Stories cho tính năng chọn phương thức Ship"* | Generates `user-stories.md` |
| **`acceptance-criteria-generator`**| *"Viết tiêu chí nghiệm thu Acceptance Criteria cho các User Stories này"*| Generates `acceptance-criteria.md` |
| **`review-checklist-generator`** | *"Tạo checklist kiểm duyệt chất lượng tài liệu đặc tả màn hình"* | Generates `review-checklist.md` |
| **`test-case-generator`** | *"Sinh kịch bản test cases kiểm thử từ tài liệu User Story và AC"* | Generates `test-cases.md` |
| **`mini-doc-pack-generator`** | *"Hợp nhất đầy đủ các tài liệu BA này thành Mini BA Pack bàn giao"* | Generates complete `mini-ba-pack.md` with trace IDs |

---

## 2. Running a Manual Smoke Test

1. Open Antigravity in this workspace.
2. Select any prompt from the table above.
3. Check that Antigravity invokes the correct target skill.
4. Verify that the generated file contains all sections specified in the corresponding template file under `templates/`.
5. Run the hard guardrail check:
   ```bash
   python3 scripts/validate-document-quality.py --doc <path-to-generated-file>
   ```

## Figma MCP Lab Check

1. Confirm an authorized Figma MCP connection exists in the course workspace.
2. Generate `wireframe-request.md`, invoke Figma MCP, and record its frame or node reference.
3. Verify the review note uses the same Screen ID and action labels as the request.

## Installed Payload Check

```bash
./scripts/install-antigravity-workspace.sh
test -f .agents/ba-survival-kit/scripts/validate-document-quality.py
python3 .agents/ba-survival-kit/scripts/validate-document-quality.py --doc resources/module-08/sample-mini-ba-pack.md
```
