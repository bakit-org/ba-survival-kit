# Runtime Adapters and Bridges

This folder is reserved for containing runtime-specific adapters and sync overlays.

---

## 1. Directory Structure (Deferred)

```text
runtimes/
├── README.md                 # This file
├── antigravity/              # Sync files and overrides for Antigravity
├── codex/                    # Tool definitions and wrappers for Codex
└── claude/                   # Custom tool profiles and aliases for Claude
```

---

## 2. Portability Guidelines

To ensure the base skills in `/skills` remain 100% portable and runtime-agnostic:

1.  **Do not write runtime-specific prompts** inside the base `SKILL.md` files. Keep instructions focused on requirements extraction and standard formatting.
2.  **Use adapters for executable scripts:** If a script relies on platform-specific environment variables or API keys, place it inside the runtime overlay folder, or read it dynamically from the environment.
3.  **One-way sync only:** Always edit the canonical skills inside the `/skills` root directory. Use scripts to publish or sync them to local/global agent folders.
