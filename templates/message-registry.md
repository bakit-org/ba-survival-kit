---
title: System Messages and Notifications Registry
status: draft
updated: 2026-05-24
---

# System Messages and Notifications Registry

This registry serves as the single source of truth for all user-facing notification messages, validation error alerts, and system toasts. Under the screen specifications, reference messages using their **Message Code** (e.g. `[MSG-001]`).

---

## 1. Message Registry Table

| Message Code | Message Type | Default Content | Trigger / Validation Condition |
| :--- | :--- | :--- | :--- |
| **MSG-001** | Inline Error | *"Product Name cannot be empty. Please enter a valid name."* | Triggered when the user attempts to submit the form with the Product Name field blank. |
| **MSG-002** | Inline Error | *"Invalid selection. Please choose an option from the list."* | Triggered when a dropdown selection is corrupted or doesn't match predefined options. |
| **MSG-003** | Toast Alert | *"Success! The product has been successfully updated."* | Displayed as a floating green notification on successful database transaction. |
| **MSG-004** | Toast Alert | *"Error! Unable to save changes. Connection timed out."* | Displayed as a floating red notification on database write failure. |
| **MSG-005** | Modal Dialog | *"Discard changes? You have unsaved changes that will be lost."* | Displayed when user clicks 'Cancel' button or attempts navigation while form is dirty. |
