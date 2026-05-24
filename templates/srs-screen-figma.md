---
title: SRS Figma Screen Template
status: draft
updated: 2026-05-24
---

# Screen UI Specification: [Screen ID] - [Screen Name]

## 1. Screen Metadata

- **Screen ID:** e.g., SCR-001
- **Screen Name:** e.g., Product Details Dashboard
- **User Roles:** Primary users accessing this screen
- **Pre-conditions:** What state must the system/user be in to view this screen
- **Triggers & Entry Points:** How the user navigates here

## 2. Page Layout and Visual Zones

Describe the high-level wireframe zones (e.g., Header, Left Sidebar Navigation, Main Workspace Panel, Right Context Panel).

- **Zone A (Header):** [Describe elements, e.g., Logo, Profile dropdown, global search]
- **Zone B (Sidebar):** [Describe navigation items, e.g., Dashboard, Products, Sales, Settings]
- **Zone C (Main Panel):** [Describe primary content area, e.g., product detail card, tabs]

## 3. UI Component Details

For each UI element/field, specify the following details:

### Form Fields & Inputs

*   **Field 1: [Field Name, e.g., Product Name]**
    *   **Display Rules:** Text Input. Placeholder: "Enter product name". Active when page loads. Max length 100 characters.
    *   **Behaviour Rules:** Typing updates the local page state. Pressing Enter key triggers the Save Action.
    *   **Validation Rules:** Cannot be empty. If left blank, display inline error code `[MSG-001]`.

*   **Field 2: [Field Name, e.g., Status Selection]**
    *   **Display Rules:** Dropdown field. Options: [Active, Draft, Archived]. Default: "Draft". Disabled for read-only user roles.
    *   **Behaviour Rules:** Selecting an option updates the UI state immediately.
    *   **Validation Rules:** Must match options. If invalid selection, show inline error code `[MSG-002]`.

### Actions & Controls

*   **Action 1: [Action Name, e.g., Save Button]**
    *   **Display Rules:** Primary color button on the bottom right. Label: "Save". Enabled when form is modified.
    *   **Behaviour Rules:** Clicking submits the form. On success, navigates to the Details Page and triggers toast `[MSG-003]`. On failure, displays error toast `[MSG-004]`.
    *   **Validation Rules:** None.

### Data Tables / Visual Lists

*   **List 1: [List Name, e.g., Inventory List]**
    *   **Display Rules:** Grid/Table showing columns: [SKU, Location, Quantity, Status].
    *   **Behaviour Rules:** Clicking a row selects the item. Hovering over a row shows highlights.
    *   **Validation Rules:** None.


---

## 4. Figma Make Prompt (AI Wireframe Prompt)

> [!TIP]
> Copy and paste the fenced prompt below directly into the Figma Make plugin or AI prompt box.

```text
Design a web application screen for a [Describe Screen Goal / App Context].
Layout:
- Standard 1440px desktop wireframe, modern clean layout, use HSL harmonized colors (cool grays, deep blue accents).
- [Describe Zone A: e.g., Top header with a logo on the left, a center search bar, and a user profile avatar on the far right].
- [Describe Zone B: e.g., A left navigation sidebar containing icons and text labels for Dashboard, Products, Inventory, Reports, and Settings].
- [Describe Zone C: e.g., A spacious main content area displaying:
  1. A page title "Product Details" with a green badge indicating "In Stock".
  2. A form panel with fields: "Product Name" (text input with placeholder text), "Category" (dropdown field showing "Electronics"), and "Price" (number input showing "$599.99").
  3. A horizontal row of action buttons: a primary blue button labeled "Save Changes" and a secondary neutral outline button labeled "Cancel".
  4. An inventory data table with column headers: SKU, Location, Quantity, Status. Populate with 3 rows of realistic sample data.]
Style & Theme:
- Use clean modern typography, light mode background, clear hierarchy with cards, and subtle gray borders.
- Keep elements aligned on a standard grid with good spacing.
```

---

## 5. State Modifications & Edge Cases

- **Empty State:** [How the screen looks when no data is loaded]
- **Loading State:** [Skeletal loader layout]
- **Error State:** [Inline alerts or validation error message displays]
- **Mobile Responsive Layout:** [Layout adjustments for smaller viewports, e.g., collapsed hamburger menu]
